ConnectionTypeField
This field manages the type of connections such as wired, wireless, VPN, etc., which is essential for configuration and maintenance of diverse network environments.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class ConnectionTypeField(CharField):
    description = "A field to specify the type of network connections."

    CONNECTION_CHOICES = [
        ("WIRED", "Wired"),
        ("WIRELESS", "Wireless"),
        ("VPN", "VPN"),
        ("VIRTUAL", "Virtual"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.CONNECTION_CHOICES
        kwargs["max_length"] = 8  # Enough for "Wireless"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.CONNECTION_CHOICES):
            raise ValidationError("Invalid connection type.")
        return value
