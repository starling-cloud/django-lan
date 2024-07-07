AccessControlList Model
This model manages access control lists (ACLs) for network devices to regulate traffic based on IP addresses, protocols, and more.


from django.db import models

class AccessControlList(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    rule_name = models.CharField(max_length=100)
    ip_address = IPAddressField()  # Custom field for validating IP addresses
    protocol = NetworkProtocolField()  # TCP, UDP, ICMP, etc.
    action = models.CharField(max_length=10, choices=[('ALLOW', 'Allow'), ('DENY', 'Deny')])
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.rule_name} on {self.device.device_name}"
