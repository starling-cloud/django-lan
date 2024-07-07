TrafficFlowField
This field will manage data related to traffic flow direction, crucial for monitoring and controlling ingress and egress points.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class TrafficFlowField(CharField):
    description = "A field to specify the direction of network traffic flow."

    FLOW_CHOICES = [
        ("INGRESS", "Ingress"),
        ("EGRESS", "Egress"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.FLOW_CHOICES
        kwargs["max_length"] = 7  # Enough for "Ingress"
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.FLOW_CHOICES):
            raise ValidationError("Invalid traffic flow direction.")
        return value
