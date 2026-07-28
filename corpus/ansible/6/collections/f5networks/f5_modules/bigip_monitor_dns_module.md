---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_monitor_dns module – Manage DNS monitors on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_monitor_dns_module.html
fetched_at: 2026-07-27T17:27:10+00:00
---
# f5networks.f5_modules.bigip_monitor_dns module – Manage DNS monitors on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_dns`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_dns_module.md#synopsis)
- [Parameters](bigip_monitor_dns_module.md#parameters)
- [Notes](bigip_monitor_dns_module.md#notes)
- [Examples](bigip_monitor_dns_module.md#examples)
- [Return Values](bigip_monitor_dns_module.md#return-values)

## [Synopsis](bigip_monitor_dns_module.md#id1)

- Manages DNS health monitors on a BIG-IP.

## [Parameters](bigip_monitor_dns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_rcode**  string | Specifies the RCODE required in the response for an up status.  When creating a new monitor, if this parameter is not specified, the default value is `no-error`.  When `no-error`, specifies the status of the node will be marked up if the received DNS message has no error.  When `anything`, specifies the status of the node will be marked up irrespective of the RCODE in the DNS message received.  If this parameter is set to `anything`, it will disregard the `receive` string, and nullify it if the monitor is being updated.  Choices:   - `"no-error"` - `"anything"` |
| **adaptive**  boolean | Specifies whether adaptive response time monitoring is enabled for this monitor.  When `yes`, the monitor determines the state of a service based on how divergent from the mean latency a monitor probe for that service is allowed to be. Also, values for the `allowed_divergence`, `adaptive_limit`, and and `sampling_timespan` will be enforced.  When `disabled`, the monitor determines the state of a service based on the `interval`, `up_interval`, `time_until_up`, and `timeout` monitor settings.  Choices:   - `false` - `true` |
| **adaptive_limit**  integer | Specifies the absolute number of milliseconds that may not be exceeded by a monitor probe, regardless of `allowed_divergence` setting, for a probe to be considered successful.  This value applies regardless of the value of the `allowed_divergence` setting.  While this value can be configured when `adaptive` is `no`, it will not take effect on the system until `adaptive` is `yes`. |
| **allowed_divergence_type**  string | When specifying a new monitor, if `adaptive` is `yes`, the default is `relative`.  When `absolute`, the number of milliseconds the latency of a monitor probe can exceed the mean latency of a monitor probe for the service being probed. In typical cases, if the monitor detects three probes in a row that miss the latency value you set, the pool member or node is marked down.  When `relative`, the percentage of deviation the latency of a monitor probe can exceed the mean latency of a monitor probe for the service being probed.  Choices:   - `"relative"` - `"absolute"` |
| **allowed_divergence_value**  integer | When specifying a new monitor, if `adaptive` is `yes`, and `type` is `relative`, the default is `25` percent. |
| **answer_section_contains**  string | Specifies the type of DNS query the monitor sends.  When creating a new monitor, if this value is not specified, the default value is `query-type`.  When `query-type`, specifies that the response should contain at least one answer of which the resource record type matches the query type.  When `any-type`, specifies the DNS message should contain at least one answer.  When `anything`, specifies an empty answer is enough to mark the status of the node up.  Choices:   - `"any-type"` - `"anything"` - `"query-type"` |
| **description**  string | The description of the monitor. |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template will run.  This value **must** be less than the `timeout` value.  When creating a new monitor, if this parameter is not provided, the default `5` will be used. |
| **ip**  string | IP address part of the IP/port definition.  If this parameter is not provided when creating a new monitor, the default value will be `*`. |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  If `yes`, you must manually re-enable the resource before the system can use it for load balancing connections.  When creating a new monitor, if this parameter is not specified, the default value is `no`.  When `yes`, specifies you must manually re-enable the resource after an unsuccessful monitor check.  When `no`, specifies the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the monitor. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `dns` parent on the `Common` partition.  Default: `"/Common/dns"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  string | Port address part of the IP/port definition.  If this parameter is not provided when creating a new monitor, the default value will be `*`.  Note that if specifying an IP address, you must use a value between 1 and 65535. |
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
| **query_name**  string | Specifies a query name for the monitor to use in a DNS query. |
| **query_type**  string | Specifies the type of DNS query the monitor sends.  When creating a new monitor, if this parameter is not specified, the default value is `a`.  When `a`, specifies the monitor will send a DNS query of type A.  When `aaaa`, specifies the monitor will send a DNS query of type AAAA.  Choices:   - `"a"` - `"aaaa"` |
| **receive**  string | Specifies the IP address the monitor uses from the resource record sections of the DNS response.  The IP address should be specified in the dotted-decimal notation or IPv6 notation. |
| **reverse**  boolean | Specifies whether the monitor operates in reverse mode.  When the monitor is in reverse mode, a successful receive string match marks the monitored object down instead of up. You can use the this mode only if you configure the `receive` option.  This parameter is not compatible with the `time_until_up` parameter. If `time_until_up` is specified, it must be `0`. Or, if it already exists, it must be `0`.  Choices:   - `false` - `true` |
| **sampling_timespan**  integer | Specifies the length, in seconds, of the probe history window the system uses to calculate the mean latency and standard deviation of a monitor probe.  While this value can be configured when `adaptive` is `no`, it will not take effect on the system until `adaptive` is `yes`. |
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **time_until_up**  integer | Specifies the amount of time in seconds after the first successful response before a node will be marked up.  A value of 0 will cause a node to be marked up immediately after a valid response is received from the node.  If this parameter is not provided when creating a new monitor, the default value will be `0`. |
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request.  If the target responds within the set time period, it is considered up.  If the target does not respond within the set time period, it is considered down.  You can change this to any number, however, it should be 3 times the interval number of seconds plus 1 second.  If this parameter is not provided when creating a new monitor, the default value will be `16`. |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Monitors in transparent mode can monitor pool members through firewalls.  When creating a new monitor, if this parameter is not provided, the default value will be `no`.  Choices:   - `false` - `true` |
| **up_interval**  integer | Specifies the interval for the system to use to perform the health check when a resource is up.  When `0`, specifies the system uses the interval specified in `interval` to check the health of the resource.  When any other number, enables you to specify a different interval to use when checking the health of a resource that is up.  When creating a new monitor, if this parameter is not provided, the default `0` will be used. |

## [Notes](bigip_monitor_dns_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_dns_module.md#id4)

```yaml+jinja
- name: Create a DNS monitor
  bigip_monitor_dns:
    name: DNS-UDP-V6
    interval: 2
    query_name: localhost
    query_type: aaaa
    up_interval: 5
    adaptive: no
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_monitor_dns_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **accept_rcode**  string | RCODE required in the response for an up status.  Returned: changed  Sample: `"no-error"` |
| **adaptive**  boolean | Whether adaptive is enabled or not.  Returned: changed  Sample: `true` |
| **adaptive_limit**  integer | Absolute number of milliseconds that may not be exceeded by a monitor probe.  Returned: changed  Sample: `200` |
| **allowed_divergence_type**  string | Type of divergence used for adaptive response time monitoring.  Returned: changed  Sample: `"absolute"` |
| **allowed_divergence_value**  integer | Value of the type of divergence used for adaptive response time monitoring.  May be `percent` or `ms` depending on whether `relative` or `absolute`.  Returned: changed  Sample: `25` |
| **answer_section_contains**  string | Type of DNS query that the monitor sends.  Returned: changed  Sample: `"query-type"` |
| **description**  string | The description of the monitor.  Returned: changed  Sample: `"Important Monitor"` |
| **interval**  integer | The new interval in which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **manual_resume**  string | Whether the system automatically changes the status of a resource to enabled at the next successful monitor check.  Returned: changed  Sample: `"query-type"` |
| **parent**  string | New parent template of the monitor.  Returned: changed  Sample: `"http"` |
| **port**  string | Alias port or service for the monitor to check, on behalf of the pools or pool members with which the monitor is associated.  Returned: changed  Sample: `"80"` |
| **query_name**  string | Query name for the monitor to use in a DNS query.  Returned: changed  Sample: `"foo"` |
| **query_type**  string | Type of DNS query the monitor sends. Either `a` or `aaaa`.  Returned: changed  Sample: `"aaaa"` |
| **receive**  string | IP address the monitor uses from the resource record sections of the DNS response.  Returned: changed  Sample: `"2.3.2.4"` |
| **reverse**  boolean | Whether the monitor operates in reverse mode.  Returned: changed  Sample: `true` |
| **sampling_timespan**  integer | Absolute number of milliseconds that may not be exceeded by a monitor probe.  Returned: changed  Sample: `200` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  Returned: changed  Sample: `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |
| **transparent**  boolean | Whether the monitor operates in transparent mode.  Returned: changed  Sample: `false` |
| **up_interval**  integer | Interval for the system to use to perform the health check when a resource is up.  Returned: changed  Sample: `0` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
