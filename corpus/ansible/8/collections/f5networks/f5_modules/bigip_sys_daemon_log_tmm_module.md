---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_sys_daemon_log_tmm module – Manage BIG-IP tmm daemon log settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_sys_daemon_log_tmm_module.html
fetched_at: 2026-07-28T02:07:25+00:00
---
# f5networks.f5_modules.bigip_sys_daemon_log_tmm module – Manage BIG-IP tmm daemon log settings

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_sys_daemon_log_tmm`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_sys_daemon_log_tmm_module.md#synopsis)
- [Parameters](bigip_sys_daemon_log_tmm_module.md#parameters)
- [Notes](bigip_sys_daemon_log_tmm_module.md#notes)
- [Examples](bigip_sys_daemon_log_tmm_module.md#examples)
- [Return Values](bigip_sys_daemon_log_tmm_module.md#return-values)

## [Synopsis](bigip_sys_daemon_log_tmm_module.md#id1)

- Manage BIG-IP tmm log settings.

## [Parameters](bigip_sys_daemon_log_tmm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arp_log_level**  string | Specifies the lowest level of ARP messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
| **http_compression_log_level**  string | Specifies the lowest level of HTTP compression messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
| **http_log_level**  string | Specifies the lowest level of HTTP messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
| **ip_log_level**  string | Specifies the lowest level of IP address messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"informational"` - `"notice"` - `"warning"` |
| **irule_log_level**  string | Specifies the lowest level of iRule messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
| **layer4_log_level**  string | Specifies the lowest level of Layer 4 messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"informational"` - `"notice"` |
| **net_log_level**  string | Specifies the lowest level of network messages from the tmm daemon to include in the system log.  **Choices:**   - `"critical"` - `"debug"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
| **os_log_level**  string | Specifies the lowest level of operating system messages from the tmm daemon to include in the system log.  **Choices:**   - `"alert"` - `"critical"` - `"debug"` - `"emergency"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
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
| **pva_log_level**  string | Specifies the lowest level of PVA messages from the tmm daemon to include in the system log.  **Choices:**   - `"debug"` - `"informational"` - `"notice"` |
| **ssl_log_level**  string | Specifies the lowest level of SSL messages from the tmm daemon to include in the system log.  **Choices:**   - `"alert"` - `"critical"` - `"debug"` - `"emergency"` - `"error"` - `"informational"` - `"notice"` - `"warning"` |
| **state**  string | The state of the log level on the system. When `present`, guarantees an existing log level is set to `value`.  **Choices:**   - `"present"` ← (default) |

## [Notes](bigip_sys_daemon_log_tmm_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_sys_daemon_log_tmm_module.md#id4)

```yaml+jinja
- name: Set SSL log level to debug
  bigip_sys_daemon_log_tmm:
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
    ssl_log_level: debug
  delegate_to: localhost
```

## [Return Values](bigip_sys_daemon_log_tmm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arp_log_level**  string | Lowest level of ARP messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"error"` |
| **http_compression_log_level**  string | Lowest level of HTTP compression messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"debug"` |
| **http_log_level**  string | Lowest level of HTTP messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"notice"` |
| **ip_log_level**  string | Lowest level of IP address messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"warning"` |
| **irule_log_level**  string | Lowest level of iRule messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"error"` |
| **layer4_log_level**  string | Lowest level of Layer 4 messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"notice"` |
| **net_log_level**  string | Lowest level of network messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"critical"` |
| **os_log_level**  string | Lowest level of operating system messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"critical"` |
| **pva_log_level**  string | Lowest level of PVA messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"debug"` |
| **ssl_log_level**  string | Lowest level of SSL messages from the tmm daemon to log.  **Returned:** changed  **Sample:** `"critical"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
