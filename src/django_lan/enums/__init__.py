# -*- coding: utf-8 -*-

"""
Django LAN Enums Module
=======================


"""

# =============================================================================
# Imports
# =============================================================================

# Local enumeration modules
from .enum_authentication_type import AuthenticationTypeEnum
from .enum_device_role import DeviceRoleEnum
from .enum_device_status import DeviceStatusEnum
from .enum_device_type import DeviceTypeEnum
from .enum_interface_type import InterfaceTypeEnum
from .enum_ip_address_version import IPAddressVersionEnum
from .enum_logging_level import LoggingLevelEnum
from .enum_network_protocol_type import NetworkProtocolEnum
from .enum_port_status import PortStatusEnum
from .enum_security_level import SecurityLevelEnum
from .enum_traffic_type import TrafficTypeEnum
from .enum_vlan_status import VLANStatusEnum


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "AuthenticationTypeEnum",
    "DeviceRoleEnum",
    "DeviceStatusEnum",
    "DeviceTypeEnum",
    "InterfaceTypeEnum",
    "IPAddressVersionEnum",
    "LoggingLevelEnum",
    "NetworkProtocolEnum",
    "PortStatusEnum",
    "SecurityLevelEnum",
    "TrafficTypeEnum",
    "VLANStatusEnum",
]
