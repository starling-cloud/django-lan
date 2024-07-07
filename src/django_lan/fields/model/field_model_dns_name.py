DNSNameField
A field to store and validate DNS names, ensuring they adhere to DNS naming conventions.


from django.core.exceptions import ValidationError
from django.db.models import CharField
import re

class DNSNameField(CharField):
    description = "A DNS name field with validation."

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255  # Typical max length for DNS names
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if not re.match(r'^(?!-)[A-Z\d-]{1,63}(?<!-)(\.(?!-)[A-Z\d-]{1,63}(?<!-))*$', value, re.IGNORECASE):
            raise ValidationError("Invalid DNS name format")
        return value
