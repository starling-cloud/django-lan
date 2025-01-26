"""
Convert IP Address to Binary
A utility function that converts an IP address into its binary representation, useful for subnetting and network calculations.
"""

import ipaddress


def ip_to_binary(ip_address) -> str:
    """
    Converts an IP address to its binary representation.

    Args:
    ip_address (str): The IP address to convert.

    Returns:
    str: The binary representation of the IP address.
    """
    ip: ipaddress.IPv4Address | ipaddress.IPv6Address = ipaddress.ip_address(address=ip_address)
    return format(int(ip), format_spec='0>128b') if ip.version == 6 else format(int(x=ip), format_spec='0>32b')
