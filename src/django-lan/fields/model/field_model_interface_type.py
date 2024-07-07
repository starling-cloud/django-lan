InterfaceTypeField
This field categorizes the types of network interfaces, such as Ethernet, Wi-Fi, Fiber, etc., essential for inventory and configuration.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class InterfaceTypeField(CharField):
    description = "A field that categorizes types of network interfaces."

    INTERFACE_TYPES = [
        ("ETH", "Ethernet"),
        ("WIFI", "Wi-Fi"),
        ("FIB", "Fiber Optic"),
        ("USB", "USB"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.INTERFACE_TYPES
        kwargs["max_length"] = 4  # Enough to cover the abbreviation
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.INTERFACE_TYPES):
            raise ValidationError("Invalid interface type.")
        return value
