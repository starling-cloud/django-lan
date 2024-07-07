Encrypt Network Data
A function to encrypt sensitive network data, such as passwords or configuration details, using AES encryption.

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_data(data, password):
    """
    Encrypts data using AES encryption based on a password.

    Args:
    data (str): The plaintext data to encrypt.
    password (str): The password to use for generating the key.

    Returns:
    bytes: The encrypted data.
    """
    backend = default_backend()
    salt = os.urandom(16)
    # Create a key from the password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(password.encode())
    # Encrypt the data
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
    return salt + iv + encrypted_data
