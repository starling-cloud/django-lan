Format MAC Address
This utility standardizes MAC addresses to a common format, which is useful for database storage and consistency.


import re

def format_mac_address(mac):
    """
    Formats a MAC address to standard colon-separated format.

    Args:
    mac (str): The MAC address to format.

    Returns:
    str: Formatted MAC address.
    """
    mac = re.sub('[.:-]', '', mac).lower()  # Remove any separators and convert to lower case
    return ':'.join(mac[i:i+2] for i in range(0, 12, 2))
