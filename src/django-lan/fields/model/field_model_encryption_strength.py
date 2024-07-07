EncryptionStrengthField
A field to specify and validate the encryption strength used in network security settings, measured in bits.


from django.db.models import IntegerField
from django.core.exceptions import ValidationError

class EncryptionStrengthField(IntegerField):
    description = "A field to store and validate encryption strength in bits."

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        valid_strengths = [128, 192, 256]  # Typical AES key lengths
        if value not in valid_strengths:
            raise ValidationError("Invalid encryption strength. Valid options are 128, 192, or 256 bits.")
        return value
