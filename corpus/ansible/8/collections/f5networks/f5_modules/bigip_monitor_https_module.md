---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_monitor_https module – Manages F5 BIG-IP LTM HTTPS monitors"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_monitor_https_module.html
fetched_at: 2026-07-28T02:06:42+00:00
---
# f5networks.f5_modules.bigip_monitor_https module – Manages F5 BIG-IP LTM HTTPS monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_https`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_https_module.md#synopsis)
- [Parameters](bigip_monitor_https_module.md#parameters)
- [Notes](bigip_monitor_https_module.md#notes)
- [Examples](bigip_monitor_https_module.md#examples)
- [Return Values](bigip_monitor_https_module.md#return-values)

## [Synopsis](bigip_monitor_https_module.md#id1)

- Manages F5 BIG-IP LTM HTTPS monitors.

## [Parameters](bigip_monitor_https_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cipher_list**  string  *added in f5networks.f5_modules 1.3.0* | Specifies the list of ciphers for this monitor.  The items in the cipher list are separated with a colon `:`. |
| **description**  string | The description of the monitor. |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template runs. If this parameter is not provided when creating a new monitor, the default value is 5. This value **must** be less than the `timeout` value. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `https` parent on the `Common` partition.  **Default:** `"/Common/https"` |
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
| **receive**  string | The Receive string for the monitor call. |
| **receive_disable**  string | This setting works like `receive`, except the system marks the node or pool member disabled when its response matches the `receive_disable` string but not `receive`. To use this setting, you must specify both `receive_disable` and `receive`. |
| **reverse**  boolean  *added in f5networks.f5_modules 1.12.0* | Specifies whether the monitor operates in reverse mode.  When the monitor is in reverse mode, a successful receive string match marks the monitored object down instead of up. You can use the this mode only if you configure the `receive` option.  This parameter is not compatible with the `time_until_up` parameter. If `time_until_up` is specified, it must be `0`. Or, if it already exists, it must be `0`.  **Choices:**   - `false` - `true` |
| **send**  string | The Send string for the monitor call. When creating a new monitor, if this value is not provided, the default `GET /\\r\\n` is used. |
| **ssl_profile**  string | Specifies the SSL profile to use for the HTTPS monitor.  Defining SSL profiles enables refined customization of the SSL attributes for an HTTPS monitor.  This parameter is only supported on BIG-IP versions 13.x and later. |
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **target_password**  string | Specifies the password, if the monitored target requires authentication. |
| **target_username**  string | Specifies the user name, if the monitored target requires authentication. |
| **time_until_up**  integer | Specifies the amount of time in seconds after the first successful response before a node is marked up. A value of 0 causes a node to be marked up immediately after a valid response is received from the node. If this parameter is not provided when creating a new monitor, then the default value is 0. |
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request. If the target responds within the set time period, it is considered up. If the target does not respond within the set time period, it is considered down. You can change this to any number, however, it should be 3 times the interval number of seconds plus 1 second. If this parameter is not provided when creating a new monitor, the default value is 16. |
| **up_interval**  integer | Specifies the interval for the system to use to perform the health check when a resource is up.  When `0`, specifies the system uses the interval specified in `interval` to check the health of the resource.  When any other number, enables you to specify a different interval when checking the health of a resource that is up. |

## [Notes](bigip_monitor_https_module.md#id3)

> **Note:**
>
> - Requires BIG-IP software version >= 12
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_https_module.md#id4)

```yaml+jinja
- name: Create HTTPS Monitor
  bigip_monitor_https:
    name: my_http_monitor
    state: present
    ip: 10.10.10.10
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove HTTPS Monitor
  bigip_monitor_https:
    name: my_http_monitor
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_monitor_https_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cipher_list**  string | The new value for the cipher list.  **Returned:** changed  **Sample:** `"+3DES:+kEDH"` |
| **description**  string | The description of the monitor.  **Returned:** changed  **Sample:** `"Important Monitor"` |
| **interval**  integer | The new interval at which to run the monitor check.  **Returned:** changed  **Sample:** `2` |
| **ip**  string | The new IP of IP/port definition.  **Returned:** changed  **Sample:** `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  **Returned:** changed  **Sample:** `"https"` |
| **reverse**  boolean | Whether the monitor operates in reverse mode.  **Returned:** changed  **Sample:** `true` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  **Returned:** changed  **Sample:** `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  **Returned:** changed  **Sample:** `10` |
| **up_interval**  integer | Interval for the system to use to perform the health check when a resource is up.  **Returned:** changed  **Sample:** `0` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
