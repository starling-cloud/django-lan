Logging Level
Specify logging levels within the network management system for debugging and monitoring purposes.

from enum import Enum

class LoggingLevel(Enum):
    DEBUG = 'Debug'
    INFO = 'Info'
    WARNING = 'Warning'
    ERROR = 'Error'
    CRITICAL = 'Critical'

    def __str__(self):
        return self.value
