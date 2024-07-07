NetworkSpeedField
A field for network speed that automatically handles conversion between Mbps, Gbps, etc.


from django.db.models import BigIntegerField
from django.core.exceptions import ValidationError
import re

class NetworkSpeedField(BigIntegerField):
    description = "A field to store network speeds with automatic conversion."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if isinstance(value, str):
            match = re.match(r'^(\d+)([MmGgTt])[Bb]ps$', value)
            if match:
                speed, unit = int(match.group(1)), match.group(2).upper()
                if unit == 'G':
                    value = speed * 1000
                elif unit == 'T':
                    value = speed * 1000000
                else:
                    value = speed
            else:
                raise ValidationError("Invalid speed format. Use Mbps, Gbps, or Tbps.")
        return value
