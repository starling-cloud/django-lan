import socket
import ssl
from datetime import datetime


def check_ssl_certificate(domain: str, port: int = 443) -> dict:
    """
    Checks SSL certificate details for a given domain.

    Args:
        domain (str): The domain to check the SSL certificate for.
        port (int): The port to connect to, defaults to 443 for HTTPS.

    Returns:
        dict: Information about the certificate such as issuer, expiration date, and any errors.
    """
    context = ssl.create_default_context()
    with context.wrap_socket(
        socket.socket(socket.AF_INET), server_hostname=domain
    ) as sock:
        sock.settimeout(5)
        try:
            sock.connect((domain, port))
            cert = sock.getpeercert()
            issuer = dict(x[0] for x in cert["issuer"])
            issuer_common_name = issuer["commonName"]
            valid_until = datetime.strptime(
                cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
            )
            return {
                "issuer": issuer_common_name,
                "valid_until": valid_until,
                "expired": valid_until < datetime.now(),
                "errors": None,
            }
        except Exception as e:
            return {
                "issuer": None,
                "valid_until": None,
                "expired": None,
                "errors": str(e),
            }
