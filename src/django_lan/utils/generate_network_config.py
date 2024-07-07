Generate Network Device Configuration
This function generates a basic network configuration for a device based on given parameters.


def generate_network_config(hostname, ip_address, subnet_mask, gateway):
    """
    Generates a basic network configuration for a device.

    Args:
    hostname (str): The name of the network device.
    ip_address (str): The IP address for the device.
    subnet_mask (str): The subnet mask.
    gateway (str): The default gateway.

    Returns:
    str: A formatted string of the network configuration.
    """
    config = f"""
    Device: {hostname}
    IP Address: {ip_address}
    Subnet Mask: {subnet_mask}
    Default Gateway: {gateway}
    """
    return config.strip()
