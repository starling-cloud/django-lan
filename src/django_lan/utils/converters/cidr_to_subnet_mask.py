"""
Convert CIDR to Subnet Mask
A function to convert CIDR notation to a subnet mask, useful for network configuration tasks.
"""

import ipaddress


def cidr_to_subnet_mask(cidr) -> str:
    """
    Converts CIDR notation to a subnet mask.

    Args:
    cidr (str): The CIDR notation (e.g., '192.168.1.0/24').

    Returns:
    str: The corresponding subnet mask.
    """
    network: ipaddress.IPv4Network | ipaddress.IPv6Network = ipaddress.ip_network(address=cidr, strict=False,)
    return str(object=network.netmask)
