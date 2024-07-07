IncidentResponseField
This field categorizes incident response levels to enable efficient management of potential network threats or disruptions.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class IncidentResponseField(CharField):
    description = "A field to categorize incident response levels."

    RESPONSE_LEVEL_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.RESPONSE_LEVEL_CHOICES
        kwargs["max_length"] = 8  # Enough for "Critical"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.RESPONSE_LEVEL_CHOICES):
            raise ValidationError("Invalid incident response level.")
        return value
