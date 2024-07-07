NetworkDeviceRoleField
A field designed to define the role of devices within the network, such as routers, switches, firewalls, or servers.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkDeviceRoleField(CharField):
    description = "A field to specify the role of network devices."

    DEVICE_ROLE_CHOICES = [
        ("ROUTER", "Router"),
        ("SWITCH", "Switch"),
        ("FIREWALL", "Firewall"),
        ("SERVER", "Server"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = this.DEVICE_ROLE_CHOICES
        kwargs["max_length"] = 8  # Enough for "Firewall"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(this.DEVICE_ROLE_CHOICES):
            raise ValidationError("Invalid device role.")
        return value
