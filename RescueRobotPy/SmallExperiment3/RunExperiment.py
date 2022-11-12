from RunSingleExperiment import RunSingleExperiment
from sklearn.preprocessing import MinMaxScaler
import statistics
import numpy as np
from RadarPlotAlgorithms import RadarPlotAlgorithms
from RadarPlotSummary import RadarPlotSummary
from BoxPlot import BoxPlotVariables
import argparse

def makeResultFile(alg_name, results) -> None:

    
    file = open(alg_name + '_results.txt', 'w')
    
    file.write('[MAXIMUM SEVERITY]\n')
    file.write('\t[LOWER BOUND]\n')
    file.write('\t\t[S0 e1 S1]' + str(results[0][0]) + '\n')
    file.write('\t\t[S0 e1 S2]' + str(results[0][1]) + '\n')
    file.write('\t\t[S0 e1 S6]' + str(results[0][2]) + '\n')
    file.write('\t\t[S3 e1 S1]' + str(results[0][3]) + '\n')
    file.write('\t\t[S3 e1 S4]' + str(results[0][4]) + '\n')
    file.write('\t\t[S3 e1 S5]' + str(results[0][5]) + '\n')
    file.write('\t[HIGH BOUND]\n')
    file.write('\t\t[S0 e1 S1]' + str(results[1][0]) + '\n')
    file.write('\t\t[S0 e1 S2]' + str(results[1][1]) + '\n')
    file.write('\t\t[S0 e1 S6]' + str(results[1][2]) + '\n')
    file.write('\t\t[S3 e1 S1]' + str(results[1][3]) + '\n')
    file.write('\t\t[S3 e1 S4]' + str(results[1][4]) + '\n')
    file.write('\t\t[S3 e1 S5]' + str(results[1][5]) + '\n')
    file.write('[AVERAGE SEVERITY]\n')
    file.write('\t[LOWER BOUND]\n')
    file.write('\t\t[S0 e1 S1]' + str(results[2][0]) + '\n')
    file.write('\t\t[S0 e1 S2]' + str(results[2][1]) + '\n')
    file.write('\t\t[S0 e1 S6]' + str(results[2][2]) + '\n')
    file.write('\t\t[S3 e1 S1]' + str(results[2][3]) + '\n')
    file.write('\t\t[S3 e1 S4]' + str(results[2][4]) + '\n')
    file.write('\t\t[S3 e1 S5]' + str(results[2][5]) + '\n')
    file.write('\t[HIGH BOUND]\n')
    file.write('\t\t[S0 e1 S1]' + str(results[3][0]) + '\n')
    file.write('\t\t[S0 e1 S2]' + str(results[3][1]) + '\n')
    file.write('\t\t[S0 e1 S6]' + str(results[3][2]) + '\n')
    file.write('\t\t[S3 e1 S1]' + str(results[3][3]) + '\n')
    file.write('\t\t[S3 e1 S4]' + str(results[3][4]) + '\n')
    file.write('\t\t[S3 e1 S5]' + str(results[3][5]) + '\n')
    file.write('\t[AVERAGE]\n')
    file.write('\t\t[S0 e1 S1]' + str(results[4][0]) + '\n')
    file.write('\t\t[S0 e1 S2]' + str(results[4][1]) + '\n')
    file.write('\t\t[S0 e1 S6]' + str(results[4][2]) + '\n')
    file.write('\t\t[S3 e1 S1]' + str(results[4][3]) + '\n')
    file.write('\t\t[S3 e1 S4]' + str(results[4][4]) + '\n')
    file.write('\t\t[S3 e1 S5]' + str(results[4][5]) + '\n')

    file.close()

def summarizeData(alg_severities) -> list:

    summary = [[], [], [], [], []]
    
    for i in range(0, 6):
        summary[0] = summary[0] + [min(alg_severities[0][i])]
        summary[1] = summary[1] + [max(alg_severities[0][i])]
        summary[2] = summary[2] + [min(alg_severities[1][i])]
        summary[3] = summary[3] + [max(alg_severities[1][i])]
        summary[4] = summary[4] + [statistics.mean(alg_severities[1][i])]

    return summary

def main():

    parser = argparse.ArgumentParser(description='Experiment on falsification with many-objective search using different algorithms, with computation of minimun and average distances.')
    parser.add_argument("-s", "--size", type=int, help="population size", required=False, default=2)
    parser.add_argument("-n", "--niterations", type=int, help="number of iterations", required=False, default=8)
    parser.add_argument("-r", "--repetitions", type=int, help="number of repetitions", required=False, default=20)
    args = parser.parse_args()

    population_size = args.size
    niterations = args.niterations
    nrepetitions = args.repetitions

    runner = RunSingleExperiment(nrepetitions)

    random_raw = runner.runWithAlgorithm('RANDOM', population_size, niterations)
    nsga3_raw = runner.runWithAlgorithm('NSGA3', population_size, niterations)
    unsga3_raw = runner.runWithAlgorithm('UNSGA3', population_size, niterations)
    moead_raw = runner.runWithAlgorithm('MOEAD', population_size, niterations)
    ctaea_raw = runner.runWithAlgorithm('CTAEA', population_size, niterations)
    agemoea_raw = runner.runWithAlgorithm('AGEMOEA', population_size, niterations)

    random_scaled = [[], []]
    nsga3_scaled = [[], []]
    unsga3_scaled = [[], []]
    moead_scaled = [[], []]
    ctaea_scaled = [[], []]
    agemoea_scaled = [[], []]
    scaling_set = [[], [], [], [], [], []]

    for i in range(0, 6):
        scaling_set[i] = random_raw[0][i] + random_raw[1][i] + nsga3_raw[0][i] + nsga3_raw[1][i] + unsga3_raw[0][i] + unsga3_raw[1][i] + moead_raw[0][i] + moead_raw[1][i] + ctaea_raw[0][i] + ctaea_raw[1][i] + agemoea_raw[0][i] + agemoea_raw[1][i]
    
    scaling_set = np.array(scaling_set)
    scaling_set = scaling_set.transpose()
    scaler = MinMaxScaler()
    scaler.fit(scaling_set)


    for j in range(0, 2):
        random_scaled[j] = np.array(scaler.transform(np.array(random_raw[j]).transpose())).transpose().tolist()
        nsga3_scaled[j] = np.array(scaler.transform(np.array(nsga3_raw[j]).transpose())).transpose().tolist()
        unsga3_scaled[j] = np.array(scaler.transform(np.array(unsga3_raw[j]).transpose())).transpose().tolist()
        moead_scaled[j] = np.array(scaler.transform(np.array(moead_raw[j]).transpose())).transpose().tolist()
        ctaea_scaled[j] = np.array(scaler.transform(np.array(ctaea_raw[j]).transpose())).transpose().tolist()
        agemoea_scaled[j] = np.array(scaler.transform(np.array(agemoea_raw[j]).transpose())).transpose().tolist()
    
    for i in range(0, 6):
        plot_scaled = BoxPlotVariables(nsga3_scaled[0][i], unsga3_scaled[0][i], agemoea_scaled[0][i], ctaea_scaled[0][i], moead_scaled[0][i], random_scaled[0][i])
        plot_scaled.makePlot()

    nsga3_summary = summarizeData(nsga3_scaled)
    plot_algorithms = RadarPlotAlgorithms(nsga3_summary[0], nsga3_summary[1], nsga3_summary[2], nsga3_summary[3])
    plot_algorithms.makePlot()
    makeResultFile('nsga3', nsga3_summary)
    unsga3_summary = summarizeData(unsga3_scaled)
    plot_algorithms = RadarPlotAlgorithms(unsga3_summary[0], unsga3_summary[1], unsga3_summary[2], unsga3_summary[3])
    plot_algorithms.makePlot()
    makeResultFile('unsga3', unsga3_summary)
    agemoea_summary = summarizeData(agemoea_scaled)
    plot_algorithms = RadarPlotAlgorithms(agemoea_summary[0], agemoea_summary[1], agemoea_summary[2], agemoea_summary[3])
    plot_algorithms.makePlot()
    makeResultFile('agemoea', agemoea_summary)
    ctaea_summary = summarizeData(ctaea_scaled)
    plot_algorithms = RadarPlotAlgorithms(ctaea_summary[0], ctaea_summary[1], ctaea_summary[2], ctaea_summary[3])
    plot_algorithms.makePlot()
    makeResultFile('ctaea', ctaea_summary)
    moead_summary = summarizeData(moead_scaled)
    plot_algorithms = RadarPlotAlgorithms(moead_summary[0], moead_summary[1], moead_summary[2], moead_summary[3])
    plot_algorithms.makePlot()
    makeResultFile('moead', moead_summary)
    random_summary = summarizeData(random_scaled)
    plot_algorithms = RadarPlotAlgorithms(random_summary[0], random_summary[1], random_summary[2], random_summary[3])
    plot_algorithms.makePlot()
    makeResultFile('random', random_summary)

    plot_summary = RadarPlotSummary([nsga3_summary[1],
            unsga3_summary[1],
            agemoea_summary[1],
            ctaea_summary[1],
            moead_summary[1],
            random_summary[1]],
        [nsga3_summary[4],
            unsga3_summary[4],
            agemoea_summary[4],
            ctaea_summary[4],
            moead_summary[4],
            random_summary[4]] )
    
    plot_summary.makePlot()


if __name__ == "__main__":
    main()