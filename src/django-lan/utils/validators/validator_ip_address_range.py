# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Range Validation Function
=============================================


Links:
- https://en.wikipedia.org/wiki/IP_address

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

def validate_ip_address_range(value: str) -> None:
    """
    IP Address Range Validation Function
    ======================================

    Validates that the input string is a properly formatted IP address range.

    The function checks if the provided string includes two valid IP addresses
    separated by a hyphen ('-') and that the start IP address is not greater
    than the end IP address.

    Args:
        value (str): The IP address range to validate, in the format
            'start_ip-end_ip'.

    Raises:
        ValidationError: If the value does not contain a valid IP address
            range.
    """

    try:
        start_ip_str, end_ip_str = value.split('-')
        start_ip = ipaddress.ip_address(start_ip_str.strip())
        end_ip = ipaddress.ip_address(end_ip_str.strip())

        if start_ip > end_ip:
            raise ValidationError(
                _("Start IP address cannot be greater than end IP address in the range."),  # noqa E501
                code='invalid_ip_range'
            )
    except ValueError:
        raise ValidationError(
            _("Invalid IP address range format. Use 'start_ip-end_ip'."),
            code='invalid_format'
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_ip_address_range",
]
