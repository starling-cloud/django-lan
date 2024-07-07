Traffic Type
Define different types of network traffic to handle specific Quality of Service (QoS) settings or monitoring rules.



from enum import Enum

class TrafficType(Enum):
    VOIP = 'VoIP'
    STREAMING = 'Streaming'
    DATA = 'Data'
    CONTROL = 'Control'
    UNKNOWN = 'Unknown'

    def __str__(self):
        return self.value
