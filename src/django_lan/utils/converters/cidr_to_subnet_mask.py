Convert CIDR to Subnet Mask
A function to convert CIDR notation to a subnet mask, useful for network configuration tasks.


import ipaddress

def cidr_to_subnet_mask(cidr):
    """
    Converts CIDR notation to a subnet mask.

    Args:
    cidr (str): The CIDR notation (e.g., '192.168.1.0/24').

    Returns:
    str: The corresponding subnet mask.
    """
    network = ipaddress.ip_network(cidr, strict=False)
    return str(network.netmask)
