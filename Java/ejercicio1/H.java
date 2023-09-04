package ejercicio1;

public class H {
    public static void main(String[] args) throws InterruptedException {
        String letra = "H";
        String padrePID = args[0];

        System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: " + ProcessHandle.current().parent().get().pid() + ")");
        Thread.sleep(10000);
    }
}