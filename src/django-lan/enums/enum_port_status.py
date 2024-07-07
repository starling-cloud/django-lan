# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Port Status Enum Class
===============================

This enum can be used to define the status of network ports, which is crucial
for monitoring and managing port states.


Links:
- https://en.wikipedia.org/wiki/Port_(computer_networking)

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

class PortStatusEnum(BaseEnum):
    """
    Port Status Enum Class
    ======================

    Enum for representing various states of network ports.

    """

    # Class | Enum Members
    # =========================================================================

    OPEN = _("Open")
    CLOSED = _("Closed")
    FILTERED = _("Filtered")

    # Class | Methods
    # =========================================================================


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "PortStatusEnum",
]
