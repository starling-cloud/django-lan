# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Version Enum Class
======================================

This Enum class provides a standardized way to handle IP address versions,
supporting clear differentiation between IPv4 and IPv6 addresses within your
Django applications.

Links:
- https://en.wikipedia.org/wiki/IP_address

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

from enum import Enum

# Import | Standard Library
from typing import List, Tuple

# Import | Local Modules
from .enum_base import BaseEnum

# Import | Libraries
# from django.utils.translation import gettext_lazy as _


# =============================================================================
# Classes
# =============================================================================


class IPAddressVersionEnum(BaseEnum):
    """
    IP Address Version Enum Class
    =============================

    An enumeration for IP address versions.

    This class encapsulates the versioning of IP addresses to ensure that
    operations related to IP handling are type-safe and less prone to errors
    related to string literals.

    """

    # Class | Enum Members
    # =========================================================================

    IPv4: str = "IPv4"
    IPv6: str = "IPv6"

    # Class | Methods
    # =========================================================================


# =============================================================================
# Public Interface
# =============================================================================

__all__: List[str] = [
    "IPAddressVersionEnum",
]
