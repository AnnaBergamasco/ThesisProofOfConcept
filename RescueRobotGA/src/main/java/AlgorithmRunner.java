import org.uma.jmetal.algorithm.Algorithm;
import org.uma.jmetal.algorithm.multiobjective.nsgaii.NSGAIIBuilder;
import org.uma.jmetal.lab.visualization.plot.impl.Plot2D;
import org.uma.jmetal.operator.crossover.CrossoverOperator;
import org.uma.jmetal.operator.crossover.impl.CompositeCrossover;
import org.uma.jmetal.operator.crossover.impl.IntegerSBXCrossover;
import org.uma.jmetal.operator.crossover.impl.SBXCrossover;
import org.uma.jmetal.operator.mutation.MutationOperator;
import org.uma.jmetal.operator.mutation.impl.CompositeMutation;
import org.uma.jmetal.operator.mutation.impl.IntegerPolynomialMutation;
import org.uma.jmetal.operator.mutation.impl.PolynomialMutation;
import org.uma.jmetal.operator.selection.SelectionOperator;
import org.uma.jmetal.problem.Problem;
import org.uma.jmetal.solution.compositesolution.CompositeSolution;
import org.uma.jmetal.util.errorchecking.JMetalException;

import java.util.ArrayList;
import java.util.List;

public class AlgorithmRunner {

    public static void main(String[] args) throws JMetalException {

        Problem<CompositeSolution> problem;
        Algorithm<List<CompositeSolution>> algorithm;
        CrossoverOperator<CompositeSolution> crossover;
        MutationOperator<CompositeSolution> mutation;

        ArrayList<CrossoverOperator> crossovers = new ArrayList<>();
        ArrayList<MutationOperator> mutations = new ArrayList<>();

        problem = new RRProblemMinObjective();

        double crossoverProbability = 0.9;
        double crossoverDistributionIndex = 20.0;
        crossovers.add(new IntegerSBXCrossover(crossoverProbability, crossoverDistributionIndex));
        crossovers.add(new SBXCrossover(crossoverProbability, crossoverDistributionIndex));
        crossover = new CompositeCrossover(crossovers);

        double mutationProbability = 1.0 / problem.getNumberOfVariables();
        double mutationDistributionIndex = 20.0;
        mutations.add(new IntegerPolynomialMutation(mutationProbability, mutationDistributionIndex));
        mutations.add(new PolynomialMutation(mutationProbability, mutationDistributionIndex));
        mutation = new CompositeMutation(mutations);

        algorithm = new NSGAIIBuilder<CompositeSolution>(problem, crossover, mutation, 20)
                .setMaxEvaluations(200)
                .build();

        algorithm.run();

        List<CompositeSolution> population = algorithm.getResult();
        System.out.println(population);


        double[][] resultObjectives = new double[population.size()][2];

        for (int i = 0; i < population.size(); i++){
            resultObjectives[i][0] = population.get(i).objectives()[0];
            resultObjectives[i][1] = population.get(i).objectives()[1];
        }

        Plot2D objectivesPlot= new Plot2D(resultObjectives,"Objectives");
        objectivesPlot.plot();

    }

}
