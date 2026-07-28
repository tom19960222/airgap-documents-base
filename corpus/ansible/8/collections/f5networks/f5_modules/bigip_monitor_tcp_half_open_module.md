---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_monitor_tcp_half_open module – Manages F5 BIG-IP LTM TCP half-open monitors"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_monitor_tcp_half_open_module.html
fetched_at: 2026-07-28T02:06:49+00:00
---
# f5networks.f5_modules.bigip_monitor_tcp_half_open module – Manages F5 BIG-IP LTM TCP half-open monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_tcp_half_open`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_tcp_half_open_module.md#synopsis)
- [Parameters](bigip_monitor_tcp_half_open_module.md#parameters)
- [Notes](bigip_monitor_tcp_half_open_module.md#notes)
- [Examples](bigip_monitor_tcp_half_open_module.md#examples)
- [Return Values](bigip_monitor_tcp_half_open_module.md#return-values)

## [Synopsis](bigip_monitor_tcp_half_open_module.md#id1)

- Manages F5 BIG-IP LTM TCP half-open monitors.

## [Parameters](bigip_monitor_tcp_half_open_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description of the monitor. |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template will run. If this parameter is not provided when creating a new monitor, the default value is 5. This value **must** be less than the `timeout` value. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’.  If this value is an IP address, and the `type` is `tcp` (the default), then a `port` number must be specified. |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `tcp_half_open` parent on the `Common` partition.  **Default:** `"/Common/tcp_half_open"` |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. If specifying an IP address, you must specify a value between 1 and 65535. |
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
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time_until_up**  integer | Specifies the amount of time in seconds after the first successful response before a node will be marked up. A value of `0` will cause a node to be marked up immediately after a valid response is received from the node. If this parameter is not provided when creating a new monitor, the default value is be 0. |
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this to any number, however, it should be 3 times the interval number of seconds plus 1 second. If this parameter is not provided when creating a new monitor, then the default value is 16. |

## [Notes](bigip_monitor_tcp_half_open_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_tcp_half_open_module.md#id4)

```yaml+jinja
- name: Create TCP half-open Monitor
  bigip_monitor_tcp_half_open:
    state: present
    ip: 10.10.10.10
    name: my_tcp_monitor
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove TCP half-open Monitor
  bigip_monitor_tcp_half_open:
    state: absent
    name: my_tcp_monitor
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add half-open monitor for all addresses, port 514
  bigip_monitor_tcp_half_open:
    port: 514
    name: my_tcp_monitor
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_monitor_tcp_half_open_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description of the monitor.  **Returned:** changed  **Sample:** `"Important Monitor"` |
| **interval**  integer | The new interval in which to run the monitor check.  **Returned:** changed  **Sample:** `2` |
| **ip**  string | The new IP of IP/port definition.  **Returned:** changed  **Sample:** `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  **Returned:** changed  **Sample:** `"tcp"` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  **Returned:** changed  **Sample:** `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  **Returned:** changed  **Sample:** `10` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
