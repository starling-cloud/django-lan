# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Logging Level Enum Class
=======================================

Specify logging levels within the network management system for debugging
and monitoring purposes.

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

class LoggingLevelEnum(BaseEnum):
    """
    Logging Level Enum Class
    ==============================

    """

    # Class | Enum Members
    # =========================================================================

    DEBUG = _("Debug")
    INFO = _("Info")
    WARNING = _("Warning")
    ERROR = _("Error")
    CRITICAL = _("Critical")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "LoggingLevelEnum",
]
