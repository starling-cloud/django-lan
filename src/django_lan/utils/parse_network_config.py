Parse Network Configuration from JSON
This utility function parses network configuration details from a JSON string, handling errors gracefully.


import json

def parse_network_config(json_data):
    """
    Parses network configuration from a JSON string.

    Args:
    json_data (str): JSON string containing network configuration.

    Returns:
    dict: A dictionary of network settings or None if invalid data.
    """
    try:
        config = json.loads(json_data)
        # Validate that required fields are present
        if 'hostname' in config and 'ip_address' in config:
            return config
        else:
            return None
    except json.JSONDecodeError:
        return None
