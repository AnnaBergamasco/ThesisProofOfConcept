# UAVS

This is the python implementation of the UAVS example, using `Pymoo`. Also, the directory contains some experiments on its functioning.
Here follow the explaination of the content.

For the implementation to work mbt_module_dir has to be changed to the local directory of the `MBT-module` at line 11 of the `sim_launcher.py` file.

## UAVS.py

Is the `Pymoo` implementation. It contains two implementations of the problem, one that uses the minimum distance fitness function and the other that uses all distances fitness function.

It also contains a main function that sets which algorithm to use and its parameteres and runs it. The available algorithms are NSGA-II (a multi-objective algortihm, recomended for the minimum distance fitness mode), NSGA-III, AGE-MOEA, C-TAEA, U-NSGA-II, MOEA-D (many-objective algorithms recommended for the all distances fitness mode) and RANDOM.

To run the script install the `Pymoo` library (instructions at [https://pymoo.org/installation.html](https://pymoo.org/installation.html)) and then use the command:
```
usage: UACS.py [-h] [-s SIZE] [-n NITERATIONS] [-o] alg

Falsification with many-objective search.

positional arguments:
  alg                   selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, CTAEA, RANDOM]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  population size
  -n NITERATIONS, --niterations NITERATIONS
                        number of iterations
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        output file
```

## sim_launcher_uavs.py

Is a modified version of the laucher `mdp_simulator_launcher`: the only difference is that it returns the output so that it is possible to read the results.

## SimulatorRunnerUAVS.py

Defines a class used to run the simulation and parse the output to obtain the results.

## Experiment1

Contains the results of the first experiment concerning what algorithm is better suited to solve the UAVS problem using the number of disequilibriums founded as a metric.

## Experiment2

Contains the results of the second experiment concerning what algorithm is better suited to solve the UAVS problem using the severity of disequilibrium of each variable metrics.