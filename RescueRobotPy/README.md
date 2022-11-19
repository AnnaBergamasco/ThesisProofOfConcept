# RescueRobotPy

This is the python implementation of the RescueRobot example, using both `JMetalPy` and `Pymoo`. Also, some experiments on the `Pymoo` implementation are included.
Here follow the explaination of the content.

For the implementations to work mbt_module_dir has to be changed to the local directory of the `MBT-module` at line 11 of the `sim_launcher.py` file.


## RescueRobotGA.py

Is the `JMetalPy` implementation. It contains two implementations of the problem, one that uses the minimum distance fitness function: for each uncertain zone of the model there is one objective to compute, and one that uses the all distances fitness function: each uncertain probability corresponds to one objective.

The script also contains a main funciton that sets the algorithm's (NSGA-II) parameters and let the user choose which of the two policies to use.

To run the script install the `JMetalPy` library (instructions at [https://jmetal.github.io/jMetalPy/index.html](https://jmetal.github.io/jMetalPy/index.html)) and then use the command:
```
python3 RescueRobotGA.py [-a]
```
The option `-a` enables the all distances fitness mode.

## RescueRobotPymoo.py

Is the `Pymoo` implementation. It contains two implementations of the problem, one that uses the minimum distance fitness function and the other that uses all distances fitness function.

It also contains a main function that sets which algorithm to use and its parameteres and runs it. The available algorithms are NSGA-II (a multi-objective algortihm, recomended for the minimum distance fitness mode), NSGA-III, AGE-MOEA, C-TAEA, U-NSGA-II, MOEA-D (many-objective algorithms recommended for the all distances fitness mode) and RANDOM.

To run the script install the `Pymoo` library (instructions at [https://pymoo.org/installation.html](https://pymoo.org/installation.html)) and then use the command:
```
usage: RescueRobotPymoo.py [-h] [-a] [-f] [-s SIZE] [-n NITERATIONS] [-v] [-o] alg

Falsification with many-objective search.

positional arguments:
  alg                   selected many-objective search algorithm in [NSGA2, NSGA3, MOEAD, AGEMOEA, UNSGA3, CTAEA, RANDOM]

optional arguments:
  -h, --help            show this help message and exit
  -a, --alldist         enables var-wise fitness mode (default: region-wise)
  -f, --fast            enables fast mode
  -s SIZE, --size SIZE  population size
  -n NITERATIONS, --niterations NITERATIONS
                        number of iterations
  -v, --verbose         enables verbose log
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        output file
```

## sim_launcher.py

Is a modified version of the laucher `mdp_simulator_launcher`: the only difference is that it returns the output so that it is possible to read the results.

## SimulatorRunner.py

Defines a class used to run the simulation and parse the output to obtain the results.

## SmallExperimet1

Contains the result of the first experiment concerning the best version of the fitness function for the RescueRobot problem.

## SmallExperimetn2

Contains the results of the second experiment concerning what algorithm is better suited to solve the RescueRobot problem using the number of disequilibriums founded as a metric.

## SmallExperiment3

Contains the results of the third experiment concerning what algorithm is better suited to solve the RescueRobot problem using the severity of disequilibrium of each variable metrics.