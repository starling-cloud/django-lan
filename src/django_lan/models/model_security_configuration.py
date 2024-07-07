SecurityConfiguration Model
This model manages security settings for network devices, including firewall configurations and SSL certificate statuses.

from django.db import models

class SecurityConfiguration(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    firewall_status = FirewallStatusField()  # Active, Inactive, Audit Mode
    ssl_cert_status = SSLCertStatusField()  # Valid, Expired, Renewing
    authentication_method = AuthenticationMethodField()  # WPA2, WPA3, OAuth, SAML
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Security Config for {self.device.device_name}"
