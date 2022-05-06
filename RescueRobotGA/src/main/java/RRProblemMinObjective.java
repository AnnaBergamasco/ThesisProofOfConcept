import org.apache.commons.math3.analysis.function.Min;
import org.uma.jmetal.problem.AbstractGenericProblem;
import org.uma.jmetal.solution.compositesolution.CompositeSolution;
import org.uma.jmetal.solution.doublesolution.DoubleSolution;
import org.uma.jmetal.solution.doublesolution.impl.DefaultDoubleSolution;
import org.uma.jmetal.solution.integersolution.IntegerSolution;
import org.uma.jmetal.solution.integersolution.impl.DefaultIntegerSolution;
import org.uma.jmetal.util.bounds.Bounds;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RRProblemMinObjective extends AbstractGenericProblem<CompositeSolution> {

    private List<Bounds<Integer>> batteryBound;
    private List<Bounds<Double>> lightBound;
    private int evaluationNumber;

    public RRProblemMinObjective(){
        setNumberOfVariables(2);
        setNumberOfObjectives(2);
        setNumberOfConstraints(0);
        setName("RRMinObjective");

        batteryBound = new ArrayList<>(1);
        lightBound = new ArrayList<>(1);

        batteryBound.add(Bounds.create(0, 100));
        lightBound.add(Bounds.create(10.0, 10000.0));
        this.evaluationNumber = 0;

    }

    @Override
    public CompositeSolution evaluate(CompositeSolution s) {

        this.evaluationNumber++;

        SimulatorRunner simulator = new SimulatorRunner(  ((IntegerSolution) s.variables().get(0)).variables().get(0), ((DoubleSolution) s.variables().get(1)).variables().get(0));
        try {
            simulator.runSimulator();
        } catch (Exception e){
            System.out.println(e.getMessage());
        }

        double o1 = 100, o2 = 100;
        ArrayList<Double> t1Distances = simulator.getT1Distances();
        ArrayList<Double> t2Distances = simulator.getT2Distances();


        for(int i = 0; i < 3; i++){
            if (t1Distances.get(i) < o1){
                o1 = t1Distances.get(i);
            }
            if (t2Distances.get(i) < o2){
                o2 = t2Distances.get(i);
            }
        }

        System.out.println("Evaluation number: " + evaluationNumber);
        System.out.println("Objectives: " + o1 + " " + o2);
        System.out.println("-");
        s.objectives()[0] = o1;
        s.objectives()[1] = o2;

        return s;
    }

    @Override
    public CompositeSolution createSolution() {
        IntegerSolution battery = new DefaultIntegerSolution(getNumberOfObjectives(), getNumberOfConstraints(), batteryBound);
        DoubleSolution light = new DefaultDoubleSolution(getNumberOfObjectives(), getNumberOfConstraints(), lightBound);
        return new CompositeSolution(Arrays.asList(battery, light));
    }

}
