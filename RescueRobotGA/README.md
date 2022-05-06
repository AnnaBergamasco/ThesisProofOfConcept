# RescueRobotGA

This is the Java implementation using `JMetal`, the algorithm used is NSGA-II.
Here follow the explaination of the used classes.

## AlgorithmRunner

Contains the main method of the program and is used to set the algorithm (NSGA-II).

## RRProblemMinObjective

Is the implementation of the search problem, using the minimum distance fitness function: for each uncertain zone of the model there is one objective to compute.

## SimulatorRunner

Is used to run the `mdp_simulator_launcher` and to parse its output into usable results.