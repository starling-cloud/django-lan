ChangeManagementStatusField
This field tracks the status of network changes, such as pending, in progress, or completed, which is vital for change management processes.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class ChangeManagementStatusField(CharField):
    description = "A field that tracks the status of network changes."

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.STATUS_CHOICES
        kwargs["max_length"] = 11  # Enough for "IN_PROGRESS"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.STATUS_CHOICES):
            raise ValidationError("Invalid change management status.")
        return value
