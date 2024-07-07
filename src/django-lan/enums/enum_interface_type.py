Interface Type
Specify the types of network interfaces to allow detailed configuration and compatibility checks.


from enum import Enum

class InterfaceType(Enum):
    ETHERNET = 'Ethernet'
    WIFI = 'Wi-Fi'
    FIBER_OPTIC = 'Fiber Optic'
    USB = 'USB'

    def __str__(self):
        return self.value
