# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Authentication Type Enum Class
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

class AuthenticationTypeEnum(BaseEnum):
    """
    Authentication Type Enum Class
    ==============================

    """

    # Class | Enum Members
    # =========================================================================

    PASSWORD = _("Password")
    PUBLIC_KEY = _("Public Key")
    BIOMETRIC = _("Biometric")
    TWO_FACTOR = _("Two Factor")


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "AuthenticationTypeEnum",
]
