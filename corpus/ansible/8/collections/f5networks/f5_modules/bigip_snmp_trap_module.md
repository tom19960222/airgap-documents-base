---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_snmp_trap module – Manipulate SNMP trap information on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_snmp_trap_module.html
fetched_at: 2026-07-28T02:07:18+00:00
---
# f5networks.f5_modules.bigip_snmp_trap module – Manipulate SNMP trap information on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_snmp_trap`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_snmp_trap_module.md#synopsis)
- [Parameters](bigip_snmp_trap_module.md#parameters)
- [Notes](bigip_snmp_trap_module.md#notes)
- [Examples](bigip_snmp_trap_module.md#examples)
- [Return Values](bigip_snmp_trap_module.md#return-values)

## [Synopsis](bigip_snmp_trap_module.md#id1)

- Manipulate SNMP trap information on a BIG-IP system.

## [Parameters](bigip_snmp_trap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_password**  string  *added in f5networks.f5_modules 1.16.0* | Specifies the Authentication protocol password to be used for snmp v3 traps  Required for the `snmp_version` matches `v3` and for the `security_level` |
| **auth_protocol**  string  *added in f5networks.f5_modules 1.16.0* | Specifies the Authentication protocol to be used for snmp v3 traps  Required for the `security_level`  **Choices:**   - `"sha"` - `"md5"` |
| **community**  string | Specifies the community name for the trap destination. |
| **destination**  string | Specifies the address for the trap destination. This can be either an IP address or a hostname. |
| **name**  string / required | Name of the SNMP configuration endpoint. |
| **network**  string | Specifies the name of the trap network. This option is not supported in versions of BIG-IP prior to 12.1.0, and is simply ignored on those versions.  The value `default` was removed in BIG-IP version 13.1.0. Specifying this value when configuring a BIG-IP causes the module to stop and report an error. In this case, choose one of the other options, such as `management`.  **Choices:**   - `"other"` - `"management"` - `"default"` |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **port**  string | Specifies the port for the trap destination. |
| **privacy_password**  string  *added in f5networks.f5_modules 1.16.0* | Specifies the Privacy protocol password to be used for snmp v3 traps  Required for the `security_level` matches c(auth-privacy) |
| **privacy_protocol**  string  *added in f5networks.f5_modules 1.16.0* | Specifies the Privacy protocol to be used for snmp v3 traps  Required for the `security_level` matches c(auth-privacy)  **Choices:**   - `"aes"` - `"des"` |
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
| **security_level**  string  *added in f5networks.f5_modules 1.16.0* | Specifies the port for the trap destination.  Required for the `snmp_version` matches `v3`.  **Choices:**   - `"auth-no-privacy"` - `"auth-privacy"` |
| **security_name**  string  *added in f5networks.f5_modules 1.16.0* | Specifies the security name to used for v3 snmp trap  Required for the `snmp_version` matches `v3`. |
| **snmp_version**  string | Specifies to which Simple Network Management Protocol (SNMP) version the trap destination applies.  **Choices:**   - `"1"` - `"2c"` - `"3"` |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource does not exist.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_snmp_trap_module.md#id3)

> **Note:**
>
> - This module only supports version v1 and v2c of SNMP.
> - The `network` option is not supported on versions of BIG-IP prior to 12.1.0 because the platform did not support that option until 12.1.0. If used on versions prior to 12.1.0, it is simply be ignored.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_snmp_trap_module.md#id4)

```yaml+jinja
- name: Create snmp v1 trap
  bigip_snmp_trap:
    community: general
    destination: 1.2.3.4
    name: my-trap1
    network: management
    port: 9000
    snmp_version: 1
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create snmp v2 trap
  bigip_snmp_trap:
    community: general
    destination: 5.6.7.8
    name: my-trap2
    network: default
    port: 7000
    snmp_version: 2c
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Create snmp v3 trap
  bigip_snmp_trap:
    community: general
    destination: 5.6.7.9
    name: my-trap3
    network: management
    port: 7001
    snmp_version: 3
    auth_protocol: 'sha'
    auth_password: 'test12345'
    security_name: "testsec2"
    security_level: "auth-no-privacy"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
    state: absent
  delegate_to: localhost

- name: Create snmp v3 trap-2
  bigip_snmp_trap:
    community: general
    destination: 5.6.7.10
    name: my-trap4
    network: management
    port: 7002
    snmp_version: 3
    auth_protocol: 'sha'
    auth_password: 'test123456'
    security_name: "testsec3"
    security_level: "auth-privacy"
    privacy_protocol: "des"
    privacy_password: 'test@12345'
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
    state: absent
  delegate_to: localhost
```

## [Return Values](bigip_snmp_trap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **community**  list / elements=string | The new `community` name for the trap destination.  **Returned:** changed and success  **Sample:** `["secret"]` |
| **destination**  string | The new address for the trap destination in either IP or hostname form.  **Returned:** changed and success  **Sample:** `"1.2.3.4"` |
| **network**  string | The new name of the network the SNMP trap is on.  **Returned:** changed and success  **Sample:** `"management"` |
| **port**  string | The new `port` of the trap destination.  **Returned:** changed and success  **Sample:** `"900"` |
| **snmp_version**  string | The new `snmp_version` configured on the remote device.  **Returned:** changed and success  **Sample:** `"2c"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
