ResourceAllocationField
A field for tracking resource allocations such as bandwidth or CPU cycles to network devices or services, supporting effective resource management.

from django.db.models import IntegerField
from django.core.exceptions import ValidationError

class ResourceAllocationField(IntegerField):
    description = "A field that represents the amount of a resource allocated."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value < 0:
            raise ValidationError("Resource allocation must be a non-negative integer.")
        return value
