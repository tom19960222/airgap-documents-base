---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_asm_advanced_settings module – Manage BIG-IP system ASM advanced settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_asm_advanced_settings_module.html
fetched_at: 2026-07-27T17:26:12+00:00
---
# f5networks.f5_modules.bigip_asm_advanced_settings module – Manage BIG-IP system ASM advanced settings

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_asm_advanced_settings`.

New in f5networks.f5_modules 1.4.0

- [Synopsis](bigip_asm_advanced_settings_module.md#synopsis)
- [Parameters](bigip_asm_advanced_settings_module.md#parameters)
- [Notes](bigip_asm_advanced_settings_module.md#notes)
- [Examples](bigip_asm_advanced_settings_module.md#examples)
- [Return Values](bigip_asm_advanced_settings_module.md#return-values)

## [Synopsis](bigip_asm_advanced_settings_module.md#id1)

- Manage BIG-IP system ASM advanced settings.

## [Parameters](bigip_asm_advanced_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | The ASM setting to manipulate. |
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
| **state**  string | The state of the setting on the system. When `present`, guarantees that an existing setting is set to `value`. When `reset`, sets the setting back to the default value. At least one of value and state `reset` are required.  Choices:   - `"present"` ← (default) - `"reset"` |
| **value**  string | The value to set the key to. At least one of value and state `reset` are required. |

## [Notes](bigip_asm_advanced_settings_module.md#id3)

> **Note:**
>
> - Requires BIG-IP version 12.0.0 or greater
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_asm_advanced_settings_module.md#id4)

```yaml+jinja
- name: Set the long_request_buffer_size asm setting
  bigip_asm_advanced_settings:
    name: long_request_buffer_size
    value: 20000000
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Reset the long_request_buffer_size to default value
  bigip_asm_advanced_settings:
    name: long_request_buffer_size
    state: reset
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_asm_advanced_settings_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **default_value**  string | The default value of the specified ASM setting  Returned: changed and success  Sample: `"10000000"` |
| **name**  string | The name of the ASM setting that was specified  Returned: changed and success  Sample: `"long_request_buffer_size"` |
| **value**  string | The value you set the ASM setting to  Returned: changed and success  Sample: `"20000000"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
