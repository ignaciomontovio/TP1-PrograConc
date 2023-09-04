package ejercicio1;

public class A {
    public static void main(String[] args) {
        String procesoAPID = Long.toString(ProcessHandle.current().pid());
       
        System.out.println("A (PID: " + procesoAPID + ", PID Padre: " + ProcessHandle.current().parent().get().pid() + ")");
        
        
        try {
            ProcessBuilder builderB = new ProcessBuilder("java", "ejercicio1/B.java", procesoAPID);
            ProcessBuilder builderC = new ProcessBuilder("java", "ejercicio1/C.java", procesoAPID);

            builderB.inheritIO().start().waitFor();
            builderC.inheritIO().start().waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    
}