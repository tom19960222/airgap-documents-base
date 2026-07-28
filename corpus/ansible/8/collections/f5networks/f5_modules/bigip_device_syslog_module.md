---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_syslog module – Manage system-level syslog settings on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_syslog_module.html
fetched_at: 2026-07-28T02:05:59+00:00
---
# f5networks.f5_modules.bigip_device_syslog module – Manage system-level syslog settings on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_syslog`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_syslog_module.md#synopsis)
- [Parameters](bigip_device_syslog_module.md#parameters)
- [Notes](bigip_device_syslog_module.md#notes)
- [Examples](bigip_device_syslog_module.md#examples)
- [Return Values](bigip_device_syslog_module.md#return-values)

## [Synopsis](bigip_device_syslog_module.md#id1)

- Manage system-level syslog settings on BIG-IP.

## [Parameters](bigip_device_syslog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_priv_from**  string | Specifies the lowest level of messages about user authentication to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **auth_priv_to**  string | Specifies the highest level of messages about user authentication to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **console_log**  boolean | Enables or disables logging emergency syslog messages to the console.  **Choices:**   - `false` - `true` |
| **cron_from**  string | Specifies the lowest level of messages about time-based scheduling to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **cron_to**  string | Specifies the highest level of messages about time-based scheduling to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **daemon_from**  string | Specifies the lowest level of messages about daemon performance to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **daemon_to**  string | Specifies the highest level of messages about daemon performance to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **include**  string | Syslog-NG configuration to include in the device syslog config. |
| **iso_date**  boolean | Enables or disables the ISO date format for messages in the log files.  **Choices:**   - `false` - `true` |
| **kern_from**  string | Specifies the lowest level of kernel messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **kern_to**  string | Specifies the highest level of kernel messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **local6_from**  string | Specifies the lowest error level for messages from the local6 facility to include in the log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **local6_to**  string | Specifies the highest error level for messages from the local6 facility to include in the log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **mail_from**  string | Specifies the lowest level of mail log messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **mail_to**  string | Specifies the highest level of mail log messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **messages_from**  string | Specifies the lowest level of system messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **messages_to**  string | Specifies the highest level of system messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
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
| **user_log_from**  string | Specifies the lowest level of user account messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |
| **user_log_to**  string | Specifies the highest level of user account messages to include in the system log.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"err"` - `"info"` - `"notice"` - `"warning"` |

## [Notes](bigip_device_syslog_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_syslog_module.md#id4)

```yaml+jinja
- name: Create a syslog config
  bigip_device_syslog:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_syslog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auth_priv_from**  string | The new lowest user authentication logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **auth_priv_to**  string | The new highest user authentication logging level.  **Returned:** changed  **Sample:** `"emerg"` |
| **console_log**  boolean | Whether logging to the console is enabled or not.  **Returned:** changed  **Sample:** `true` |
| **cron_from**  string | The new lowest time-based scheduling logging level.  **Returned:** changed  **Sample:** `"emerg"` |
| **cron_to**  string | The new highest time-based scheduling logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **daemon_from**  string | The new lowest daemon performance logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **daemon_to**  string | The new highest daemon performance logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **include**  string | The new extra syslog-ng configuration to include in syslog config.  **Returned:** changed  **Sample:** `"filter f_remote_syslog { not (facility(local6)) };"` |
| **iso_date**  boolean | Whether ISO date format in logs is enabled or not.  **Returned:** changed  **Sample:** `false` |
| **kern_from**  string | The new lowest kernel messages logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **kern_to**  string | The new highest kernel messages logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **local6_from**  string | The new lowest local6 facility logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **local6_to**  string | The new highest local6 facility logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **mail_from**  string | The new lowest mail log logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **mail_to**  string | The new highest mail log logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **messages_from**  string | The new lowest system logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **messages_to**  string | The new highest system logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **user_log_from**  string | The new lowest user account logging level.  **Returned:** changed  **Sample:** `"alert"` |
| **user_log_to**  string | The new highest user account logging level.  **Returned:** changed  **Sample:** `"alert"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
