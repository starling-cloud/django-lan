NetworkEventLog Model
This model logs network events, categorizing them by severity and storing messages related to specific incidents.


from django.db import models

class NetworkEventLog(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    event_log_level = NetworkEventLogLevelField()  # Debug, Info, Warning, Error, Critical
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_log_level} Event on {self.device.device_name} at {self.timestamp}"
