# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides ASN Validation Function
================================

Validates Autonomous System Numbers (ASNs) which are critical for routing
decisions on the internet.

Links:
- https://en.wikipedia.org/wiki/Autonomous_system_(Internet)

"""


# =============================================================================
# Import
# =============================================================================

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

def validate_asn(value: Any) -> None:
    """
    ASN Validation Function
    =======================

    Validates that the provided value is a valid Autonomous System Number
    (ASN).

    An ASN is a special number assigned by IANA to each autonomous system
    which uses BGP routing. This function checks if the provided ASN is
    within the  valid range of 1 to 4294967295, inclusive.

    Args:
        value (Any): The ASN to validate. While typically an integer, this
            accepts `Any` to gracefully handle unexpected input types.

    Raises:
        ValidationError: If the ASN is not within the valid range.

    Examples:
        >>> validate_asn(64512)
        None
        >>> validate_asn(4294967296)
        ValidationError: ASN must be between 1 and 4294967295 (inclusive).

    """

    try:
        asn = int(value)
    except ValueError:
        raise ValidationError(
            _("ASN must be a number.")
        )

    if not (1 <= asn <= 4294967295):
        raise ValidationError(
            _("ASN must be between 1 and 4294967295 (inclusive).")
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_asn",
]
