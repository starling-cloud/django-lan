# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Security Level Enum Class
=======================================

Set predefined security levels that can be applied to network segments or
devices to simplify security management.


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

class SecurityLevelEnum(BaseEnum):
    """
    Security Level Enum Class
    ==============================

    """

    # Class | Enum Members
    # =========================================================================

    LOW = _("Low")
    MEDIUM = _("Medium")
    HIGH = _("High")
    CRITICAL = _("Critical")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "SecurityLevelEnum",
]
