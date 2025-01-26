import networkx as nx


def discover_network_topology(devices: list, connections: list) -> nx.Graph:
    """
    Discovers network topology based on a list of devices and their connections.

    Args:
        devices (list): A list of device identifiers.
        connections (list): A list of tuples representing connections between devices.

    Returns:
        nx.Graph: A graph representing the network topology.
    """
    G = nx.Graph()
    G.add_nodes_from(devices)
    G.add_edges_from(connections)
    return G
