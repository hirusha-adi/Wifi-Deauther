import subprocess


def iwconfig():
    return subprocess.check_output(["ifconfig"]).decode().split("\n\n")
