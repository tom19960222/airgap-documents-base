---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_monitor_external module – Manages external LTM monitors on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_monitor_external_module.html
fetched_at: 2026-07-27T17:27:11+00:00
---
# f5networks.f5_modules.bigip_monitor_external module – Manages external LTM monitors on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_external`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_external_module.md#synopsis)
- [Parameters](bigip_monitor_external_module.md#parameters)
- [Notes](bigip_monitor_external_module.md#notes)
- [Examples](bigip_monitor_external_module.md#examples)
- [Return Values](bigip_monitor_external_module.md#return-values)

## [Synopsis](bigip_monitor_external_module.md#id1)

- Manages external LTM monitors on a BIG-IP device.

## [Parameters](bigip_monitor_external_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arguments**  string | Specifies any command-line arguments the script requires. |
| **description**  string | The description of the monitor. |
| **external_program**  string | Specifies the name of the file for the monitor to use. In order to reference a file, you must first import it using options on the **System > File Management > External Monitor Program File List > Import** screen. The BIG-IP system automatically places the file in the proper location on the file system. |
| **interval**  integer | The interval specifying how frequently the monitor instance of this template will run. If this parameter is not provided when creating a new monitor, the default value will be 5. This value **must** be less than the `timeout` value. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value will be ‘\*’. |
| **name**  string / required | Specifies the name of the monitor. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `external` parent on the `Common` partition.  Default: `"/Common/external"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, then the default value will be ‘\*’. If specifying an IP address, you must use a value between 1 and 65535. |
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
| **timeout**  integer | The number of seconds in which the node or service must respond to the monitor request.  If the target responds within the set time period, it is considered up.  If the target does not respond within the set time period, it is considered down.  You can change this to any number, however, it should be 3 times the interval number of seconds plus 1 second.  If this parameter is not provided when creating a new monitor, the default value will be `16`. |
| **variables**  dictionary | Specifies any variables the script requires.  Note that double quotes in values will be suppressed. |

## [Notes](bigip_monitor_external_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_external_module.md#id4)

```yaml+jinja
- name: Create an external monitor
  bigip_monitor_external:
    name: foo
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Create an external monitor with variables
  bigip_monitor_external:
    name: foo
    timeout: 10
    variables:
      var1: foo
      var2: bar
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Add a variable to an existing set
  bigip_monitor_external:
    name: foo
    timeout: 10
    variables:
      var1: foo
      var2: bar
      cat: dog
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_monitor_external_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description of the monitor.  Returned: changed  Sample: `"Important Monitor"` |
| **interval**  integer | The new interval at which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **parent**  string | New parent template of the monitor.  Returned: changed  Sample: `"external"` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
