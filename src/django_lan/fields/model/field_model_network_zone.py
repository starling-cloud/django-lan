NetworkZoneField
A field for defining network zones such as DMZ, internal, external, which is crucial for security and traffic management.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkZoneField(CharField):
    description = "A field to define network zones."

    ZONE_CHOICES = [
        ("DMZ", "DMZ"),
        ("INTERNAL", "Internal"),
        ("EXTERNAL", "External"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.ZONE_CHOICES
        kwargs["max_length"] = 8  # To cover "External"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.ZONE_CHOICES):
            raise ValidationError("Invalid network zone.")
        return value
