import subprocess
import time

from src.adapters.wireless import WirelessAdapter
from src.utils import commands


def setMonitorMode(adapter: WirelessAdapter) -> None:

    print("Killing unwanted processes successfully")
    try:
        print("Running: 'airmon-ng check kill'")
        subprocess.check_call(["airmon-ng", "check", "kill"])
    except subprocess.CalledProcessError as e:
        print("Command failed with error code:", e.returncode)

    print(f"Setting monitor mode for: {adapter.name}")
    try:
        print(f"Running: 'airmon-ng start {adapter.name}'")
        subprocess.check_call(["airmon-ng", "start", f"{adapter.name}"])
    except subprocess.CalledProcessError as e:
        print("Command failed with error code:", e.returncode)

    for adp2 in commands.getAdapters():
        if adp2.name == adapter.name:
            print(f"Mode of {adapter.name}: {adp2.mode}")
            if adp2.mode == "Monitor":
                return
            else:
                print("Mode has not been changed to Monitor. Trying again in 3 seconds.")
                time.sleep(3)
                setMonitorMode()
