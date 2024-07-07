Calculate Network Utilization
This function calculates the network utilization based on the bandwidth usage and capacity, providing insights into network performance.

def calculate_network_utilization(current_load, max_capacity):
    """
    Calculates the network utilization percentage.

    Args:
    current_load (float): Current bandwidth usage in Mbps.
    max_capacity (float): Maximum bandwidth capacity in Mbps.

    Returns:
    float: Network utilization as a percentage.
    """
    if max_capacity <= 0:
        raise ValueError("Maximum capacity must be greater than zero.")
    utilization = (current_load / max_capacity) * 100
    return round(utilization, 2)
