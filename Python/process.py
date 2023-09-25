import time
import os
import sys

def process_b():
    pid_b = os.fork()
    if pid_b == -1:
        sys.exit("Error al crear el hijo")
    if pid_b > 0:
        process_c()
    else:
        process_d()

def process_c():
    pid_c = os.fork()
    if pid_c == -1:
        sys.exit("Error al crear el hijo")
    if pid_c > 0:
        print("Proceso A - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        sys.exit(os.EX_OK)
    else:
        process_f()

def process_d():
    pid_d = os.fork()
    if pid_d == -1:
        sys.exit("Error al crear el hijo")
    if pid_d > 0:
        process_e()
    else:
        print("Proceso D - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def process_e():
    pid_e = os.fork()
    if pid_e == -1:
        sys.exit("Error al crear el hijo")
    if pid_e > 0:
        print("Proceso B - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)
    else:
        process_g()

def process_f():
    pid_f = os.fork()
    if pid_f == -1:
        sys.exit("Error al crear el hijo")
    if pid_f > 0:
        print("Proceso C - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)
    else:
        print("Proceso F - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def process_g():
    pid_g = os.fork()
    if pid_g == -1:
        sys.exit("Error al crear el hijo")
    if pid_g > 0:
        process_h()
    else:
        print("Proceso G - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def process_h():
    pid_h = os.fork()
    if pid_h == -1:
        sys.exit("Error al crear el hijo")
    if pid_h > 0:
        print("Proceso E - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)
    else:
        print("Proceso H - ID:", os.getpid(), "PID:", os.getppid(), "\n", end="", flush=True)
        time.sleep(15)
        os._exit(os.EX_OK)

def main():
    process_b()

if __name__ == '__main__':
    main()