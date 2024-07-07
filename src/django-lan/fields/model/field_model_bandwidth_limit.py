BandwidthLimitField
This field is for managing bandwidth limits on specific network links or devices, storing values in Mbps or Gbps.

from django.db.models import IntegerField
from django.core.exceptions import ValidationError

class BandwidthLimitField(IntegerField):
    description = "A field that stores bandwidth limits in Mbps."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value < 1:  # Assuming the minimum bandwidth limit you'd want to impose is 1 Mbps
            raise ValidationError("Bandwidth limit must be at least 1 Mbps.")
        return value
