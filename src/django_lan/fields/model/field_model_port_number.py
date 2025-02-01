# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Port Number Model Field Class
======================================

A custom field to ensure that the port numbers are within the valid
range (1-65535).

Links:
- https://en.wikipedia.org/wiki/Port_(computer_networking)

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any

# Import | Libraries
from django.db.models import IntegerField
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...utils.validators.validator_port_number import validate_port_number

# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================


class PortNumberModelField(IntegerField):
    """
    Port Number Model Field Class
    =============================

    A Django model field that stores and validates network port numbers.

    Attributes:
        description (str): Description of what the field is used for.

    """

    # Class | Variables
    # =========================================================================

    description: str = _(
        message="A field that stores and validates network port numbers."
    )

    # Class | Methods
    # =========================================================================

    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Initializes the PortNumberModelField with custom validation.
        """
        super().__init__(*args, **kwargs)
        self.validators.append(validate_port_number)

    def clean(
        self,
        value: Any,
        model_instance: Any,
    ) -> Any:
        """
        Cleans and validates the input value using the superclass’s
        cleaning logic.

        Args:
            value (Any): The value that needs to be cleaned.
            model_instance (Any): The Django model instance that this field
                belongs to.

        Returns:
            Any: The cleaned and validated value.
        """
        # Validator will handle port range check
        return super().clean(value=value, model_instance=model_instance)


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "PortNumberModelField",
]
