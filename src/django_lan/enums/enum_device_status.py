# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Device Status Enum Class
=================================

Define the possible statuses for network devices, such as active, inactive,
or under maintenance.

Links:
-

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from .enum_base import BaseEnum

# =============================================================================
# Classes
# =============================================================================


class DeviceStatusEnum(BaseEnum):
    """
    Device Status Enum Class
    ========================

    """

    # Class | Enum Members
    # =========================================================================

    ACTIVE: str = _(message="Active")
    INACTIVE: str = _(message="Inactive")
    MAINTENANCE: str = _(message="Maintenance")


# =============================================================================
# Public Interface
# =============================================================================

__all__: list[str] = [
    "DeviceStatusEnum",
]
