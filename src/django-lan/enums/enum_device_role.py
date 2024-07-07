Device Role
This enum defines roles for network devices, facilitating role-based configuration and actions.



from enum import Enum

class DeviceRole(Enum):
    ROUTER = 'Router'
    SWITCH = 'Switch'
    ACCESS_POINT = 'Access Point'
    BRIDGE = 'Bridge'

    def __str__(self):
        return self.value
