RoutingProtocolField
A field for selecting routing protocols used within the network, such as OSPF, BGP, etc. This can help in setting up configurations and monitoring.


from django.db.models import CharField
from django.core.exceptions import ValidationError

class RoutingProtocolField(CharField):
    description = "A field for routing protocols."

    PROTOCOL_CHOICES = [
        ("OSPF", "Open Shortest Path First"),
        ("BGP", "Border Gateway Protocol"),
        ("RIP", "Routing Information Protocol"),
        ("IGRP", "Interior Gateway Routing Protocol"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.PROTOCOL_CHOICES
        kwargs["max_length"] = 4  # OSPF, BGP, RIP, IGRP
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.PROTOCOL_CHOICES):
            raise ValidationError("Invalid routing protocol specified.")
        return value
