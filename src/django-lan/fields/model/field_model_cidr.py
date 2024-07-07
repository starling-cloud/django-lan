# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides CIDR Model Field Class
===============================

A field to store network masks in CIDR (Classless Inter-Domain Routing)
notation, useful for defining subnets.

Links:
- https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing

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
from ...utils.validators.validator_cidr import validate_cidr


# =============================================================================
# Classes
# =============================================================================

class CIDRModelField(CharField):
    """
    CIDR Model Field Class
    =====================

    A Django model field that stores network masks in CIDR notation and
    validates them.

    Attributes:
        description (str): Description of what the field is used for.

    """

    # Class | Variables
    # =========================================================================

    description = _(
        "A CIDR block field with validation."
    )

    # Class | Methods
    # =========================================================================

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes the CIDRModelField with a default maximum length for
        IPv6 CIDR notation.
        """
        kwargs["max_length"] = 43  # Max length considering IPv6 CIDR notation
        super().__init__(*args, **kwargs)
        self.validators.append(validate_cidr)  # Add the custom validator

    def clean(self, value: Any, model_instance: Any) -> Any:
        """
        Cleans and validates the input value.

        Args:
            value (Any): The value that needs to be cleaned and validated.
            model_instance (Any): The Django model instance that this field
                belongs to.

        Returns:
            Any: The cleaned and validated value.

        Raises:
            ValidationError: If the input value is not a valid CIDR notation.
        """
        value = super().clean(value, model_instance)
        # The custom validator in the validators list handles the validation
        return value


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "CIDRModelField",
]
