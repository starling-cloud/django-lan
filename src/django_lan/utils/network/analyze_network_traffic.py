def analyze_network_traffic(
    packets: list,
) -> dict:
    """
    Analyzes network traffic from captured packets.

    Args:
        packets (list): A list of packet data structures captured from the network.

    Returns:
        dict: Summary statistics about the traffic such as total data, common protocols, etc.
    """
    summary = {
        "total_packets": len(packets),
        "total_data": sum(p.size for p in packets),
        "protocols": {},
    }
    for packet in packets:
        protocol = packet.protocol
        summary["protocols"][protocol] = (
            summary["protocols"].get(protocol, 0) + 1
        )
    return summary
