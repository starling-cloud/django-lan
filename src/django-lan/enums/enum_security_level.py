Security Level
Set predefined security levels that can be applied to network segments or devices to simplify security management.


from enum import Enum

class SecurityLevel(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

    def __str__(self):
        return self.value
