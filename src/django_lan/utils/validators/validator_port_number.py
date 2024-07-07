# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Port Number Validation Function
========================================


This module defines a function to validate network port numbers, ensuring
they are within the standard range for TCP/UDP ports.

Links:
- https://en.wikipedia.org/wiki/Port_(computer_networking)

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from typing import Any

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

# def validate_port_number(value: Any) -> None:
def validate_port_number(value: int) -> None:
    """
    Port Number Validation Function
    ===============================

    Validates that a given value is a valid network port number.

    Ensures that the port number falls within the standard range for TCP
    and UDP ports, which is between 1 and 65535. This function is intended to
    enforce correct data entry for fields that store port numbers in
    applications.

    Args:
        value (Any): The port number to validate. The function attempts to
            cast non-integers to integer.

    Raises:
        ValidationError: If the port number is not within the valid range
            of 1 to 65535.

    Examples:
        >>> validate_port_number(80)
        None
        >>> validate_port_number(70000)
        ValidationError: Port number must be between 1 and 65535

    """

    try:
        # Attempt to convert value to int
        port = int(value)

    except ValueError:
        raise ValidationError(
            _("Port number must be an integer"),
            code = "invalid_port_number_type",
        )

    if not (1 <= port <= 65535):
        raise ValidationError(
            _("Port number must be between 1 and 65535"),
            code = "invalid_port_number",
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_port_number",
]
