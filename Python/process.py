import time
import os
import sys


def process_a():
    process_b()
    process_c()
    print(
        "Proceso A - ID: ",
        os.getpid(),
        "PID: ",
        os.getppid(),
        "\n",
        end="",
        flush=True,
    )
    time.sleep(15)
    sys.exit(os.EX_OK)


def process_b():
    pid_b = os.fork()
    if pid_b == -1:
        sys.exit("Error al crear el hijo")
    if pid_b == 0:
        process_d()
        process_e()
        print(
            "Proceso B - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def process_c():
    pid_c = os.fork()
    if pid_c == -1:
        sys.exit("Error al crear el hijo")
    if pid_c == 0:
        process_f()
        print(
            "Proceso C - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def process_d():
    pid_d = os.fork()
    if pid_d == -1:
        sys.exit("Error al crear el hijo")
    if pid_d == 0:
        print(
            "Proceso D - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def process_e():
    pid_e = os.fork()
    if pid_e == -1:
        sys.exit("Error al crear el hijo")
    if pid_e == 0:
        process_g()
        process_h()
        print(
            "Proceso E - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def process_f():
    pid_f = os.fork()
    if pid_f == -1:
        sys.exit("Error al crear el hijo")
    if pid_f == 0:
        print(
            "Proceso F - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def process_g():
    pid_g = os.fork()
    if pid_g == -1:
        sys.exit("Error al crear el hijo")
    if pid_g == 0:
        print(
            "Proceso G - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def process_h():
    pid_h = os.fork()
    if pid_h == -1:
        sys.exit("Error al crear el hijo")
    if pid_h == 0:
        print(
            "Proceso H - ID: ",
            os.getpid(),
            "PID: ",
            os.getppid(),
            "\n",
            end="",
            flush=True,
        )
        time.sleep(15)
        os._exit(os.EX_OK)


def main():
    process_a()


if __name__ == "__main__":
    main()
