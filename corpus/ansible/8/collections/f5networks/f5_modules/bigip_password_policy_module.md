---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_password_policy module – Manages the authentication password policy on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_password_policy_module.html
fetched_at: 2026-07-28T02:06:52+00:00
---
# f5networks.f5_modules.bigip_password_policy module – Manages the authentication password policy on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_password_policy`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_password_policy_module.md#synopsis)
- [Parameters](bigip_password_policy_module.md#parameters)
- [Notes](bigip_password_policy_module.md#notes)
- [Examples](bigip_password_policy_module.md#examples)
- [Return Values](bigip_password_policy_module.md#return-values)

## [Synopsis](bigip_password_policy_module.md#id1)

- Manages the authentication password policy on a BIG-IP device.

## [Parameters](bigip_password_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **expiration_warning**  integer | Specifies the number of days before a password expires.  This value determines when the BIG-IP system automatically warns users their password is about to expire. |
| **max_duration**  integer | Specifies the maximum number of days a password is valid. |
| **max_login_failures**  integer | Specifies the number of consecutive unsuccessful login attempts the system allows before locking out the user.  Specify zero (0) to disable this parameter. |
| **min_duration**  integer | Specifies the minimum number of days a password is valid. |
| **min_length**  integer | Specifies the minimum number of characters in a valid password.  This value must be between 6 and 255. |
| **password_memory**  integer | Specifies whether the user has configured the BIG-IP system to remember a password on a specific computer and how many passwords to remember. |
| **policy_enforcement**  boolean | Enables or disables the password policy on the BIG-IP system.  **Choices:**   - `false` - `true` |
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
| **required_lowercase**  integer | Specifies the number of lowercase alpha characters that must be present in a password for the password to be valid. |
| **required_numeric**  integer | Specifies the number of numeric characters that must be present in a password for the password to be valid. |
| **required_special**  integer | Specifies the number of special characters that must be present in a password for the password to be valid. |
| **required_uppercase**  integer | Specifies the number of uppercase alpha characters that must be present in a password for the password to be valid. |

## [Notes](bigip_password_policy_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_password_policy_module.md#id4)

```yaml+jinja
- name: Change password policy to require 2 numeric characters
  bigip_password_policy:
    required_numeric: 2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_password_policy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **expiration_warning**  integer | The new expiration warning.  **Returned:** changed  **Sample:** `7` |
| **max_duration**  integer | The new max duration.  **Returned:** changed  **Sample:** `99999` |
| **max_login_failures**  integer | The new max login failures.  **Returned:** changed  **Sample:** `0` |
| **min_duration**  integer | The new minimum duration.  **Returned:** changed  **Sample:** `0` |
| **min_length**  integer | The new minimum password length.  **Returned:** changed  **Sample:** `6` |
| **password_memory**  integer | The new number of remembered passwords  **Returned:** changed  **Sample:** `0` |
| **policy_enforcement**  boolean | The new policy enforcement setting.  **Returned:** changed  **Sample:** `true` |
| **required_lowercase**  integer | The lowercase requirement.  **Returned:** changed  **Sample:** `1` |
| **required_numeric**  integer | The numeric requirement.  **Returned:** changed  **Sample:** `2` |
| **required_special**  integer | The special character requirement.  **Returned:** changed  **Sample:** `1` |
| **required_uppercase**  integer | The uppercase character requirement.  **Returned:** changed  **Sample:** `1` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
