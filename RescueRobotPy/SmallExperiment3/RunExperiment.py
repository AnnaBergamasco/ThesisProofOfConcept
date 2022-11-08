from RunSingleExperiment import RunSingleExperiment
from sklearn.preprocessing import MinMaxScaler
import statistics
import numpy as np
from RadarPlotAlgorithms import RadarPlotAlgorithms
from RadarPlotSummary import RadarPlotSummary

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

    runner = RunSingleExperiment()

    random_raw = runner.runWithAlgorithm('RANDOM')
    nsga3_raw = runner.runWithAlgorithm('NSGA3')
    unsga3_raw = runner.runWithAlgorithm('UNSGA3')
    moead_raw = runner.runWithAlgorithm('MOEAD')
    ctaea_raw = runner.runWithAlgorithm('CTAEA')
    agemoea_raw = runner.runWithAlgorithm('AGEMOEA')

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
    
    
    nsga3_summary = summarizeData(nsga3_scaled)
    plot_algorithms = RadarPlotAlgorithms(nsga3_summary[0], nsga3_summary[1], nsga3_summary[2], nsga3_summary[3])
    plot_algorithms.makePlot()
    unsga3_summary = summarizeData(unsga3_scaled)
    plot_algorithms = RadarPlotAlgorithms(unsga3_summary[0], unsga3_summary[1], unsga3_summary[2], unsga3_summary[3])
    plot_algorithms.makePlot()
    agemoea_summary = summarizeData(agemoea_scaled)
    plot_algorithms = RadarPlotAlgorithms(agemoea_summary[0], agemoea_summary[1], agemoea_summary[2], agemoea_summary[3])
    plot_algorithms.makePlot()
    ctaea_summary = summarizeData(ctaea_scaled)
    plot_algorithms = RadarPlotAlgorithms(ctaea_summary[0], ctaea_summary[1], ctaea_summary[2], ctaea_summary[3])
    plot_algorithms.makePlot()
    moead_summary = summarizeData(moead_scaled)
    plot_algorithms = RadarPlotAlgorithms(moead_summary[0], moead_summary[1], moead_summary[2], moead_summary[3])
    plot_algorithms.makePlot()
    random_summary = summarizeData(random_scaled)
    plot_algorithms = RadarPlotAlgorithms(random_summary[0], random_summary[1], random_summary[2], random_summary[3])
    plot_algorithms.makePlot()

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