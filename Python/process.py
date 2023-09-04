import time
import os
import sys

pidB = os.fork()
if pidB == -1:
  sys.exit("Error al crear el hijo")
if pidB > 0:
  pidC = os.fork()
  if pidC == -1:
    sys.exit("Error al crear el hijo")
  if pidC > 0:
    print("Proceso A - ID: ", os.getpid(), "PID: ", os.getppid())
    time.sleep(15)
    sys.exit(os.EX_OK)
  else:
    pidF = os.fork()
    if pidF == -1:
      sys.exit("Error al crear el hijo")
    if pidF > 0:
      print("Proceso C - ID: ", os.getpid(), "PID: ", os.getppid())
      time.sleep(15)
      os._exit(os.EX_OK)
    else:
      print("Proceso F - ID: ", os.getpid(), "PID: ", os.getppid())
      time.sleep(15)
      os._exit(os.EX_OK)
else:
  pidD = os.fork()
  if pidD == -1:
    sys.exit("Error al crear el hijo")
  if pidD > 0:
    pidE = os.fork()
    if pidE == -1:
      sys.exit("Error al crear el hijo")
    if pidE > 0:
      print("Proceso B - ID: ", os.getpid(), "PID: ", os.getppid())
      time.sleep(15)
      os._exit(os.EX_OK)
    else:
      pidG = os.fork()
      if pidG == -1:
        sys.exit("Error al crear el hijo")
      if pidG > 0:
        pidH = os.fork()
        if pidH == -1:
          sys.exit("Error al crear el hijo")
        if pidH > 0:
          print("Proceso E - ID: ", os.getpid(), "PID: ", os.getppid())
          time.sleep(15)
          os._exit(os.EX_OK)
        else:
          print("Proceso H - ID: ", os.getpid(), "PID: ", os.getppid())
          time.sleep(15)
          os._exit(os.EX_OK)
      else:
        print("Proceso G - ID: ", os.getpid(), "PID: ", os.getppid())
        time.sleep(15)
        os._exit(os.EX_OK)
  else:
    print("Proceso D - ID: ", os.getpid(), "PID: ", os.getppid())
    time.sleep(15)
    os._exit(os.EX_OK)