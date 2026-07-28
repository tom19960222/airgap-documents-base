---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_monitor_oracle module – Manages BIG-IP Oracle monitors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_monitor_oracle_module.html
fetched_at: 2026-07-27T17:27:16+00:00
---
# f5networks.f5_modules.bigip_monitor_oracle module – Manages BIG-IP Oracle monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_oracle`.

New in f5networks.f5_modules 1.3.0

- [Synopsis](bigip_monitor_oracle_module.md#synopsis)
- [Parameters](bigip_monitor_oracle_module.md#parameters)
- [Notes](bigip_monitor_oracle_module.md#notes)
- [Examples](bigip_monitor_oracle_module.md#examples)
- [Return Values](bigip_monitor_oracle_module.md#return-values)

## [Synopsis](bigip_monitor_oracle_module.md#id1)

- Manages BIG-IP Oracle monitors.

## [Parameters](bigip_monitor_oracle_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **app_service**  string | The iApp service to be associated with this profile. When no service is specified, the default is None. |
| **count**  integer | Specifies the number of monitor probes after which the connection to the database will be terminated.  Count value of zero indicates that the connection will never be terminated. |
| **database**  string | Specifies the name of the database the monitor tries to access. |
| **debug**  boolean | Specifies whether the monitor sends error messages and additional information to a log file created and labeled specifically for this monitor.  Choices:   - `false` - `true` |
| **description**  string | Specifies descriptive text that identifies the monitor. |
| **interval**  integer | Specifies the frequency, in seconds, at which the system issues the monitor check when either the resource is down or the status of the resource is unknown. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  If you set this option to `yes`, you must manually re-enable the resource before the system can use it for load balancing connections.  When `yes`, specifies you must manually re-enable the resource after an unsuccessful monitor check.  When `no`, specifies the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  Choices:   - `false` - `true` |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed.  By default, this value is the `oracle` parent on the `Common` partition. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’.  If specifying an IP address, you must specify a value between 1 and 65535. |
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
| **recv**  string | Specifies the text string that the monitor looks for in the returned resource.  The most common receive expressions contain a text string that is included in a field in your database.  If you do not specify both `send` and a `recv` parameters, the monitor performs a simple service check and connect only. |
| **recv_column**  string | Specifies the column in the database where the specified `recv` string should be located.  This is an optional setting and is applicable only if you configure the `send` and the `recv` parameters. |
| **recv_row**  string | Specifies the row in the database where the specified `recv` string should be located.  This is an optional setting, and is applicable only if you configure the `send` and the `recv` parameters. |
| **send**  string | Specifies the SQL query the monitor sends to the target object.  Since the string may have special characters, the system may require the string be enclosed with single quotation marks. If this value is `none`, a valid connection suffices to determine the service is up. In this case, the system does not need the recv, recv-row, and recv-column options and ignores them even if not `none`. |
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **target_password**  string | Specifies the password, if the monitored target requires authentication. |
| **target_username**  string | Specifies the user name, if the monitored target requires authentication. |
| **time_until_up**  integer | Specifies the number of seconds to wait after a resource first responds correctly to the monitor before setting the resource to ‘up’.  During the interval, all responses from the resource must be correct.  When the interval expires, the resource is marked ‘up’.  A value of 0 means the resource is marked up immediately upon receipt of the first correct response. |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  If the target responds within the set time period, it is considered ‘up’. If the target does not respond within the set time period, it is considered ‘down’. When this value is set to 0 (zero), the system uses the interval from the parent monitor.  Note that `timeout` and `time_until_up` combine to control when a resource is set to up. |
| **up_interval**  integer | Specifies the interval for the system to use to perform the health check when a resource is up.  When `0`, specifies the system uses the interval in `interval` to check the health of the resource.  When any other number, enables you to specify a different interval to use when checking the health of a resource that is up. |
| **update_password**  string | `always` will update passwords if the `target_password` is specified.  `on_create` will only set the password for newly created monitors.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_monitor_oracle_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_oracle_module.md#id4)

```yaml+jinja
- name: Create an oracle monitor
  bigip_monitor_oracle:
    ip: 10.10.10.10
    port: 10923
    name: my_oracle_monitor
    send: "SELECT status FROM v$instance"
    recv: OPEN
    recv_column: 2
    recv_row: 1
    database: primary1
    target_username: bigip
    target_password: secret
    update_password: on_create
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Modify an oracle monitor
  bigip_monitor_oracle:
    name: my_oracle_monitor
    recv_column: 4
    recv_row: 3
    database: primary2
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Remove oracle monitor
  bigip_monitor_oracle:
    state: absent
    name: my_oracle_monitor
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_monitor_oracle_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **app_service**  string | The iApp service associated with this monitor.  Returned: changed  Sample: `"/Common/good_service.app/good_service"` |
| **database**  string | The name of the database that the monitor tries to access.  Returned: changed  Sample: `"primary1"` |
| **debug**  boolean | Whether the monitor sends error messages and additional information to a log file created and labeled specifically for this monitor.  Returned: changed  Sample: `false` |
| **description**  string | The description of the monitor.  Returned: changed  Sample: `"Important Monitor"` |
| **interval**  integer | The new interval at which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.  Returned: changed  Sample: `true` |
| **parent**  string | The parent monitor.  Returned: changed  Sample: `"/Common/foo_oracle"` |
| **port**  string | Alias port or service for the monitor to check, on behalf of the pools or pool members with which the monitor is associated.  Returned: changed  Sample: `"80"` |
| **recv**  string | The text string that the monitor looks for in the returned resource.  Returned: changed  Sample: `"OPEN"` |
| **recv_column**  string | The column in the database where the specified string should be located.  Returned: changed  Sample: `"2"` |
| **recv_row**  string | The row in the database where the specified string should be located.  Returned: changed  Sample: `"1"` |
| **send**  string | The SQL query the monitor sends to the target object.  Returned: changed  Sample: `"SELECT status FROM v$instance"` |
| **target_username**  string | The user name for the the monitored target.  Returned: changed  Sample: `"bigip"` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  Returned: changed  Sample: `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |
| **up_interval**  integer | Interval for the system to use to perform the health check when a resource is up.  Returned: changed  Sample: `0` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
