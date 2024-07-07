# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Django LAN Config Class
===============================


"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
# from typing import Dict, List, Union

# Import | Libraries
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================

class DjangoLanConfig(AppConfig):
    """
    Django LAN Config Class
    ======================

    Django AppConfig for managing the Django LAN application.


    """

    # Full Python path to the application
    name = "django-lan"

    # Short name for the application, used in relation naming
    label = "django-lan"

    # Human-readable name for the application
    verbose_name = _("Django LAN")

    # Specifies the type of primary key to use by default for models in
    # this application
    default_auto_field = "django.db.models.BigAutoField"
