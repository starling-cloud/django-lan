from django.db import models

class NetworkSegment(models.Model):
    network_name = models.CharField(max_length=100)
    asn = ASNField()
    subnet_mask = SubnetMaskField()
    ip_range = NetworkRangeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.network_name} - ASN {self.asn}"
