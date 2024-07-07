Network Device Discovery
Scans and identifies devices within a network, useful for inventory management and new device integration.

def discover_network_devices(subnet):
    """
    Simulates the discovery of network devices within a given subnet.

    Args:
    subnet (str): The subnet to scan for devices.

    Returns:
    list: A list of discovered devices.
    """
    # Simulated device discovery
    devices = [
        {'ip': '192.168.1.10', 'device_type': 'router'},
        {'ip': '192.168.1.20', 'device_type': 'switch'},
        {'ip': '192.168.1.30', 'device_type': 'printer'}
    ]
    print(f"Devices discovered in {subnet}: {devices}")
    return devices

