# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides MAC Address Model Field Class
======================================

This field will store and validate MAC addresses, which are unique identifiers
assigned to network interfaces.

Links:
- https://en.wikipedia.org/wiki/MAC_address

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
from ...utils.validators.validator_mac_address import validate_mac_address


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class MACAddressModelField(CharField):
    """
    MAC Address Model Field Class
    =============================

    A Django model field that stores and validates MAC addresses.

    Attributes:
        description (str): Description of what the field is used for.

    """

    # Class | Variables
    # =========================================================================

    description = _(
        "An MAC address field with validation."
    )

    # Class | Methods
    # =========================================================================

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the MACAddressModelField with a set maximum length for
        MAC addresses.
        """
        # MAC addresses are 17 characters long, including colons
        kwargs['max_length'] = 17
        super().__init__(*args, **kwargs)
        self.validators.append(validate_mac_address)

    def clean(self, value: Any, model_instance: Any) -> Any:
        """
        Cleans and validates the input value using the superclass’s cleaning
        logic and additional MAC address formatting checks.

        Args:
            value (Any): The value that needs to be cleaned.
            model_instance (Any): The Django model instance that this field
                belongs to.

        Returns:
            Any: The cleaned and validated value.
        """
        return super().clean(value, model_instance)


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "MACAddressModelField",
]
