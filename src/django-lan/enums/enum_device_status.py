# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Change Action Enum Class
=====================================

Network Device Status
Define the possible statuses for network devices, such as active, inactive, or under maintenance.
"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from enum import Enum, auto

# Import | Libraries
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

from enum import Enum

class NetworkDeviceStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    MAINTENANCE = 'maintenance'

    def __str__(self):
        return self.value
