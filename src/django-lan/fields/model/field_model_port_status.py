# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Port Status Model Field Class
======================================


Links:
- https://en.wikipedia.org/wiki/Port_(computer_networking)

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db.models import IntegerField
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...enums.enum_port_status import PortStatusEnum
from ...utils.validators.validator_port_status import validate_port_status


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================

class PortStatusModelField(IntegerField):
    """
    Port Status Model Field Class
    =============================

    Custom Django model field for storing port status with validation against
    PortStatusEnum.

    Attributes:
        description (str): Description of what the field is used for.

    """

    # Class | Variables
    # =========================================================================

    description = _(
        "A field that stores and validates port status based on predefined enums."  # noqa E501
    )

    # Class | Methods
    # =========================================================================

    def __init__(self, *args, **kwargs):
        """
        Initializes the field with specific choices from PortStatusEnum and a
        custom validator.
        """
        kwargs['choices'] = PortStatusEnum.choices()
        kwargs['max_length'] = 8  # Assume 'Filtered' is the longest value
        super().__init__(*args, **kwargs)
        self.validators.append(validate_port_status)

    def deconstruct(self):
        """
        Deconstructs the field to be suitable for migrations.
        """
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "PortStatusModelField",
]
