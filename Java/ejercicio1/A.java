package ejercicio1;

public class A
{

  public static void main(String[] args)
  {
    String procesoAPID = Long.toString(ProcessHandle.current().pid());
    System.out.println("A (PID: " + procesoAPID + ", PID Padre: "
        + ProcessHandle.current().parent().get().pid() + ")");
    try
    {
      ProcessBuilder builderB = new ProcessBuilder("java", "ejercicio1/B.java");
      ProcessBuilder builderC = new ProcessBuilder("java", "ejercicio1/C.java");

      builderB.inheritIO().start();
      builderC.inheritIO().start().waitFor();
      builderB.waitFor();
    } catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}