from django.db import models

class NetworkEquipment(models.Model):
    equipment_name = models.CharField(max_length=100)
    hardware_type = HardwareAddressTypeField()
    topology = NetworkTopologyField()
    routing_protocol = RoutingProtocolField()
    description = models.TextField()

    def __str__(self):
        return f"{self.equipment_name} - {self.routing_protocol}"
