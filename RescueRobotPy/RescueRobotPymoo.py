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

    def __init__(self, fast):
        super().__init__(n_var= 4, n_obj = 2, n_constr = 0, xl = [1, 10.0, 1, 0.1], xu = [100, 10000.0, 10, 2.0])
        self.evaluationNumber = 0
        self.fast = fast

    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        battery = x[0]
        light = x[1]
        quality = x[2]
        obstacleSize = x[3]

        print("-")
        print("-")
        print("-")
        print("EVALUATING: battery = " + str(battery) + " light = " + str(light) + " quality = " + str(quality) + " obstacleSize = " + str(obstacleSize))
        print("-")
        print("-")
        print("-")

        sim = SimulatorRunner(battery=battery, light=light, quality=quality, obstacleSize=obstacleSize)

        if self.fast:
            sim.runSimulatorFast()
        else:
            sim.runSimulator()


        f1 = min(sim.getT1Distances())
        f2 = min(sim.getT2Distances())

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

class RescueRobotProblemA(ElementwiseProblem):

    def __init__(self, fast):
        super().__init__(n_var= 4, n_obj = 6, n_constr = 0, xl = [1, 10.0, 1, 0.1], xu = [100, 10000.0, 10, 2.0])
        self.evaluationNumber = 0
        self.fast = fast

    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        battery = x[0]
        light = x[1]
        quality = x[2]
        obstacleSize = x[3]

        print("-")
        print("-")
        print("-")
        print("EVALUATING: battery = " + str(battery) + " light = " + str(light) + " quality = " + str(quality) + " obstacleSize = " + str(obstacleSize))
        print("-")
        print("-")
        print("-")

        sim = SimulatorRunner(battery=battery, light=light, quality=quality, obstacleSize=obstacleSize)
        
        if self.fast:
            sim.runSimulatorFast()
        else:
            sim.runSimulator()

        f1 = sim.getT1Distances()
        f2 = sim.getT2Distances()

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


if __name__ == "__main__":

    selection = 1
    fast = False

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if "-a" in opts:
        selection = 2
    
    if "-f" in opts:
        fast = True
        print("FAST SIMULATION MODE ON")

    if selection == 1:
        print("MODE: minimum distance mode")
        problem  = RescueRobotProblemM(fast=fast)
        numb_obj = 2
        


    else:
        print("MODE: all distances mode")
        problem = RescueRobotProblemA(fast=fast)
        numb_obj = 6
        
    
    alg_name = None
    if np.size(sys.argv) > 1:
        alg_name = sys.argv[1]
    
    if alg_name == "NSGA2":
        print("selected algorithm: NSGA-II")
        algorithm = NSGA2(
            pop_size= 2,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation
        )
    
    elif alg_name == "NSGA3":
        print("selected algorithm: NSGA-III")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=12)
        algorithm = NSGA3(
            pop_size= 2,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs
        )
    
    elif alg_name == "UNSGA3":
        print("selected algorithm: U-NSGA-III")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=12)
        algorithm = UNSGA3(
            pop_size= 2,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs
        )

    elif alg_name == "MOEAD":
        print("selected algorithm: MOEA-D")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=2)
        algorithm = MOEAD(
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs,
            n_neighbors=2,
            prob_neighbor_mating= 0.7
        )

    elif alg_name == "AGEMOEA":
        print("selected algorithm: AGE-MOEA")
        algorithm = AGEMOEA(
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            pop_size= 2
        )
    
    else:
        print("selected algorithm: invalid. Default algorithm (NSGA-II) applied.")
        algorithm = NSGA2(
            pop_size= 2,
            n_offsprings= None,
            sampling= sampling,
            crossover= crossover,
            mutation= mutation
        )
    

    
    termination = get_termination("n_gen", 8)

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
    
    if selection == 1:

        plt.figure(figsize=(7, 5))
        plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
        plt.title("Objective Space")
        plt.show()

    else:

        PCP().add(F).show()
        Heatmap().add(F).show()
        Petal(bounds=[0, 1]).add(F).show()
