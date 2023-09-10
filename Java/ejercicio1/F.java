package ejercicio1;

public class F
{

  public static void main(String[] args) throws InterruptedException
  {
    String letra = "F";

    System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: "
        + ProcessHandle.current().parent().get().pid() + ")");
    Thread.sleep(10000);
  }
}