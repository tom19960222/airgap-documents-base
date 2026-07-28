---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_monitor_snmp_dca module – Manages BIG-IP SNMP data collecting agent (DCA) monitors"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_monitor_snmp_dca_module.html
fetched_at: 2026-07-28T02:06:46+00:00
---
# f5networks.f5_modules.bigip_monitor_snmp_dca module – Manages BIG-IP SNMP data collecting agent (DCA) monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_snmp_dca`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_snmp_dca_module.md#synopsis)
- [Parameters](bigip_monitor_snmp_dca_module.md#parameters)
- [Notes](bigip_monitor_snmp_dca_module.md#notes)
- [Examples](bigip_monitor_snmp_dca_module.md#examples)
- [Return Values](bigip_monitor_snmp_dca_module.md#return-values)

## [Synopsis](bigip_monitor_snmp_dca_module.md#id1)

- The BIG-IP has an SNMP data collecting agent (DCA) that can query remote SNMP agents of various types, including the UC Davis agent (UCD) and the Windows 2000 Server agent (WIN2000).

## [Parameters](bigip_monitor_snmp_dca_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **agent_type**  string | Specifies the SNMP agent running on the monitored server. When creating a new monitor, the default is `UCD` (UC-Davis).  **Choices:**   - `"UCD"` - `"WIN2000"` - `"GENERIC"` |
| **community**  string | Specifies the community name the system must use to authenticate with the host server through SNMP. When creating a new monitor, the default value is `public`. This value is case sensitive. |
| **cpu_coefficient**  string | Specifies the coefficient the system uses to calculate the weight of the CPU threshold in the dynamic ratio load balancing algorithm. When creating a new monitor, the default is `1.5`. |
| **cpu_threshold**  integer | Specifies the maximum acceptable CPU usage on the target server. When creating a new monitor, the default is `80` percent. |
| **description**  string | Specifies descriptive text that identifies the monitor. |
| **disk_coefficient**  string | Specifies the coefficient the system uses to calculate the weight of the disk threshold in the dynamic ratio load balancing algorithm. When creating a new monitor, the default is `2.0`. |
| **disk_threshold**  integer | Specifies the maximum acceptable disk usage on the target server. When creating a new monitor, the default is `90` percent. |
| **interval**  integer | Specifies the frequency, in seconds, at which the system issues the monitor check when either the resource is down or the status of the resource is unknown. When creating a new monitor, the default is `10`. |
| **memory_coefficient**  string | Specifies the coefficient the system uses to calculate the weight of the memory threshold in the dynamic ratio load balancing algorithm. When creating a new monitor, the default is `1.0`. |
| **memory_threshold**  integer | Specifies the maximum acceptable memory usage on the target server. When creating a new monitor, the default is `70` percent. |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `snmp_dca` parent on the `Common` partition.  **Default:** `"/Common/snmp_dca"` |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
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
| **time_until_up**  integer | Specifies the number of seconds to wait after a resource first responds correctly to the monitor before setting the resource to ‘up’. During the interval, all responses from the resource must be correct. When the interval expires, the resource is marked ‘up’. A value of 0, means that the resource is marked up immediately upon receipt of the first correct response. When creating a new monitor, the default is `0`. |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request. When creating a new monitor, the default is `30` seconds. If the target responds within the set time period, it is considered ‘up’. If the target does not respond within the set time period, it is considered ‘down’. When this value is set to 0 (zero), the system uses the interval from the parent monitor. Note that `timeout` and `time_until_up` combine to control when a resource is set to up. |
| **version**  string | Specifies the version of SNMP the host server uses. When creating a new monitor, the default is `v1`. When `v1`, specifies the host server uses SNMP version 1. When `v2c`, specifies that the host server uses SNMP version 2c.  **Choices:**   - `"v1"` - `"v2c"` |

## [Notes](bigip_monitor_snmp_dca_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - This module does not support the `variables` option because it is broken in the REST API and does not function correctly in `tmsh`; for example you cannot remove user-defined params. Therefore, there is no way to automatically configure it.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_snmp_dca_module.md#id4)

```yaml+jinja
- name: Create SNMP DCS monitor
  bigip_monitor_snmp_dca:
    name: my_monitor
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove TCP Echo Monitor
  bigip_monitor_snmp_dca:
    name: my_monitor
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_monitor_snmp_dca_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **agent_type**  string | The new agent type to be used by the monitor.  **Returned:** changed  **Sample:** `"UCD"` |
| **community**  string | The new community for the monitor.  **Returned:** changed  **Sample:** `"foobar"` |
| **cpu_coefficient**  float | The new CPU coefficient.  **Returned:** changed  **Sample:** `2.4` |
| **cpu_threshold**  integer | The new CPU threshold.  **Returned:** changed  **Sample:** `85` |
| **description**  string | The description of the monitor.  **Returned:** changed  **Sample:** `"Important Monitor"` |
| **disk_coefficient**  float | The new disk coefficient.  **Returned:** changed  **Sample:** `10.2` |
| **disk_threshold**  integer | The new disk threshold.  **Returned:** changed  **Sample:** `34` |
| **interval**  integer | The new interval at which to run the monitor check.  **Returned:** changed  **Sample:** `2` |
| **memory_coefficient**  float | The new memory coefficient.  **Returned:** changed  **Sample:** `6.4` |
| **memory_threshold**  integer | The new memory threshold.  **Returned:** changed  **Sample:** `50` |
| **parent**  string | New parent template of the monitor.  **Returned:** changed  **Sample:** `"snmp_dca"` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  **Returned:** changed  **Sample:** `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  **Returned:** changed  **Sample:** `10` |
| **version**  string | The new new SNMP version to be used by the monitor.  **Returned:** changed  **Sample:** `"v2c"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
