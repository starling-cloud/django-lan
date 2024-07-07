LoadBalanceStrategyField
A field to select the load balancing strategy, useful for settings in routers and network servers.

from django.db.models import CharField
from django.core.exceptions import ValidationError

class LoadBalanceStrategyField(CharField):
    description = "A field that selects a load balancing strategy."

    STRATEGY_CHOICES = [
        ("RR", "Round Robin"),
        ("LC", "Least Connections"),
        ("IP", "IP Hash"),
        ("URI", "URI Hash"),
    ]

    def __init__(self, *args, **kwargs):
        kwargs["choices"] = self.STRATEGY_CHOICES
        kwargs["max_length"] = 3  # To accommodate the abbreviations
        super().__init__(*args, **kwargs)

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        if value not in dict(self.STRATEGY_CHOICES):
            raise ValidationError("Invalid load balancing strategy.")
        return value
