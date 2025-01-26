from pythonping import ping


def ping_sweep(ip_range: List[str]) -> Dict[str, bool]:
    """
    Performs a ping sweep across a range of IP addresses.

    Args:
        ip_range (List[str]): A list of IP addresses to ping.

    Returns:
        Dict[str, bool]: A dictionary with IP addresses as keys and boolean values indicating if they are reachable.
    """
    results = {}
    for ip in ip_range:
        response = ping(ip, count=1, timeout=1)
        results[ip] = response.success()
    return results
