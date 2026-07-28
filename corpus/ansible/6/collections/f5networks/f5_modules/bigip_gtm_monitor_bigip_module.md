---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_gtm_monitor_bigip module – Manages F5 BIG-IP GTM BIG-IP monitors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_gtm_monitor_bigip_module.html
fetched_at: 2026-07-27T17:26:48+00:00
---
# f5networks.f5_modules.bigip_gtm_monitor_bigip module – Manages F5 BIG-IP GTM BIG-IP monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_monitor_bigip`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_monitor_bigip_module.md#synopsis)
- [Parameters](bigip_gtm_monitor_bigip_module.md#parameters)
- [Notes](bigip_gtm_monitor_bigip_module.md#notes)
- [Examples](bigip_gtm_monitor_bigip_module.md#examples)
- [Return Values](bigip_gtm_monitor_bigip_module.md#return-values)

## [Synopsis](bigip_gtm_monitor_bigip_module.md#id1)

- Manages F5 BIG-IP GTM (now BIG-IP DNS) BIG-IP monitors. This monitor is used by GTM to monitor BIG-IPs themselves.

## [Parameters](bigip_gtm_monitor_bigip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate_dynamic_ratios**  string | Specifies how the system combines the module values to create the proportion (score) for the load balancing operation.  The score represents the module’s estimated capacity for handing traffic.  Averaged values are appropriate for downstream Web Accelerator or Application Security Manager (ASM) virtual servers.  When creating a new monitor, if this parameter is not specified, the default of `none` is used, meaning the system does not use the scores in the load balancing operation.  When `none`, specifies the monitor ignores the nodes and pool member scores.  When `average-nodes`, specifies the system averages the dynamic ratios on the nodes associated with the monitor’s target virtual servers and returns that average as the virtual servers’ score.  When `sum-nodes`, specifies the system adds together the scores of the nodes associated with the monitor’s target virtual servers and uses that value in the load balancing operation.  When `average-members`, specifies the system averages the dynamic ratios on the pool members associated with the monitor’s target virtual servers and returns that average as the virtual servers’ score.  When `sum-members`, specifies the system adds together the scores of the pool members associated with the monitor’s target virtual servers and uses that value in the load balancing operation.  Choices:   - `"none"` - `"average-nodes"` - `"sum-nodes"` - `"average-members"` - `"sum-members"` |
| **ignore_down_response**  boolean | Specifies the monitor allows more than one probe attempt per interval.  When `yes`, specifies the monitor ignores down responses for the duration of the monitor timeout. Once the monitor timeout is reached without the system receiving an up response, the system marks the object down.  When `no`, specifies the monitor immediately marks an object down when it receives a down response.  When creating a new monitor, if this parameter is not provided, the default value will be `no`.  Choices:   - `false` - `true` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  When creating a new monitor, if this parameter is not provided, the default value will be `30`. This value **must** be less than the `timeout` value. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value will be ‘\*’. |
| **name**  string / required | Name of the monitor. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `bigip` parent on the `Common` partition.  Default: `"/Common/bigip"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value will be ‘\*’. Note that if specifying an IP address, you must use a value between 1 and 65535. |
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
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  If the target responds within the set time period, it is considered up.  If the target does not respond within the set time period, it is considered down.  When this value is set to 0 (zero), the system uses the interval from the parent monitor.  When creating a new monitor, if this parameter is not provided, the default value will be `90`. |

## [Notes](bigip_gtm_monitor_bigip_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_monitor_bigip_module.md#id4)

```yaml+jinja
- name: Create BIG-IP Monitor
  bigip_gtm_monitor_bigip:
    state: present
    ip: 10.10.10.10
    name: my_monitor
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove BIG-IP Monitor
  bigip_gtm_monitor_bigip:
    state: absent
    name: my_monitor
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add BIG-IP monitor for all addresses, port 514
  bigip_gtm_monitor_bigip:
    port: 514
    name: my_monitor
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_monitor_bigip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **aggregate_dynamic_ratios**  string | The new aggregate of to the monitor.  Returned: changed  Sample: `"sum-members"` |
| **ignore_down_response**  boolean | Whether to ignore the down response or not.  Returned: changed  Sample: `true` |
| **interval**  integer | The new interval at which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  Returned: changed  Sample: `"bigip"` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
