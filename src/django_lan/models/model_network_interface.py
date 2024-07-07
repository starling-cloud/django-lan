from django.db import models

class NetworkInterface(models.Model):
    interface_name = models.CharField(max_length=100)
    bandwidth_limit = BandwidthLimitField()
    link_status = NetworkLinkStatusField()
    ssl_cert_status = SSLCertStatusField()
    qos_policy = QoSPolicyField()
    description = models.TextField()

    def __str__(self):
        return f"{self.interface_name} - Status: {self.link_status}"


from django.db import models

class NetworkInterface(models.Model):
    device_name = models.CharField(max_length=100)
    port_number = PortNumberField()
    is_active = BooleanNetworkField()
    max_speed = NetworkSpeedField()

    def __str__(self):
        return self.device_name


from django.db import models

class NetworkInterface(models.Model):
    interface_name = models.CharField(max_length=100)
    bandwidth_limit = BandwidthLimitField()
    link_status = NetworkLinkStatusField()
    ssl_cert_status = SSLCertStatusField()
    qos_policy = QoSPolicyField()
    description = models.TextField()

    def __str__(self):
        return f"{self.interface_name} - Status: {self.link_status}"
