# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Port Status Enum Class
===============================

This enum can be used to define the status of network ports, which is crucial
for monitoring and managing port states.


Links:
- https://en.wikipedia.org/wiki/Port_(computer_networking)

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import List, Tuple
from enum import Enum

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class PortStatusEnum(Enum):
    """
    Port Status Enum Class
    ======================

    Enum for representing various states of network ports.

    """

    # Class | Enum Members
    # =========================================================================

    OPEN = _("Open")
    CLOSED = _("Closed")
    FILTERED = _("Filtered")

    # Class | Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        Return the user-friendly name of the enum member.

        Overrides the default string representation of Enum members to return
        the value directly, making it more readable when used in user-facing
        interfaces.

        Returns:
            str: The value of the enum member, ensuring that it is
                user-friendly.

        """
        try:
            return self.value
        except ValueError as e:
            return str(e)  # Log the error or handle it appropriately

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        """
        Provides a list of tuple pairs suitable for use in Django model
        field choices.

        This class method facilitates the use of this enum in model fields,
        forms, and serializers where choices need to be defined in the format
        expected by Django.

        Returns:
            List[Tuple[str, str]]: A list of tuples, where each tuple
                contains the enum member's name and value.

        """
        return [(member.name, member.value) for member in cls]

    @classmethod
    def has_value(cls, value: str) -> bool:
        """
        Checks if the given value is a valid member of the enum.

        This utility method provides a simple way to validate if a provided
        value matches any of the enum's values, enhancing validation logic
        across your application.

        Args:
            value (str): The value to check against the enum's members.

        Returns:
            bool: True if the value is a member of the enum, False otherwise.

        """
        return value in (member.value for member in cls)


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "PortStatusEnum",
]
