---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_gtm_monitor_tcp module – Manages F5 BIG-IP GTM TCP monitors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_gtm_monitor_tcp_module.html
fetched_at: 2026-07-27T17:26:51+00:00
---
# f5networks.f5_modules.bigip_gtm_monitor_tcp module – Manages F5 BIG-IP GTM TCP monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_monitor_tcp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_monitor_tcp_module.md#synopsis)
- [Parameters](bigip_gtm_monitor_tcp_module.md#parameters)
- [Notes](bigip_gtm_monitor_tcp_module.md#notes)
- [Examples](bigip_gtm_monitor_tcp_module.md#examples)
- [Return Values](bigip_gtm_monitor_tcp_module.md#return-values)

## [Synopsis](bigip_gtm_monitor_tcp_module.md#id1)

- Manages F5 BIG-IP GTM (now BIG-IP DNS) TCP monitors.

## [Parameters](bigip_gtm_monitor_tcp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ignore_down_response**  boolean | Specifies the monitor allows more than one probe attempt per interval.  When `yes`, specifies the monitor ignores down responses for the duration of the monitor timeout. Once the monitor timeout is reached without the system receiving an up response, the system marks the object down.  When `no`, specifies the monitor immediately marks an object down when it receives a down response.  When creating a new monitor, if this parameter is not provided, the default value will be `no`.  Choices:   - `false` - `true` |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template will run.  If this parameter is not provided when creating a new monitor, the default value will be 30.  This value **must** be less than the `timeout` value. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value will be ‘\*’.  If this value is an IP address, a `port` number must be specified. |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `tcp` parent on the `Common` partition.  Default: `"/Common/tcp"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value will be ‘\*’. Note that if using an IP address, you must specify a value between 1 and 65535. |
| **probe_timeout**  integer | Specifies the number of seconds after which the system times out the probe request to the system.  When creating a new monitor, if this parameter is not provided, then the default value will be `5`. |
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
| **receive**  string | The receive string for the monitor call. |
| **reverse**  boolean | Instructs the system to mark the target resource down when the test is successful. This setting is useful, for example, if the content on your web site home page is dynamic and changes frequently, you may want to set up a reverse ECV service check that looks for the string Error.  A match for this string means the web server was down.  To use this option, you must specify values for `send` and `receive`.  Choices:   - `false` - `true` |
| **send**  string | The send string for the monitor call. |
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this number to any number you want, however, it should be 3 times the interval number of seconds plus 1 second.  If this parameter is not provided when creating a new monitor, the default value will be 120. |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  A monitor in transparent mode directs traffic through the associated pool members or nodes (usually a router or firewall) to the aliased destination (that is, it probes the `ip`-`port` combination specified in the monitor).  If the monitor cannot successfully reach the aliased destination, the pool member or node through which the monitor traffic was sent is marked down.  When creating a new monitor, if this parameter is not provided, then the default value will be `no`.  Choices:   - `false` - `true` |

## [Notes](bigip_gtm_monitor_tcp_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_monitor_tcp_module.md#id4)

```yaml+jinja
- name: Create a GTM TCP monitor
  bigip_gtm_monitor_tcp:
    name: my_monitor
    ip: 1.1.1.1
    port: 80
    send: my send string
    receive: my receive string
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove TCP Monitor
  bigip_gtm_monitor_tcp:
    name: my_monitor
    state: absent
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add TCP monitor for all addresses, port 514
  bigip_gtm_monitor_tcp:
    name: my_monitor
    port: 514
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_monitor_tcp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ignore_down_response**  boolean | Whether to ignore the down response or not.  Returned: changed  Sample: `true` |
| **interval**  integer | The new interval in which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  Returned: changed  Sample: `"tcp"` |
| **port**  string | The new port on which the monitor checks the resource.  Returned: changed  Sample: `"8080"` |
| **probe_timeout**  integer | The new timeout in which the system will timeout the monitor probe.  Returned: changed  Sample: `10` |
| **receive**  string | The new receive string for this monitor.  Returned: changed  Sample: `"tcp string to receive"` |
| **reverse**  boolean | The new value for whether the monitor operates in reverse mode.  Returned: changed  Sample: `false` |
| **send**  string | The new send string for this monitor.  Returned: changed  Sample: `"tcp string to send"` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |
| **transparent**  boolean | The new value for whether the monitor operates in transparent mode.  Returned: changed  Sample: `false` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
