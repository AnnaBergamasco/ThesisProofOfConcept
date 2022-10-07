
import subprocess
from RadarPlot import RadarPlot


def main():
    min_low_bounds = [10, 10, 10, 10, 10, 10]
    min_hi_bounds = [-10, -10, -10, -10, -10, -10]
    avg_low_bounds = [10, 10, 10, 10, 10, 10]
    avg_hi_bounds = [-10, -10, -10, -10, -10, -10]

    for i in range(1, 21):
        test_out = subprocess.run(["python3", "/home/anna/RescueRobotGA/RescueRobotPy/RescueRobotPymoo.py", "-a", "-f", "-s 30", "-n 30", "AGEMOEA", "-o prova" + str(i) + ".txt"], stdout=subprocess.PIPE, text = True)
        logLines = (test_out.stdout).split('\n')

        for s in logLines:
            if s.__contains__("Minimum S0 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[0] = min(result, min_low_bounds[0])
                min_hi_bounds[0] = max(result, min_hi_bounds[0])
            if s.__contains__("Minimum S0 e1 S2 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[1] = min(result, min_low_bounds[1])
                min_hi_bounds[1] = max(result, min_hi_bounds[1])
            if s.__contains__("Minimum S0 e1 S6 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[2] = min(result, min_low_bounds[2])
                min_hi_bounds[2] = max(result, min_hi_bounds[2])
            if s.__contains__("Minimum S3 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[3] = min(result, min_low_bounds[3])
                min_hi_bounds[3] = max(result, min_hi_bounds[3])
            if s.__contains__("Minimum S3 e1 S4 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[4] = min(result, min_low_bounds[4])
                min_hi_bounds[4] = max(result, min_hi_bounds[4])
            if s.__contains__("Minimum S3 e1 S5 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                min_low_bounds[5] = min(result, min_low_bounds[5])
                min_hi_bounds[5] = max(result, min_hi_bounds[5])
            if s.__contains__("Average S0 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[0] = min(result, avg_low_bounds[0])
                avg_hi_bounds[0] = max(result, avg_hi_bounds[0])
            if s.__contains__("Average S0 e1 S2 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[1] = min(result, avg_low_bounds[1])
                avg_hi_bounds[1] = max(result, avg_hi_bounds[1])
            if s.__contains__("Average S0 e1 S6 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[2] = min(result, avg_low_bounds[2])
                avg_hi_bounds[2] = max(result, avg_hi_bounds[2])
            if s.__contains__("Average S3 e1 S1 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[3] = min(result, avg_low_bounds[3])
                avg_hi_bounds[3] = max(result, avg_hi_bounds[3])
            if s.__contains__("Average S3 e1 S4 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[4] = min(result, avg_low_bounds[4])
                avg_hi_bounds[4] = max(result, avg_hi_bounds[4])
            if s.__contains__("Average S3 e1 S5 distance: "):
                tokens = s.split(':')
                result = float(tokens[1].replace(" ", ""))
                avg_low_bounds[5] = min(result, avg_low_bounds[5])
                avg_hi_bounds[5] = max(result, avg_hi_bounds[5])

    print(min_low_bounds)
    print(min_hi_bounds)       
    print(avg_low_bounds)
    print(avg_hi_bounds) 

    radarPlot = RadarPlot(min_low_bounds, min_hi_bounds, avg_low_bounds, avg_hi_bounds)
    radarPlot.makePlot()

if __name__ == "__main__":
    main()