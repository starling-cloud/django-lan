FirewallStatusField
This field manages the status of a firewall setting, such as active, inactive, or in audit mode.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class FirewallStatusField(CharField):
    description = "A field that tracks the status of firewall settings."

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("AUDIT", "Audit Mode"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.STATUS_CHOICES
        kwargs["max_length"] = 8  # Enough for "Inactive"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.STATUS_CHOICES):
            raise ValidationError("Invalid firewall status.")
        return value
