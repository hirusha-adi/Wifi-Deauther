class iWconfig():
    def __init__(self, output: str) -> None:
        self.output = output

        # for support
        self._error = False

        # properties
        self._name = None
        self._mode = None
        self._isConnectedToWifi = False
        self._essid = None
        self._frequency = None
        self._access_point = None
        self._bit_rate = None
        self._tx_power = None

        self.extractData()

    @property
    def name(self) -> str:
        return self._name

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def isConnected(self) -> bool:
        return self._isConnectedToWifi

    @property
    def essid(self) -> str:
        return self._essid

    @property
    def frequency(self) -> str:
        return self._frequency

    @property
    def access_point(self) -> str:
        return self._access_point

    @property
    def bitrate(self) -> str:
        return self._bit_rate

    @property
    def tx_power(self) -> str:
        return self._tx_power

    def extractData(self) -> None:

        if not self._error:
            # name
            try:
                self._name = self.output.split()[0]
            except IndexError:
                self._error = True
                return

            # mode
            for line in self.output.split('\n'):
                if 'Mode:' in line:
                    self._mode = line.split('Mode:')[1].split()[0]

            # if connected to a network
            if 'ESSID:' in self.output:
                self._isConnectedToWifi = True
                self._essid = self.output.split('ESSID:"')[1].split('"')[0]
                for line in self.output.split('\n'):
                    if 'Frequency:' in line:
                        self._frequency = line.split()[1].split(":")[-1]
                    if 'Access Point:' in line:
                        self._access_point = line.split()[-1]
                    if 'Bit Rate=' in line:
                        self._bit_rate = line.split()[1].split("=")[-1]
                    if 'Tx-Power=' in line:
                        self._tx_power = line.split('=')[-1].strip()

        else:
            return

    def __repr__(self) -> str:
        txt = f'<Adapter name="{self._name}" mode="{self._mode}" isConnected={self._isConnectedToWifi}'
        if self._isConnectedToWifi:
            txt += f' frequency="{self._frequency}" accessPoint="{self._access_point}" bitrate="{self._bit_rate}" txpower="{self._tx_power}"'
        txt += ">"
        return txt
