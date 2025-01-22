# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
DNSNameField

A field to store and validate DNS names, ensuring they adhere to DNS naming conventions.
"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import re

# Import | Libraries
from django.core.exceptions import ValidationError
from django.db.models import CharField

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Classes
# =============================================================================


class DNSNameField(CharField):
    """
    "Docstring for DNSNameField

    :var description: Description
    :vartype description: Literal['A DNS name field with validation.']
    """

    description = "A DNS name field with validation."

    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        """
        Docstring for __init__

        :param self: Description
        :type self:
        :param args: Description
        :type args:
        :param kwargs: Description
        :type kwargs:
        """
        kwargs["max_length"] = 255  # Typical max length for DNS names
        super().__init__(*args, **kwargs)

    def clean(
        self,
        value,
        model_instance,
    ):  # -> Any:
        value = super().clean(value=value, model_instance=model_instance)
        if not re.match(
            pattern=r"^(?!-)[A-Z\d-]{1,63}(?<!-)(\.(?!-)[A-Z\d-]{1,63}(?<!-))*$",
            string=value,
            flags=re.IGNORECASE,
        ):
            raise ValidationError(message="Invalid DNS name format")
        return value
        return value
