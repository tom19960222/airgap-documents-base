---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_snmp module – Manipulate general SNMP settings on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_snmp_module.html
fetched_at: 2026-07-27T17:27:45+00:00
---
# f5networks.f5_modules.bigip_snmp module – Manipulate general SNMP settings on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_snmp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_snmp_module.md#synopsis)
- [Parameters](bigip_snmp_module.md#parameters)
- [Notes](bigip_snmp_module.md#notes)
- [Examples](bigip_snmp_module.md#examples)
- [Return Values](bigip_snmp_module.md#return-values)

## [Synopsis](bigip_snmp_module.md#id1)

- Manipulate general SNMP settings on a BIG-IP system.

## [Parameters](bigip_snmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **agent_authentication_traps**  string | When `enabled`, ensures the system sends authentication warning traps to the trap destinations. This is usually disabled by default on a BIG-IP.  Choices:   - `"enabled"` - `"disabled"` |
| **agent_status_traps**  string | When `enabled`, ensures the system sends a trap whenever the SNMP agent starts running or stops running. This is usually enabled by default on a BIG-IP.  Choices:   - `"enabled"` - `"disabled"` |
| **allowed_addresses**  any | Configures the IP addresses of the SNMP clients from which the snmpd daemon accepts requests.  This value can be hostnames, IP addresses, or IP networks.  You may specify a single list item of `default` to set the value back to the system default of `127.0.0.0/8`.  You can remove all allowed addresses by either providing the word `none`, or by providing the empty string `""`. |
| **contact**  string | Specifies the name of the person who administers the SNMP service for this system. |
| **device_warning_traps**  string | When `enabled`, ensures the system sends device warning traps to the trap destinations. This is usually enabled by default on a BIG-IP.  Choices:   - `"enabled"` - `"disabled"` |
| **location**  string | Specifies the description of this system’s physical location. |
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

## [Notes](bigip_snmp_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_snmp_module.md#id4)

```yaml+jinja
- name: Set snmp contact
  bigip_snmp:
    contact: Joe User
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set snmp location
  bigip_snmp:
    location: US West 1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_snmp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **agent_authentication_traps**  string | Value of the authentication status traps.  Returned: changed  Sample: `"enabled"` |
| **agent_status_traps**  string | Value of the agent status traps.  Returned: changed  Sample: `"enabled"` |
| **allowed_addresses**  list / elements=string | The new allowed addresses for SNMP client connections.  Returned: changed  Sample: `["127.0.0.0/8", "foo.bar.com", "10.10.10.10"]` |
| **contact**  string | The new value for the person who administers SNMP on the device.  Returned: changed  Sample: `"Joe User"` |
| **device_warning_traps**  string | Value of the warning status traps.  Returned: changed  Sample: `"enabled"` |
| **location**  string | The new value for the system’s physical location.  Returned: changed  Sample: `"US West 1a"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
