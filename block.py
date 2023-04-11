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
from src.adapters.wireless import WirelessAdapter


# output = subprocess.check_output(["ifconfig"]).decode()


with open("iwconfig.txt") as _f:
    iwconfig = _f.read()

adapters = [adapter.strip() for adapter in iwconfig.split('\n\n')]


for a in adapters:
    obj = WirelessAdapter(output=a)
    print(obj)
