# SmallExperiment3

This is the third experiment of the SmallExperiment serie on the `Pymoo` implementation of the search program. Its goal is to measure the goodness of the results provided by different many-objective algorithms. 
Each execution is of the search is run using the fast mode and the var-wise fitness mode; the experiment is repeated 20 times for each algorithm, using a population size of 30 and a number of generations of 30. The metrics used are 12 for each execution: the minimum and the average of all 6 variables. This metrics of each algorithm are then collected in intervals for a clearer comparison between algorithms and a better graphical representation (radar plot).

The material, code and results of the experiment are divided in the following files.

## Execution results files

These are the results relative to each execution of the search program, containing both the values of all the metrics but also the values of the final population (except in the case of the random search).

The name of these files are of the type
```
[name of the algorithm]_[number of the experiment].txt
```

## Combined results files

These are the results relative to each algorithm, in the form of intervals for both the average and the minimum metrics.

The name of these files are of the type
```
[name of the algorithm]_results.txt
```

## RunExperiment.py

This is the code that runs the experiments given the algorithm and collects the 12 metrics. It also computes the extremes of two intervals for each variable: one containing the average values for that variable, the other containing the minimum values for that variable.
Finally, it also creates a radar plot of the resulting extreme values by runnin the `RadarPlot.py` code.

To run the script follow the instructions to run the `RescueRobotPymoo.py` script, modify the conde at line 41 to have the correct path to the `RescueRobotPymoo.py` file and then use the command: 
```
usage: RunExperiment.py [-h] alg

Experiment on falsification with many-objective search, with computation of minimun and average distances.

positional arguments:
  alg         selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, RNSGA3, TAEA, RANDOM]

optional arguments:
  -h, --help  show this help message and exit
```

## RadarPlot.py

This is the script used by `RunExperiment.py` to generate the radar plot of the results of each algorithm. It inverts the signs of all the results to make the graph more legible since low values of the metrics are considered preferable.

## Radar plots

These are the plots of each algorithm results, showing the values of the interval's extremes for each metric, both minimum and average.

The name of these files are of the type
```
[name of the algorithm]_radarPlot.png
```

