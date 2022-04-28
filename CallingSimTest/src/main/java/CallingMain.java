import org.python.antlr.ast.Str;

import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.SimpleScriptContext;
import java.io.*;
import java.util.List;
import java.nio.*;

public class CallingMain {

    public static void main(String[] args) throws Exception {

        ProcessBuilder pb = new ProcessBuilder("python3", "sim_launcher.py");
        pb.directory(new File("/home/anna/Documenti/Uni/Tesi/mdp_simulator_launcher"));
        pb.environment().put("R_HOME", "/usr/lib/R");
        pb.inheritIO();
        Process p = pb.start();

        /*BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String out = "ciao";

        while(out != null){
           out = in.readLine();
           System.out.println(out);
        }*/

    }

}
