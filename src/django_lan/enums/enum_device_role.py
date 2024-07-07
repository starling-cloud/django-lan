# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Device Role Enum Class
===============================

This enum defines roles for network devices, facilitating role-based
configuration and actions.

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

class DeviceRoleEnum(BaseEnum):
    """
    Device Role Enum Class
    ======================

    """

    # Class | Enum Members
    # =========================================================================

    ROUTER = _("Router")
    SWITCH = _("Switch")
    ACCESS_POINT = _("Access Point")
    BRIDGE = _("Bridge")

    # Class | Methods
    # =========================================================================


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "DeviceRoleEnum",
]
