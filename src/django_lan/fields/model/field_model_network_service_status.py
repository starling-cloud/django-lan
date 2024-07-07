NetworkServiceStatusField
A field to track the status of various network services, such as whether they are active, inactive, or in maintenance.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkServiceStatusField(CharField):
    description = "A field to track the operational status of network services."

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("MAINTENANCE", "Maintenance"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.STATUS_CHOICES
        kwargs["max_length"] = 11  # Maximum length of the choices
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.STATUS_CHOICES):
            raise ValidationError("Invalid service status.")
        return value
