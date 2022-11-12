# SmallExperiment3

This is the third experiment of the SmallExperiment serie on the `Pymoo` implementation of the search program. Its goal is to measure the goodness of the results provided by different many-objective algorithms. 
Each execution is of the search is run using the fast mode and the var-wise fitness mode; the experiment is repeated 20 times for each algorithm, using a population size of 30 and a number of generations of 30. The metrics used are 12 for each execution: the maximum and average severity of equilibrium violation of each variable, computed by the inversion of signs and min-max scaling of the minimum and average values of the 6 variables. This metrics of each algorithm are then collected in intervals for a clearer comparison between algorithms and a better graphical representation (radar plot).

The material, code and results of the experiment are divided in the following files.

## Execution results files

These are the results relative to each execution of the search program, containing both the values of all the metrics but also the values of the final population (except in the case of the random search).

The name of these files are of the type
```
[name of the algorithm]_[number of the experiment].txt
```

## Combined results files

These are the results relative to each algorithm, in the form of intervals for both the average and the maximum metrics, and also the averages of the averages.

The name of these files are of the type
```
[name of the algorithm]_results.txt
```

## RunExperiment.py

This is the code that runs all the experiments (by calling the `RunSingleExperiment.py`), computes the scaling and collects the 12 metrics. It also computes the extremes of two intervals for each variable: one containing the average values for that severity, the other containing the maximum values for that severity.
Finally, it also creates several plots to compare the results: a box plot for each variables comparing the maximum severities of the algorithms, a radar plot for each algorithm showing the intervals containing the maximum and average severities values and two summary radar plot comparing the total average and maximum severities of each algorithms.

To run the script use the command: 
```
usage: RunExperiment.py [-h] [-s] [-n] [-r]

Experiment on falsification with many-objective search using different algorithms, with computation of minimun and average distances.

positional arguments:
  alg         selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, RNSGA3, TAEA, RANDOM]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  population size
  -n NITERATIONS, --niterations NITERATIONS
                        number of iterations
  -r REPETITIONS, --repetitions REPETITIONS
                        number of repetitions
```

## RunSingleExperiment.py

This is the script used by `RunExperiment.py` iteratively run the experiment on each algorithm. It also contributes to the computation of the metrics by changing the signs of the variables.

To run this script separately follow the instructions to run the `RescueRobotPymoo.py` script, modify the conde at line 41 to have the correct path to the `RescueRobotPymoo.py` file and then run the following command:

```
usage: RunSingleExperiment.py [-h] alg

Experiment on falsification with many-objective search, with computation of minimun and average
distances.

positional arguments:
  alg         selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA,
              UNSGA3, RNSGA3, CTAEA, RANDOM]

optional arguments:
  -h, --help  show this help message and exit
```

## RadarPlotAlgorithms.py

This is the script used by `RunExperiment.py` to generate the radar plot of the severities of each algorithm.

## Radar plots

These are the plots of each algorithm results, showing the values of the interval's extremes for each metric, both maximum and average.

The names of these files are of the type
```
[name of the algorithm]_radarPlot.png
```

## BoxPlot.py

This is the code used by `RunExperiment.py` to generate the box plots of the maximum severities for each variable.

## Box plots

These are the plots of the maximum severities found by the algorithms for each variables.

The names of these files are of the type:
```
BoxPlot_[name of the variable].png
```

## RadarPlotSummary.py

This is the script used by `RunExperiment.py` to generate `RadarPlot_SummaryMax.png` e `RadarPlot_SummaryAvg.png` containg the values of the total averages and maximums severities.

## RadarPlot_SummaryMax.png

Is the radar plot showing for each algorithm the absolute maximum severity for each variable.

## RadarPlot_SummaryAvg.png

Is the radar plot showing for each algorithm the total average severity for each variable.
