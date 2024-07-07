# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Version Validation Function
===============================================

This function validates whether a given input is a recognized IP address
version (IPv4 or IPv6), using an enumerated type to ensure consistency
across validations.

Links:
- https://en.wikipedia.org/wiki/IP_address

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Union

# Import | Libraries
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...enums.enum_ip_address_version import IPAddressVersion


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Functions
# =============================================================================

def validate_ip_address_version(value: Union[str, int]) -> None:
    """
    IP Address Version Validation Function
    ======================================

    Validates that the input corresponds to a valid IP address version.

    This function checks whether the provided input matches one of the defined
    IP address versions using an Enum to enforce consistency and eliminate
    hard-coded values.

    Args:
        value (Union[str, int]): The IP address version to validate, which
            can be an integer or string.

    Raises:
        ValidationError: If the provided value is not a valid IP address
            version as defined in the Enum.

    Examples:
        >>> validate_ip_address_version("IPv4")
        None
        >>> validate_ip_address_version(6)  # Assuming enum supports int representations
        None
        >>> validate_ip_address_version("IPv9")
        Raises ValidationError: "Invalid IP address version. Expected 'IPv4' or 'IPv6'."

    """  # noqa E501

    # Convert integers to their corresponding string representation
    # if necessary
    if isinstance(value, int):
        value = f"IPv{value}"

    if not IPAddressVersion.has_value(value):
        valid_versions = ", ".join([ver.value for ver in IPAddressVersion])
        raise ValidationError(
            _("Invalid IP address version. Expected one of: {}.").format(valid_versions),  # noqa E501
            code = "invalid_ip_version",
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_ip_address_version",
]
