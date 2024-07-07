Log Network Events
A simple utility to log network events for monitoring and troubleshooting.

import logging

def log_network_event(message, level='INFO'):
    """
    Logs a network event.

    Args:
    message (str): The message to log.
    level (str): The logging level ('INFO', 'WARNING', 'ERROR').
    """
    logger = logging.getLogger('network_event_logger')
    if level == 'INFO':
        logger.info(message)
    elif level == 'WARNING':
        logger.warning(message)
    elif level == 'ERROR':
        logger.error(message)
    else:
        logger.debug(message)
