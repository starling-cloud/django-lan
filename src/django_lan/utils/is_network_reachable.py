Validate Network Reachability
A utility that checks if a given IP address or hostname is reachable within the network using ICMP echo requests (ping).


import subprocess

def is_network_reachable(host, count=1, timeout=1):
    """
    Checks if a network host is reachable by sending ICMP echo requests.

    Args:
    host (str): The hostname or IP address to check.
    count (int): Number of ping attempts.
    timeout (int): Timeout in seconds for each ping.

    Returns:
    bool: True if the host is reachable, False otherwise.
    """
    command = ['ping', '-c', str(count), '-W', str(timeout), host]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
