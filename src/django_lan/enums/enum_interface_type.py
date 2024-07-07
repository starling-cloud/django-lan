# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Interface Type Enum Class
==================================

Specify the types of network interfaces to allow detailed configuration and
compatibility checks.

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

class InterfaceTypeEnum(BaseEnum):
    """
    Interface Type Enum Class
    =========================

    """

    # Class | Enum Members
    # =========================================================================

    ETHERNET = _("Ethernet")
    WIFI = _("Wi-Fi")
    FIBER_OPTIC = _("Fiber Optic")
    USB = _("USB")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "InterfaceTypeEnum",
]
