Restore Network Configuration
Complements the backup utility by providing functionality to restore network configurations from a file.

def restore_network_config(filepath):
    """
    Restores network configuration from a specified JSON file.

    Args:
    filepath (str): The file path from which to restore the configuration.

    Returns:
    dict: The restored network configuration, or None if an error occurs.
    """
    try:
        with open(filepath, 'r') as file:
            configuration = json.load(file)
        return configuration
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error restoring network configuration: {e}")
        return None
