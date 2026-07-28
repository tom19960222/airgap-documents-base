---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_software_install module – Install software images on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_software_install_module.html
fetched_at: 2026-07-27T17:27:49+00:00
---
# f5networks.f5_modules.bigip_software_install module – Install software images on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_software_install`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_software_install_module.md#synopsis)
- [Parameters](bigip_software_install_module.md#parameters)
- [Notes](bigip_software_install_module.md#notes)
- [Examples](bigip_software_install_module.md#examples)

## [Synopsis](bigip_software_install_module.md#id1)

- Install new software images on a BIG-IP system.

## [Parameters](bigip_software_install_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **block_device_image**  string  added in f5networks.f5_modules 1.2.0 | Image to install on the remote device. In the case of a VCMP guest, ensure this image is present on the VCMP host and is referenced from there, and not from the VCMP guest. An ISO image directly uploaded to the VCMP guest will not work. |
| **image**  string | Image to install on the remote device. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **state**  string | When `installed`, ensures the software is installed on the volume and the volume is set to be booted from. The device is **not** rebooted into the new software.  When `activated`, performs the same operation as `installed`, but the system is rebooted to the new software.  Choices:   - `"activated"` ← (default) - `"installed"` |
| **type**  string  added in f5networks.f5_modules 1.2.0 | The type of the BIG-IP.  Defaults to `standard`, the other choice is `vcmp`.  Choices:   - `"standard"` ← (default) - `"vcmp"` |
| **volume**  string | The volume on which to install the software image. |

## [Notes](bigip_software_install_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_software_install_module.md#id4)

```yaml+jinja
- name: Ensure an existing image is installed in specified volume
  bigip_software_install:
    image: BIGIP-13.0.0.0.0.1645.iso
    volume: HD1.2
    state: installed
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Ensure an existing image is activated in specified volume
  bigip_software_install:
    image: BIGIP-13.0.0.0.0.1645.iso
    state: activated
    volume: HD1.2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Ensure an existing image is activated in specified volume in a VCMP guest
  bigip_software_install:
    block_device_image: BIGIP-13.0.0.0.0.1645.iso
    type: vcmp
    state: activated
    volume: HD1.2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)
- Nitin Khanna (@nitinthewiz)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
