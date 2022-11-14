
import sim_launcher_uavs

class SimulatorRunnerUAVS():

    def __init__(
        self,
        formation,
        speed,
        counter,
        weather,
        time,
        ranget,
        nthreat,
        #TODO verbose mode
    ): 
        super(SimulatorRunnerUAVS, self).__init__()

        self.formation = formation
        self.speed = speed
        self.counter = counter
        self.weather = weather
        self.time = time
        self.ranget = ranget
        self.nthreat = nthreat

        self.t1Probabilities = [0,0,0]
        self.t2Probabilities = [0,0,0,0]
        self.t3Probabilities = [0,0,0,0]
        self.t4Probabilities = [0,0,0]

        self.t1Bounds = [0.75, 0.82, 0.02, 0.07, 0.13, 0.17]
        self.t2Bounds = [0.4, 0.45, 0.4, 0.45, 0.0, 0.2, 0.0, 0.1]
        self.t3Bounds = [0.45, 0.47, 0.45, 0.48, 0.0, 0.06, 0.0, 0.05]
        self.t4Bounds = [0.9, 0.97, 0.0, 0.023, 0.0, 0.05]
    
    #TODO: add normal mode

    def runSimulatorFast(self) -> None:
        
        results = sim_launcher_uavs.run_fast_try([('formation', self.formation), ('flying_speed', self.speed), ('countermeasure', self.counter), ('weather', self.weather), ('day_time', self.time), ('threat_range', self.ranget), ('threats', self.nthreat)])

        self.t1Probabilities[0] = results.get('S0 sTrt S1')
        self.t1Probabilities[1] = results.get('S0 sTrt S21')
        self.t1Probabilities[2] = results.get('S0 sTrt S22')
        self.t2Probabilities[0] = results.get('S7 sTrt S6')
        self.t2Probabilities[1] = results.get('S7 sTrt S8')
        self.t2Probabilities[2] = results.get('S7 sTrt S21')
        self.t2Probabilities[2] = results.get('S7 sTrt S22')
        self.t3Probabilities[0] = results.get('S14 sTrt S13')
        self.t3Probabilities[1] = results.get('S14 sTrt S15')
        self.t3Probabilities[2] = results.get('S14 sTrt S21')
        self.t3Probabilities[2] = results.get('S14 sTrt S22')
        self.t4Probabilities[0] = results.get('S20 sTrt S19')
        self.t4Probabilities[1] = results.get('S20 sTrt S21')
        self.t4Probabilities[2] = results.get('S20 sTrt S22')

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
        result=[0,0,0,0]
        for i in range (0, 4):
            result[i] = self.distance(self.t2Probabilities[i], self.t2Bounds[i*2], self.t2Bounds[i*2+1])
        return result

    def getT3Distances(self):
        result=[0,0,0,0]
        for i in range (0, 4):
            result[i] = self.distance(self.t3Probabilities[i], self.t3Bounds[i*2], self.t3Bounds[i*2+1])
        return result

    def getT4Distances(self):
        result=[0,0,0]
        for i in range (0, 3):
            result[i] = self.distance(self.t4Probabilities[i], self.t4Bounds[i*2], self.t4Bounds[i*2+1])
        return result