---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_group module – Manage device groups on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_group_module.html
fetched_at: 2026-07-28T02:05:52+00:00
---
# f5networks.f5_modules.bigip_device_group module – Manage device groups on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_group`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_group_module.md#synopsis)
- [Parameters](bigip_device_group_module.md#parameters)
- [Notes](bigip_device_group_module.md#notes)
- [Examples](bigip_device_group_module.md#examples)
- [Return Values](bigip_device_group_module.md#return-values)

## [Synopsis](bigip_device_group_module.md#id1)

- Managing device groups allows you to create HA pairs and clusters of BIG-IP devices. Usage of this module should be done in conjunction with the `bigip_configsync_actions` to sync the configuration across the pair or cluster if auto-sync is disabled.

## [Parameters](bigip_device_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **asm_sync**  boolean  *added in f5networks.f5_modules 1.22.0* | Specifies whether to synchronize ASM configurations of device group members.  A device can be a member of only one ASM-enabled device group.  When creating a new device group, this option defaults to `false`.  **Choices:**   - `false` - `true` |
| **auto_sync**  boolean | Indicates whether configuration synchronization occurs manually or automatically.  When creating a new device group, this option defaults to `false`.  **Choices:**   - `false` - `true` |
| **description**  string | Description of the device group. |
| **full_sync**  boolean | Specifies whether the system synchronizes the entire configuration during synchronization operations.  When `no`, the system performs incremental synchronization operations, based on the cache size specified in `max_incremental_sync_size`.  Incremental configuration synchronization is a mechanism for synchronizing a device-group’s configuration among its members, without requiring a full configuration load for each configuration change.  In order for this to work, all devices in the device-group must initially agree on the configuration. Typically this requires at least one full configuration load to each device.  When creating a new device group, this option defaults to `false`.  **Choices:**   - `false` - `true` |
| **max_incremental_sync_size**  integer | Specifies the size of the changes cache for incremental sync.  For example, using the default, if you make more than 1024 KB worth of incremental changes, the system performs a full synchronization operation.  Using incremental synchronization operations can reduce the per-device sync/load time for configuration changes.  This setting is relevant only when `full_sync` is `no`. |
| **name**  string / required | Specifies the name of the device group. |
| **network_failover**  boolean | Indicates whether failover occurs over the network or is hard-wired.  This parameter is only valid for `type`s that are `sync-failover`.  **Choices:**   - `false` - `true` |
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
| **save_on_auto_sync**  boolean | When performing an auto-sync, specifies whether the configuration is saved or not.  When `false`, only the running configuration is changed on the device(s) being synced to.  When creating a new device group, this option defaults to `false`.  **Choices:**   - `false` - `true` |
| **state**  string | When `state` is `present`, ensures the device group exists.  When `state` is `absent`, ensures the device group is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | Specifies the type of group.  A `sync-failover` device group contains devices that synchronize their configuration data and fail over to one another when a device becomes unavailable.  A `sync-only` device group has no such failover. When creating a new device group, this option defaults to `sync-only`.  This setting cannot be changed once it has been set.  **Choices:**   - `"sync-failover"` - `"sync-only"` |

## [Notes](bigip_device_group_module.md#id3)

> **Note:**
>
> - This module is primarily used as a component of configuring HA pairs of BIG-IP devices.
> - Requires BIG-IP >= 12.1.x.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_group_module.md#id4)

```yaml+jinja
- name: Create a sync-only device group
  bigip_device_group:
    name: foo-group
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a sync-only device group with auto-sync enabled
  bigip_device_group:
    name: foo-group
    auto_sync: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a sync-only device group with auto-sync and asm-sync enabled
  bigip_device_group:
    name: foo-group
    auto_sync: true
    asm_sync: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **asm_sync**  boolean | The new asm_sync value of the device group.  **Returned:** changed  **Sample:** `true` |
| **auto_sync**  boolean | The new auto_sync value of the device group.  **Returned:** changed  **Sample:** `true` |
| **description**  string | The new description of the device group.  **Returned:** changed  **Sample:** `"this is a device group"` |
| **full_sync**  boolean | The new full_sync value of the device group.  **Returned:** changed  **Sample:** `false` |
| **max_incremental_sync_size**  integer | The new sync size of the device group.  **Returned:** changed  **Sample:** `1000` |
| **network_failover**  boolean | Whether or not network failover is enabled.  **Returned:** changed  **Sample:** `true` |
| **save_on_auto_sync**  boolean | The new save_on_auto_sync value of the device group.  **Returned:** changed  **Sample:** `true` |
| **type**  string | The new type of the device group.  **Returned:** changed  **Sample:** `"sync-failover"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
