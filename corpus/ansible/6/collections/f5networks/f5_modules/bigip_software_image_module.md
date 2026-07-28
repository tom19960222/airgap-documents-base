---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_software_image module – Manage software images on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_software_image_module.html
fetched_at: 2026-07-27T17:27:48+00:00
---
# f5networks.f5_modules.bigip_software_image module – Manage software images on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_software_image`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_software_image_module.md#synopsis)
- [Parameters](bigip_software_image_module.md#parameters)
- [Notes](bigip_software_image_module.md#notes)
- [Examples](bigip_software_image_module.md#examples)
- [Return Values](bigip_software_image_module.md#return-values)

## [Synopsis](bigip_software_image_module.md#id1)

- Manages software images on a BIG-IP. These images may include both base images and hotfix images.

## [Parameters](bigip_software_image_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | When `yes`, uploads the file every time and replaces the file on the device.  When `no`, the file is only uploaded if it does not already exist.  Generally should be `yes` only in cases where you have reason to believe the image was corrupted during upload.  Choices:   - `false` ← (default) - `true` |
| **image**  string / required | The image to put on the remote device.  This may be an absolute or relative location on the Ansible controller.  Image names, whether they are base ISOs or hotfix ISOs, **must** be unique. |
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
| **state**  string | When `present`, ensures the image is uploaded.  When `absent`, ensures the image is removed.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](bigip_software_image_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_software_image_module.md#id4)

```yaml+jinja
- name: Upload relative image to the BIG-IP
  bigip_software_image:
    image: BIGIP-13.0.0.0.0.1645.iso
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Upload absolute image to the BIG-IP
  bigip_software_image:
    image: /path/to/images/BIGIP-13.0.0.0.0.1645.iso
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Upload image in a role to the BIG-IP
  bigip_software_image:
    image: "{{ role_path }}/files/BIGIP-13.0.0.0.0.1645.iso"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_software_image_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build version of the software contained in the image.  Returned: changed  Sample: `"0.0.3"` |
| **checksum**  string | MD5 checksum of the ISO.  Returned: changed  Sample: `"8cdbd094195fab4b2b47ff4285577b70"` |
| **file_size**  integer | Size of the uploaded image in MB.  Returned: changed  Sample: `1948` |
| **image_type**  string | Whether the image is a release or hotfix image.  Returned: changed  Sample: `"release"` |
| **version**  string | Version of the software contained in the image.  Returned: changed  Sample: `"13.1.0.8"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
