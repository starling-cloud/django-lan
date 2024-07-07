# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides MAC Address Validation Function
========================================

This module includes a function to validate MAC addresses, ensuring they
adhere to standard MAC address formats
(e.g., XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX).

Links:
- https://en.wikipedia.org/wiki/MAC_address

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import re

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

def validate_mac_address(value: str) -> None:
    """
    MAC Address Validation Function
    ===============================

    Validates that the input string is a properly formatted MAC address.

    This function checks if the provided string matches the common
    representation of a MAC address, which should consist of six groups of two
    hexadecimal digits, separated by either colons (:) or hyphens (-).

    Args:
        value (str): The MAC address to validate, expected to be in the form
            of 'XX:XX:XX:XX:XX:XX' or 'XX-XX-XX-XX-XX-XX'.

    Raises:
        ValidationError: If the provided value is not a valid MAC address
            format.

    Examples:
        validate_mac_address("01:23:45:67:89:AB")  # No exception
        validate_mac_address("01-23-45-67-89-AB")  # No exception
        validate_mac_address("0123.4567.89AB")

    """
    # Regex to check the standard MAC address format
    if not re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', value):
        raise ValidationError(
            _("Invalid MAC address format. Expected format is XX:XX:XX:XX:XX:XX or XX-XX-XX-XX-XX-XX."),  # noqa E501
            code = "invalid_mac"
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_mac_address",
]
