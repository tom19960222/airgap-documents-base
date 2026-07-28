---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_profile_persistence_src_addr module – Manage source address persistence profiles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_profile_persistence_src_addr_module.html
fetched_at: 2026-07-28T02:07:03+00:00
---
# f5networks.f5_modules.bigip_profile_persistence_src_addr module – Manage source address persistence profiles

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_persistence_src_addr`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_persistence_src_addr_module.md#synopsis)
- [Parameters](bigip_profile_persistence_src_addr_module.md#parameters)
- [Notes](bigip_profile_persistence_src_addr_module.md#notes)
- [Examples](bigip_profile_persistence_src_addr_module.md#examples)
- [Return Values](bigip_profile_persistence_src_addr_module.md#return-values)

## [Synopsis](bigip_profile_persistence_src_addr_module.md#id1)

- Manages source address persistence profiles on a BIG-IP.

## [Parameters](bigip_profile_persistence_src_addr_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **entry_timeout**  string | Specifies the duration of the persistence entries.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  To specify an indefinite timeout, use the value `indefinite`.  If specifying a numeric timeout, the value must be between `1` and `4294967295`. |
| **hash_algorithm**  string | Specifies the algorithm the system uses for hash persistence load balancing. The hash result is the input for the algorithm.  When `default`, specifies the system uses the index of pool members to obtain the hash result for the input to the algorithm.  When `carp`, specifies the system uses the Cache Array Routing Protocol (CARP) to obtain the hash result for the input to the algorithm.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `"default"` - `"carp"` |
| **mask**  string | Specifies a value the system applies as the prefix length.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **match_across_pools**  boolean | When `true`, specifies the system can use any pool that contains this persistence record.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **match_across_services**  boolean | When `true`, specifies all persistent connections from a client IP address that go to the same virtual IP address also go to the same node.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **match_across_virtuals**  boolean | When `true`, specifies all persistent connections from the same client IP address go to the same node.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **mirror**  boolean | When `true`, specifies that if the active unit goes into the standby mode, the system mirrors any persistence records to its peer.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  **Choices:**   - `false` - `true` |
| **name**  string / required | Specifies the name of the profile. |
| **override_connection_limit**  boolean | When `true`, specifies the system allows you to specify that pool member connection limits will be overridden for persisted clients.  Per-virtual connection limits remain hard limits and are not overridden.  **Choices:**   - `false` - `true` |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `source_addr` profile. |
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

## [Notes](bigip_profile_persistence_src_addr_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_persistence_src_addr_module.md#id4)

```yaml+jinja
- name: Create a profile
  bigip_profile_persistence_src_addr:
    name: foo
    state: present
    hash_algorithm: carp
    match_across_services: true
    match_across_virtuals: true
    mirror: true
    mask: 255.255.255.255
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_persistence_src_addr_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entry_timeout**  string | The duration of the persistence entries.  **Returned:** changed  **Sample:** `"180"` |
| **hash_algorithm**  string | The algorithm used for hash persistence.  **Returned:** changed  **Sample:** `"default"` |
| **mask**  string | The persist mask value.  **Returned:** changed  **Sample:** `"255.255.255.255"` |
| **match_across_pools**  boolean | The new Match Across Pools value.  **Returned:** changed  **Sample:** `true` |
| **match_across_services**  boolean | The new Match Across Services value.  **Returned:** changed  **Sample:** `false` |
| **match_across_virtuals**  boolean | The new Match Across Virtuals value.  **Returned:** changed  **Sample:** `true` |
| **mirror**  boolean | The new Mirror value.  **Returned:** changed  **Sample:** `true` |
| **override_connection_limit**  boolean | The new Override Connection Limit value.  **Returned:** changed  **Sample:** `false` |
| **parent**  string | The parent profile.  **Returned:** changed  **Sample:** `"/Common/cookie"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
