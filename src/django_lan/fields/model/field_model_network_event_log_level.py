NetworkEventLogLevelField
This field is for categorizing the severity or importance of network events, which is crucial for managing logs and alerts.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkEventLogLevelField(CharField):
    description = "A field to categorize the log level of network events."

    LOG_LEVEL_CHOICES = [
        ("DEBUG", "Debug"),
        ("INFO", "Info"),
        ("WARNING", "Warning"),
        ("ERROR", "Error"),
        ("CRITICAL", "Critical"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.LOG_LEVEL_CHOICES
        kwargs["max_length"] = 8  # Enough for "Critical"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.LOG_LEVEL_CHOICES):
            raise ValidationError("Invalid log level.")
        return value
