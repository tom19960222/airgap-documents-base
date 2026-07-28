---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_analytics module – Manage HTTP analytics profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_analytics_module.html
fetched_at: 2026-07-28T02:06:56+00:00
---
# f5networks.f5_modules.bigip_profile_analytics module – Manage HTTP analytics profiles on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_analytics`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_analytics_module.md#synopsis)
- [Parameters](bigip_profile_analytics_module.md#parameters)
- [Notes](bigip_profile_analytics_module.md#notes)
- [Examples](bigip_profile_analytics_module.md#examples)
- [Return Values](bigip_profile_analytics_module.md#return-values)

## [Synopsis](bigip_profile_analytics_module.md#id1)

- Manage HTTP analytics profiles on a BIG-IP device.

## [Parameters](bigip_profile_analytics_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **collect_geo**  boolean | Enables or disables the collection of the names of the countries from where the traffic was sent.  **Choices:**   - `false` - `true` |
| **collect_ip**  boolean | Enables or disables the collection of client IPs statistics.  **Choices:**   - `false` - `true` |
| **collect_max_tps_and_throughput**  boolean | Enables or disables the collection of maximum TPS and throughput for all collected entities.  **Choices:**   - `false` - `true` |
| **collect_page_load_time**  boolean | Enables or disables the collection of the page load time statistics.  **Choices:**   - `false` - `true` |
| **collect_url**  boolean | Enables or disables the collection of requested URL statistics.  **Choices:**   - `false` - `true` |
| **collect_user_agent**  boolean | Enables or disables the collection of user agents.  **Choices:**   - `false` - `true` |
| **collect_user_sessions**  boolean | Enables or disables the collection of the unique user sessions.  **Choices:**   - `false` - `true` |
| **collected_stats_external_logging**  boolean | Enables or disables the external logging of the collected statistics.  **Choices:**   - `false` - `true` |
| **collected_stats_internal_logging**  boolean | Enables or disables the internal logging of the collected statistics.  **Choices:**   - `false` - `true` |
| **description**  string | Description of the profile. |
| **external_logging_publisher**  string | Specifies the external logging publisher used to send statistical data to one or more destinations. |
| **name**  string / required | Specifies the name of the profile. |
| **notification_by_email**  boolean | Enables or disables sending the analytics alerts by email.  **Choices:**   - `false` - `true` |
| **notification_by_syslog**  boolean | Enables or disables logging of the analytics alerts into the Syslog.  **Choices:**   - `false` - `true` |
| **notification_email_addresses**  list / elements=string | Specifies which email addresses receive alerts by email when `notification_by_email` is enabled. |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `analytics` profile. |
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
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_profile_analytics_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_analytics_module.md#id4)

```yaml+jinja
- name: Create a profile
  bigip_profile_analytics:
    name: profile1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_analytics_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **param1**  boolean | The new param1 value of the resource.  **Returned:** changed  **Sample:** `true` |
| **param2**  string | The new param2 value of the resource.  **Returned:** changed  **Sample:** `"Foo is bar"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
