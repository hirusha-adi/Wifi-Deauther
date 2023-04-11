import sys
import subprocess


def iwconfig():
    try:
        output = subprocess.check_output(["iwconfig"]).decode()
    except FileNotFoundError:
        print(f"Unable to check for wireless adapters using the 'iwconfig' command. Output is 'iwconfig: command not found'")
        sys.exit()

    adapters = [adapter.strip() for adapter in output.split('\n\n')]
    return adapters
