---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_monitor_gateway_icmp module – Manages F5 BIG-IP LTM gateway ICMP monitors"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_monitor_gateway_icmp_module.html
fetched_at: 2026-07-28T02:06:40+00:00
---
# f5networks.f5_modules.bigip_monitor_gateway_icmp module – Manages F5 BIG-IP LTM gateway ICMP monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_gateway_icmp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_gateway_icmp_module.md#synopsis)
- [Parameters](bigip_monitor_gateway_icmp_module.md#parameters)
- [Notes](bigip_monitor_gateway_icmp_module.md#notes)
- [Examples](bigip_monitor_gateway_icmp_module.md#examples)
- [Return Values](bigip_monitor_gateway_icmp_module.md#return-values)

## [Synopsis](bigip_monitor_gateway_icmp_module.md#id1)

- Manages gateway ICMP monitors on a BIG-IP LTM.

## [Parameters](bigip_monitor_gateway_icmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adaptive**  boolean | Specifies whether adaptive response time monitoring is enabled for this monitor.  When `true`, the monitor determines the state of a service based on how divergent from the mean latency a monitor probe for that service is allowed to be. Also, values for the `allowed_divergence`, `adaptive_limit`, and and `sampling_timespan` will be enforced.  When `disabled`, the monitor determines the state of a service based on the `interval`, `up_interval`, `time_until_up`, and `timeout` monitor settings.  **Choices:**   - `false` - `true` |
| **adaptive_limit**  integer | Specifies the absolute number of milliseconds that may not be exceeded by a monitor probe, regardless of `allowed_divergence` setting, for a probe to be considered successful.  This value applies regardless of the value of the `allowed_divergence` setting.  While this value can be configured when `adaptive` is `false`, it will not take effect on the system until `adaptive` is `true`. |
| **allowed_divergence_type**  string | When specifying a new monitor, if `adaptive` is `true`, the default is `relative`.  When `absolute`, the number of milliseconds the latency of a monitor probe can exceed the mean latency of a monitor probe for the service being probed. In typical cases, if the monitor detects three probes in a row that miss the latency value you set, the pool member or node is marked down.  When `relative`, the percentage of deviation the latency of a monitor probe can exceed the mean latency of a monitor probe for the service being probed.  **Choices:**   - `"relative"` - `"absolute"` |
| **allowed_divergence_value**  integer | When specifying a new monitor, if `adaptive` is `true`, and `type` is `relative`, the default is `25` percent. |
| **description**  string | The description of the monitor. |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  If you set this option to `true`, you must manually re-enable the resource before the system can use it for load balancing connections.  When `true`, specifies you must manually re-enable the resource after an unsuccessful monitor check.  When `false`, specifies the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  **Choices:**   - `false` - `true` |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `gateway_icmp` parent on the `Common` partition.  **Default:** `"/Common/gateway_icmp"` |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. If specifying an IP address, you must use a value between 1 and 65535. |
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
| **sampling_timespan**  integer | Specifies the length, in seconds, of the probe history window that the system uses to calculate the mean latency and standard deviation of a monitor probe.  While this value can be configured when `adaptive` is `false`, it will not take effect on the system until `adaptive` is `true`. |
| **state**  string | When `present`, ensures that the monitor exists.  When `absent`, ensures the monitor is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time_until_up**  integer | Specifies the number of seconds to wait after a resource first responds correctly to the monitor before setting the resource to ‘up’.  During the interval, all responses from the resource must be correct.  When the interval expires, the resource is marked ‘up’.  A value of `0` means the resource is marked up immediately upon receipt of the first correct response. |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  If the target responds within the set time period, it is considered ‘up’. If the target does not respond within the set time period, it is considered ‘down’. When this value is set to 0 (zero), the system uses the interval from the parent monitor.  Note that `timeout` and `time_until_up` combine to control when a resource is set to up. |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  A monitor in transparent mode directs traffic through the associated pool members or nodes (usually a router or firewall) to the aliased destination (that is, it probes the `ip`-`port` combination specified in the monitor).  If the monitor cannot successfully reach the aliased destination, the pool member or node through which the monitor traffic was sent is marked down.  When creating a new monitor, if this parameter is not provided, then the default value will be whatever is provided by the `parent`.  **Choices:**   - `false` - `true` |
| **up_interval**  integer | Specifies the interval for the system to use to perform the health check when a resource is up.  When `0`, specifies the system uses the interval specified in `interval` to check the health of the resource.  When any other number, enables you to specify a different interval to use when checking the health of a resource that is up. |

## [Notes](bigip_monitor_gateway_icmp_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_gateway_icmp_module.md#id4)

```yaml+jinja
- name: Create a monitor
  bigip_monitor_gateway_icmp:
    name: gw1
    adaptive: false
    interval: 1
    time_until_up: 0
    timeout: 3
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_monitor_gateway_icmp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **adaptive**  boolean | Whether adaptive is enabled or not.  **Returned:** changed  **Sample:** `true` |
| **adaptive_limit**  integer | Absolute number of milliseconds that may not be exceeded by a monitor probe.  **Returned:** changed  **Sample:** `200` |
| **allowed_divergence_type**  string | Type of divergence used for adaptive response time monitoring.  **Returned:** changed  **Sample:** `"absolute"` |
| **allowed_divergence_value**  integer | Value of the type of divergence used for adaptive response time monitoring.  May be `percent` or `ms` depending on whether `relative` or `absolute`.  **Returned:** changed  **Sample:** `25` |
| **description**  string | The description of the monitor.  **Returned:** changed  **Sample:** `"Important Monitor"` |
| **interval**  integer | The new interval at which to run the monitor check.  **Returned:** changed  **Sample:** `2` |
| **ip**  string | The new IP of IP/port definition.  **Returned:** changed  **Sample:** `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  **Returned:** changed  **Sample:** `"gateway-icmp"` |
| **port**  string | Alias port or service for the monitor to check, on behalf of the pools or pool members with which the monitor is associated.  **Returned:** changed  **Sample:** `"80"` |
| **sampling_timespan**  integer | Absolute number of milliseconds that may not be exceeded by a monitor probe.  **Returned:** changed  **Sample:** `200` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  **Returned:** changed  **Sample:** `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  **Returned:** changed  **Sample:** `10` |
| **transparent**  boolean | Whether the monitor operates in transparent mode.  **Returned:** changed  **Sample:** `false` |
| **up_interval**  integer | Interval for the system to use to perform the health check when a resource is up.  **Returned:** changed  **Sample:** `0` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
