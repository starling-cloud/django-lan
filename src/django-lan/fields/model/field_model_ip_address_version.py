# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Version Model Field Class
=============================================

This field allows specifying whether an IP address is IPv4 or IPv6, critical
in configurations where both protocols might be in use.

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
from ...enums.enum_ip_address_version import IPAddressVersion
from ...utils.validators.validator_ip_address_version import validate_ip_address_version  # noqa E501


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IPAddressVersionModelField(CharField):
    """
    IP Address Version Model Field Class
    ====================================

    A Django model field that stores and validates IP address versions
    (IPv4, IPv6).

    Attributes:
        description (str): Description of what the field is used for.
    """

    # Class | Variables
    # =========================================================================

    description = _(
        "A field to specify IP address version."
    )

    VERSION_CHOICES = [
        ("IPv4", "IPv4"),
        ("IPv6", "IPv6"),
    ]

    # Class | Methods
    # =========================================================================

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the IPAddressVersionModelField with predefined choices
        for IP versions using Enum.
        """
        kwargs["choices"] = IPAddressVersion.choices()
        kwargs["max_length"] = 4  # Maximum length for 'IPv6'
        super().__init__(*args, **kwargs)
        self.validators.append(validate_ip_address_version)

    def clean(self, value: Any, model_instance: Any) -> Any:
        """
        Cleans and validates the input value using the superclass’s cleaning
        logic and additional validation for IP version.

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
    "IPAddressVersionModelField",
]
