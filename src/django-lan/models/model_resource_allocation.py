ResourceAllocation Model
This model tracks and manages resource allocations like bandwidth and processing power across network devices, ensuring optimal performance.


from django.db import models

class ResourceAllocation(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=50, choices=[('BANDWIDTH', 'Bandwidth'), ('CPU', 'CPU'), ('MEMORY', 'Memory')])
    allocation_value = ResourceAllocationField()  # Custom field for resource values
    effective_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.resource_type} Allocation for {self.device.device_name}"
