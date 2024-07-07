from typing import Any, Tuple
from urllib.parse import urlparse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_url(value: Any, schemes: Tuple[str, ...] = ('http', 'https', 'ftp')) -> None:
    """
    Validates that the input is a well-formed URL within specific schemes.

    This function checks if the given URL is well-formed and conforms to one of the specified schemes.
    It's crucial for ensuring that URL entries in data fields are not only syntactically correct but also match
    predefined protocol requirements.

    Args:
        value (Any): The URL to validate. It's expected to be a string, but can handle other types by converting to string first.
        schemes (Tuple[str, ...]): A tuple containing the allowed URL schemes. Defaults to ('http', 'https', 'ftp').

    Raises:
        ValidationError: If the URL does not have a valid scheme or is missing a domain.

    Examples:
        >>> validate_url("https://www.example.com")
        None
        >>> validate_url("ftp://example.com")
        None
        >>> validate_url("mailto:test@example.com")
        ValidationError: Invalid URL scheme.
        >>> validate_url("http://")
        ValidationError: Invalid URL: missing domain.
    """
    try:
        # Convert value to string to ensure compatibility with urlparse
        parsed = urlparse(str(value))
        if not parsed.scheme or parsed.scheme not in schemes:
            raise ValidationError(_("Invalid URL scheme."), code='invalid_scheme')
        if not parsed.netloc:
            raise ValidationError(_("Invalid URL: missing domain."), code='invalid_domain')
    except Exception as e:
        # Catch any unexpected exceptions during URL parsing and raise as ValidationError
        raise ValidationError(_("Invalid URL: {error}").format(error=str(e)), code='invalid_url')
