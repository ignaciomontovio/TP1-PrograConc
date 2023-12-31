package ejercicio1;

public class E
{

  public static void main(String[] args)
  {
    String letra = "E";

    System.out.println(letra + " (PID: " + ProcessHandle.current().pid() + ", PID Padre: "
        + ProcessHandle.current().parent().get().pid() + ")");
    try
    {
      ProcessBuilder builderG = new ProcessBuilder("java", "ejercicio1/G.java");
      ProcessBuilder builderH = new ProcessBuilder("java", "ejercicio1/H.java");

      builderG.inheritIO().start();
      builderH.inheritIO().start().waitFor();
      builderG.waitFor();
    } catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
