# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Validation Function
=======================================

This validator checks if a given string is a valid IPv4 or IPv6 address.

Links:
- https://en.wikipedia.org/wiki/IP_address

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any
import ipaddress

# Import | Libraries
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Functions
# =============================================================================

def validate_ip_address(value: Any) -> None:
    """
    IP Address Validation Function
    ==============================

    Validates that the input is a valid IPv4 or IPv6 address.

    This function checks whether the provided string representation of an
    IP address is a valid IPv4 or IPv6 address. This is crucial for ensuring
    that network-related configurations or data entries are correct and
    operational.

    Args:
        value (Any): The IP address to validate, expected to be a string but
            can handle other types by converting to string first.

    Raises:
        ValidationError: If the provided value is not a valid IP address.
            This includes the case where the input is not properly formatted
            as an IP address.

    Examples:
        >>> validate_ip_address("192.168.0.1")
        None
        >>> validate_ip_address("999.999.999.999")
        ValidationError: Invalid IP address
        >>> validate_ip_address(12345)  # Non-string input
        ValidationError: Invalid IP address

    """

    try:
        # Convert to string to ensure compatibility with ipaddress library
        ipaddress.ip_address(str(value))
    except ValueError:
        raise ValidationError(
            _("Invalid IP address"),
            code = "invalid_ip",
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_ip_address",
]
