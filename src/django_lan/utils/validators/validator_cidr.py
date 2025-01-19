# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides CIDR Validation Function
=================================

Validates CIDR (Classless Inter-Domain Routing) notations which are used to
describe the network portion and the host identifier portion of an IP address.

Links:
- https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing

"""


# =============================================================================
# Import
# =============================================================================

import ipaddress
# Import | Standard Library
from typing import Any

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

def validate_cidr(value: Any) -> None:
    """
    CIDR Validation Function
    ========================

    Validates that the provided value is a valid CIDR notation.

    CIDR notation is a compact representation of an IP address and its
    associated network mask. CIDR notation is a more flexible and universal
    method to allocate IP addresses than the older system based on classes
    (A, B, C).

    Args:
        value (Any): The CIDR notation to validate. It's expected to be a
            string, but the function handles other types by attempting
            conversion.

    Raises:
        ValidationError: If the provided value is not a valid CIDR notation.

    Examples:
        >>> validate_cidr("192.168.1.0/24")
        None
        >>> validate_cidr("192.168.1.0/35")  # This example should raise a
        ValidationError
        ValidationError: Invalid CIDR notation

    """

    try:
        # Allows network address to be non-strict
        ipaddress.ip_network(
            address=value,
            strict = False,
        )
    except ValueError:
        raise ValidationError(
            message=_(message="Invalid CIDR notation"),
            code = "invalid_cidr",
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "validate_cidr",
]
