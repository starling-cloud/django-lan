# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides VLAN Status Enum Class
===============================

Manage and monitor VLAN configurations with predefined statuses.

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

class VLANStatusEnum(BaseEnum):
    """
    VLAN Status Enum Class
    ======================

    """

    # Class | Enum Members
    # =========================================================================

    ACTIVE = _("Active")
    INACTIVE = _("Inactive")
    CONFIGURING = _("Configuring")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "VLANStatusEnum",
]
