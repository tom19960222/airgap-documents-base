---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_profile_persistence_universal module – Manage universal persistence profiles"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_profile_persistence_universal_module.html
fetched_at: 2026-07-27T17:27:34+00:00
---
# f5networks.f5_modules.bigip_profile_persistence_universal module – Manage universal persistence profiles

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_persistence_universal`.

New in f5networks.f5_modules 1.1.0

- [Synopsis](bigip_profile_persistence_universal_module.md#synopsis)
- [Parameters](bigip_profile_persistence_universal_module.md#parameters)
- [Notes](bigip_profile_persistence_universal_module.md#notes)
- [Examples](bigip_profile_persistence_universal_module.md#examples)
- [Return Values](bigip_profile_persistence_universal_module.md#return-values)

## [Synopsis](bigip_profile_persistence_universal_module.md#id1)

- Manages universal persistence profiles on the BIG-IP system.

## [Parameters](bigip_profile_persistence_universal_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **app_service**  string | The iApp service to be associated with this profile. When no service is specified, the default is None. |
| **match_across_pools**  boolean | When `yes`, specifies the system can use any pool that contains this persistence record.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **match_across_services**  boolean | When `yes`, specifies all persistent connections from a client IP address that go to the same virtual IP address also go to the same node.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **match_across_virtuals**  boolean | When `yes`, specifies all persistent connections from the same client IP address go to the same node.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **mirror**  boolean | When `yes`, specifies if the active unit goes into the standby mode, the system mirrors any persistence records to its peer.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the profile. |
| **override_connection_limit**  boolean | When `yes`, specifies the system allows you to specify that pool member connection limits will be overridden for persisted clients.  Per-virtual connection limits remain hard limits and are not overridden.  Choices:   - `false` - `true` |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `universal` profile. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
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
| **rule**  string | Specifies the iRule used to select a persistence entry.  When creating a new profile, if this parameter is not specified, the default is `None`, which disables this setting. |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  string | Specifies the duration of the persistence entries.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  To specify an indefinite timeout, use the value `indefinite`.  If specifying a numeric timeout, the value must be between `1` and `4294967295`. |

## [Notes](bigip_profile_persistence_universal_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_persistence_universal_module.md#id4)

```yaml+jinja
- name: Create a profile
  bigip_profile_persistence_universal:
    name: foo
    state: present
    match_across_services: yes
    match_across_virtuals: yes
    mirror: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_persistence_universal_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **app_service**  string | The iApp service associated with this profile  Returned: changed  Sample: `"/Common/good_service.app/good_service"` |
| **match_across_pools**  boolean | The new Match Across Pools value.  Returned: changed  Sample: `true` |
| **match_across_services**  boolean | The new Match Across Services value.  Returned: changed  Sample: `false` |
| **match_across_virtuals**  boolean | The new Match Across Virtuals value.  Returned: changed  Sample: `true` |
| **mirror**  boolean | The new Mirror value.  Returned: changed  Sample: `true` |
| **override_connection_limit**  boolean | The new Override Connection Limit value.  Returned: changed  Sample: `false` |
| **parent**  string | The parent profile.  Returned: changed  Sample: `"/Common/cookie"` |
| **rule**  string | The iRule used to select persistence entry.  Returned: changed  Sample: `"/Common/_sys_https_redirect"` |
| **timeout**  string | The duration of the persistence entries.  Returned: changed  Sample: `"180"` |

### Authors

- Nitin Khanna (@nitinthewiz)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
