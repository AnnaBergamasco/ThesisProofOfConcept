import argparse
from ast import arg
from ctypes import sizeof
from random import Random
from xml.etree.ElementTree import tostring
import numpy as np
from pymoo.core.problem import ElementwiseProblem
from SimulatorRunner import SimulatorRunner
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_reference_directions
from pymoo.operators.mixed_variable_operator import MixedVariableSampling, MixedVariableMutation, MixedVariableCrossover
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_termination
from pymoo.optimize import minimize
import matplotlib.pyplot as plt
import sys
from pymoo.visualization.pcp import PCP
from pymoo.core.problem import starmap_parallelized_eval
from multiprocessing.pool import ThreadPool
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.algorithms.moo.moead import MOEAD, ParallelMOEAD
from pymoo.algorithms.moo.age import AGEMOEA
from pymoo.visualization.heatmap import Heatmap
from pymoo.visualization.petal import Petal
from pymoo.algorithms.moo.unsga3 import UNSGA3
import random


mask = ["int", "real", "int", "real"]

sampling = MixedVariableSampling(mask, {
    "real": get_sampling("real_random"),
    "int": get_sampling("int_random"),
})

crossover = MixedVariableCrossover(mask, {
    "real": get_crossover("real_sbx", prob=1.0, eta=20.0),
    "int": get_crossover("int_sbx", prob=1.0, eta=20.0)
})

mutation = MixedVariableMutation(mask, {
    "real": get_mutation("real_pm", eta=20.0),
    "int": get_mutation("int_pm", eta=20.0)
})

class RescueRobotProblemM(ElementwiseProblem):

    def __init__(self, fast = False, verbose = False):
        super().__init__(n_var= 4, n_obj = 2, n_constr = 0, xl = [1, 10.0, 1, 0.1], xu = [100, 10000.0, 10, 2.0])
        self.evaluationNumber = 0
        self.fast = fast
        self.verbose = verbose
        self.disequilibrium_count = 0

    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        battery = x[0]
        light = x[1]
        quality = x[2]
        obstacleSize = x[3]

        if self.verbose:
            print("-")
            print("-")
            print("-")
            print("EVALUATING: battery = " + str(battery) + " light = " + str(light) + " quality = " + str(quality) + " obstacleSize = " + str(obstacleSize))
            print("-")
            print("-")
            print("-")

        sim = SimulatorRunner(battery=battery, light=light, quality=quality, obstacleSize=obstacleSize, verbose=self.verbose)

        if self.fast:
            sim.runSimulatorFast()
        else:
            sim.runSimulator()


        f1 = min(sim.getT1Distances())
        f2 = min(sim.getT2Distances())

        if self.verbose:
            print("-")
            print("-")
            print("-")
            print("Evaluation number: " + str(self.evaluationNumber))
            print("Objectives: " + str(f1) + " " + str(f2))
            print("-")
            print("-")
            print("-")

        out["F"] = [f1, f2]
        out["G"] = []

        for o in out["F"]:
            if o < 0.0:
                self.disequilibrium_count += 1
                break

class RescueRobotProblemA(ElementwiseProblem):

    def __init__(self, fast = False, verbose = False):
        super().__init__(n_var= 4, n_obj = 6, n_constr = 0, xl = [1, 10.0, 1, 0.1], xu = [100, 10000.0, 10, 2.0])
        self.evaluationNumber = 0
        self.fast = fast
        self.verbose = verbose
        self.disequilibrium_count = 0

    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        battery = x[0]
        light = x[1]
        quality = x[2]
        obstacleSize = x[3]

        if self.verbose:
            print("-")
            print("-")
            print("-")
            print("EVALUATING: battery = " + str(battery) + " light = " + str(light) + " quality = " + str(quality) + " obstacleSize = " + str(obstacleSize))
            print("-")
            print("-")
            print("-")

        sim = SimulatorRunner(battery=battery, light=light, quality=quality, obstacleSize=obstacleSize, verbose=self.verbose)

        if self.fast:
            sim.runSimulatorFast()
        else:
            sim.runSimulator()

        f1 = sim.getT1Distances()
        f2 = sim.getT2Distances()


        if self.verbose:
            print("-")
            print("-")
            print("-")
            print("Evaluation number: " + str(self.evaluationNumber))
            print("Objectives: " + str(f1[0]) + " " + str(f1[1]) + " " + str(f1[2]) + " " + str(f2[0]) + " " + str(f2[1]) + " " + str(f2[2]))
            print("-")
            print("-")
            print("-")

        out["F"] = [f1[0], f1[1], f1[2], f2[0], f2[1], f2[2]]
        out["G"] = []

        for o in out["F"]:
            if o < 0.0:
                self.disequilibrium_count += 1
                break


def main():

    parser = argparse.ArgumentParser(description='Falsification with many-objective search.')
    parser.add_argument("alg", help="selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3]")
    parser.add_argument("-a", "--alldist", action='store_true', help="enables var-wise fitness mode (default: region-wise)", required=False)
    parser.add_argument("-f", "--fast", action='store_true', help="enables fast mode", required=False)
    parser.add_argument("-s", "--size", type=int, help="population size", required=False, default=2)
    parser.add_argument("-n", "--niterations", type=int, help="number of iterations", required=False, default=8)
    parser.add_argument("-v", "--verbose", action='store_true', help="enables verbose log", required=False)
    parser.add_argument("-rf", "--results_file", action='store_true', help="enables saving of results file", required=False)
    args = parser.parse_args()

    selection = 1
    fast = False
    population_size = args.size
    niterations = args.niterations
    alg_name = args.alg
    partitions = 2

    if args.alldist:
        selection = 2

    if args.verbose:
        print("Verbose mode on.")

    if args.fast:
        fast = True
        print("Fast simulation mode on.")
    
    if args.results_file:
        print("Results file saving mode on.")

    if selection == 1:
        print("Region-wise distance mode on.")
        problem  = RescueRobotProblemM(fast=fast, verbose=args.verbose)
        numb_obj = 2
    else:
        print("Var-wise distance mode on.")
        problem = RescueRobotProblemA(fast=fast, verbose=args.verbose)
        numb_obj = 6

    if alg_name == "NSGA2":
        print("Selected algorithm: NSGA-II.")
        algorithm = NSGA2(
            pop_size= population_size,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation
        )

    elif alg_name == "NSGA3":
        print("Selected algorithm: NSGA-III.")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=partitions)
        algorithm = NSGA3(
            pop_size= population_size,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs
        )

    elif alg_name == "UNSGA3":
        print("Selected algorithm: U-NSGA-III.")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=partitions)
        algorithm = UNSGA3(
            pop_size= population_size,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs
        )

    elif alg_name == "MOEAD":
        print("Selected algorithm: MOEA-D.")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=partitions)
        algorithm = MOEAD(
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs,
            n_neighbors=12,
            prob_neighbor_mating= 0.7
        )

    elif alg_name == "AGEMOEA":
        print("selected algorithm: AGE-MOEA")
        algorithm = AGEMOEA(
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            pop_size= population_size
        )
    
    elif alg_name == 'RANDOM':
        n_tries = population_size * niterations
        n_disequiliburium = 0
        for i in range(1, n_tries):

            battery = random.randint(1, 100)
            quality = random.randint(1, 10)
            light = random.uniform(10.0, 10000.0)
            obstacleSize = random.uniform(0.1, 2.0)

            sim = SimulatorRunner(battery=battery, light=light, quality=quality, obstacleSize=obstacleSize, verbose=args.verbose)

            if args.fast:
                sim.runSimulatorFast()
            else:
                sim.runSimulator()

            f1 = sim.getT1Distances()
            f2 = sim.getT2Distances()

            results = [f1[0], f1[1], f1[2], f2[0], f2[1], f2[2]]

            for o in results:
                if o < 0.0:
                    n_disequiliburium += 1
                    break

        print("Disequilibrium count: {}".format(n_disequiliburium))

    else:
        raise ValueError("Invalid algorithm (use -h to see the valid options).")


    if alg_name != 'RANDOM':

        termination = get_termination("n_gen", niterations)

        res = minimize(
            problem,
            algorithm,
            termination,
            seed= None,
            save_history= True,
            verbose= True
        )


        X = res.X
        F = res.F

        xl, xu = problem.bounds()
        '''plt.figure(figsize=(7, 5))
        plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
        plt.xlim(xl[0], xu[0])
        plt.ylim(xl[1], xu[1])
        plt.title("Design Space")
        plt.show()'''

        if args.verbose:
            if selection == 1:
                plt.figure(figsize=(7, 5))
                plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
                plt.title("Objective Space")
                plt.show()
            else:
                PCP().add(F).show()
                Heatmap().add(F).show()
                Petal(bounds=[0, 1]).add(F).show()

        print("Disequilibrium count: {}".format(problem.disequilibrium_count))

    if args.results_file:

        file = open('results.txt', 'w')
    
        file.write("[METRICS]\n")
        if alg_name == "RANDOM":
            file.write("\t[DISEQUILIBRIUM COUNT] " + str(n_disequiliburium) + "\n")
        else:
            file.write("\t[DISEQUILIBRIUM COUNT] " + str(problem.disequilibrium_count) + "\n")
            file.write("[VARIABLES]\n")
            ind = 0
            for x in X:
                ind = ind  +1
                file.write("\t[RESULT " + str(ind) + "] " + str(x) + "\n")
            file.write("[OBJECTIVES]\n")
            ind = 0
            for f in F:
                ind = ind  +1
                file.write("\t[RESULT " + str(ind) + "] " + str(f) + "\n")

        file.close()

if __name__ == "__main__":
    main()
