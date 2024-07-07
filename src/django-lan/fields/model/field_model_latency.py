LatencyField
This field measures network latency, storing values in milliseconds, ensuring that the entered values are valid for network performance assessments.


from django.db.models import IntegerField
from django.core.exceptions import ValidationError

class LatencyField(IntegerField):
    description = "A field that stores network latency in milliseconds."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value < 0:
            raise ValidationError("Latency must be a non-negative integer.")
        return value
