# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides IFC Change Action Enum Class
=====================================


For more information, refer to:
https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcutilityresource/lexical/ifcchangeactionenum.htm

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

class DeviceType(Enum):

    COMPUTER = auto()
    PRINTER = auto()
    ROUTER = auto()
    SWITCH = auto()
    ACCESS_POINT = auto()
    SERVER = auto()
    OTHER = auto()

    def __str__(self):
        # Provides a more readable string representation
        return self.name.capitalize()
