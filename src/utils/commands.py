import sys
import subprocess
import typing as t

from src.adapters.wireless import WirelessAdapter
from src.utils.console import *


def __iwconfig():
    try:
        output = subprocess.check_output(["iwconfig"]).decode()
    except FileNotFoundError:
        red(f"Unable to check for wireless adapters using the 'iwconfig' command. 'iwconfig' command is not found")
        sys.exit()

    adapters = [adapter.strip() for adapter in output.split("\n\n")]
    return adapters


def getAdapters() -> t.List[WirelessAdapter]:
    return [WirelessAdapter(output=a) for a in __iwconfig()]
