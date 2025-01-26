import socket


def check_dns_resolution(
    domain_name: str,
) -> str:
    """
    Checks DNS resolution for a given domain name.

    Args:
        domain_name (str): The domain name to resolve.

    Returns:
        str: The IP address the domain resolves to.
    """
    return socket.gethostbyname(domain_name)
