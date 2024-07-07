Network Protocol Types
Enumerate supported network protocols to ensure consistent configuration across network devices.

from enum import Enum

class NetworkProtocol(Enum):
    TCP = 'TCP'
    UDP = 'UDP'
    HTTP = 'HTTP'
    HTTPS = 'HTTPS'
    FTP = 'FTP'

    def __str__(self):
        return self.value
