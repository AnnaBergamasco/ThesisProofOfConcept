import numpy as np
from pymoo.core.problem import ElementwiseProblem
from SimulatorRunner import SimulatorRunner
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.operators.mixed_variable_operator import MixedVariableSampling, MixedVariableMutation, MixedVariableCrossover
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_termination
from pymoo.optimize import minimize
import matplotlib.pyplot as plt
import sys


mask = ["int", "real"]

sampling = MixedVariableSampling(mask, {
    "real": get_sampling("real_random"),
    "int": get_sampling("int_random")
})

crossover = MixedVariableCrossover(mask, {
    "real": get_crossover("real_sbx", prob=1.0, eta=20.0),
    "int": get_crossover("int_sbx", prob=1.0, eta=20.0)
})

mutation = MixedVariableMutation(mask, {
    "real": get_mutation("real_pm", eta=20.0),
    "int": get_mutation("int_pm", eta=20.0)
})

class RescueRobotProblemM(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var= 2, n_obj = 2, n_constr = 0, xl = [0, 10.0], xu = [100, 10000.0])
        self.evaluationNumber = 0

    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        battery = x[0]
        light = x[1]

        print("-")
        print("-")
        print("-")
        print("EVALUATING: battery = " + str(battery) + " light = " + str(light))
        print("-")
        print("-")
        print("-")

        sim = SimulatorRunner(battery=battery, light=light)
        sim.runSimulator()

        f1 = min(sim.getT1Distances())
        f2 = min(sim.getT2Distances())

        print("-")
        print("-")
        print("-")
        print("Evaluation number: " + str(self.evaluationNumber))
        print("Objectives: " + str(f1) + " " + str(f2))
        print("-")
        print("-")
        print("-")

        out["F"] = [f1, f2]
        out["G"] = []

class RescueRobotProblemA(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var= 2, n_obj = 6, n_constr = 0, xl = [0, 10.0], xu = [100, 10000.0])
        self.evaluationNumber = 0

    def _evaluate(self, x, out, *args, **kwargs):
        self.evaluationNumber = self.evaluationNumber + 1

        battery = x[0]
        light = x[1]

        print("-")
        print("-")
        print("-")
        print("EVALUATING: battery = " + str(battery) + " light = " + str(light))
        print("-")
        print("-")
        print("-")

        sim = SimulatorRunner(battery=battery, light=light)
        sim.runSimulator()

        f1 = sim.getT1Distances()
        f2 = sim.getT2Distances()

        print("-")
        print("-")
        print("-")
        print("Evaluation number: " + str(self.evaluationNumber))
        print("Objectives: " + str(f1[0]) + " " + str(f1[1]) + " " + str(f1[2]) + " " + str(f2[0]) + " " + str(f2[1]) + " " + str(f2[2]))
        print("-")
        print("-")
        print("-")

        out["F"] = [f1[0], f1[1], f1[2], f2[0], f2[1], f2[2]]
        out["G"] = []


if __name__ == "__main__":

    selection = 1

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if "-a" in opts:
        selection = 2

    

    if selection == 1:
        print("MODe: minimum distance mode")
        problem  = RescueRobotProblemM()
    
    else:
        print("MODE: all distances mode")
        problem = RescueRobotProblemA()
    
    

    algorithm = NSGA2(
        pop_size= 2,
        n_offsprings= None,
        sampling= sampling,
        crossover= crossover,
        mutation= mutation,
        eliminate_duplicates= True
    )

    termination = get_termination("n_gen", 5)

    res = minimize(
        problem,
        algorithm,
        termination,
        seed= None,
        save_history= True,
        verbose= True
    )

    X = res.X
    F = res.F
    
    if selection == 1:

        xl, xu = problem.bounds()
        plt.figure(figsize=(7, 5))
        plt.scatter(X[:, 0], X[:, 1], s=30, facecolors='none', edgecolors='r')
        plt.xlim(xl[0], xu[0])
        plt.ylim(xl[1], xu[1])
        plt.title("Design Space")
        plt.show()

        plt.figure(figsize=(7, 5))
        plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
        plt.title("Objective Space")
        plt.show()
