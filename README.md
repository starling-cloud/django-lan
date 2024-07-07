# Django LAN

Django LAN is a Django plugin designed to facilitate local area network (LAN) management directly from your Django applications. It provides a suite of tools and custom model fields to manage network configurations, validate network parameters, and interact with network hardware efficiently.

## Features

- **Network Device Management**: Manage and store configurations for various network devices.
- **Custom Field Types**: Includes custom Django model fields for IP addresses, MAC addresses, CIDR notations, and more.
- **Network Validation Tools**: Extensive validators for network-related data such as IP addresses, MAC addresses, port numbers, and CIDR blocks.
- **Dynamic Form Components**: Utilize dynamic form fields that integrate directly with your network management models.

## Quick Start

To get started with Django LAN, follow these steps:

### Prerequisites

- Django 3.1 or newer
- Python 3.6 or newer

### Installation

1. **Install Django LAN**:

   ``` bash
   pip install django-lan
   ```

2. **Add `django_lan` to your INSTALLED_APPS in `settings.py`**:

   ``` python
   INSTALLED_APPS = [
       ...
       'django_lan',
       ...
   ]
   ```

3. **Run Migrations**:

   ``` bash
   python manage.py migrate
   ```

### Usage

To use the custom model fields provided by Django LAN in your models:

``` python
from django.db import models
from django_lan.fields import IPAddressModelField, MACAddressModelField, PortNumberModelField

class NetworkDevice(models.Model):
    ip_address = IPAddressModelField()
    mac_address = MACAddressModelField()
    port = PortNumberModelField()
```

### Validators

Apply validators in your forms like this:

``` python
from django import forms
from django_lan.validators import validate_ip_address, validate_mac_address

class NetworkDeviceForm(forms.ModelForm):
    class Meta:
        model = NetworkDevice
        fields = '__all__'

    def clean_ip_address(self):
        ip_address = self.cleaned_data.get('ip_address')
        validate_ip_address(ip_address)
        return ip_address
```

## Documentation

For more detailed documentation, visit [Django LAN Documentation](#).

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to propose bugfixes and improvements, and how to build and test your changes to Django LAN.

## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.
