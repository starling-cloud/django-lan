NetworkMaintenance Model
This model schedules and records maintenance activities for network devices, which is crucial for operational reliability and compliance.


from django.db import models

class NetworkMaintenance(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    maintenance_type = models.CharField(max_length=100)  # Types like 'Hardware Upgrade', 'Software Patch', etc.
    status = ChangeManagementStatusField()  # Pending, In Progress, Completed, Failed
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Maintenance {self.maintenance_type} for {self.device.device_name} on {self.scheduled_date.strftime('%Y-%m-%d')}"
