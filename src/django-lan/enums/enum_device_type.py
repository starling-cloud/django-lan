# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Device Type Enum Class
=======================================

Enum for different authentication methods used in network security settings.


Links:
- 

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from .enum_base import BaseEnum


# =============================================================================
# Classes
# =============================================================================

class DeviceTypeEnum(BaseEnum):
    """
    Device Type Enum Class
    ======================

    """

    # Class | Enum Members
    # =========================================================================

    COMPUTER = _("Computer")
    PRINTER =  _("Printer")
    ROUTER =  _("Router")
    SWITCH =  _("Switch")
    ACCESS_POINT = _("Access Point")
    SERVER =  _("Server")
    OTHER =  _("Other")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "DeviceTypeEnum",
]
