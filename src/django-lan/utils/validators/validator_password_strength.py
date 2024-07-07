Password Strength Validator
A validator to check the strength of passwords, ensuring they meet a minimum complexity requirement.


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_password_strength(value):
    """
    Validates that the input is a strong password with minimum criteria: length, digits, uppercase, and special characters.
    """
    import re
    if len(value) < 8:
        raise ValidationError(_("Password must be at least 8 characters long."), code='invalid')
    if not re.findall('\d', value):
        raise ValidationError(_("Password must contain at least one digit."), code='invalid')
    if not re.findall('[A-Z]', value):
        raise ValidationError(_("Password must contain at least one uppercase letter."), code='invalid')
    if not re.findall('[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError(_("Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)."), code='invalid')
