---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_auth_radius module – Manages RADIUS auth configuration on a BIG-IP device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_auth_radius_module.html
fetched_at: 2026-07-28T02:05:48+00:00
---
# f5networks.f5_modules.bigip_device_auth_radius module – Manages RADIUS auth configuration on a BIG-IP device

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_auth_radius`.

New in f5networks.f5_modules 1.3.0

- [Synopsis](bigip_device_auth_radius_module.md#synopsis)
- [Parameters](bigip_device_auth_radius_module.md#parameters)
- [Notes](bigip_device_auth_radius_module.md#notes)
- [Examples](bigip_device_auth_radius_module.md#examples)
- [Return Values](bigip_device_auth_radius_module.md#return-values)

## [Synopsis](bigip_device_auth_radius_module.md#id1)

- Module creates a RADIUS configuration.

## [Parameters](bigip_device_auth_radius_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accounting_bug**  boolean | Enables or disables validation of the accounting response vector.  This option should be necessary only on older servers.  **Choices:**   - `false` - `true` |
| **fallback_to_local**  boolean | Specifies the system uses the Local authentication method if the remote authentication method is not available.  Option only available on `TMOS 13.0.0` and above.  **Choices:**   - `false` - `true` |
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
| **retries**  integer | Specifies the number of authentication retries the BIG-IP Local Traffic Management system allows before authentication fails. |
| **servers**  list / elements=string | Specifies the names of RADIUS servers for use with RADIUS authentication profiles. |
| **service_type**  string | Specifies the type of service requested from the RADIUS server. The default value is `authenticate-only`.  **Choices:**   - `"authenticate-only"` - `"login"` - `"default"` - `"framed"` - `"callback-login"` - `"callback-framed"` - `"outbound"` - `"administrative"` - `"nas-prompt"` - `"callback-nas-prompt"` - `"call-check"` - `"callback-administrative"` |
| **state**  string | When `state` is `present`, ensures the RADIUS server exists.  When `state` is `absent`, ensures the RADIUS server is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_for_auth**  boolean | Specifies whether or not this auth source is put in use on the system.  If `true`, the module sets the current system auth type to the value of `radius`.  If `false`, the module sets the authentication type to `local`, similar behavior to when `state` is `absent`, without removing the configured RADIUS resource.  **Choices:**   - `false` - `true` |

## [Notes](bigip_device_auth_radius_module.md#id3)

> **Note:**
>
> - This module is based on the command line (TMSH) configuration capabilities of RADIUS authentication, not the GUI.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_auth_radius_module.md#id4)

```yaml+jinja
- name: Create an RADIUS device configuration
  bigip_device_auth_radius:
    servers:
      - "ansible_test1"
      - "ansible_test2"
    retries: 3
    service_type: authenticate-only
    accounting_bug: false
    use_for_auth: true
    fallback_to_local: true
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update an RADIUS device configuration
  bigip_device_auth_radius:
    retries: 5
    service_type: administrative
    accounting_bug: true
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Delete RADIUS auth configuration
  bigip_device_auth_radius:
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_auth_radius_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **accounting_bug**  boolean | Enables or disables validation of the accounting response vector.  **Returned:** changed  **Sample:** `true` |
| **retries**  integer | Number of authentication retries before authentication fails.  **Returned:** changed  **Sample:** `10` |
| **servers**  list / elements=string | The servers value of the resource.  **Returned:** changed  **Sample:** `["hash/dictionary of values"]` |
| **service_type**  string | Type of service requested from the RADIUS server.  **Returned:** changed  **Sample:** `"login"` |

### Authors

- Andrey Kashcheev (@andreykashcheev)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
