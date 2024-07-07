# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Traffic Type Enum Class
===============================

Define different types of network traffic to handle specific Quality of
Service (QoS) settings or monitoring rules.

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

class TrafficTypeEnum(BaseEnum):
    """
    Traffic Type Enum Class
    ======================

    """

    # Class | Enum Members
    # =========================================================================

    VOIP = _("VoIP")
    STREAMING = _("Streaming")
    DATA = _("Data")
    CONTROL = _("Control")
    UNKNOWN = _("Unknown")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "TrafficTypeEnum",
]
