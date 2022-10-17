# SmallExperiment2

This is the second experiment of the SmallExperiment serie on the `Pymoo` implementation of the search program. Its goal is to measure the goodness of the results provided by different many-objective algorithms. 
Each execution is of the search is run using the fast mode and the var-wise fitness mode; the experiment is repeated 20 times for each algorithm, using a population size of 30 and a number of generations of 30. The metric used is the number of elements considered by the algorithm that break the equilibrium constraint, meaninig that one of the variables of its fitness is negative.
The metrics of each algorithm are compared using box plots.

The material, code and results of the experiment are divided in the following files.

## Execution results files

These are the results relative to each execution of the search program, containing both the values of the metric but also the values of the final population (except in the case of the random search).

The name of these files are of the type
```
[name of the algorithm]_[number of the experiment].txt
```
## results.txt

Contains the summarized version of the results: for each algorithm the files shows all the 20 values of the metric obtained by the experiments.

## BoxPlot.py

This is the script used to produce the boxs plot of the result: the results need to be added to the code that then produces one plot for each algorithm.

## BoxPlot.png

Is an image containing all the plots of the algorithm's results.