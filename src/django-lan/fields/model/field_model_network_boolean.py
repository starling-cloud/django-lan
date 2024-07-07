BooleanNetworkField
A Boolean field that uses "enabled" and "disabled" as choices instead of True/False, which can be more intuitive in network settings.


from django.db.models import BooleanField

class BooleanNetworkField(BooleanField):
    description = "A Boolean field with 'enabled' and 'disabled' choices."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return "enabled" if value else "disabled"

    def to_python(self, value):
        if isinstance(value, str):
            if value.lower() in ("enabled", "true", "1"):
                return True
            elif value.lower() in ("disabled", "false", "0"):
                return False
        return value

    def get_prep_value(self, value):
        if isinstance(value, str):
            return value.lower() in ("enabled", "true", "1")
        return value
