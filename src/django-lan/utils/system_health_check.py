System Health Check
Performs a series of system diagnostics to determine the health and readiness of network components.

def system_health_check(components):
    """
    Performs a health check on specified system components.

    Args:
    components (dict): A dictionary of component names and their check functions.

    Returns:
    dict: A dictionary with component names and their health status (True if healthy).
    """
    health_status = {}
    for component, check_func in components.items():
        try:
            health_status[component] = check_func()
        except Exception as e:
            health_status[component] = False
            print(f"Health check failed for {component}: {e}")
    return health_status

