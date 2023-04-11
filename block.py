import subprocess
import typing as t

# output = subprocess.check_output(["ifconfig"]).decode()


class Adapter():
    def __init__(self, output: str, _type: t.Literal["ifconfig", "iwconfig"]) -> None:
        self.output = output
        self._type = _type

        # for support
        self.error = False

        # properties
        self.name = None
        self.mode = None
        self.isConnectedToWifi = False
        self.essid = None
        self.frequency = None
        self.access_point = None
        self.bit_rate = None
        self.tx_power = None

        self.extractData()

    def extractData(self) -> None:

        if self._type == "iwconfig":

            if not self.error:
                # name
                try:
                    self.name = self.output.split()[0]
                except IndexError:
                    self.error = True
                    return

                # mode
                for line in self.output.split('\n'):
                    if 'Mode:' in line:
                        self.mode = line.split('Mode:')[1].split()[0]

                # if connected to a network
                if 'ESSID:' in self.output:
                    self.isConnectedToWifi = True
                    self.essid = self.output.split('ESSID:"')[1].split('"')[0]
                    for line in self.output.split('\n'):
                        if 'Frequency:' in line:
                            self.frequency = line.split()[1].split(":")[-1]
                        if 'Access Point:' in line:
                            self.access_point = line.split()[-1]
                        if 'Bit Rate=' in line:
                            self.bit_rate = line.split()[1]
                        if 'Tx-Power=' in line:
                            self.tx_power = line.split('=')[-1].strip()

    def __repr__(self) -> str:
        txt = f'<Adapter name="{self.name}" mode="{self.mode}" isConnected={self.isConnectedToWifi}'
        if self.isConnectedToWifi:
            txt += f' frequency="{self.frequency}" accessPoint="{self.access_point}" bitrate="{self.bit_rate}" txpower="{self.tx_power}"'
        txt += ">"
        return txt


with open("iwconfig.txt") as _f:
    iwconfig = _f.read()

adapters = [adapter.strip() for adapter in iwconfig.split('\n\n')]


for a in adapters:
    obj = Adapter(output=a, _type="iwconfig")
    print(obj)
