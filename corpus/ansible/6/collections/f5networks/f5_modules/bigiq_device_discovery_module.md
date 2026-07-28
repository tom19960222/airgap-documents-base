---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigiq_device_discovery module – Manage BIG-IP devices through BIG-IQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigiq_device_discovery_module.html
fetched_at: 2026-07-27T17:28:08+00:00
---
# f5networks.f5_modules.bigiq_device_discovery module – Manage BIG-IP devices through BIG-IQ

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_device_discovery`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_device_discovery_module.md#synopsis)
- [Parameters](bigiq_device_discovery_module.md#parameters)
- [Notes](bigiq_device_discovery_module.md#notes)
- [Examples](bigiq_device_discovery_module.md#examples)
- [Return Values](bigiq_device_discovery_module.md#return-values)

## [Synopsis](bigiq_device_discovery_module.md#id1)

- Discovers and imports BIG-IP device configuration on the BIG-IQ.

## [Parameters](bigiq_device_discovery_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_conflict_policy**  string | Sets the conflict resolution policy for Access module `apm` objects. Only used when the `apm` module is specified.  Choices:   - `"use_bigiq"` - `"use_bigip"` - `"keep_version"` |
| **access_group_first_device**  boolean | Specifies if the imported device is the first device in the access group to import shared configuration for that access group.  Choices:   - `false` - `true` ← (default) |
| **access_group_name**  string | Access group name to import Access configuration for devices. Once set it cannot be changed. |
| **conflict_policy**  string | Sets the conflict resolution policy for shared objects across BIG-IP devices, except LTM profiles and monitors.  Choices:   - `"use_bigiq"` ← (default) - `"use_bigip"` |
| **device_address**  string / required | The IP address of the BIG-IP device to be imported/managed. |
| **device_conflict_policy**  string | Sets the conflict resolution policy for objects that are specific to a particular to a BIG-IP device and not shared among BIG-IP devices.  Choices:   - `"use_bigiq"` ← (default) - `"use_bigip"` |
| **device_password**  string | The administrator password for the BIG-IP device.  This parameter is only required when adding a new BIG-IP device to be managed. |
| **device_port**  integer | The port on which a device trust setup between BIG-IQ and BIG-IP should happen.  Default: `443` |
| **device_username**  string | The administrator username for the BIG-IP device.  This parameter is only required when adding a new BIG-IP device to be managed. |
| **force**  boolean | Forces rediscovery and import of existing modules on the managed BIG-IP.  Choices:   - `false` ← (default) - `true` |
| **ha_name**  string | DSC cluster name of the BIG-IP device to be managed.  This is optional if the managed device is not a part of a cluster group.  When `use_bigiq_sync` is set to `yes`, this parameter is required. |
| **modules**  list / elements=string | List of modules to be discovered and imported into the device.  These modules must be provisioned on the target device, otherwise operation will fail.  The `ltm` module must always be specified when performing discovery or re-discovery of the the device.  When `asm` or `afm` are specified, the `shared_security` module also needs to be declared.  Choices:   - `"ltm"` - `"asm"` - `"apm"` - `"afm"` - `"dns"` - `"websafe"` - `"security_shared"` |
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
| **state**  string | The state of the managed device on the system.  When `present`, enables new device addition as well as device rediscovery/import.  When `absent`, completely removes the device from the system.  Choices:   - `"absent"` - `"present"` ← (default) |
| **statistics**  dictionary | Specify the statistics collection for discovered device. |
| **enable**  boolean | Enables statistics collection on a device.  Choices:   - `false` ← (default) - `true` |
| **interval**  integer | Specifies the interval the data is collected from the discovered device, in seconds.  Choices:   - `30` - `60` ← (default) - `120` - `500` |
| **stat_modules**  list / elements=string | Specifies for which modules the data is being collected.  Choices:   - `"device"` ← (default) - `"ltm"` ← (default) - `"dns"`   Default: `["device", "ltm"]` |
| **zone**  string | Specifies in which DCD zone is collecting the data from device.  Default: `"default"` |
| **use_bigiq_sync**  boolean | When set to `no`, initiate BIG-IP DSC sync when deploying configuration changes.  When set to `yes`, ignore BIG-IP DSC sync when deploying configuration changes.  Choices:   - `false` ← (default) - `true` |
| **versioned_conflict_policy**  string | Sets the conflict resolution policy for LTM profile and monitor objects that are specific to a BIG-IP software version.  Choices:   - `"use_bigiq"` - `"use_bigip"` - `"keep_version"` |

## [Notes](bigiq_device_discovery_module.md#id3)

> **Note:**
>
> - BIG-IQ >= 6.1.0.
> - This module does not support atomic removal of discovered modules on the device.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigiq_device_discovery_module.md#id4)

```yaml+jinja
- name: Discover a new device and import config, use default conflict policy.
  bigiq_device_discovery:
    device_address: 192.168.1.1
    device_username: bigipadmin
    device_password: bigipsecret
    modules:
      - ltm
      - afm
      - shared_security
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Discover a new device and import config, use non- default conflict policy.
  bigiq_device_discovery:
    device_address: 192.168.1.1
    modules:
      - ltm
      - dns
    conflict_policy: use_bigip
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Force full device rediscovery
  bigiq_device_discovery:
    device_address: 192.168.1.1
    modules:
      - ltm
      - afm
      - dns
      - shared_security
    force: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove discovered device and its config
  bigiq_device_discovery:
    device_address: 192.168.1.1
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigiq_device_discovery_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **access_conflict_policy**  string | Sets the conflict resolution policy for Access module `apm` objects.  Returned: changed  Sample: `"keep_version"` |
| **access_group_first_device**  boolean | First device in the access group to import shared configuration for that access group.  Returned: changed  Sample: `true` |
| **access_group_name**  string | Access group name to import Access configuration for devices.  Returned: changed  Sample: `"foo_group"` |
| **conflict_policy**  string | Sets the conflict resolution policy for shared objects across BIG-IP devices.  Returned: changed  Sample: `"use_bigip"` |
| **device_address**  string | The IP address of the BIG-IP device to be imported/managed.  Returned: changed  Sample: `"192.168.1.1"` |
| **device_conflict_policy**  string | Sets the conflict resolution policy for objects that are specific to a particular to a BIG-IP device.  Returned: changed  Sample: `"use_bigip"` |
| **device_port**  integer | The port on which a device trust setup between BIG-IQ and BIG-IP should happen.  Returned: changed  Sample: `10443` |
| **ha_name**  string | DSC cluster name of the BIG-IP device to be managed.  Returned: changed  Sample: `"GROUP_1"` |
| **modules**  list / elements=string | List of modules to be discovered and imported into the device.  Returned: changed  Sample: `["ltm", "dns"]` |
| **use_bigiq_sync**  boolean | Indicates if BIG-IQ should manually synchronize DSC configuration.  Returned: changed  Sample: `true` |
| **versioned_conflict_policy**  string | Sets the conflict resolution policy for LTM profile and monitor objects.  Returned: changed  Sample: `"keep_version"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
