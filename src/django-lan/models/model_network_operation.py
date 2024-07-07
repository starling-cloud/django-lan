from django.db import models

class NetworkOperation(models.Model):
    operation_name = models.CharField(max_length=100)
    event_log_level = NetworkEventLogLevelField()
    redundancy_mode = RedundancyModeField()
    resource_allocation = ResourceAllocationField()
    change_status = ChangeManagementStatusField()
    description = models.TextField()

    def __str__(self):
        return f"{self.operation_name} - Status: {self.change_status}"
