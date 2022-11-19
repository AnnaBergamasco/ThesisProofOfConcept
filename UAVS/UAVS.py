from SimulatorRunnerUAVS import SimulatorRunnerUAVS
from pymoo.core.problem import ElementwiseProblem
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_reference_directions
from pymoo.operators.mixed_variable_operator import MixedVariableSampling, MixedVariableMutation, MixedVariableCrossover
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_termination
from pymoo.optimize import minimize
from pymoo.visualization.pcp import PCP
from pymoo.core.problem import starmap_parallelized_eval
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.algorithms.moo.moead import MOEAD, ParallelMOEAD
from pymoo.algorithms.moo.age import AGEMOEA
from pymoo.visualization.heatmap import Heatmap
from pymoo.visualization.petal import Petal
from pymoo.algorithms.moo.unsga3 import UNSGA3
from pymoo.algorithms.moo.ctaea import CTAEA
import argparse
import random

mask = ['int', 'real', 'int', 'int', 'int', 'real', 'int']

sampling = MixedVariableSampling(mask, {
    'real': get_sampling('real_random'),
    'int': get_sampling('int_random')
})

crossover = MixedVariableCrossover(mask, {
    'real': get_crossover('real_sbx'),
    'int': get_crossover('int_sbx')
})

mutation = MixedVariableMutation(mask, {
    'real': get_mutation('real_pm'),
    'int': get_mutation('int_pm')
})

class UAVSProblem(ElementwiseProblem):

    def __init__(self):

        #TODO: add verbose mode

        super().__init__(n_var = 7, n_obj = 14, n_constr = 0, xl = [0, 5.0, 0, 1, 0, 1000.0, 1], xu = [1, 50.0, 1, 4, 24, 4000.0, 100])
        self.evaluationNumber = 0

        self.disequilibrium_count = 0

        self.minimum_distance_0_1 = 10000
        self.minimum_distance_0_21 = 10000
        self.minimum_distance_0_22 = 10000
        self.minimum_distance_7_6 = 10000
        self.minimum_distance_7_8 = 10000
        self.minimum_distance_7_21 = 10000
        self.minimum_distance_7_22 = 10000
        self.minimum_distance_14_13 = 10000
        self.minimum_distance_14_15 = 10000
        self.minimum_distance_14_21 = 10000
        self.minimum_distance_14_22 = 10000
        self.minimum_distance_20_19 = 10000
        self.minimum_distance_20_21 = 10000
        self.minimum_distance_20_22 = 10000

        self.average_distance_0_1 = 0
        self.average_distance_0_21 = 0
        self.average_distance_0_22 = 0
        self.average_distance_7_6 = 0
        self.average_distance_7_8 = 0
        self.average_distance_7_21 = 0
        self.average_distance_7_22 = 0
        self.average_distance_14_13 = 0
        self.average_distance_14_15 = 0
        self.average_distance_14_21 = 0
        self.average_distance_14_22 = 0
        self.average_distance_20_19 = 0
        self.average_distance_20_21 = 0
        self.average_distance_20_22 = 0

        #TODO: add metrics
    
    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        formation = x[0]
        speed = x[1]
        counter = x[2]
        weather = x[3]
        time = x[4]
        ranget = x[5]
        nthreat = x[6]

        sim = SimulatorRunnerUAVS(formation=formation, speed=speed, counter=counter, weather=weather, time=time, ranget=ranget, nthreat=nthreat)

        sim.runSimulatorFast()

        #TODO: add slow mode
        
        f1 = sim.getT1Distances()
        f2 = sim.getT2Distances()
        f3 = sim.getT3Distances()
        f4 = sim.getT4Distances()

        out["F"] = [f1[0],
            f1[1],
            f1[2],
            f2[0],
            f2[1],
            f2[2],
            f2[3],
            f3[0],
            f3[1],
            f3[2],
            f3[3],
            f4[0],
            f4[1],
            f4[2]]
        out["G"] = []

        for o in out["F"]:
            if o < 0.0:
                self.disequilibrium_count += 1
                break
        
        self.minimum_distance_0_1 = min(self.minimum_distance_0_1, f1[0])
        self.minimum_distance_0_21 = min(self.minimum_distance_0_21, f1[1])
        self.minimum_distance_0_22 = min(self.minimum_distance_0_22, f1[2])
        self.minimum_distance_7_6 = min(self.minimum_distance_7_6, f2[0])
        self.minimum_distance_7_8 = min(self.minimum_distance_7_8, f2[1])
        self.minimum_distance_7_21 = min(self.minimum_distance_7_21, f2[2])
        self.minimum_distance_7_22 = min(self.minimum_distance_7_22, f2[3])
        self.minimum_distance_14_13 = min(self.minimum_distance_14_13, f3[0])
        self.minimum_distance_14_15 = min(self.minimum_distance_14_15, f3[1])
        self.minimum_distance_14_21 = min(self.minimum_distance_14_21, f3[2])
        self.minimum_distance_14_22 = min(self.minimum_distance_14_22, f3[3])
        self.minimum_distance_20_19 = min(self.minimum_distance_20_19, f4[0])
        self.minimum_distance_20_21 = min(self.minimum_distance_20_21, f4[1])
        self.minimum_distance_20_22 = min(self.minimum_distance_20_22, f4[2])

        self.average_distance_0_1 = self.average_distance_0_1 + (f1[0] - self.average_distance_0_1)/self.evaluationNumber
        self.average_distance_0_21 = self.average_distance_0_21 + (f1[1] - self.average_distance_0_21)/self.evaluationNumber
        self.average_distance_0_22 = self.average_distance_0_22 + (f1[2] - self.average_distance_0_22)/self.evaluationNumber
        self.average_distance_7_6 = self.average_distance_7_6 + (f2[0] - self.average_distance_7_6)/self.evaluationNumber
        self.average_distance_7_8 = self.average_distance_7_8 + (f2[1] - self.average_distance_7_8)/self.evaluationNumber
        self.average_distance_7_21 = self.average_distance_7_21 + (f2[2] - self.average_distance_7_21)/self.evaluationNumber
        self.average_distance_7_22 = self.average_distance_7_22 + (f2[3] - self.average_distance_7_22)/self.evaluationNumber
        self.average_distance_14_13 = self.average_distance_14_13 + (f3[0] - self.average_distance_14_13)/self.evaluationNumber
        self.average_distance_14_15 = self.average_distance_14_15 + (f3[1] - self.average_distance_14_15)/self.evaluationNumber
        self.average_distance_14_21 = self.average_distance_14_21 + (f3[2] - self.average_distance_14_21)/self.evaluationNumber
        self.average_distance_14_22 = self.average_distance_14_22 + (f3[3] - self.average_distance_14_22)/self.evaluationNumber
        self.average_distance_20_19 = self.average_distance_20_19 + (f4[0] - self.average_distance_20_19)/self.evaluationNumber
        self.average_distance_20_21 = self.average_distance_20_21 + (f4[1] - self.average_distance_20_21)/self.evaluationNumber
        self.average_distance_20_22 = self.average_distance_20_22 + (f4[2] - self.average_distance_20_22)/self.evaluationNumber


def main():

    parser = argparse.ArgumentParser(description='Falsification with many-objective search.')
    parser.add_argument("alg", help="selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, RNSGA3, CTAEA, RANDOM]")
    parser.add_argument("-s", "--size", type=int, help="population size", required=False, default=2)
    parser.add_argument("-n", "--niterations", type=int, help="number of iterations", required=False, default=8)
    parser.add_argument("-o", "--output_file", type= str, help='output file', required=False, default=None)
    parser.add_argument("-l", "--log_random", action='store_true', help="enables storing of random results", required=False)
    args = parser.parse_args()

    randLog = False
    population_size = args.size
    niterations = args.niterations
    alg_name = args.alg
    partitions = 2

    if args.log_random:
        randLog = True
        print("Random log storage mode on.")
    
    problem = UAVSProblem()
    numb_obj = 14

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

    elif alg_name == "CTAEA":
        print("selected algorithm: C-TAEA")
        ref_dirs = get_reference_directions("das-dennis", numb_obj, n_partitions=partitions)
        algorithm = CTAEA(
            sampling= sampling,
            crossover= crossover,
            mutation= mutation,
            ref_dirs= ref_dirs
        )

    elif alg_name == "RANDOM":
        n_tries = population_size * niterations
        n_disequilibrium = 0

        minimum_distance_0_1 = 10000
        minimum_distance_0_21 = 10000
        minimum_distance_0_22 = 10000
        minimum_distance_7_6 = 10000
        minimum_distance_7_8 = 10000
        minimum_distance_7_21 = 10000
        minimum_distance_7_22 = 10000
        minimum_distance_14_13 = 10000
        minimum_distance_14_15 = 10000
        minimum_distance_14_21 = 10000
        minimum_distance_14_22 = 10000
        minimum_distance_20_19 = 10000
        minimum_distance_20_21 = 10000
        minimum_distance_20_22 = 10000

        average_distance_0_1 = 0
        average_distance_0_21 = 0
        average_distance_0_22 = 0
        average_distance_7_6 = 0
        average_distance_7_8 = 0
        average_distance_7_21 = 0
        average_distance_7_22 = 0
        average_distance_14_13 = 0
        average_distance_14_15 = 0
        average_distance_14_21 = 0
        average_distance_14_22 = 0
        average_distance_20_19 = 0
        average_distance_20_21 = 0
        average_distance_20_22 = 0

        if randLog:
            log = open('random_log.txt', 'w')

        for i in range(1, n_tries + 1):

            formation = random.randint(0, 1)
            speed = random.uniform(5.0, 50.0)
            counter = random.randint(0, 1)
            weather = random.randint(1, 4)
            time = random.randint(0, 24)
            ranget = random.uniform(1000.0, 4000.0)
            nthreat = random.randint(1, 100)

            sim = SimulatorRunnerUAVS(formation=formation, speed=speed, counter=counter, weather=weather, time=time, ranget=ranget, nthreat=nthreat)

            sim.runSimulatorFast()
        
            f1 = sim.getT1Distances()
            f2 = sim.getT2Distances()
            f3 = sim.getT3Distances()
            f4 = sim.getT4Distances()

            results = [f1[0],
                f1[1],
                f1[2],
                f2[0],
                f2[1],
                f2[2],
                f2[3],
                f3[0],
                f3[1],
                f3[2],
                f3[3],
                f4[0],
                f4[1],
                f4[2]]
            
            if randLog:
                log.write(str(sim.t1Probabilities) + ' ' + str(sim.t2Probabilities) + ' ' + str(sim.t3Probabilities) + ' ' + str(sim.t4Probabilities) + '\n')
        
            for o in results:
                    if o < 0.0:
                        n_disequilibrium += 1
                        break
            
            minimum_distance_0_1 = min(minimum_distance_0_1, f1[0])
            minimum_distance_0_21 = min(minimum_distance_0_21, f1[1])
            minimum_distance_0_22 = min(minimum_distance_0_22, f1[2])
            minimum_distance_7_6 = min(minimum_distance_7_6, f2[0])
            minimum_distance_7_8 = min(minimum_distance_7_8, f2[1])
            minimum_distance_7_21 = min(minimum_distance_7_21, f2[2])
            minimum_distance_7_22 = min(minimum_distance_7_22, f2[3])
            minimum_distance_14_13 = min(minimum_distance_14_13, f3[0])
            minimum_distance_14_15 = min(minimum_distance_14_15, f3[1])
            minimum_distance_14_21 = min(minimum_distance_14_21, f3[2])
            minimum_distance_14_22 = min(minimum_distance_14_22, f3[3])
            minimum_distance_20_19 = min(minimum_distance_20_19, f4[0])
            minimum_distance_20_21 = min(minimum_distance_20_21, f4[1])
            minimum_distance_20_22 = min(minimum_distance_20_22, f4[2])

            average_distance_0_1 = average_distance_0_1 + (f1[0] - average_distance_0_1)/i
            average_distance_0_21 = average_distance_0_21 + (f1[1] - average_distance_0_21)/i
            average_distance_0_22 = average_distance_0_22 + (f1[2] - average_distance_0_22)/i
            average_distance_7_6 = average_distance_7_6 + (f2[0] - average_distance_7_6)/i
            average_distance_7_8 = average_distance_7_8 + (f2[1] - average_distance_7_8)/i
            average_distance_7_21 = average_distance_7_21 + (f2[2] - average_distance_7_21)/i
            average_distance_7_22 = average_distance_7_22 + (f2[3] - average_distance_7_22)/i
            average_distance_14_13 = average_distance_14_13 + (f3[0] - average_distance_14_13)/i
            average_distance_14_15 = average_distance_14_15 + (f3[1] - average_distance_14_15)/i
            average_distance_14_21 = average_distance_14_21 + (f3[2] - average_distance_14_21)/i
            average_distance_14_22 = average_distance_14_22 + (f3[3] - average_distance_14_22)/i
            average_distance_20_19 = average_distance_20_19 + (f4[0] - average_distance_20_19)/i
            average_distance_20_21 = average_distance_20_21 + (f4[1] - average_distance_20_21)/i
            average_distance_20_22 = average_distance_20_22 + (f4[2] - average_distance_20_22)/i



        if randLog:
            log.close()

        
        print("Minimum S0 sTrt S1 distance: {}".format(minimum_distance_0_1))
        print("Minimum S0 sTrt S21 distance: {}".format(minimum_distance_0_21))
        print("Minimum S0 sTrt S22 distance: {}".format(minimum_distance_0_22))
        print("Minimum S7 sTrt S6 distance: {}".format(minimum_distance_7_6))
        print("Minimum S7 sTrt S8 distance: {}".format(minimum_distance_7_8))
        print("Minimum S7 sTrt S21 distance: {}".format(minimum_distance_7_21))
        print("Minimum S7 sTrt S22 distance: {}".format(minimum_distance_7_22))
        print("Minimum S14 sTrt S13 distance: {}".format(minimum_distance_14_13))
        print("Minimum S14 sTrt S15 distance: {}".format(minimum_distance_14_15))
        print("Minimum S14 sTrt S21 distance: {}".format(minimum_distance_14_21))
        print("Minimum S14 sTrt S22 distance: {}".format(minimum_distance_14_22))
        print("Minimum S20 sTrt S19 distance: {}".format(minimum_distance_20_19))
        print("Minimum S20 sTrt S21 distance: {}".format(minimum_distance_20_21))
        print("Minimum S20 sTrt S22 distance: {}".format(minimum_distance_20_22))
        

        print("Average S0 sTrt S1 distance: {}".format(average_distance_0_1))
        print("Average S0 sTrt S21 distance: {}".format(average_distance_0_21))
        print("Average S0 sTrt S22 distance: {}".format(average_distance_0_22))
        print("Average S7 sTrt S6 distance: {}".format(average_distance_7_6))
        print("Average S7 sTrt S8 distance: {}".format(average_distance_7_8))
        print("Average S7 sTrt S21 distance: {}".format(average_distance_7_21))
        print("Average S7 sTrt S22 distance: {}".format(average_distance_7_22))
        print("Average S14 sTrt S13 distance: {}".format(average_distance_14_13))
        print("Average S14 sTrt S15 distance: {}".format(average_distance_14_15))
        print("Average S14 sTrt S21 distance: {}".format(average_distance_14_21))
        print("Average S14 sTrt S22 distance: {}".format(average_distance_14_22))
        print("Average S20 sTrt S19 distance: {}".format(average_distance_20_19))
        print("Average S20 sTrt S21 distance: {}".format(average_distance_20_21))
        print("Average S20 sTrt S22 distance: {}".format(average_distance_20_22))

        print("Disequilibrium count: {}".format(n_disequilibrium))

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

        

        print("Minimum S0 sTrt S1 distance: {}".format(problem.minimum_distance_0_1))
        print("Minimum S0 sTrt S21 distance: {}".format(problem.minimum_distance_0_21))
        print("Minimum S0 sTrt S22 distance: {}".format(problem.minimum_distance_0_22))
        print("Minimum S7 sTrt S6 distance: {}".format(problem.minimum_distance_7_6))
        print("Minimum S7 sTrt S8 distance: {}".format(problem.minimum_distance_7_8))
        print("Minimum S7 sTrt S21 distance: {}".format(problem.minimum_distance_7_21))
        print("Minimum S7 sTrt S22 distance: {}".format(problem.minimum_distance_7_22))
        print("Minimum S14 sTrt S13 distance: {}".format(problem.minimum_distance_14_13))
        print("Minimum S14 sTrt S15 distance: {}".format(problem.minimum_distance_14_15))
        print("Minimum S14 sTrt S21 distance: {}".format(problem.minimum_distance_14_21))
        print("Minimum S14 sTrt S22 distance: {}".format(problem.minimum_distance_14_22))
        print("Minimum S20 sTrt S19 distance: {}".format(problem.minimum_distance_20_19))
        print("Minimum S20 sTrt S21 distance: {}".format(problem.minimum_distance_20_21))
        print("Minimum S20 sTrt S22 distance: {}".format(problem.minimum_distance_20_22))
        

        print("Average S0 sTrt S1 distance: {}".format(problem.average_distance_0_1))
        print("Average S0 sTrt S21 distance: {}".format(problem.average_distance_0_21))
        print("Average S0 sTrt S22 distance: {}".format(problem.average_distance_0_22))
        print("Average S7 sTrt S6 distance: {}".format(problem.average_distance_7_6))
        print("Average S7 sTrt S8 distance: {}".format(problem.average_distance_7_8))
        print("Average S7 sTrt S21 distance: {}".format(problem.average_distance_7_21))
        print("Average S7 sTrt S22 distance: {}".format(problem.average_distance_7_22))
        print("Average S14 sTrt S13 distance: {}".format(problem.average_distance_14_13))
        print("Average S14 sTrt S15 distance: {}".format(problem.average_distance_14_15))
        print("Average S14 sTrt S21 distance: {}".format(problem.average_distance_14_21))
        print("Average S14 sTrt S22 distance: {}".format(problem.average_distance_14_22))
        print("Average S20 sTrt S19 distance: {}".format(problem.average_distance_20_19))
        print("Average S20 sTrt S21 distance: {}".format(problem.average_distance_20_21))
        print("Average S20 sTrt S22 distance: {}".format(problem.average_distance_20_22))

        print("Disequilibrium count: {}".format(problem.disequilibrium_count))
        

    if args.output_file:

        file = open(args.output_file, 'w')

        file.write("[METRICS]\n")
        if alg_name == 'RANDOM':
            file.write("\t[DISEQUILIBRIUM COUNT] " + str(n_disequilibrium) + "\n")
            
            file.write("\t[MINIMUM S0 sTrt S1 DISTANCE]" + str(minimum_distance_0_1) + "\n")
            file.write("\t[MINIMUM S0 sTrt S21 DISTANCE]" + str(minimum_distance_0_21) + "\n")
            file.write("\t[MINIMUM S0 sTrt S22 DISTANCE]" + str(minimum_distance_0_22) + "\n")
            file.write("\t[MINIMUM S7 sTrt S6 DISTANCE]" + str(minimum_distance_7_6) + "\n")
            file.write("\t[MINIMUM S7 sTrt S8 DISTANCE]" + str(minimum_distance_7_8) + "\n")
            file.write("\t[MINIMUM S7 sTrt S21 DISTANCE]" + str(minimum_distance_7_21) + "\n")
            file.write("\t[MINIMUM S7 sTrt S22 DISTANCE]" + str(minimum_distance_7_22) + "\n")
            file.write("\t[MINIMUM S14 sTrt S13 DISTANCE]" + str(minimum_distance_14_13) + "\n")
            file.write("\t[MINIMUM S14 sTrt S15 DISTANCE]" + str(minimum_distance_14_15) + "\n")
            file.write("\t[MINIMUM S14 sTrt S21 DISTANCE]" + str(minimum_distance_14_21) + "\n")
            file.write("\t[MINIMUM S14 sTrt S22 DISTANCE]" + str(minimum_distance_14_22) + "\n")
            file.write("\t[MINIMUM S20 sTrt S19 DISTANCE]" + str(minimum_distance_20_19) + "\n")
            file.write("\t[MINIMUM S20 sTrt S21 DISTANCE]" + str(minimum_distance_20_21) + "\n")
            file.write("\t[MINIMUM S20 sTrt S22 DISTANCE]" + str(minimum_distance_20_22) + "\n")

            file.write("\t[AVERAGE S0 sTrt S1 DISTANCE]" + str(average_distance_0_1) + "\n")
            file.write("\t[AVERAGE S0 sTrt S21 DISTANCE]" + str(average_distance_0_21) + "\n")
            file.write("\t[AVERAGE S0 sTrt S22 DISTANCE]" + str(average_distance_0_22) + "\n")
            file.write("\t[AVERAGE S7 sTrt S6 DISTANCE]" + str(average_distance_7_6) + "\n")
            file.write("\t[AVERAGE S7 sTrt S8 DISTANCE]" + str(average_distance_7_8) + "\n")
            file.write("\t[AVERAGE S7 sTrt S21 DISTANCE]" + str(average_distance_7_21) + "\n")
            file.write("\t[AVERAGE S7 sTrt S22 DISTANCE]" + str(average_distance_7_22) + "\n")
            file.write("\t[AVERAGE S14 sTrt S13 DISTANCE]" + str(average_distance_14_13) + "\n")
            file.write("\t[AVERAGE S14 sTrt S15 DISTANCE]" + str(average_distance_14_15) + "\n")
            file.write("\t[AVERAGE S14 sTrt S21 DISTANCE]" + str(average_distance_14_21) + "\n")
            file.write("\t[AVERAGE S14 sTrt S22 DISTANCE]" + str(average_distance_14_22) + "\n")
            file.write("\t[AVERAGE S20 sTrt S19 DISTANCE]" + str(average_distance_20_19) + "\n")
            file.write("\t[AVERAGE S20 sTrt S21 DISTANCE]" + str(average_distance_20_21) + "\n")
            file.write("\t[AVERAGE S20 sTrt S22 DISTANCE]" + str(average_distance_20_22) + "\n")

        else: 
            file.write("\t[DISEQUILIBRIUM COUNT] " + str(problem.disequilibrium_count) + "\n")
            
            file.write("\t[MINIMUM S0 sTrt S1 DISTANCE]" + str(problem.minimum_distance_0_1) + "\n")
            file.write("\t[MINIMUM S0 sTrt S21 DISTANCE]" + str(problem.minimum_distance_0_21) + "\n")
            file.write("\t[MINIMUM S0 sTrt S22 DISTANCE]" + str(problem.minimum_distance_0_22) + "\n")
            file.write("\t[MINIMUM S7 sTrt S6 DISTANCE]" + str(problem.minimum_distance_7_6) + "\n")
            file.write("\t[MINIMUM S7 sTrt S8 DISTANCE]" + str(problem.minimum_distance_7_8) + "\n")
            file.write("\t[MINIMUM S7 sTrt S21 DISTANCE]" + str(problem.minimum_distance_7_21) + "\n")
            file.write("\t[MINIMUM S7 esTrt S22 DISTANCE]" + str(problem.minimum_distance_7_22) + "\n")
            file.write("\t[MINIMUM S14 sTrt S13 DISTANCE]" + str(problem.minimum_distance_14_13) + "\n")
            file.write("\t[MINIMUM S14 sTrt S15 DISTANCE]" + str(problem.minimum_distance_14_15) + "\n")
            file.write("\t[MINIMUM S14 sTrt S21 DISTANCE]" + str(problem.minimum_distance_14_21) + "\n")
            file.write("\t[MINIMUM S14 sTrt S22 DISTANCE]" + str(problem.minimum_distance_14_22) + "\n")
            file.write("\t[MINIMUM S20 sTrt S19 DISTANCE]" + str(problem.minimum_distance_20_19) + "\n")
            file.write("\t[MINIMUM S20 sTrt S21 DISTANCE]" + str(problem.minimum_distance_20_21) + "\n")
            file.write("\t[MINIMUM S20 sTrt S22 DISTANCE]" + str(problem.minimum_distance_20_22) + "\n")

            file.write("\t[AVERAGE S0 sTrt S1 DISTANCE]" + str(problem.average_distance_0_1) + "\n")
            file.write("\t[AVERAGE S0 sTrt S21 DISTANCE]" + str(problem.average_distance_0_21) + "\n")
            file.write("\t[AVERAGE S0 sTrt S22 DISTANCE]" + str(problem.average_distance_0_22) + "\n")
            file.write("\t[AVERAGE S7 sTrt S6 DISTANCE]" + str(problem.average_distance_7_6) + "\n")
            file.write("\t[AVERAGE S7 sTrt S8 DISTANCE]" + str(problem.average_distance_7_8) + "\n")
            file.write("\t[AVERAGE S7 sTrt S21 DISTANCE]" + str(problem.average_distance_7_21) + "\n")
            file.write("\t[AVERAGE S7 sTrt S22 DISTANCE]" + str(problem.average_distance_7_22) + "\n")
            file.write("\t[AVERAGE S14 sTrt S13 DISTANCE]" + str(problem.average_distance_14_13) + "\n")
            file.write("\t[AVERAGE S14 sTrt S15 DISTANCE]" + str(problem.average_distance_14_15) + "\n")
            file.write("\t[AVERAGE S14 sTrt S21 DISTANCE]" + str(problem.average_distance_14_21) + "\n")
            file.write("\t[AVERAGE S14 sTrt S22 DISTANCE]" + str(problem.average_distance_14_22) + "\n")
            file.write("\t[AVERAGE S20 sTrt S19 DISTANCE]" + str(problem.average_distance_20_19) + "\n")
            file.write("\t[AVERAGE S20 sTrt S21 DISTANCE]" + str(problem.average_distance_20_21) + "\n")
            file.write("\t[AVERAGE S20 sTrt S22 DISTANCE]" + str(problem.average_distance_20_22) + "\n")


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
