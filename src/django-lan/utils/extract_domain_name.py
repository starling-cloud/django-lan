Extract Domain Name from URL
This function extracts the domain name from a given URL, which can be useful for logging or network security purposes.

from urllib.parse import urlparse

def extract_domain_name(url):
    """
    Extracts the domain name from a given URL.

    Args:
    url (str): The URL from which to extract the domain name.

    Returns:
    str: The domain name or an empty string if the URL is invalid.
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc
