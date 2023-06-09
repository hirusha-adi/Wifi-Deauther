"""
-----------------------------
enable monitor mode
-----------------------------
ifconfig
airmon-ng check
airmon-ng check kill
airmon-ng start wlan0
sudo iwconfig
-----------------------------
disable monitor mode
-----------------------------
sudo airmon-ng stop wlan0
sudo systemctl start NetworkManager
-----------------------------


-----------------------------
airodump-ng wlan0
-----------------------------
aireplay-ng --deauth <number of deauth packets> -a <target BSSID> wlan0
-----------------------------
"""

import subprocess
import typing as t
import sys

from src.adapters.wireless import WirelessAdapter
from src.utils import commands
from src.utils import config
from src.utils.console import *

workingAdapter = None


def selectAdapter() -> WirelessAdapter:
    adapters = commands.getAdapters()
    c = 0
    print("[?] Please select an adpater -> ")
    for adapter in adapters:
        print(f"\t{c}: {adapter.name}")
        c += 1
    while True:
        try:
            indx = int(input("?> "))
            if indx <= c:
                break
        except ValueError:
            print("[?] Please enter a number> ")
    return adapters[indx]


def main():
    global workingAdapter
    workingAdapter = selectAdapter()
    config.setMonitorMode(adapter=workingAdapter)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"error occured: {e}")
    finally:
        config.restore(adapter=workingAdapter)
