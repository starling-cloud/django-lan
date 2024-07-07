ProtocolVersionField
This field allows specifying versions of protocols used, such as HTTP 1.1, HTTP/2, or SMTP, ensuring precise communication protocol management.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class ProtocolVersionField(CharField):
    description = "A field to specify protocol versions."

    PROTOCOL_VERSION_CHOICES = [
        ("HTTP_1_1", "HTTP 1.1"),
        ("HTTP_2", "HTTP/2"),
        ("SMTP", "SMTP"),
        ("FTP", "FTP"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.PROTOCOL_VERSION_CHOICES
        kwargs["max_length"] = 7  # To cover "HTTP/2"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.PROTOCOL_VERSION_CHOICES):
            raise ValidationError("Invalid protocol version.")
        return value
