import socket
from typing import List


def scan_ports(ip: str, port_range: List[int]) -> List[int]:
    """
    Scans specified ports on a given IP address to find open ports.

    Args:
        ip (str): The IP address to scan.
        port_range (List[int]): A list of ports to scan on the given IP.

    Returns:
        List[int]: A list of open ports.
    """
    open_ports = []
    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout to speed up the scan
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports
