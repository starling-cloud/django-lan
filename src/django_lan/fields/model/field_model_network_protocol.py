NetworkProtocolField
A field for selecting network protocols from a predefined list of common choices like TCP, UDP, ICMP, etc.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkProtocolField(CharField):
    description = "A field that stores network protocols with validation."
    PROTOCOL_CHOICES = [
        ("TCP", "TCP"),
        ("UDP", "UDP"),
        ("ICMP", "ICMP"),
        ("HTTP", "HTTP"),
        ("HTTPS", "HTTPS"),
        ("FTP", "FTP")
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.PROTOCOL_CHOICES
        kwargs["max_length"] = 5  # Max length of protocol names
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.PROTOCOL_CHOICES):
            raise ValidationError(f"Invalid network protocol: {value}")
        return value
