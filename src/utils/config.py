import subprocess
import time

from src.adapters.wireless import WirelessAdapter
from src.utils import commands
from src.utils.console import *


def spoofMACaddress(adapter: WirelessAdapter) -> None:
    # ---------------------
    # ifconfig wlan0 down
    # macchanger -r wlan0
    # ifconfig wlan0 up
    # ---------------------
    stuff = [
        {
            "message": f"Disabling {adapter.name}",
            "message2": "Running {cmnd}",
            "command": ["ifconfig", adapter.name, "down"]
        },
        {
            "message": f"Changing MAC Address of {adapter.name}",
            "message2": "Running {cmnd}",
            "command": ["macchanger", "-r", adapter.name]
        },
        {
            "message": f"Enabling {adapter.name}",
            "message": "Running {cmnd}",
            "command": ["ifconfig", adapter.name, "up"]
        }
    ]
    for dic in stuff:
        blue(dic['message'])
        try:
            blue(dic["message2"].format(cmnd=' '.join(dic["command"])))
            subprocess.check_call(dic["command"])
        except subprocess.CalledProcessError as e:
            red("Command failed with error code:", e.returncode)


def __setMonitorModeAuto(adapter: WirelessAdapter) -> None:
    # ---------------------
    # airmon-ng start wlan0
    # ---------------------

    spoofMACaddress()

    blue(f"Enabling Monitor Mode using the aircrack-ng suite {adapter.name}")
    try:
        blue(f"Running airmon-ng start {adapter.name}")
        subprocess.check_call(["airmon-ng", "start", adapter.name])
    except subprocess.CalledProcessError as e:
        red("Command failed with error code:", e.returncode)


def __setMonitorModeCustom(adapter: WirelessAdapter) -> None:
    # ---------------------
    # ifconfig wlan0 down
    # macchanger -r wlan0
    # iwconfig wlan0 mode monitor
    # ifconfig wlan0 up
    # ---------------------
    stuff = [
        {
            "message": f"Disabling {adapter.name}",
            "message2": "Running {cmnd}",
            "command": ["ifconfig", adapter.name, "down"]
        },
        {
            "message": f"Changing MAC Address of {adapter.name}",
            "message2": "Running {cmnd}",
            "command": ["macchanger", "-r", adapter.name]
        },
        {
            "message": f"Enabling Monitor Mode for {adapter.name}",
            "message2": "Running {cmnd}",
            "command": ["iwconfig", adapter.name, "mode", "monitor"]
        },
        {
            "message": f"Enabling {adapter.name}",
            "message": "Running {cmnd}",
            "command": ["ifconfig", adapter.name, "up"]
        }
    ]
    for dic in stuff:
        blue(dic['message'])
        try:
            blue(dic["message2"].format(cmnd=' '.join(dic["command"])))
            subprocess.check_call(dic["command"])
        except subprocess.CalledProcessError as e:
            red("Command failed with error code:", e.returncode)


def setMonitorMode(adapter: WirelessAdapter) -> None:
    blue("Killing unwanted processes")
    try:
        blue("Running: 'airmon-ng check kill'")
        subprocess.check_call(["airmon-ng", "check", "kill"])
    except subprocess.CalledProcessError as e:
        red("Command failed with error code:", e.returncode)

    __setMonitorModeAuto(adapter=adapter)
    __setMonitorModeCustom(adapter=adapter)

    for adp2 in commands.getAdapters():
        if adp2.name == adapter.name:
            print(f"Mode of {adapter.name}: {adp2.mode}")
            if adp2.mode == "Monitor":
                print(f"{adapter.name} set to Monitor Mode successfully.")
            else:
                print("Mode has not been changed to Monitor. Trying again in 3 seconds.")
                time.sleep(3)
                setMonitorMode()
