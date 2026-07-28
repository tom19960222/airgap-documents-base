---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_monitor_ldap module – Manages BIG-IP LDAP monitors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_monitor_ldap_module.html
fetched_at: 2026-07-27T17:27:15+00:00
---
# f5networks.f5_modules.bigip_monitor_ldap module – Manages BIG-IP LDAP monitors

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_monitor_ldap`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_monitor_ldap_module.md#synopsis)
- [Parameters](bigip_monitor_ldap_module.md#parameters)
- [Notes](bigip_monitor_ldap_module.md#notes)
- [Examples](bigip_monitor_ldap_module.md#examples)
- [Return Values](bigip_monitor_ldap_module.md#return-values)

## [Synopsis](bigip_monitor_ldap_module.md#id1)

- Manages BIG-IP LDAP monitors.

## [Parameters](bigip_monitor_ldap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **base**  string | Specifies the location in the LDAP tree from which the monitor starts the health check. |
| **chase_referrals**  boolean | Upon receipt of an LDAP referral entry, specifies whether the target follows (or chases) that referral.  Choices:   - `false` - `true` |
| **debug**  boolean | Specifies whether the monitor sends error messages and additional information to a log file created and labeled specifically for this monitor.  Choices:   - `false` - `true` |
| **description**  string | Specifies descriptive text that identifies the monitor. |
| **filter**  string | Specifies an LDAP key for which the monitor searches. |
| **interval**  integer | Specifies the frequency, in seconds, at which the system issues the monitor check when either the resource is down or the status of the resource is unknown. |
| **ip**  string | IP address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’. |
| **mandatory_attributes**  boolean | Specifies whether the target must include attributes in its response to be considered up.  Choices:   - `false` - `true` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  If you set this option to `yes`, you must manually re-enable the resource before the system can use it for load balancing connections.  When `yes`, specifies you must manually re-enable the resource after an unsuccessful monitor check.  When `no`, specifies the system automatically changes the status of a resource to **enabled** at the next successful monitor check.  Choices:   - `false` - `true` |
| **name**  string / required | Monitor name. |
| **parent**  string | The parent template of this monitor template. Once this value has been set, it cannot be changed.  By default, this value is the `ldap` parent on the `Common` partition.  Default: `"/Common/ldap"` |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **port**  string | Port address part of the IP/port definition. If this parameter is not provided when creating a new monitor, the default value is ‘\*’.  Note that if specifying an IP address, you must specify a value between 1 and 65535. |
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
| **security**  string | Specifies the secure protocol type for communication with the target.  Choices:   - `"none"` - `"ssl"` - `"tls"` |
| **state**  string | When `present`, ensures the monitor exists.  When `absent`, ensures the monitor is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **target_password**  string | Specifies the password, if the monitored target requires authentication. |
| **target_username**  string | Specifies the user name, if the monitored target requires authentication. |
| **time_until_up**  integer | Specifies the number of seconds to wait after a resource first responds correctly to the monitor before setting the resource to ‘up’.  During the interval, all responses from the resource must be correct.  When the interval expires, the resource is marked ‘up’.  A value of 0 means the resource is marked up immediately upon receipt of the first correct response. |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  If the target responds within the set time period, it is considered ‘up’. If the target does not respond within the set time period, it is considered ‘down’. When this value is set to 0 (zero), the system uses the interval from the parent monitor.  Note that `timeout` and `time_until_up` combine to control when a resource is set to up. |
| **up_interval**  integer | Specifies the interval for the system to use to perform the health check when a resource is up.  When `0`, specifies the system uses the interval specified in `interval` to check the health of the resource.  When any other number, enables you to specify a different interval to use when checking the health of a resource that is up. |
| **update_password**  string | `always` will update passwords if the `target_password` is specified.  `on_create` will only set the password for newly created monitors.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_monitor_ldap_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_monitor_ldap_module.md#id4)

```yaml+jinja
- name: Create a LDAP monitor
  bigip_monitor_ldap:
    name: foo
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_monitor_ldap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **base**  string | The new LDAP Base setting of the resource.  Returned: changed  Sample: `"base"` |
| **chase_referrals**  boolean | The new Chase Referrals setting of the resource.  Returned: changed  Sample: `true` |
| **debug**  boolean | The new Debug setting of the resource.  Returned: changed  Sample: `true` |
| **description**  string | The description of the monitor.  Returned: changed  Sample: `"Important_Monitor"` |
| **filter**  string | The new LDAP Filter setting of the resource.  Returned: changed  Sample: `"filter1"` |
| **interval**  integer | The new interval in which to run the monitor check.  Returned: changed  Sample: `2` |
| **ip**  string | The new IP of IP/port definition.  Returned: changed  Sample: `"10.12.13.14"` |
| **mandatory_attributes**  boolean | The new Mandatory Attributes setting of the resource.  Returned: changed  Sample: `false` |
| **manual_resume**  boolean | The new Manual Resume setting of the resource.  Returned: changed  Sample: `false` |
| **parent**  string | New parent template of the monitor.  Returned: changed  Sample: `"ldap"` |
| **security**  string | The new Security setting of the resource.  Returned: changed  Sample: `"ssl"` |
| **time_until_up**  integer | The new time in which to mark a system as up after first successful response.  Returned: changed  Sample: `2` |
| **timeout**  integer | The new timeout in which the remote system must respond to the monitor.  Returned: changed  Sample: `10` |

### Authors

- Tim Rupp (@caphrim007)
- Greg Crosby (@crosbygw)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
