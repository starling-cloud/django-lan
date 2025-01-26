from typing import Dict, List

from scapy.all import ARP, Ether, srp


def scan_network(
    ip_range: str = "192.168.1.1/24",
) -> List[Dict[str, str]]:
    """
    Scans the network for devices using ARP requests.

    Args:
        ip_range (str): The IP range to scan in CIDR notation, defaults to "192.168.1.1/24".

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each containing 'ip' and 'mac' of each responding device.
    """
    # IP Range to ARP over
    # The packet
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    # Send the packet and get answers
    answered, unanswered = srp(
        arp_request,
        timeout=2,
        retry=1,
        verbose=False,
    )

    devices = []
    for sent, received in answered:
        # For each response, append IP and MAC address to `devices` list
        devices.append(
            {"ip": received.psrc, "mac": received.hwsrc},
        )

    return devices
