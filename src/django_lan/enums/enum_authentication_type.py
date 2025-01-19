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

    PASSWORD: str = _(message="Password")
    PUBLIC_KEY: str = _(message="Public Key")
    BIOMETRIC: str = _(message="Biometric")
    TWO_FACTOR: str = _(message="Two Factor")


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "AuthenticationTypeEnum",
]
