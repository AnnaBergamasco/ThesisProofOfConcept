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
        partitions = 3
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

        if randLog:
            log.close()

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

        print("Disequilibrium count: {}".format(problem.disequilibrium_count))

    if args.output_file:

        file = open(args.output_file, 'w')

        file.write("[METRICS]\n")
        if alg_name == 'RANDOM':
            file.write("\t[DISEQUILIBRIUM COUNT] " + str(n_disequilibrium) + "\n")
            
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
