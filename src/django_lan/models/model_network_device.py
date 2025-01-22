# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Network Device Model Class
===================================

This model keeps track of network devices, including details about their type,
IP addresses, MAC addresses, and roles within the network.

Links:

"""  # noqa E501


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library

# Import | Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from ..fields.model import (
    CIDRField,
    DataRateField,
    FrequencyField,
    InterfaceTypeField,
    IPAddressField,
    MACAddressField,
    NetworkDeviceRoleField,
    NetworkLinkStatusField,
    PacketSizeField,
)

# =============================================================================
# Classes
# =============================================================================


class NetworkDeviceModel(models.Model):
    """
    Network Device Model Class
    ==========================

    """

    # Class | Model Fields
    # =========================================================================

    name = models.CharField(
        max_length=100,
        verbose_name=_(message="Device Name"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_(message="Description"),
    )

    role = NetworkDeviceRoleField(
        verbose_name=_(message="Device Role"),
    )
    status = NetworkLinkStatusField(
        verbose_name=_(message="Network Status"),
    )

    ip_address = IPAddressField(
        verbose_name=_(message="IP Address"),
    )
    mac_address = MACAddressField(
        verbose_name=_(message="MAC Address"),
    )
    subnet = CIDRField(
        verbose_name=_(message="Subnet"),
    )

    interface_type = InterfaceTypeField(
        verbose_name=_(message="Interface Type"),
    )
    frequency_check = FrequencyField(
        verbose_name=_(message="Frequency Check"),
    )
    packet_size = PacketSizeField(
        verbose_name=_(message="Packet Size"),
    )
    data_rate = DataRateField(
        verbose_name=_(message="Data Rate"),
    )

    # Class | Model Methods
    # =========================================================================

    def __str__(self) -> str:
        """
        Returns a string representation of the network device, showing its
        name and role.
        """
        return f"{self.name} ({self.role})"
        # return f"{self.name} - {self.interface_type}"


# =============================================================================
# Module Variables
# =============================================================================

__all__: list[str] = [
    "NetworkDeviceModel",
]
