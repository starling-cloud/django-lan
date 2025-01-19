# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IP Address Range Model Field Class
=============================================

A field that helps in storing and validating a range of IP addresses.

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
from ...utils.validators.validator_ip_address_range import \
    validate_ip_address_range  # noqa E501

# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class IPAddressRangeModelField(CharField):
    """
    IP Address Range Model Field Class
    ====================================

    A Django model field that stores and validates IP address versions
    (IPv4, IPv6).

    Attributes:
        description (str): Description of what the field is used for.
    """

    # Class | Variables
    # =========================================================================

    description: str = _(
        message="A field that stores and validates ranges of IP addresses."
    )

    # Class | Methods
    # =========================================================================

    def __init__(self, *args: Any, **kwargs: Any,) -> None:
        """
        Initializes the IPAddressRangeModelField with sufficient maximum length
        to store two IPv4 or IPv6 addresses and custom validation.
        """
        # Enough for two IPv6 addresses "XXXX:XXXX:...-XXXX:XXXX:..."
        kwargs['max_length'] = 39
        super().__init__(*args, **kwargs)
        self.validators.append(validate_ip_address_range)

    def clean(self, value: Any, model_instance: Any) -> Any:
        """
        Cleans and validates the input value using the superclass’s cleaning
        logic and the custom IP range validator.

        Args:
            value (Any): The value that needs to be cleaned.
            model_instance (Any): The Django model instance that this field
                belongs to.

        Returns:
            Any: The cleaned and validated value.
        """
        # Validator will handle range check
        return super().clean(value=value, model_instance=model_instance,)


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "IPAddressRangeModelField",
]
