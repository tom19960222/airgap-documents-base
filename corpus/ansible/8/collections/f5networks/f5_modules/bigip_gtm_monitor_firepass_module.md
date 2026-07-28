---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_gtm_monitor_firepass module – Manages F5 BIG-IP GTM FirePass monitors"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_gtm_monitor_firepass_module.html
fetched_at: 2026-07-28T02:06:16+00:00
---
# f5networks.f5_modules.bigip_gtm_monitor_firepass module – Manages F5 BIG-IP GTM FirePass monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_monitor_firepass`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_monitor_firepass_module.md#synopsis)
- [Parameters](bigip_gtm_monitor_firepass_module.md#parameters)
- [Notes](bigip_gtm_monitor_firepass_module.md#notes)
- [Examples](bigip_gtm_monitor_firepass_module.md#examples)
- [Return Values](bigip_gtm_monitor_firepass_module.md#return-values)

## [Synopsis](bigip_gtm_monitor_firepass_module.md#id1)

- Manages F5 BIG-IP GTM (now BIG-IP DNS) FirePass monitors.

## [Parameters](bigip_gtm_monitor_firepass_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cipher_list**  string | Specifies the list of ciphers for this monitor.  The items in the cipher list are separated with the colon `:` symbol.  When creating a new monitor, if this parameter is not specified, the default list is `HIGH:!ADH`. |
| **concurrency_limit**  integer | Specifies the maximum percentage of licensed connections currently in use under which the monitor marks the Secure Access Manager system up.  As an example, a setting of 95 percent means that the monitor marks the Secure Access Manager system up until 95 percent of licensed connections are in use.  When the number of in-use licensed connections exceeds 95 percent, the monitor marks the Secure Access Manager system down.  When creating a new monitor, if this parameter is not specified, the default is `95`. |
| **ignore_down_response**  boolean | Specifies the monitor allows more than one probe attempt per interval.  When `true`, specifies the monitor ignores down responses for the duration of the monitor timeout. Once the monitor timeout is reached without the system receiving an up response, the system marks the object down.  When `no`, specifies the monitor immediately marks an object down when it receives a down response.  When creating a new monitor, if this parameter is not provided, the default value is `false`.  **Choices:**   - `false` - `true` |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template runs.  If this parameter is not provided when creating a new monitor, then the default value is 30.  This value **must** be less than the `timeout` value. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’.  If this value is an IP address, a `port` number must be specified. |
| **max_load_average**  integer | Specifies the number the monitor uses to mark the Secure Access Manager system up or down.  The system compares the Max Load Average setting against a one-minute average of the Secure Access Manager system load.  When the Secure Access Manager system-load average falls within the specified Max Load Average, the monitor marks the Secure Access Manager system up.  When the average exceeds the setting, the monitor marks the system down.  When creating a new monitor, if this parameter is not specified, the default is `12`. |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `tcp` parent on the `Common` partition.  **Default:** `"/Common/firepass_gtm"` |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. Note that if specifying an IP address, a value between 1 and 65535 must be specified. |
| **probe_timeout**  integer | Specifies the number of seconds after which the system times out the probe request to the system.  When creating a new monitor, if this parameter is not provided, the default value is `5`. |
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
| **target_password**  string | Specifies the password, if the monitored target requires authentication. |
| **target_username**  string | Specifies the user name, if the monitored target requires authentication. |
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this to any number, however, it should be 3 times the interval number of seconds plus 1 second.  If this parameter is not provided when creating a new monitor, the default value is 90. |
| **update_password**  string | `always` updates passwords if the `target_password` is specified.  `on_create` only sets the password for newly created monitors.  **Choices:**   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_gtm_monitor_firepass_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_monitor_firepass_module.md#id4)

```yaml+jinja
- name: Create a GTM FirePass monitor
  bigip_gtm_monitor_firepass:
    name: my_monitor
    ip: 1.1.1.1
    port: 80
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove FirePass Monitor
  bigip_gtm_monitor_firepass:
    name: my_monitor
    state: absent
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add FirePass monitor for all addresses, port 514
  bigip_gtm_monitor_firepass:
    name: my_monitor
    port: 514
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_gtm_monitor_firepass_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cipher_list**  string | The new value for the cipher list.  **Returned:** changed  **Sample:** `"+3DES:+kEDH"` |
| **concurrency_limit**  integer | The new value for the concurrency limit.  **Returned:** changed  **Sample:** `95` |
| **ignore_down_response**  boolean | Whether to ignore the down response or not.  **Returned:** changed  **Sample:** `true` |
| **interval**  integer | The new interval in which to run the monitor check.  **Returned:** changed  **Sample:** `2` |
| **ip**  string | The new IP of IP/port definition.  **Returned:** changed  **Sample:** `"10.12.13.14"` |
| **max_load_average**  integer | The new value for the max load average.  **Returned:** changed  **Sample:** `12` |
| **parent**  string | New parent template of the monitor.  **Returned:** changed  **Sample:** `"firepass_gtm"` |
| **port**  string | The new port the monitor checks the resource on.  **Returned:** changed  **Sample:** `"8080"` |
| **probe_timeout**  integer | The new timeout in which the system will timeout the monitor probe.  **Returned:** changed  **Sample:** `10` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  **Returned:** changed  **Sample:** `10` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
