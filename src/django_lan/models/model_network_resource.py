from django.db import models

class NetworkResource(models.Model):
    resource_name = models.CharField(max_length=100)
    authentication_method = AuthenticationMethodField()
    traffic_flow = TrafficFlowField()
    incident_response = IncidentResponseField()
    device_role = NetworkDeviceRoleField()
    description = models.TextField()

    def __str__(self):
        return f"{self.resource_name} - Role: {self.device_role}"
