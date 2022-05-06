# RescueRobotPy

This is the python implementation, using both `JMetalPy` and `Pymoo`, the algorithm used is NSGA-II.
Here follo the explaination of each python script.

## RescueRobotGA.py

Is the `JMetalPy` implementation. It contains two implementations of the problem, one that uses the minimum distance fitness function: for each uncertain zone of the model there is one objective to compute, and one that uses the all distances fitness function: each uncertain probability corresponds to one objective.

The script also contains a main funciton that sets the algorithm's (NSGA-II) parameters and let the user choose which of the two policies to use.

## RescueRobotPymoo.py

Is the `Pymoo` implementation. It uses the minimum distance fitness function. It contains the implementation of the problem as well as a main function that sets the algorithm (NSGA-II) and runs it.

## sim_launcher.py

Is a modified version of the laucher `mdp_simulator_launcher`: the only difference is that it returns the output so that it is possible to read the results.

## SimulatorRunner

Defines a class used to run the simulation and parse the output to obtain the results.