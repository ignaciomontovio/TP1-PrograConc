package ejercicio1;

public class E {
    public static void main(String[] args) {
        String letra = "E";
        String padrePID = args[0];

        System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: " + ProcessHandle.current().parent().get().pid() + ")");
        try {
            ProcessBuilder builderG = new ProcessBuilder("java", "ejercicio1/G.java", padrePID);
            ProcessBuilder builderH = new ProcessBuilder("java", "ejercicio1/H.java", padrePID);

            builderG.inheritIO().start().waitFor();
            builderH.inheritIO().start().waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
