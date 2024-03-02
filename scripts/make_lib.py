from sys import path as spath


def errexit():
    print("Compilation error, exiting")
    exit(1)


spath.append("./submodules/CircuitMPY/")
import circuitmpy

circuitmpy.fetch_mpy()

try:
    print(f"ftp_server.py -> ftp_server.mpy")
    circuitmpy.compile_mpy(f"./submodules/CircuitPython_FTP_Server/src/ftp_server.py", f"./files/ftp_server.mpy")
except:
    errexit()

print()
