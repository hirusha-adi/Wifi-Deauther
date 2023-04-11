import subprocess
import typing as t
from src.modals.adapters import iWconfig


# output = subprocess.check_output(["ifconfig"]).decode()


with open("iwconfig.txt") as _f:
    iwconfig = _f.read()

adapters = [adapter.strip() for adapter in iwconfig.split('\n\n')]


for a in adapters:
    obj = iWconfig(output=a)
    print(obj)
