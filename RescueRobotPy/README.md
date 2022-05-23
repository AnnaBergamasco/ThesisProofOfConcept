# RescueRobotPy

This is the python implementation, using both `JMetalPy` and `Pymoo`, the algorithm used is NSGA-II.
Here follow the explaination of each python script.

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

It also contains a main function that sets which algorithm to use and its parameteres and runs it. The available algorithms are NSGA-II (a multi-objective algortihm, recomended for the minimum distance fitness mode), NSGA-III and MOEA-D (many-objective algorithms recommended for the all distances fitness mode)

To run the script install the `Pymoo` library (instructions at [https://pymoo.org/installation.html](https://pymoo.org/installation.html)) and then use the command:
```
python3 RescueRobotPymoo.py [algorithm name] [-a]
```
Where the algorithm name can be "NSGA2", "NSGA3" and "MOEAD".

The option `-a` enables the all distances fitness mode.


## sim_launcher.py

Is a modified version of the laucher `mdp_simulator_launcher`: the only difference is that it returns the output so that it is possible to read the results.

## SimulatorRunner

Defines a class used to run the simulation and parse the output to obtain the results.