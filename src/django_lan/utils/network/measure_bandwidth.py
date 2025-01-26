import subprocess


def measure_bandwidth(host: str) -> str:
    """
    Measures the bandwidth to a host using the `iperf3` tool.

    Args:
        host (str): The hostname or IP address of the target device to measure bandwidth to.

    Returns:
        str: Results of the bandwidth measurement.
    """
    result = subprocess.run(
        ["iperf3", "-c", host],
        capture_output=True,
        text=True,
    )
    return result.stdout
