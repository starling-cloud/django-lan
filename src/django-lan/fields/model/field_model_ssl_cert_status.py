SSLCertStatusField
This field manages the status of SSL certificates for network services or devices, ensuring security settings are up to date.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class SSLCertStatusField(CharField):
    description = "A field that tracks the status of SSL certificates."

    STATUS_CHOICES = [
        ("VALID", "Valid"),
        ("EXPIRED", "Expired"),
        ("RENEWING", "Renewing"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.STATUS_CHOICES
        kwargs["max_length"] = 8  # Enough for "Renewing"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.STATUS_CHOICES):
            raise ValidationError("Invalid SSL certificate status.")
        return value
