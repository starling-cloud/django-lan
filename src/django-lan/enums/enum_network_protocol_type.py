# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Network Protocol Enum Class
=======================================

Enumerate supported network protocols to ensure consistent configuration
across network devices.

Links:
- 

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
# from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from .enum_base import BaseEnum


# =============================================================================
# Classes
# =============================================================================

class NetworkProtocolEnum(BaseEnum):
    """
    Network Protocol Enum Class
    ===========================

    """

    # Class | Enum Members
    # =========================================================================

    TCP = "TCP"
    UDP = "UDP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    FTP = "FTP"


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "NetworkProtocolEnum",
]
