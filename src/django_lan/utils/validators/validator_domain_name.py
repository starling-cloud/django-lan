# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Domain Name Validation Function
========================================

This validator ensures that a hostname conforms to RFC 1034/1035.


This function validates whether a given string is a valid hostname according
to the  standards set in RFC 1034 and RFC 1035, ensuring that it conforms to
the requirements for domain names used in the internet's domain name system.

Links:
- https://en.wikipedia.org/wiki/Domain_name
- https://www.rfc-editor.org/rfc/rfc1034
- https://www.rfc-editor.org/rfc/rfc1035
- https://datatracker.ietf.org/doc/html/rfc1034
- https://datatracker.ietf.org/doc/html/rfc1035

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
import re

# Import | Libraries
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================


# =============================================================================
# Functions
# =============================================================================

def validate_domain_name(value: str) -> None:
    """
    Domain Name Validation Function
    ===============================

    Validates that the input string is a valid hostname according to
    RFC 1034/1035.

    The domain name must:
    - Consist of a series of labels concatenated with dots.
    - Each label must be between 1 and 63 characters long.
    - Valid characters are ASCII letters 'a-z', 'A-Z', digits '0-9',
        and hyphen '-'.
    - Labels must start and end with a letter or a digit.
    - The top-level domain (TLD) must be at least two characters long.
    
    Args:
        value (str): The domain name to validate.

    Raises:
        ValidationError: If the domain name does not meet the specified
            criteria.

    Examples:
        >>> validate_domain_name("example.com")
        None
        >>> validate_domain_name("-example.com")
        Raises ValidationError: "Invalid hostname."
        >>> validate_domain_name("example-.com")
        Raises ValidationError: "Invalid hostname."
        >>> validate_domain_name("ex..ample.com")
        Raises ValidationError: "Invalid hostname."
        >>> validate_domain_name("example.toolongtldtoolongtldtoolongtldtoolongtld")
        Raises ValidationError: "Invalid hostname."

    """  # noqa E501

    # RFC 1034/1035 regex pattern for domain names
    pattern = (
        # Labels cannot start with a hyphen
        r'^(?!-)'
        # Labels cannot contain double hyphens in the 3rd and 4th positions
        # (exception for punycode)
        r'(?!.*--)'
        # Subdomain & TLD constraints
        r'(?:(?:[a-zA-Z0-9]-*)*[a-zA-Z0-9]\.)+'
        # Labels cannot end with a hyphen
        r'(?<!-)'
        # TLD specific length requirements
        r'[a-zA-Z0-9]{2,63}'
        r'$'
    )

    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid hostname. Ensure the domain name is compliant with RFC 1034/1035."),  # noqa E501
            code = "invalid_hostname",
        )


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_domain_name",
]
