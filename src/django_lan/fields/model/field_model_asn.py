# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides ASN Model Field Class
==============================

An Autonomous System Number (ASN) field for storing and validating ASNs used
in various routing protocols.

Links:
- https://en.wikipedia.org/wiki/Autonomous_system_(Internet)

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any

# Import | Libraries
from django.db.models import BigIntegerField
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ...utils.validators.validator_asn import validate_asn


# =============================================================================
# Classes
# =============================================================================

class ASNModelField(BigIntegerField):
    """
    ASN Model Field Class
    =====================

    A Django model field for storing and validating ASNs.

    Ensures the ASN value is within the allowed range from 1 to 4294967295,
    suitable for use in network routing configurations.

    Attributes:
        description (str): Description of what the field stores and validates.

    """

    # Class | Variables
    # =========================================================================

    description = _(
        "Stores and validates Autonomous System Numbers (ASNs)."
    )

    # Class | Methods
    # =========================================================================

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initializes a new instance of ASNModelField, appending the
        custom ASN validator.
        """
        super().__init__(*args, **kwargs)
        self.validators.append(validate_asn)


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "ASNModelField",
]
