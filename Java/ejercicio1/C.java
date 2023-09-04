package ejercicio1;

public class C {
    public static void main(String[] args) {
        String letra = "C";
        String padrePID = args[0];

        System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: " + ProcessHandle.current().parent().get().pid() + ")");
        try {
            ProcessBuilder builderF = new ProcessBuilder("java", "ejercicio1/F.java", padrePID);
            builderF.inheritIO().start().waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}