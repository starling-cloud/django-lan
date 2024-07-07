Convert IP Address to Binary
A utility function that converts an IP address into its binary representation, useful for subnetting and network calculations.


import ipaddress

def ip_to_binary(ip_address):
    """
    Converts an IP address to its binary representation.

    Args:
    ip_address (str): The IP address to convert.

    Returns:
    str: The binary representation of the IP address.
    """
    ip = ipaddress.ip_address(ip_address)
    return format(int(ip), '0>128b') if ip.version == 6 else format(int(ip), '0>32b')
