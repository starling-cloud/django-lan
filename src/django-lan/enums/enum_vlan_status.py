VLAN Status
Manage and monitor VLAN configurations with predefined statuses.


from enum import Enum

class VLANStatus(Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    CONFIGURING = 'Configuring'

    def __str__(self):
        return self.value
