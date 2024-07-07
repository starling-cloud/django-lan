# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Port Status Validation Function
========================================


Links:
- https://en.wikipedia.org/wiki/Port_(computer_networking)

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from typing import Any

# Import | Libraries
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...enums.enum_port_status import PortStatusEnum


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Functions
# =============================================================================

def validate_port_status(value: str) -> None:
    """
    Port Status Validation Function
    ===============================

    Validates that the input string is a valid port status defined in
    PortStatusEnum.

    Args:
        value (str): The port status to validate.

    Raises:
        ValidationError: If the provided value is not a valid port status.

    """

    if not PortStatusEnum.has_value(value):
        raise ValidationError(
            _("Invalid port status. Expected one of: {}.").format(
                ', '.join([e.value for e in PortStatusEnum])
            ),
            code='invalid_port_status'
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_port_status",
]
