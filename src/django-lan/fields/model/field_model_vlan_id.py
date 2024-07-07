VLANIDField
A field for handling VLAN IDs, which must be within the standard VLAN range (1-4095).


from django.core.exceptions import ValidationError
from django.db.models import IntegerField

class VLANIDField(IntegerField):
    description = "A field that stores and validates VLAN IDs."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)  # Use superclass’s cleaning logic
        if not (1 <= value <= 4095):
            raise ValidationError("VLAN ID must be between 1 and 4095")
        return value
