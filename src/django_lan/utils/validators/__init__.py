# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Django LAN Validator Utils Module
=================================

This module provides a collection of utility functions designed to validate
various network-related data inputs used within the Django LAN application.
It includes validators for ASN, CIDR, domain names, IP addresses, MAC 
addresses, port numbers, and more, ensuring that all network configurations
adhere to industry standards and specifications.

These validators can be used directly in model validations, form clean
methods, or serializers to maintain data integrity and enforce proper
network configurations.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .validator_asn import validate_asn
from .validator_cidr import validate_cidr
from .validator_domain_name import validate_domain_name
from .validator_ip_address import validate_ip_address
from .validator_ip_address_range import validate_ip_address_range
from .validator_ip_address_version import validate_ip_address_version
from .validator_mac_address import validate_mac_address
from .validator_port_number import validate_port_number
from .validator_port_status import validate_port_status
from .validator_subnet_mask import validate_subnet_mask
from .validator_url import validate_url


# =============================================================================
# Module Level Variables
# =============================================================================

__all__ = [
    "validate_asn",
    "validate_cidr",
    "validate_domain_name",
    "validate_ip_address",
    "validate_ip_address_range",
    "validate_ip_address_version",
    "validate_mac_address",
    "validate_port_number",
    "validate_port_status",
    "validate_subnet_mask",
    "validate_url",
]
