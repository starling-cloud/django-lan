NetworkTraffic Model
This model is used for monitoring network traffic, recording traffic flow, and implementing QoS policies.


from django.db import models

class NetworkTraffic(models.Model):
    device = models.ForeignKey(NetworkDevice, on_delete=models.CASCADE)
    traffic_flow = TrafficFlowField()  # Ingress or Egress
    data_rate = DataRateField()  # Data rate in Mbps or Gbps
    qos_policy = QoSPolicyField()  # Describes QoS policies
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Traffic on {self.device.device_name} at {self.timestamp}"
