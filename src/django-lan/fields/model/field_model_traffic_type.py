TrafficTypeField
A field designed to categorize network traffic types, useful for monitoring and managing Quality of Service (QoS) policies.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class TrafficTypeField(CharField):
    description = "A field that categorizes traffic types for network management."

    TRAFFIC_TYPES = [
        ("VOIP", "VoIP"),
        ("STREAM", "Streaming"),
        ("DATA", "Data"),
        ("CONTROL", "Control"),
        ("UNKNOWN", "Unknown"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.TRAFFIC_TYPES
        kwargs["max_length"] = 7  # Accommodate the longest choice
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.TRAFFIC_TYPES):
            raise ValidationError("Invalid traffic type specified.")
        return value
