Analyze Packet Loss
This function calculates the packet loss percentage from transmitted and received packet counts, essential for network performance assessments.


def calculate_packet_loss(transmitted, received):
    """
    Calculates the percentage of packet loss in a network.

    Args:
    transmitted (int): The number of packets sent.
    received (int): The number of packets received.

    Returns:
    float: The packet loss percentage.
    """
    if transmitted == 0:
        raise ValueError("Transmitted packets cannot be zero.")
    lost = transmitted - received
    loss_percentage = (lost / transmitted) * 100
    return round(loss_percentage, 2)
