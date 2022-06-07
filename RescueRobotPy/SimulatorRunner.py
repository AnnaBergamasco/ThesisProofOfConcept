

from pandas import array
import sim_launcher

class SimulatorRunner():

    def __init__(
        self,
        battery,
        light,
        quality,
        obstacleSize,
        verbose = False
    ):
        super(SimulatorRunner, self).__init__()

        self.battery = battery
        self.light = light
        self.quality = quality
        self.obstacleSize = obstacleSize

        self.verbose = verbose

        self.t1Probabilities = [0,0,0]
        self.t2Probabilities = [0,0,0]
        self.t1Bounds = [0.0, 0.05, 0.955, 1.0, 0.00, 0.05]
        self.t2Bounds = [0.0, 0.05, 0.0, 0.05, 0.975, 1.0]
        # file rectangles

    def runSimulator(self) -> None:


        outputLog = sim_launcher.run_simulator([('battery', self.battery) , ('lights', self.light), ('quality', self.quality), ('obstacleSize', self.obstacleSize)])
        logLines = outputLog.split('\n')

        count = 0
        t1Mean = None
        t2Mean = None

        for s in logLines:
            if s.__contains__("Mean"):
                count = count + 1
                if count == 1:
                    t1Mean = s
                else:
                    t2Mean = s

        tokens = t1Mean.split(':')
        results = tokens[2].replace("[", "")
        results = results.replace(" ", "")
        results = results.replace("]", "")

        t1Values = results.split(",")
        tokens = t2Mean.split(':')
        results = tokens[2].replace("[", "")
        results = results.replace(" ", "")
        results = results.replace("]", "")

        t2Values = results.split(",")

        for i in range(0, 3):
            self.t1Probabilities[i] = float(t1Values[i])
            self.t2Probabilities[i] = float(t2Values[i])

        if self.verbose:
            print("-")
            print("-")
            print("-")
            print("t1 area probabilities: " + str(self.t1Probabilities[0]) + " " + str(self.t1Probabilities[1]) + " " +  str(self.t1Probabilities[2]))
            print("t2 area probabilities: " + str(self.t2Probabilities[0]) + " " + str(self.t2Probabilities[1]) + " " +  str(self.t2Probabilities[2]))
            print("-")
            print("-")
            print("-")

    def runSimulatorFast(self) -> None:

        results = sim_launcher.run_fast_try([('battery', self.battery) , ('lights', self.light), ('quality', self.quality), ('obstacleSize', self.obstacleSize)])
        self.t1Probabilities[0] = results.get('S0 e1 S1')
        self.t1Probabilities[1] = results.get('S0 e1 S2')
        self.t1Probabilities[2] = results.get('S0 e1 S6')
        self.t2Probabilities[0] = results.get('S3 e1 S1')
        self.t2Probabilities[1] = results.get('S3 e1 S4')
        self.t2Probabilities[2] = results.get('S3 e1 S5')

        if self.verbose:
            print("-")
            print("-")
            print("-")
            print("t1 area probabilities: " + str(self.t1Probabilities[0]) + " " + str(self.t1Probabilities[1]) + " " +  str(self.t1Probabilities[2]))
            print("t2 area probabilities: " + str(self.t2Probabilities[0]) + " " + str(self.t2Probabilities[1]) + " " +  str(self.t2Probabilities[2]))
            print("-")
            print("-")
            print("-")


    def distance(self, value, bound1, bound2) -> float:
        dis1 = value - bound1
        dis2 = bound2 - value
        if dis1 < dis2:
            return dis1
        else:
            return dis2

    def getT1Distances(self):
        result=[0,0,0]
        for i in range (0, 3):
            result[i] = self.distance(self.t1Probabilities[i], self.t1Bounds[i*2], self.t1Bounds[i*2+1])
        return result

    def getT2Distances(self):
        result=[0,0,0]
        for i in range (0, 3):
            result[i] = self.distance(self.t2Probabilities[i], self.t2Bounds[i*2], self.t2Bounds[i*2+1])
        return result
