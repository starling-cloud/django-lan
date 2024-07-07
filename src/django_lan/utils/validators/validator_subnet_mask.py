# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Subnet Mask Validation Function
========================================

This function validates whether a given string is a valid IPv4 subnet mask.

Links:
- https://en.wikipedia.org/wiki/Subnet

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
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

def validate_subnet_mask(mask: str) -> None:
    """
    Subnet Mask Validation Function
    ===============================

    Validates whether the provided string is a valid IPv4 subnet mask.

    Subnet masks must be contiguous blocks of ones followed by zeros when
    converted to a binary representation.

    Args:
        mask (str): The subnet mask to validate.

    Raises:
        ValidationError: If the mask is not a valid IPv4 subnet mask.

    Examples:
        >>> validate_subnet_mask("255.255.255.0")
        None
        >>> validate_subnet_mask("255.255.255.255")
        None
        >>> validate_subnet_mask("255.255.255.1")
        Raises ValidationError: "Invalid subnet mask."

    """

    try:
        # Convert the mask to an IP address and back to a string to
        # normalize it.
        ip_mask = ipaddress.IPv4Network(f"0.0.0.0/{mask}", strict=False)
        binary_mask = ''.join(format(int(x), '08b') for x in str(ip_mask.netmask).split('.'))  # noqa E501
        if '01' in binary_mask:
            raise ValueError("Subnet mask is not contiguous.")

    except (ipaddress.NetmaskValueError, ValueError):
        raise ValidationError(
            _("Invalid subnet mask. Subnet masks must be contiguous blocks of ones followed by zeros."),  # noqa E501
            code='invalid_subnet_mask'
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_subnet_mask",
]
