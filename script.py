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

output = subprocess.check_output("iwconfig").decode()
adapters = [adapter.strip() for adapter in output.split("\n\n")]

for adapter in adapters:
    try:
        name = adapter.split()[0]
    except:
        print(f"Error in adapter: {name}")

    if "Mode" in adapter:
        print(adapter)
    else:
        print(f"Error in adapter: {name}")
