import argparse
import subprocess

class RunSingleExperiment():

    def __init__(
        
        self,
        n_repetitions
    ):
        super(RunSingleExperiment, self).__init__()
        self.n_repetitions = n_repetitions
    
    def runWithAlgorithm(self, alg_name, pop_size, n_generations) -> list:

        maximum_severities = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
        average_severities = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]

        if alg_name == 'NSGA2':
            alg_des = 'nsga2'
        elif alg_name == 'NSGA3':
            alg_des = 'nsga3'
        elif alg_name == 'MOEAD':
            alg_des = 'moead'
            n_generations = int((n_generations*pop_size)/105)
        elif alg_name == 'AGEMOEA':
            alg_des = 'agemoea'
        elif alg_name == 'UNSGA3':
            alg_des = 'unsga3'
        elif alg_name == 'CTAEA':
            alg_des = 'ctaea'
            n_generations = int((n_generations*pop_size)/105)
        elif alg_name == 'RANDOM':
            alg_des = 'random'

        for i in  range(1, self.n_repetitions + 1):
            test_out = subprocess.run(["python3", "/home/anna/Documenti/Uni/Tesi/RescueRobotGA/UAVS/UAVS.py", "-s " + str(pop_size), "-n " + str(n_generations), alg_name, "-o " + alg_des + '_' + str(i) + ".txt"], stdout=subprocess.PIPE, text= True)
            logLines = (test_out.stdout).split('\n')

            for s in logLines:

                if s.__contains__("Minimum S0 sTrt S1 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[0] = maximum_severities[0] + [-result]
                if s.__contains__("Minimum S0 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[1] = maximum_severities[1] + [-result]
                if s.__contains__("Minimum S0 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[2] = maximum_severities[2] + [-result]
                if s.__contains__("Minimum S7 sTrt S6 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[3] = maximum_severities[3] + [-result]
                if s.__contains__("Minimum S7 sTrt S8 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[4] = maximum_severities[4] + [-result]
                if s.__contains__("Minimum S7 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[5] = maximum_severities[5] + [-result]
                if s.__contains__("Minimum S7 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[6] = maximum_severities[6] + [-result]
                if s.__contains__("Minimum S14 sTrt S13 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[7] = maximum_severities[7] + [-result]
                if s.__contains__("Minimum S14 sTrt S15 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[8] = maximum_severities[8] + [-result]
                if s.__contains__("Minimum S14 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[9] = maximum_severities[9] + [-result]
                if s.__contains__("Minimum S14 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[10] = maximum_severities[10] + [-result]
                if s.__contains__("Minimum S20 sTrt S19 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[11] = maximum_severities[11] + [-result]
                if s.__contains__("Minimum S20 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[12] = maximum_severities[12] + [-result]
                if s.__contains__("Minimum S20 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[13] = maximum_severities[13] + [-result]
                
                if s.__contains__("Average S0 sTrt S1 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[0] = maximum_severities[0] + [-result]
                if s.__contains__("Average S0 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[1] = average_severities[1] + [-result]
                if s.__contains__("Average S0 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[2] = average_severities[2] + [-result]
                if s.__contains__("Average S7 sTrt S6 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[3] = average_severities[3] + [-result]
                if s.__contains__("Average S7 sTrt S8 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[4] = average_severities[4] + [-result]
                if s.__contains__("Average S7 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[5] = average_severities[5] + [-result]
                if s.__contains__("Average S7 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[6] = average_severities[6] + [-result]
                if s.__contains__("Average S14 sTrt S13 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[7] = average_severities[7] + [-result]
                if s.__contains__("Average S14 sTrt S15 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[8] = average_severities[8] + [-result]
                if s.__contains__("Average S14 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[9] = average_severities[9] + [-result]
                if s.__contains__("Average S14 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[10] = average_severities[10] + [-result]
                if s.__contains__("Average S20 sTrt S19 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[11] = average_severities[11] + [-result]
                if s.__contains__("Average S20 sTrt S21 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[12] = average_severities[12] + [-result]
                if s.__contains__("Average S20 sTrt S22 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[13] = average_severities[13] + [-result]

        return [maximum_severities, average_severities]
                

    
def main():

    parser = argparse.ArgumentParser(description='Experiment on falsification with many-objective search, with computation of minimun and average distances.')
    parser.add_argument("alg", help="selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, CTAEA, RANDOM]")
    args = parser.parse_args() 
    alg_name = args.alg

    runner = RunSingleExperiment(20)

    results = runner.runWithAlgorithm(alg_name=alg_name, pop_size=120, n_generations=30)

    print(results)
    
    
if __name__ == "__main__":
    main()