import sys
import subprocess
import typing as t

from src.adapters.wireless import WirelessAdapter


def __iwconfig():
    try:
        output = subprocess.check_output(["iwconfig"]).decode()
    except FileNotFoundError:
        print(f"Unable to check for wireless adapters using the 'iwconfig' command. Output is 'iwconfig: command not found'")
        sys.exit()

    adapters = [adapter.strip() for adapter in output.split('\n\n')]
    return adapters


def getAdapters() -> t.List[WirelessAdapter]:
    return [WirelessAdapter(output=a) for a in __iwconfig()]
