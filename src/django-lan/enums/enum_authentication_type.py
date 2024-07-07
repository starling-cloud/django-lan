Authentication Type
Enum for different authentication methods used in network security settings.


from enum import Enum

class AuthenticationType(Enum):
    PASSWORD = 'Password'
    PUBLIC_KEY = 'Public Key'
    BIOMETRIC = 'Biometric'
    TWO_FACTOR = 'Two Factor'

    def __str__(self):
        return self.value
