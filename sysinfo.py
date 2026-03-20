import os
import getpass
import socket
def show_sysinfo():
    hostname = socket.gethostname()
    user = getpass.getuser()
    cwd = os.getcwd()
    print(f"Hostname: {hostname}")
    print(f"User: {user}")
    print(f"Current Directory {cwd}")
