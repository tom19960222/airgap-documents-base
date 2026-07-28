---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_license module – Manage license installation and activation on BIG-IP devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_license_module.html
fetched_at: 2026-07-28T02:05:56+00:00
---
# f5networks.f5_modules.bigip_device_license module – Manage license installation and activation on BIG-IP devices

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_license`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_license_module.md#synopsis)
- [Parameters](bigip_device_license_module.md#parameters)
- [Notes](bigip_device_license_module.md#notes)
- [Examples](bigip_device_license_module.md#examples)

## [Synopsis](bigip_device_license_module.md#id1)

- Manage license installation and activation on a BIG-IP.

## [Parameters](bigip_device_license_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_eula**  boolean | Declares whether you accept the BIG-IP EULA or not. By default, this value is `false`. You must specifically declare you have viewed and accepted the license. This module does not present you with the EULA, so it is incumbent on you to read it.  The EULA can be found here; <https://support.f5.com/csp/article/K12902>.  This parameter is not required when `state` is `absent` and will be ignored if it is provided.  **Choices:**   - `false` ← (default) - `true` |
| **addon_keys**  list / elements=string  *added in f5networks.f5_modules 1.2.0* | The list of addon keys to use to in conjunction with the base license.  This parameter will be ignored if no `license_key` is provided.  This parameter is not required when `state` is `absent` and will be ignored if it is provided. |
| **force**  boolean | Declares whether to force license renewal. By default, this value is `false`.  This parameter is not required and will be ignored if it is provided.  **Choices:**   - `false` ← (default) - `true` |
| **license_key**  string | The registration key to use to license the BIG-IP.  This parameter is required if the `state` is equal to `present` or `latest`.  This parameter is not required when `state` is `absent` and will be ignored if it is provided. |
| **license_server**  string | The F5 license server to use when getting a license and validating a dossier.  This parameter is required if the `state` is equal to `present` or `latest`.  This parameter is not required when `state` is `absent` and will be ignored if it is provided.  **Default:** `"activate.f5.com"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | The state of the license on the system.  When `present`, only guarantees that a license exists.  When `absent`, removes the license on the system.  When `latest`, ensures that the license is always valid. This is not idempotent state since re-run can modify result.  When `revoked`, removes the license on the system and revokes its future usage on the F5 license servers.  **Choices:**   - `"absent"` - `"latest"` - `"present"` ← (default) - `"revoked"` |

## [Notes](bigip_device_license_module.md#id3)

> **Note:**
>
> - This module can be used to license BIG-IPs that do not have access to internet.
> - Only the Ansible Controller needs internet access as the license activation is done on the Ansible Controller from which the module is running.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_license_module.md#id4)

```yaml+jinja
- name: License BIG-IP using a key
  bigip_device_license:
    license_key: "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXXX"
    provider:
      server: "lb.mydomain.com"
      user: "admin"
      password: "secret"
  delegate_to: localhost

- name: License BIG-IP using a key
  bigip_device_license:
    license_key: "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXXX"
    provider:
      server: "lb.mydomain.com"
      user: "admin"
      password: "secret"
  delegate_to: localhost

- name: Remove the license from the system
  bigip_device_license:
    state: "absent"
    provider:
      server: "lb.mydomain.com"
      user: "admin"
      password: "secret"
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)
- Andrey Kashcheev (@andreykashcheev)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
