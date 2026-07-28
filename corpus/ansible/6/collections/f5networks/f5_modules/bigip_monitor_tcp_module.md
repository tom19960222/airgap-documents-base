---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_monitor_tcp module – Manages F5 BIG-IP LTM TCP monitors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_monitor_tcp_module.html
fetched_at: 2026-07-27T17:27:18+00:00
---
# f5networks.f5_modules.bigip_monitor_tcp module – Manages F5 BIG-IP LTM TCP monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_tcp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_tcp_module.md#synopsis)
- [Parameters](bigip_monitor_tcp_module.md#parameters)
- [Notes](bigip_monitor_tcp_module.md#notes)
- [Examples](bigip_monitor_tcp_module.md#examples)
- [Return Values](bigip_monitor_tcp_module.md#return-values)

## [Synopsis](bigip_monitor_tcp_module.md#id1)

- Manages F5 BIG-IP LTM TCP monitors via iControl REST API.

## [Parameters](bigip_monitor_tcp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description of the monitor. |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template will run. If this parameter is not provided when creating a new monitor, the default value is 5. This value **must** be less than the `timeout` value. |
| **ip**  aliases: alias_address  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’.  If this value is an IP address, and the `type` is `tcp` (the default), then a `port` number must be specified.  In BIG IP Management UI, this field is **Alias Address**. |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `tcp` parent on the `Common` partition.  Default: `"/Common/tcp"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  aliases: alias_service_port  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. If specifying an IP address, you must specify a value between 1 and 65535.  This argument is not supported for TCP Echo types.  In BIG IP Management UI, this field is **Alias Service Port**. |
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
| **receive**  string | The Receive string for the monitor call. |
| **receive_disable**  string | The Receive Disable string for the monitor call. This setting works like `receive`, except the system marks the node or pool member disabled when its response matches the `receive_disable` string but not `receive`. To use this setting, you must specify both `receive_disable` and `receive`. |
| **send**  string | The Send string for the monitor call. |
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **time_until_up**  integer | Specifies the amount of time in seconds after the first successful response before a node will be marked up. A value of `0` causes a node to be marked up immediately after a valid response is received from the node. If this parameter is not provided when creating a new monitor, the default value is `0`. |
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this number to any number you want, however, it should be 3 times the interval number of seconds plus 1 second. If this parameter is not provided when creating a new monitor, the default value is 16. |

## [Notes](bigip_monitor_tcp_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_tcp_module.md#id4)

```yaml+jinja
- name: Create TCP Monitor
  bigip_monitor_tcp:
    state: present
    name: my_tcp_monitor
    send: tcp string to send
    receive: tcp string to receive
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove TCP Monitor
  bigip_monitor_tcp:
    state: absent
    name: my_tcp_monitor
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_monitor_tcp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description of the monitor.  Returned: changed  Sample: `"Important Monitor"` |
| **interval**  integer | The new interval at which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  Returned: changed  Sample: `"tcp"` |
| **port**  string | The new port of IP/port definition.  Returned: changed  Sample: `"admin@root.local"` |
| **receive**  string | The new Receive string for this monitor.  Returned: changed  Sample: `"tcp string to receive"` |
| **receive_disable**  string | The new Receive Disable string for this monitor.  Returned: changed  Sample: `"tcp string to receive"` |
| **send**  string | The new Send string for this monitor.  Returned: changed  Sample: `"tcp string to send"` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  Returned: changed  Sample: `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
