NetworkConfiguration Model
This model handles detailed configurations for each network segment, including subnet settings, routing information, and other parameters.

from django.db import models
from django.db.models import IntegerField
from django.core.exceptions import ValidationError

from django.db import models

class NetworkConfiguration(models.Model):
    network_name = models.CharField(max_length=100)
    managed_devices = models.ManyToManyField(NetworkDevice)  # Multiple devices can be part of a single network configuration
    subnet = CIDRField()  # Custom field for CIDR notation
    routing_protocol = RoutingProtocolField()  # OSPF, BGP, etc.
    description = models.TextField(blank=True)

    def __str__(self):
        return self.network_name



class NetworkConfig(models.Model):
    vlan_id = VLANIDField()
    protocol = NetworkProtocolField()
    dns_name = DNSNameField()
    description = models.TextField()

    def __str__(self):
        return f"{self.dns_name} ({self.protocol})"



class NetworkConfiguration(models.Model):
    resource_name = models.CharField(max_length=100)
    ip_version = IPAddressVersionField()
    latency = LatencyField()
    load_balancing = LoadBalanceStrategyField()
    firewall_status = FirewallStatusField()
    description = models.TextField()

    def __str__(self):
        return f"{self.resource_name} - {self.firewall_status}"


from django.db import models
from .validators import validate_ip_address, validate_hostname, validate_url, validate_password_strength

class NetworkConfiguration(models.Model):
    ip_address = models.CharField(max_length=255, validators=[validate_ip_address])
    hostname = models.CharField(max_length=255, validators=[validate_hostname])
    website = models.URLField(validators=[validate_url])
    admin_password = models.CharField(max_length=255, validators=[validate_password_strength])
