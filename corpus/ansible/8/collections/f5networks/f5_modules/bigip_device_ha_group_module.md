---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_ha_group module – Manage HA group settings on a BIG-IP system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_ha_group_module.html
fetched_at: 2026-07-28T02:05:53+00:00
---
# f5networks.f5_modules.bigip_device_ha_group module – Manage HA group settings on a BIG-IP system

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_ha_group`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_ha_group_module.md#synopsis)
- [Parameters](bigip_device_ha_group_module.md#parameters)
- [Notes](bigip_device_ha_group_module.md#notes)
- [Examples](bigip_device_ha_group_module.md#examples)
- [Return Values](bigip_device_ha_group_module.md#return-values)

## [Synopsis](bigip_device_ha_group_module.md#id1)

- Manage HA (High Availability) group settings on a BIG-IP system.

## [Parameters](bigip_device_ha_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active_bonus**  integer | Specifies the extra value to be added to the HA score of the active unit.  When system creates HA group this value is set to `10` by the system. |
| **description**  string | User created HA group description. |
| **enable**  boolean | When set to `false`, the system disables the HA score feature.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | Name of the HA group to create/manage. |
| **pools**  list / elements=dictionary | Specifies pools to contribute to the HA score.  The pools must exist on the BIG-IP, otherwise the operation will fail. |
| **attribute**  string | The pool attribute that contributes to the HA score.  **Choices:**   - `"percent-up-members"` ← (default) |
| **minimum_threshold**  integer | Below this value, the selected pool attribute contributes nothing to the HA score.  This value must be greater than the number of pool members present in the pool.  In TMOS versions 12.x this attribute is named `threshold`, however it has been deprecated in versions 13.x and above.  Specifying this attribute in the module running against v12.x will keep the same behavior as if `threshold` option was set. |
| **partition**  string | Device partition where the specified pool exists.  This parameter is ignored if the `pool_name` is specified in full path format.  **Default:** `"Common"` |
| **pool_name**  string / required | The pool name which is used to contribute to the HA score.  Referencing the pool can be done in the full path format for example, `/Common/pool_name`.  When the pool is referenced in full path format, the `partition` parameter is ignored. |
| **weight**  integer / required | Maximum value the selected pool attribute contributes to the HA score. |
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
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **trunks**  list / elements=dictionary | Specifies trunks to contribute to the HA score.  The trunks must exist on the BIG-IP, otherwise the operation will fail. |
| **attribute**  string | The trunk attribute that contributes to the HA score.  **Choices:**   - `"percent-up-members"` ← (default) |
| **minimum_threshold**  integer | Below this value the selected trunk attribute contributes nothing to the HA score.  This value must be greater than the number of trunk members.  In TMOS versions 12.x this attribute is named `threshold`, however it has been deprecated in versions 13.x and above.  Specifying this attribute in the module running against v12.x will keep the same behavior as if `threshold` option was set. |
| **trunk_name**  string / required | The trunk name used to contribute to the HA score. |
| **weight**  integer / required | Maximum value the selected trunk attribute contributes to the HA score. |

## [Notes](bigip_device_ha_group_module.md#id3)

> **Note:**
>
> - This module does not support atomic removal of HA group objects.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_ha_group_module.md#id4)

```yaml+jinja
- name: Create HA group no members, not active
  bigip_device_ha_group:
    name: foo_ha
    description: empty_foo
    active_bonus: 20
    enable: false
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create HA group with pools and trunks
  bigip_device_ha_group:
    name: baz_ha
    description: non_empty_baz
    active_bonus: 15
    pools:
      - pool_name: foopool
        weight: 30
        minimum_threshold: 1
    trunks:
      - trunk_name: footrunk
        weight: 70
        minimum_threshold: 2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create HA group pools using full_path format
  bigip_device_ha_group:
    name: bar_ha
    description: non_empty_bar
    active_bonus: 12
    pools:
      - pool_name: /Baz/foopool
        weight: 30
        minimum_threshold: 1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove HA group
  bigip_device_ha_group:
    name: foo_ha
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_ha_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **active_bonus**  integer | The extra value to be added to the HA score of the active unit.  **Returned:** changed  **Sample:** `20` |
| **description**  string | User created HA group description.  **Returned:** changed  **Sample:** `"Some Group"` |
| **enable**  boolean | Enables or disables the HA score feature.  **Returned:** changed  **Sample:** `true` |
| **name**  string | Name of the HA group.  **Returned:** changed  **Sample:** `"foo_HA"` |
| **pools**  complex | The pools to contribute to the HA score.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **attribute**  string | The pool attribute that contributes to the HA score.  **Returned:** changed  **Sample:** `"percent-up-members"` |
| **minimum_threshold**  integer | Below this value the selected pool attribute contributes nothing to the HA score.  **Returned:** changed  **Sample:** `2` |
| **partition**  string | Device partition where the specified pool exists.  **Returned:** changed  **Sample:** `"Common"` |
| **pool_name**  string | The pool name which is used to contribute to the HA score.  **Returned:** changed  **Sample:** `"foo_pool"` |
| **weight**  integer | Maximum value the selected pool attribute contributes to the HA score.  **Returned:** changed  **Sample:** `40` |
| **trunks**  complex | The trunks to contribute to the HA score.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **attribute**  string | The trunk attribute that contributes to the HA score.  **Returned:** changed  **Sample:** `"percent-up-members"` |
| **minimum_threshold**  integer | Below this value, the selected trunk attribute contributes nothing to the HA score.  **Returned:** changed  **Sample:** `2` |
| **trunk_name**  string | The trunk name used to contribute to the HA score.  **Returned:** changed  **Sample:** `"foo_trunk"` |
| **weight**  integer | Maximum value the selected trunk attribute contributes to the HA score.  **Returned:** changed  **Sample:** `40` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
