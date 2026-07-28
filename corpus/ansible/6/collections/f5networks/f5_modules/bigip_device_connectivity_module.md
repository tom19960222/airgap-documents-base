---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_device_connectivity module – Manages device IP configuration settings for HA on a BIG-IP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_device_connectivity_module.html
fetched_at: 2026-07-27T17:26:25+00:00
---
# f5networks.f5_modules.bigip_device_connectivity module – Manages device IP configuration settings for HA on a BIG-IP.

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_connectivity`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_connectivity_module.md#synopsis)
- [Parameters](bigip_device_connectivity_module.md#parameters)
- [Notes](bigip_device_connectivity_module.md#notes)
- [Examples](bigip_device_connectivity_module.md#examples)
- [Return Values](bigip_device_connectivity_module.md#return-values)

## [Synopsis](bigip_device_connectivity_module.md#id1)

- Manages device IP configuration settings for High Availability (HA) on a BIG-IP. Each BIG-IP device has synchronization and failover connectivity information (IP addresses) that you define as part of HA pairing or clustering. This module allows you to configure that information.

## [Parameters](bigip_device_connectivity_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_mirroring**  string | Specifies whether mirroring occurs within the same cluster or between different clusters on a multi-bladed system.  This parameter is only supported on platforms that have multiple blades, such as Viprion hardware. It is not supported on Virtual Editions (VEs).  Choices:   - `"between-clusters"` - `"within-cluster"` |
| **config_sync_ip**  string | Local IP address the system uses for ConfigSync operations. |
| **failover_multicast**  boolean | When `yes`, ensures the Failover Multicast configuration is enabled and, if no further multicast configuration is provided, ensures that `multicast_interface`, `multicast_address` and `multicast_port` are the defaults specified in the description of each option.  When `no`, ensures that Failover Multicast configuration is disabled.  Choices:   - `false` - `true` |
| **mirror_primary_address**  string | Specifies the primary IP address for the system to use to mirror connections. |
| **mirror_secondary_address**  string | Specifies the secondary IP address for the system to use to mirror connections. |
| **multicast_address**  string | IP address for the system to send multicast messages associated with failover.  When `failover_multicast` is `yes` and this option is not provided, a default of `224.0.0.245` will be used. |
| **multicast_interface**  string | Interface over which the system sends multicast messages associated with failover.  When `failover_multicast` is `yes` and this option is not provided, a default of `eth0` will be used. |
| **multicast_port**  integer | Port for the system to send multicast messages associated with failover.  When `failover_multicast` is `yes` and this option is not provided, a default of `62960` will be used. This value must be between 0 and 65535. |
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
| **unicast_failover**  list / elements=dictionary | Addresses to use for failover operations. Options `address` and `port` are supported with dictionary structure, where `address` is the local IP address the system uses for failover operations.  Port specifies the port the system uses for failover operations. If `port` is not specified, the default value `1026` will be used.  If you are specifying the (recommended) management IP address, use ‘management-ip’ in the address field.  When the value is set to empty list, the parameter value is removed from device. |

## [Notes](bigip_device_connectivity_module.md#id3)

> **Note:**
>
> - This module is primarily used as a component of configuring HA pairs of BIG-IP devices.
> - Requires BIG-IP >= 12.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_connectivity_module.md#id4)

```yaml+jinja
- name: Configure device connectivity for standard HA pair
  bigip_device_connectivity:
    config_sync_ip: 10.1.30.1
    mirror_primary_address: 10.1.30.1
    unicast_failover:
      - address: management-ip
      - address: 10.1.30.1
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_device_connectivity_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Denotes if the F5 configuration was updated.  Returned: always |
| **cluster_mirroring**  string | The current cluster-mirroring setting.  Returned: changed  Sample: `"between-clusters"` |
| **config_sync_ip**  string | The new value of the `config_sync_ip` setting.  Returned: changed  Sample: `"10.1.1.1"` |
| **failover_multicast**  boolean | Whether a failover multicast attribute has been changed or not.  Returned: changed |
| **mirror_primary_address**  string | The new value of the `mirror_primary_address` setting.  Returned: changed  Sample: `"10.1.1.2"` |
| **mirror_secondary_address**  string | The new value of the `mirror_secondary_address` setting.  Returned: changed  Sample: `"10.1.1.3"` |
| **multicast_address**  string | The new value of the `multicast_address` setting.  Returned: changed  Sample: `"224.0.0.245"` |
| **multicast_interface**  string | The new value of the `multicast_interface` setting.  Returned: changed  Sample: `"eth0"` |
| **multicast_port**  integer | The new value of the `multicast_port` setting.  Returned: changed  Sample: `1026` |
| **unicast_failover**  list / elements=string | The new value of the `unicast_failover` setting.  Returned: changed  Sample: `[{"address": "10.1.1.2", "port": 1026}]` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
