Generate Secure Random Password
This function generates a secure random password for use in network devices or user accounts.

import secrets
import string

def generate_secure_password(length=12):
    """
    Generates a secure random password.

    Args:
    length (int): The length of the password.

    Returns:
    str: A securely generated password.
    """
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
