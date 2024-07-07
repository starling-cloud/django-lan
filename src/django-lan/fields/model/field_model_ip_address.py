# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Model Field Class
=====================================

A field to store IP addresses with automatic validation to check if the stored
value is a valid IP address.

Links:
- https://en.wikipedia.org/wiki/IP_address

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any

# Import | Libraries
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...utils.validators.validator_ip_address import validate_ip_address

# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IPAddressModelField(CharField):
    """
    IP Address Model Field Class
    ============================

    A Django model field that stores and validates IP addresses.

    Attributes:
        description (str): Description of what the field is used for.

    """

    # Class | Variables
    # =========================================================================

    description = _(
        "An IP address field with validation."
    )

    # Class | Methods
    # =========================================================================

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the IPAddressModelField with a default maximum length
        for IPv6 addresses.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        kwargs['max_length'] = 39
        super().__init__(*args, **kwargs)
        self.validators.append(validate_ip_address)


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "IPAddressModelField",
]
