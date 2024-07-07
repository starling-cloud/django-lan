Hostname Validator
This validator ensures that a hostname conforms to RFC 1034/1035.


import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_hostname(value):
    """
    Validates that the input is a valid hostname according to RFC 1034/1035.
    """
    if not re.match(r"^(?![0-9]+$)(?!.*-$)(?!-)[a-zA-Z0-9-]{1,63}(?<!-)$", value):
        raise ValidationError(_("Invalid hostname."), code='invalid')
