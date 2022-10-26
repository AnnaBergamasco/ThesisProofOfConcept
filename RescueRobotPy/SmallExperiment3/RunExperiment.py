
import argparse
import subprocess
from RadarPlot import RadarPlot


def main():

    parser = argparse.ArgumentParser(description='Experiment on falsification with many-objective search, with computation of minimun and average distances.')
    parser.add_argument("alg", help="selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, RNSGA3, CTAEA, RANDOM]")
    args = parser.parse_args()
    alg_name = args.alg
    pop_size = 30
    n_generations = 30

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

    min_low_bounds = [10, 10, 10, 10, 10, 10]
    min_hi_bounds = [-10, -10, -10, -10, -10, -10]
    avg_low_bounds = [10, 10, 10, 10, 10, 10]
    avg_hi_bounds = [-10, -10, -10, -10, -10, -10]
    avg_avg = [0, 0, 0, 0, 0, 0]

    for i in range(1, 21):
        test_out = subprocess.run(["python3", "/home/anna/Documenti/Uni/Tesi/RescueRobotGA/RescueRobotPy/RescueRobotPymoo.py", "-a", "-f", "-s " + str(pop_size), "-n " + str(n_generations), alg_name, "-o " + alg_des + '_' + str(i) + ".txt"], stdout=subprocess.PIPE, text = True)
        logLines = (test_out.stdout).split('\n')

        for s in logLines:
            if s.__contains__("Minimum S0 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[0] = min(result, min_low_bounds[0])
                min_hi_bounds[0] = max(result, min_hi_bounds[0])
            if s.__contains__("Minimum S0 e1 S2 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[1] = min(result, min_low_bounds[1])
                min_hi_bounds[1] = max(result, min_hi_bounds[1])
            if s.__contains__("Minimum S0 e1 S6 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[2] = min(result, min_low_bounds[2])
                min_hi_bounds[2] = max(result, min_hi_bounds[2])
            if s.__contains__("Minimum S3 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[3] = min(result, min_low_bounds[3])
                min_hi_bounds[3] = max(result, min_hi_bounds[3])
            if s.__contains__("Minimum S3 e1 S4 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[4] = min(result, min_low_bounds[4])
                min_hi_bounds[4] = max(result, min_hi_bounds[4])
            if s.__contains__("Minimum S3 e1 S5 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[5] = min(result, min_low_bounds[5])
                min_hi_bounds[5] = max(result, min_hi_bounds[5])
            if s.__contains__("Average S0 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[0] = min(result, avg_low_bounds[0])
                avg_hi_bounds[0] = max(result, avg_hi_bounds[0])
                avg_avg[0] =  avg_avg[0] + (result - avg_avg[0])/i
            if s.__contains__("Average S0 e1 S2 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[1] = min(result, avg_low_bounds[1])
                avg_hi_bounds[1] = max(result, avg_hi_bounds[1])
                avg_avg[1] =  avg_avg[1] + (result - avg_avg[1])/i
            if s.__contains__("Average S0 e1 S6 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[2] = min(result, avg_low_bounds[2])
                avg_hi_bounds[2] = max(result, avg_hi_bounds[2])
                avg_avg[2] =  avg_avg[2] + (result - avg_avg[2])/i
            if s.__contains__("Average S3 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[3] = min(result, avg_low_bounds[3])
                avg_hi_bounds[3] = max(result, avg_hi_bounds[3])
                avg_avg[3] =  avg_avg[3] + (result - avg_avg[3])/i
            if s.__contains__("Average S3 e1 S4 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[4] = min(result, avg_low_bounds[4])
                avg_hi_bounds[4] = max(result, avg_hi_bounds[4])
                avg_avg[4] =  avg_avg[4] + (result - avg_avg[4])/i
            if s.__contains__("Average S3 e1 S5 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[5] = min(result, avg_low_bounds[5])
                avg_hi_bounds[5] = max(result, avg_hi_bounds[5])
                avg_avg[5] =  avg_avg[5] + (result - avg_avg[5])/i

    print(min_low_bounds)
    print(min_hi_bounds)       
    print(avg_low_bounds)
    print(avg_hi_bounds)
    print(avg_avg) 

    radarPlot = RadarPlot(min_low_bounds, min_hi_bounds, avg_low_bounds, avg_hi_bounds)
    radarPlot.makePlot()

    output_file = alg_des + "_results.txt"

    file = open(output_file, 'w')

    file.write("[MINIMUM LOWER BOUND]\n")
    file.write("\t[S0 e1 S1] " + str(min_low_bounds[0]) + "\n")
    file.write("\t[S0 e1 S2] " + str(min_low_bounds[1]) + "\n")
    file.write("\t[S0 e1 S6] " + str(min_low_bounds[2]) + "\n")
    file.write("\t[S3 e1 S1] " + str(min_low_bounds[3]) + "\n")
    file.write("\t[S3 e1 S4] " + str(min_low_bounds[4]) + "\n")
    file.write("\t[S3 e1 S5] " + str(min_low_bounds[5]) + "\n")
    file.write("[MINIMUM HIGER BOUND]\n")
    file.write("\t[S0 e1 S1] " + str(min_hi_bounds[0]) + "\n")
    file.write("\t[S0 e1 S2] " + str(min_hi_bounds[1]) + "\n")
    file.write("\t[S0 e1 S6] " + str(min_hi_bounds[2]) + "\n")
    file.write("\t[S3 e1 S1] " + str(min_hi_bounds[3]) + "\n")
    file.write("\t[S3 e1 S4] " + str(min_hi_bounds[4]) + "\n")
    file.write("\t[S3 e1 S5] " + str(min_hi_bounds[5]) + "\n")
    file.write("[AVERAGE LOWER BOUND]\n")
    file.write("\t[S0 e1 S1] " + str(avg_low_bounds[0]) + "\n")
    file.write("\t[S0 e1 S2] " + str(avg_low_bounds[1]) + "\n")
    file.write("\t[S0 e1 S6] " + str(avg_low_bounds[2]) + "\n")
    file.write("\t[S3 e1 S1] " + str(avg_low_bounds[3]) + "\n")
    file.write("\t[S3 e1 S4] " + str(avg_low_bounds[4]) + "\n")
    file.write("\t[S3 e1 S5] " + str(avg_low_bounds[5]) + "\n")
    file.write("[AVERAGE HIGER BOUND]\n")
    file.write("\t[S0 e1 S1] " + str(avg_hi_bounds[0]) + "\n")
    file.write("\t[S0 e1 S2] " + str(avg_hi_bounds[1]) + "\n")
    file.write("\t[S0 e1 S6] " + str(avg_hi_bounds[2]) + "\n")
    file.write("\t[S3 e1 S1] " + str(avg_hi_bounds[3]) + "\n")
    file.write("\t[S3 e1 S4] " + str(avg_hi_bounds[4]) + "\n")
    file.write("\t[S3 e1 S5] " + str(avg_hi_bounds[5]) + "\n")
    file.write("[AVERAGE]\n")
    file.write("\t[S0 e1 S1] " + str(avg_avg[0]) + "\n")
    file.write("\t[S0 e1 S2] " + str(avg_avg[1]) + "\n")
    file.write("\t[S0 e1 S6] " + str(avg_avg[2]) + "\n")
    file.write("\t[S3 e1 S1] " + str(avg_avg[3]) + "\n")
    file.write("\t[S3 e1 S4] " + str(avg_avg[4]) + "\n")
    file.write("\t[S3 e1 S5] " + str(avg_avg[5]) + "\n")

    file.close()

if __name__ == "__main__":
    main()