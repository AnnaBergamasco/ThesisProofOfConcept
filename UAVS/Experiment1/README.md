# Experiment

This is the first experiment on the UAVS problem implementation. Its goal is to measure the goodness of the results provided by different many-objective algorithms. 
Each execution is of the search is run using the fast mode and the var-wise fitness mode; the experiment is repeated 20 times for each algorithm, using a population size of 120 and a number of generations of 30. The metric used is the number of elements considered by the algorithm that break the equilibrium constraint, meaninig that one of the variables of its fitness is negative.
The metrics of each algorithm are compared using box plots.
Also, some statistical analysis is provided to verify the relevance of the obtained results, comparing the probability distributions of each algorithm.

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

## StatisticalTest.py

This file contains the code that computes the effect size and the p-value of the distributions of the metric for each couple of algorithms. It also produce the heatmaps of this two statistical parameters for better understanding.

## statistical_results.txt

Contains the values of the effect size and p-values in textual form.

## Effect_plot.png

This is the image of the heatmap of the effect size values for each couple of algorithms.

## Pvalue_plot.png

This is the image of the heatmap of the p-value for each couple of algorithms.