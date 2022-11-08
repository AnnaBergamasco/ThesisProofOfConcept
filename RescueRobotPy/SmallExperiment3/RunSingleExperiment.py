
import argparse
import subprocess


class RunSingleExperiment():

    def __init__(
        
        self
    ):
        super(RunSingleExperiment, self).__init__()

    def runWithAlgorithm(self, alg_name) -> list:
        pop_size = 30
        n_generations = 30

        maximum_severities = [[], [], [], [], [], []]
        average_severities = [[], [], [], [], [], []]

        if alg_name == 'NSGA2':
            alg_des = 'nsga2'
        elif alg_name == 'NSGA3':
            alg_des = 'nsga3'
        elif alg_name == 'MOEAD':
            alg_des = 'moead'
            n_generations = 16
        elif alg_name == 'AGEMOEA':
            alg_des = 'agemoea'
        elif alg_name == 'UNSGA3':
            alg_des = 'unsga3'
        elif alg_name == 'RNSGA3':
            alg_des = 'rnsga3'
        elif alg_name == 'CTAEA':
            alg_des = 'ctaea'
            n_generations = 43
        elif alg_name == 'RANDOM':
            alg_des = 'random'

        for i in range(1, 21):
            test_out = subprocess.run(["python3", "/home/anna/Documenti/Uni/Tesi/RescueRobotGA/RescueRobotPy/RescueRobotPymoo.py", "-a", "-f", "-s " + str(pop_size), "-n " + str(n_generations), alg_name, "-o " + alg_des + '_' + str(i) + ".txt"], stdout=subprocess.PIPE, text = True)
            logLines = (test_out.stdout).split('\n')

            for s in logLines:
                if s.__contains__("Minimum S0 e1 S1 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[0] = maximum_severities[0] + [-result]
                if s.__contains__("Minimum S0 e1 S2 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[1] = maximum_severities[1] + [-result]
                if s.__contains__("Minimum S0 e1 S6 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[2] = maximum_severities[2] + [-result]
                if s.__contains__("Minimum S3 e1 S1 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[3] = maximum_severities[3] + [-result]
                if s.__contains__("Minimum S3 e1 S4 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[4] = maximum_severities[4] + [-result]
                if s.__contains__("Minimum S3 e1 S5 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    maximum_severities[5] = maximum_severities[5] + [-result]
                if s.__contains__("Average S0 e1 S1 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[0] = average_severities[0] + [-result]
                if s.__contains__("Average S0 e1 S2 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[1] = average_severities[1] + [-result]
                if s.__contains__("Average S0 e1 S6 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[2] = average_severities[2] + [-result]
                if s.__contains__("Average S3 e1 S1 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[3] = average_severities[3] + [-result]
                if s.__contains__("Average S3 e1 S4 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[4] = average_severities[4] + [-result]
                if s.__contains__("Average S3 e1 S5 distance: "):
                    tokens = s.split(':')
                    result = float(tokens[1].replace(" ", ""))
                    average_severities[5] = average_severities[5] + [-result]
        

        return [maximum_severities, average_severities]

def main():

    parser = argparse.ArgumentParser(description='Experiment on falsification with many-objective search, with computation of minimun and average distances.')
    parser.add_argument("alg", help="selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, RNSGA3, CTAEA, RANDOM]")
    args = parser.parse_args()
    alg_name = args.alg

    runner = RunSingleExperiment()

    results = runner.runWithAlgorithm(alg_name=alg_name)

    print(results)
    
    
if __name__ == "__main__":
    main()