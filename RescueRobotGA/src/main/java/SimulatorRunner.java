import org.apache.commons.math3.analysis.function.Min;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class SimulatorRunner {

    private double light;
    private int battery;
    //S0 e1 S1, S0 e1 S2, S0 e1 S6
    private ArrayList<Double> t1Probabilities;
    //S3 e1 S1, S3 e1 S4, S3 e1 S5
    private ArrayList<Double> t2Probabilities;
    private ArrayList<Double> t1Bounds;
    private ArrayList<Double> t2Bounds;


    public SimulatorRunner(int battery, double light) {
        this.battery = battery;
        this.light = light;
        this.t1Bounds = new ArrayList<Double>(){{
            add(0.0);
            add(0.05);
            add(0.95);
            add(1.0);
            add(0.00);
            add(0.05);
        }};
        this.t2Bounds = new ArrayList<Double>() {{
           add(0.0);
           add(0.05);
           add(0.0);
           add(0.05);
           add(0.97);
           add(1.0);
        }};
        this.t1Probabilities = new ArrayList<>();
        this.t2Probabilities = new ArrayList<>();


    }

    public void runSimulator() throws Exception{

        System.out.println("EVALUATING: battery = " + Integer.toString(this.battery) + " light = " + Double.toString(this.light));


        ProcessBuilder pb = new ProcessBuilder("python3", "sim_launcher.py", Integer.toString(this.battery), Double.toString(this.light));
        pb.directory(new File("/home/anna/Documenti/Uni/Tesi/mdp_simulator_launcher"));
        pb.environment().put("R_HOME", "/usr/lib/R");
        Process p = pb.start();
        BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String out = "ciao";
        int counter = 0;

        String[] values1 = null, values2 = null;

        while(out != null){
            if (out.contains("Mean")){

                counter++;

                String[] tokens = out.split(":");
                String results;
                results = tokens[2].replace("[","");
                results = results.replace(" ", "");
                results = results.replace("]", "");
                if(counter == 1){
                    values1 = results.split(",");

                } else {
                    values2 = results.split(",");
                }
            }

            out = in.readLine();
        }

        for(int i = 0; i < 3 && values1!=null && values2 != null; i++){
            t1Probabilities.add(Double.parseDouble(values1[i]));
            t2Probabilities.add(Double.parseDouble(values2[i]));
        }

        System.out.println("t1 area probabilities: " + t1Probabilities);
        System.out.println("t2 area probabilities: " + t2Probabilities);
        System.out.println("-");

    }

    public ArrayList<Double> getT1Probabilities() {
        return t1Probabilities;
    }

    public ArrayList<Double> getT2Probabilities() {
        return t2Probabilities;
    }

    // acceptable intervals:
    // t1: [0.0, 0.02] [0.95, 0.97] [0.02, 0.05]
    // t2: [0.0, 0.015] [0.0, 0.015] [0.98, 1.0]
    private double distance(double value, double bound1, double bound2){
        double dis1, dis2;
        dis1 = value - bound1;
        dis2 = bound2 - value;
        if (dis1 < dis2){
            return dis1;
        } else {
            return  dis2;
        }
    }

    public ArrayList<Double> getT1Distances(){
        ArrayList<Double> result1 = new ArrayList<>();
        for(int i = 0; i < 3; i++){
            result1.add(distance(t1Probabilities.get(i), t1Bounds.get(i*2), t1Bounds.get(i*2 + 1)));
        }
        return result1;
    }

    public ArrayList<Double> getT2Distances() {
        ArrayList<Double> result2 = new ArrayList<>();
        for(int i = 0; i < 3; i++){
            result2.add(distance(t2Probabilities.get(i), t2Bounds.get(i*2), t2Bounds.get(i*2 +1)));
        }
        return result2;
    }
}
