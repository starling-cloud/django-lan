Validate Network Configuration Integrity
Ensures that a network configuration dictionary adheres to required schema and value types, preventing configuration errors.

def validate_network_config(config):
    """
    Validates the integrity of network configuration settings.

    Args:
    config (dict): The network configuration to validate.

    Returns:
    bool: True if the configuration is valid, False otherwise.
    """
    required_keys = {"ip_address", "subnet_mask", "gateway", "dns"}
    if not all(key in config for key in required_keys):
        print("Configuration missing required keys.")
        return False
    if any(not isinstance(config[key], str) for key in required_keys):
        print("Configuration values must be strings.")
        return False
    return True
