NetworkTopologyField
This field represents the topology type of a network, which is critical for understanding and managing the layout and interconnection of network components.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class NetworkTopologyField(CharField):
    description = "A field to represent the network topology."

    TOPOLOGY_CHOICES = [
        ("BUS", "Bus"),
        ("STAR", "Star"),
        ("RING", "Ring"),
        ("MESH", "Mesh"),
        ("HYBRID", "Hybrid"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.TOPOLOGY_CHOICES
        kwargs["max_length"] = 6  # Maximum length of the longest choice
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.TOPOLOGY_CHOICES):
            raise ValidationError("Invalid network topology specified.")
        return value
