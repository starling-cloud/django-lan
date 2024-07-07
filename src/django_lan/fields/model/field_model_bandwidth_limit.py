# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Bandwidth Limit Model Field Class
==========================================

This field is for managing bandwidth limits on specific network links or
devices, storing values in Mbps or Gbps.

Links:
- 

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db.models import BigIntegerField
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class BandwidthLimitModelField(BigIntegerField):
    """
    Bandwidth Limit Model Field Class
    =================================

    """

    # Class | Variables
    # =========================================================================

    description = _(
        "A field that stores bandwidth limits in Mbps."
    )

    # Class | Methods
    # =========================================================================

    def clean(self, value, model_instance):
        value = super().clean(value, model_instance)
        # Assuming the minimum bandwidth limit you'd want to impose is 1 Mbps
        if value < 1:
            raise ValidationError(
                "Bandwidth limit must be at least 1 Mbps."
            )
        return value


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "BandwidthLimitModelField",
]
