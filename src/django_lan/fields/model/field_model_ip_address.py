# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Model Field Class
=====================================

This class extends Django's CharField to store and validate IP addresses,
ensuring that each stored value is a valid IPv4 or IPv6 address. This field
automatically applies a validation to check the validity of IP addresses,
facilitating easier management and integrity of network-related data.

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

    A Django model field specifically for storing IP addresses with built-in
    validation.

    This field supports both IPv4 and IPv6 addresses, with automatic validation
    upon data entry. It is ideal for models that require a representation of
    network addresses where the IP address format needs to be strictly
    enforced.

    Attributes:
        description (str): Descriptive text to outline the field's use within
            models.

    """

    # Class | Variables
    # =========================================================================

    description: str = _(message="An IP address field with validation.")

    # Class | Methods
    # =========================================================================

    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Initializes the IPAddressModelField with a default maximum length
        for IPv6 addresses.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Max length for IPv6 addresses including potential subnet notation
        kwargs.setdefault(
            "max_length",
            39,
        )
        super().__init__(*args, **kwargs)
        # Ensure the field uses the IP address validator
        self.validators.append(validate_ip_address)


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "IPAddressModelField",
]
