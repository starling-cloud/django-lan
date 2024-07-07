HardwareAddressTypeField
This field can be used to distinguish between different types of hardware addresses, such as MAC addresses, WWNs (World Wide Names), etc.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class HardwareAddressTypeField(CharField):
    description = "A field to distinguish between types of hardware addresses."

    ADDRESS_TYPES = [
        ("MAC", "MAC Address"),
        ("WWN", "World Wide Name"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.ADDRESS_TYPES
        kwargs["max_length"] = 3  # Sufficient for the abbreviation
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.ADDRESS_TYPES):
            raise ValidationError("Invalid hardware address type specified.")
        return value
