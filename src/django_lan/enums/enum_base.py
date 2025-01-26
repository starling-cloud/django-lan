# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Base Enum Class
========================

Provides a base class for all enumeration classes used in the project,
adding utility methods for integration with Django models, forms, and
serializers.

"""

# =============================================================================
# Import
# =============================================================================

from enum import Enum

# Import | Standard Library
from typing import List, Tuple

# Import | Libraries

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================


class BaseEnum(Enum):
    """
    Base Enum Class
    ===============

    A base class for all enumeration types, providing common functionality
    needed for Django integration.

    """

    def __str__(self) -> str:
        """
        Return the user-friendly name of the enum member, enhancing its
        usability in user interfaces.

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
            return str(object=e)  # Log the error or handle it appropriately

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
    def has_value(
        cls,
        value: str,
    ) -> bool:
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

        # return value in cls._value2member_map_
        return value in (member.value for member in cls)


# =============================================================================
# Public Interface
# =============================================================================

__all__: List[str] = [
    "BaseEnum",
]
