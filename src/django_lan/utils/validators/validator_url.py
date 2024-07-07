# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides URL Validation Function
================================

This function validates whether a given string is a well-formed URL within
specific schemes, ensuring it meets certain structural criteria to be
considered valid for use in your application.

Links:
- https://en.wikipedia.org/wiki/URL

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any
from urllib.parse import urlparse

# Import | Libraries
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Functions
# =============================================================================

def validate_url(
    value: Any,
    schemes: tuple = ("http", "https", "ftp")
) -> None:
    """
    URL Validation Function
    =======================

    Validates that the input is a well-formed URL within specified schemes.

    Args:
        value (Any): The URL to validate. It's expected to be a string, but
            can handle other types by converting to string first.
        schemes (tuple): A tuple containing the allowed URL schemes.
            Defaults to ('http', 'https', 'ftp').

    Raises:
        ValidationError: If the URL does not conform to expected structure
        and schemes.

    Examples:
        >>> validate_url("https://www.example.com")
        None
        >>> validate_url("ftp://example.com")
        None
        >>> validate_url("mailto:test@example.com")
        Raises ValidationError: "Invalid URL scheme."
        >>> validate_url("http://")
        Raises ValidationError: "Invalid URL: missing domain."

    """

    try:
        # Convert value to string and strip any leading/trailing whitespace
        parsed_url = urlparse(str(value).strip())
        if not parsed_url.scheme:
            raise ValidationError(
                _("Invalid URL: missing scheme."),
                code="invalid_scheme"
            )
        if parsed_url.scheme not in schemes:
            raise ValidationError(
                _("Invalid URL scheme. Allowed schemes are: {}.").format(", ".join(schemes)),  # noqa E501
                code="invalid_scheme"
            )
        if not parsed_url.netloc:
            raise ValidationError(
                _("Invalid URL: missing domain."),
                code="invalid_domain"
            )

    except Exception as e:
        # Catch any unexpected exceptions during URL parsing and raise
        # as ValidationError
        raise ValidationError(
            _("Invalid URL: {error}").format(error=str(e)),
            code = "invalid_url",
        )

    # Optional: Validate that the URL has a valid domain format (could use
    # a regex or other method)


# =============================================================================
# Public Interface
# =============================================================================

__all__ = [
    "validate_url",
]
