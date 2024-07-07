RedundancyModeField
A field that represents the redundancy mode of network components, essential for managing failover and high availability configurations.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class RedundancyModeField(CharField):
    description = "A field to specify the redundancy mode of network components."

    MODE_CHOICES = [
        ("NONE", "No Redundancy"),
        ("SIMPLE", "Simple Redundancy"),
        ("N_PLUS_ONE", "N+1 Redundancy"),
        ("N_PLUS_TWO", "N+2 Redundancy"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.MODE_CHOICES
        kwargs["max_length"] = 10  # Enough for "N_PLUS_TWO"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.MODE_CHOICES):
            raise ValidationError("Invalid redundancy mode.")
        return value
