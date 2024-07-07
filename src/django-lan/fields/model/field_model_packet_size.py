PacketSizeField
This custom field validates the size of packets in bytes, common in settings where packet sizes need to be restricted or monitored.


from django.db.models import IntegerField
from django.core.exceptions import ValidationError

class PacketSizeField(IntegerField):
    description = "A field to store and validate packet sizes in bytes."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if not (64 <= value <= 1500):  # Standard Ethernet frame size range, can be adjusted
            raise ValidationError("Packet size must be between 64 and 1500 bytes.")
        return value
