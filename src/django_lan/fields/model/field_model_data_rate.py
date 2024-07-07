DataRateField
A field to manage and validate data transfer rates, ensuring they're within expected ranges or formats.


from django.db.models import CharField
from django.core.exceptions import ValidationError
import re

class DataRateField(CharField):
    description = "A field to store and validate data transfer rates (e.g., Mbps, Gbps)."

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10  # Including units
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if not re.match(r'^\d+\s*(Mbps|Gbps)$', value):
            raise ValidationError("Data rate must be specified in Mbps or Gbps.")
        return value
