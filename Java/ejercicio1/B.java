package ejercicio1;

public class B {
    public static void main(String[] args) {
        String letra = "B";
        String padrePID = args[0];
        //System.out.println("VER" + args[0]);

        System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: " + ProcessHandle.current().parent().get().pid() + ")");
        try {
            ProcessBuilder builderD = new ProcessBuilder("java", "ejercicio1/D.java", padrePID);
            ProcessBuilder builderE = new ProcessBuilder("java", "ejercicio1/E.java", padrePID);

            builderD.inheritIO().start().waitFor();
            builderE.inheritIO().start().waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
        

    }
    

}