from django.db import models

class NetworkService(models.Model):
    service_name = models.CharField(max_length=100)
    traffic_type = TrafficTypeField()
    encryption_strength = EncryptionStrengthField()
    service_status = NetworkServiceStatusField()
    description = models.TextField()

    def __str__(self):
        return f"{self.service_name} - {self.service_status}"
