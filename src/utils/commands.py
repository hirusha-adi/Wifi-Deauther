import sys
import subprocess


def iwconfig():
    output = subprocess.check_output(["iwconfig"]).decode()
    print(output)
    if "command not found" in output:
        print(f"Unable to check for wireless adapters using the 'iwconfig' command. Output is 'iwconfig: command not found'")
        sys.exit()
    adapters = [adapter.strip() for adapter in output.split('\n\n')]
    return adapters
