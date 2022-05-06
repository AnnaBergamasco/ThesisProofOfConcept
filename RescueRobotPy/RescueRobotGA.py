from asyncore import read
import random
import readline
from jmetal.core.problem import Problem
from jmetal.core.solution import CompositeSolution, IntegerSolution, FloatSolution
from SimulatorRunner import SimulatorRunner
from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.operator import IntegerPolynomialMutation, PolynomialMutation, SBXCrossover
from jmetal.operator.crossover import CompositeCrossover, IntegerSBXCrossover
from jmetal.operator.mutation import CompositeMutation
from jmetal.problem.multiobjective.unconstrained import MixedIntegerFloatProblem
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.util.comparator import DominanceComparator
from jmetal.lab.visualization import Plot
from xml.etree.ElementTree import PI
from jmetal.util.solution import get_non_dominated_solutions, print_function_values_to_file, print_variables_to_file

class RescueRobotProblemM(Problem):

    def __init__(self):
        super(RescueRobotProblemM, self).__init__()

        self.number_of_constraints= 0
        self.number_of_objectives= 2
        self.number_of_variables= 2

        self.evaluationNumber = 0

        self.obj_directions=[self.MINIMIZE, self.MINIMIZE]
        self.obj_labels= ["t1", "t2"]

        self.int_lower_bound = [0]
        self.int_upper_bound = [100]
        self.float_lower_bound = [10.0]
        self.float_upper_bound = [10000.0]

    def evaluate(self, solution: CompositeSolution) -> CompositeSolution:

        
        
        self.evaluationNumber = self.evaluationNumber + 1
        battery = solution.variables[0].variables[0]
        light = solution.variables[1].variables[0]

        print("-")
        print("-")
        print("-")
        print("EVALUATING: battery = " + str(battery) + " light = " + str(light))
        print("-")
        print("-")
        print("-")
        
        sim = SimulatorRunner(battery=battery, light=light)
        sim.runSimulator()

        o1 = min(sim.getT1Distances())
        o2 = min(sim.getT2Distances())

        print("-")
        print("-")
        print("-")
        print("Evaluation number: " + str(self.evaluationNumber))
        print("Objectives: " + str(o1) + " " + str(o2))
        print("-")
        print("-")
        print("-")

        solution.objectives[0] = o1
        solution.objectives[1] = o2

        return solution




    def create_solution(self) -> CompositeSolution:
        integer_solution = IntegerSolution(
            self.int_lower_bound, self.int_upper_bound,self.number_of_objectives, self.number_of_constraints
        )
        float_solution = FloatSolution(
            self.float_lower_bound, self.float_upper_bound, self.number_of_objectives, self.number_of_constraints
        )

        float_solution.variables = [
            random.uniform(self.float_lower_bound[0], self.float_upper_bound[0])
        ]
        
        integer_solution.variables = [
            int(random.uniform(float(self.int_lower_bound[0]), float(self.int_upper_bound[0])))
        ]

        return CompositeSolution([integer_solution, float_solution])
    
    def get_name(self):
        return "RescueRobotProblemM"

class RescueRobotProblemA(Problem):

    def __init__(self):
        super(RescueRobotProblemA, self).__init__()

        self.number_of_constraints= 0
        self.number_of_objectives= 6
        self.number_of_variables= 2

        self.evaluationNumber = 0

        self.obj_directions=[self.MINIMIZE, self.MINIMIZE, self.MINIMIZE, self.MINIMIZE, self.MINIMIZE, self.MINIMIZE]
        self.obj_labels= ["s0s1", "s0s2", "s0s6", "s3s1", "s3s4", "s3s5"]

        self.int_lower_bound = [0]
        self.int_upper_bound = [100]
        self.float_lower_bound = [10.0]
        self.float_upper_bound = [10000.0]

    def evaluate(self, solution: CompositeSolution) -> CompositeSolution:

        
        
        self.evaluationNumber = self.evaluationNumber + 1
        battery = solution.variables[0].variables[0]
        light = solution.variables[1].variables[0]

        print("-")
        print("-")
        print("-")
        print("EVALUATING: battery = " + str(battery) + " light = " + str(light))
        print("-")
        print("-")
        print("-")
        
        sim = SimulatorRunner(battery=battery, light=light)
        sim.runSimulator()

        o1 = sim.getT1Distances()
        o2 = sim.getT2Distances()

        print("-")
        print("-")
        print("-")
        print("Evaluation number: " + str(self.evaluationNumber))
        print("Objectives: " + str(o1[0]) + " " + str(o1[1]) + " " + str(o1[2]) + " " + str(o2[0]) + " " + str(o2[1]) + " " + str(o2[2]))
        print("-")
        print("-")
        print("-")

        solution.objectives[0] = o1[0]
        solution.objectives[1] = o1[1]
        solution.objectives[2] = o1[2]
        solution.objectives[3] = o2[0]
        solution.objectives[4] = o2[1]
        solution.objectives[5] = o2[2]

        return solution




    def create_solution(self) -> CompositeSolution:
        integer_solution = IntegerSolution(
            self.int_lower_bound, self.int_upper_bound,self.number_of_objectives, self.number_of_constraints
        )
        float_solution = FloatSolution(
            self.float_lower_bound, self.float_upper_bound, self.number_of_objectives, self.number_of_constraints
        )

        float_solution.variables = [
            random.uniform(self.float_lower_bound[0], self.float_upper_bound[0])
        ]
        
        integer_solution.variables = [
            int(random.uniform(float(self.int_lower_bound[0]), float(self.int_upper_bound[0])))
        ]

        return CompositeSolution([integer_solution, float_solution])
    
    def get_name(self):
        return "RescueRobotProblemA"




if __name__ == "__main__":


    print("")
    print("WELCOME:")
    print("")
    print("Please select algorithm mode:")
    print("1. minimum distance mode")
    print("2. all distances mode")
    print("")

    selection = int(input())

    print("")


    if selection == 1:
        print("Selected mode: minimum distance mode")
        problem  = RescueRobotProblemM()
    
    elif selection == 2:
        print("selected mode: all distances mode")
        problem = RescueRobotProblemA()

    else: 
        print("invalid selection: default mode selected: minimum distance mode")
        problem  = RescueRobotProblemM()

    algorithm = NSGAII(
        problem= problem,
        population_size= 20,
        offspring_population_size= 20,
        mutation= CompositeMutation([IntegerPolynomialMutation(1, 20), PolynomialMutation(1, 20)]),
        crossover= CompositeCrossover(
            [
                IntegerSBXCrossover(probability=1.0, distribution_index=20),
                SBXCrossover(probability=1.0, distribution_index=20)
            ]
        ),
        termination_criterion=StoppingByEvaluations(max_evaluations=200)
    )

    algorithm.run()

    front = get_non_dominated_solutions(algorithm.get_result())
    print_function_values_to_file(front, 'FUN.NASGAII.RescueRobotM')
    print_variables_to_file(front, 'VAR.NASGAII.RescueRobotM')

    plot_front = Plot(title='Pareto front approximation', axis_labels=['x', 'y'])
    plot_front.plot(front, label='NSGA-RescueRobotM', filename='NSGAII-RescueRobotM', format='png')


