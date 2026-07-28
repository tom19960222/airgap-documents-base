---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_remote_syslog module – Manipulate remote syslog settings on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_remote_syslog_module.html
fetched_at: 2026-07-27T17:27:40+00:00
---
# f5networks.f5_modules.bigip_remote_syslog module – Manipulate remote syslog settings on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_remote_syslog`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_remote_syslog_module.md#synopsis)
- [Parameters](bigip_remote_syslog_module.md#parameters)
- [Notes](bigip_remote_syslog_module.md#notes)
- [Examples](bigip_remote_syslog_module.md#examples)
- [Return Values](bigip_remote_syslog_module.md#return-values)

## [Synopsis](bigip_remote_syslog_module.md#id1)

- Manipulate remote syslog settings on a BIG-IP system.

## [Parameters](bigip_remote_syslog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **local_ip**  string | Specifies the local IP address of the system that is logging. To provide no local IP, specify the value `none`.  When creating a remote syslog, if this parameter is not specified, the default value is `none`. |
| **name**  string | Specifies the name of the syslog object.  This option is required when multiple `remote_host`s with the same IP or hostname are present on the device.  If `name` is not provided, `remote_host` is used by default. |
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
| **remote_host**  string / required | Specifies the IP address or hostname for the remote system, to which the system sends log messages. |
| **remote_port**  string | Specifies the port the system uses to send messages to the remote logging server.  When creating a remote syslog, if this parameter is not specified, the default value is `514`. |
| **state**  string | When `present`, guarantees the remote syslog exists with the provided attributes.  When `absent`, removes the remote syslog from the system.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](bigip_remote_syslog_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_remote_syslog_module.md#id4)

```yaml+jinja
- name: Add a remote syslog server to log to
  bigip_remote_syslog:
    remote_host: 10.10.10.10
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add a remote syslog server on a non-standard port to log to
  bigip_remote_syslog:
    remote_host: 10.10.10.10
    remote_port: 1234
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_remote_syslog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **local_ip**  string | The new local IP of the remote syslog server.  Returned: changed  Sample: `"10.10.10.10"` |
| **remote_port**  integer | New remote port of the remote syslog server.  Returned: changed  Sample: `514` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
