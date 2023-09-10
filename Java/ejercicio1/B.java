package ejercicio1;

public class B
{

  public static void main(String[] args)
  {
    String letra = "B";

    System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: "
        + ProcessHandle.current().parent().get().pid() + ")");
    try
    {
      ProcessBuilder builderD = new ProcessBuilder("java", "ejercicio1/D.java");
      ProcessBuilder builderE = new ProcessBuilder("java", "ejercicio1/E.java");

      builderD.inheritIO().start();
      builderE.inheritIO().start().waitFor();
      builderD.waitFor();
    } catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}