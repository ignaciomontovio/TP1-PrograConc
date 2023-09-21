import time
import os
import sys

def processA():
    processB()
    processC()
    print("Proceso A - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
    time.sleep(15)
    sys.exit(os.EX_OK)  

def processB():
    pidB = os.fork()
    if pidB == -1:
        sys.exit("Error al crear el hijo")
    if pidB == 0:
        processD()
        processE()
        print("Proceso B - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def processC():
  pidC = os.fork()
  if pidC == -1:
    sys.exit("Error al crear el hijo")
  if pidC == 0:
    processF()
    print("Proceso C - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
    time.sleep(15)
    os._exit(os.EX_OK)

def processD():
  pidD = os.fork()
  if pidD == -1:
    sys.exit("Error al crear el hijo")
  if pidD == 0:
    print("Proceso D - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
    time.sleep(15)
    os._exit(os.EX_OK)


def processE():
    pidE = os.fork()
    if pidE == -1:
      sys.exit("Error al crear el hijo")
    if pidE == 0:
        processG()
        processH()
        print("Proceso E - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def processF ():
    pidF = os.fork()
    if pidF == -1:
      sys.exit("Error al crear el hijo")
    if pidF == 0:
      print("Proceso F - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
      time.sleep(15)
      os._exit(os.EX_OK)

def processG():
    pidG = os.fork()
    if pidG == -1:
        sys.exit("Error al crear el hijo")
    if pidG == 0:
        print("Proceso G - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def processH():
    pidH = os.fork()
    if pidH == -1:
        sys.exit("Error al crear el hijo")
    if pidH == 0:
        print("Proceso H - ID: ", os.getpid(), "PID: ", os.getppid(),"\n",end="",flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def main():
    processA()

if __name__ == '__main__':
   main()
