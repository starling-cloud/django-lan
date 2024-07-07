Decrypt Network Data
Complementary to the encryption function, this decrypts data that was encrypted with the above utility.

def decrypt_data(encrypted_data, password):
    """
    Decrypts data encrypted by the encrypt_data function.

    Args:
    encrypted_data (bytes): The encrypted data.
    password (str): The password used to generate the encryption key.

    Returns:
    str: The decrypted plaintext data.
    """
    backend = default_backend()
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    data = encrypted_data[32:]
    # Create a key from the password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(password.encode())
    # Decrypt the data
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return decrypted_data.decode()
