NetworkLinkStatusField
A field to reflect the current operational status of network links, such as up, down, or testing.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkLinkStatusField(CharField):
    description = "A field that indicates the status of network links."

    STATUS_CHOICES = [
        ("UP", "Up"),
        ("DOWN", "Down"),
        ("TESTING", "Testing"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.STATUS_CHOICES
        kwargs["max_length"] = 8  # To accommodate "Testing"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.STATUS_CHOICES):
            raise ValidationError("Invalid network link status.")
        return value
