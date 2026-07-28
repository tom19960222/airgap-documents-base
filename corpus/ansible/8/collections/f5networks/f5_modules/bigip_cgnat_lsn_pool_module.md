---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_cgnat_lsn_pool module – Manage CGNAT LSN Pools"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_cgnat_lsn_pool_module.html
fetched_at: 2026-07-28T02:05:42+00:00
---
# f5networks.f5_modules.bigip_cgnat_lsn_pool module – Manage CGNAT LSN Pools

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_cgnat_lsn_pool`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_cgnat_lsn_pool_module.md#synopsis)
- [Parameters](bigip_cgnat_lsn_pool_module.md#parameters)
- [Notes](bigip_cgnat_lsn_pool_module.md#notes)
- [Examples](bigip_cgnat_lsn_pool_module.md#examples)
- [Return Values](bigip_cgnat_lsn_pool_module.md#return-values)

## [Synopsis](bigip_cgnat_lsn_pool_module.md#id1)

- Manage CGNAT LSN (Large Scale NAT) Pools.

## [Parameters](bigip_cgnat_lsn_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup_members**  list / elements=string | Specifies translation IP addresses available for backup members, which are used by Deterministic translation mode if `deterministic` mode translation fails and falls back to `napt` mode.  This is a collection of IP prefixes with their prefix lengths. |
| **client_conn_limit**  integer | Specifies the maximum number of simultaneous translated connections a client or subscriber is allowed to have.  Valid range of values is between `0` and `4294967295` inclusive. |
| **description**  string | User created LSN pool description. |
| **egress_interfaces**  list / elements=string | Specifies the set of interfaces on which the source address translation is allowed or disallowed, as determined by the `egress_intf_enabled` setting. |
| **egress_intf_enabled**  boolean | Specifies how the system handles address translation on the interfaces specified in `egress_interfaces`.  When set to `true`, source address translation is allowed only on the specified `egress_interfaces`.  When set to `false`, source address translation is disabled on the specified `egress_interfaces`.  **Choices:**   - `false` - `true` |
| **harpin_mode**  boolean | Enables or disables hairpinning for incoming connections to active translation end-points.  **Choices:**   - `false` - `true` |
| **icmp_echo**  boolean | Enables or disables ICMP echo on translated addresses.  **Choices:**   - `false` - `true` |
| **inbound_connections**  string | Controls whether or not the BIG-IP system supports inbound connections for each outbound mapping.  When `disabled`, system does not support inbound connections for outbound mappings, which prevents Port Control Protocol `pcp` from functioning.  When `explicit`, the system supports inbound connections for explicit outbound mappings.  When `automatic` the system supports inbound connections for every outbound mapping as it gets used.  **Choices:**   - `"disabled"` - `"explicit"` - `"automatic"` |
| **log_profile**  string | Specifies the name of the logging profile the pool uses. |
| **log_publisher**  string | Specifies the name of the log publisher that logs translation events. |
| **members**  list / elements=string | Specifies the set of translation IP addresses available in the pool. This is a collection of IP prefixes with their prefix lengths.  All public-side addresses come from the addresses in this group of subnets. Members of two or more deterministic LSN pools must not overlap. Every external address used for deterministic mapping must occur only in one LSN pool. |
| **mode**  string | Specifies the translation address mapping mode.  The `napt` mode provides standard address and port translation allowing multiple clients in a private network to access remote networks using the single IP address assigned to their router.  The `deterministic` address translation mode provides address translation that eliminates the logging of every address mapping, while still allowing internal client address tracking using only an external address and port, and a destination address and port.  The `pba` mode logs the allocation and release of port blocks for subscriber translation requests, instead of separately logging each translation request.  **Choices:**   - `"napt"` - `"deterministic"` - `"pba"` |
| **name**  string / required | Specifies the name of the LSN pool to manage. |
| **partition**  string | Device partition on which to manage resources.  **Default:** `"Common"` |
| **pba_block_idle_timeout**  integer | Specifies the timeout duration subsequent to the point when the port block becomes idle.  Valid range of values is between `0` and `4294967295` inclusive.” |
| **pba_block_lifetime**  integer | Specifies the timeout for the port block, after which the block is not used for new port allocations.  Valid range of values is between `0` and `4294967295` inclusive.  The value of `0` corresponds to an infinite timeout. |
| **pba_block_size**  integer | Specifies the number of ports in a block.  Valid range of values is between `0` and `65535` inclusive.  The `pba_block_size` value should be less than or equal to the LSN pool range, i.e the range of ports defined by `port_range_low` and `port_range_high` values. |
| **pba_client_block_limit**  integer | Specifies the number of blocks that can be assigned to a single subscriber IP address. |
| **pba_zombie_timeout**  integer | Specifies the timeout duration for a zombie port block, which is a timed out port block with one or more active connections. When the timeout duration expires, connections using the zombie block are killed and the zombie port block becomes an available port block.  The value of `0` corresponds to an infinite timeout.  System ignores this parameter value if `pba_block_lifetime` is `0`. |
| **persistence_mode**  string | Specifies the persistence settings for LSN translation entries.  When `address`, the translation attempts to reuse the address mapping, but not the port mapping.  When `address-port`, the translation attempts to reuse both the address and port mapping for subsequent packets sent from the same internal IP address and port.  When `none`, peristence is disabled.  **Choices:**   - `"address"` - `"address-port"` - `"none"` |
| **persistence_timeout**  integer | Specifies the persistence timeout value for LSN translation entries.  If a particular mapping is unused for this length of time, the mapping expires and the public-side address/port pair is free for use in other mappings.  Valid range of values is between `0` and `31536000` inclusive. |
| **port_range_high**  integer | Specifies the high end of the range of port numbers available for use with translation IP addresses.  The `port_range_high` must always be higher or equal to `port_range_high` value.  Valid range of values is between `0` and `65535` inclusive. |
| **port_range_low**  integer | Specifies the low end of the range of port numbers available for use with translation IP addresses.  The `port_range_low` must always be lower or equal to `port_range_high` value.  Valid range of values is between `0` and `65535` inclusive. |
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
| **route_advertisement**  boolean | Specifies whether the translation addresses are passed to the Advanced Routing Module for advertisement through dynamic routing protocols.  **Choices:**   - `false` - `true` |
| **state**  string | When `state` is `present`, ensures the LSN pool exists.  When `state` is `absent`, ensures the LSN pool is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_cgnat_lsn_pool_module.md#id3)

> **Note:**
>
> - Requires CGNAT is licensed and enabled on BIG-IP.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_cgnat_lsn_pool_module.md#id4)

```yaml+jinja
- name: Create an lsn pool
  bigip_cgnat_lsn_pool:
    name: foo
    mode: napt
    client_conn_limit: 100
    log_profile: foo_profile
    log_publisher: foo_publisher
    members:
      - 10.1.1.0/24
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Update lsn pool
  bigip_cgnat_lsn_pool:
    name: foo
    mode: pba
    pba_block_size: 128
    pba_block_lifetime: 7200
    pba_block_idle_timeout: 1800
    pba_zombie_timeout: 900
    log_profile: foo_profile
    log_publisher: foo_publisher
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove lsn pool
  bigip_cgnat_lsn_pool:
    name: foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_cgnat_lsn_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_members**  list / elements=string | The translation IP addresses available for backup members.  **Returned:** changed  **Sample:** `["/Common/10.10.10.0/24", "/Common/11.11.11.0/25"]` |
| **client_conn_limit**  integer | The maximum number of simultaneous translated connections a client or subscriber is allowed to have.  **Returned:** changed  **Sample:** `50` |
| **description**  string | User created LSN pool description.  **Returned:** changed  **Sample:** `"some description"` |
| **egress_interfaces**  list / elements=string | The set of interfaces on which source address translation is allowed or disallowed.  **Returned:** changed  **Sample:** `["/Common/tunnel1", "/Common/tunnel2"]` |
| **egress_intf_enabled**  boolean | Specifies how the system handles address translation on the egress interfaces.  **Returned:** changed  **Sample:** `false` |
| **harpin_mode**  boolean | Enables or disables hairpinning for incoming connections to active translation end-points.  **Returned:** changed  **Sample:** `true` |
| **icmp_echo**  boolean | Enables or disables ICMP echo on translated addresses.  **Returned:** changed  **Sample:** `false` |
| **inbound_connections**  string | Controls BIG-IP system support of inbound connections for each outbound mapping.  **Returned:** changed  **Sample:** `"explicit"` |
| **log_profile**  string | The name of the logging profile the pool uses.  **Returned:** changed  **Sample:** `"/Common/foo_log_profile"` |
| **log_publisher**  list / elements=string | The name of the log publisher that logs translation events.  **Returned:** changed  **Sample:** `["/Common/publisher_1"]` |
| **members**  list / elements=string | The set of translation IP addresses available in the pool.  **Returned:** changed  **Sample:** `["/Common/10.10.10.0/24", "/Common/11.11.11.0/25"]` |
| **mode**  string | Specifies the translation address mapping mode.  **Returned:** changed  **Sample:** `"napt"` |
| **pba_block_idle_timeout**  integer | The timeout duration subsequent to the point when the port block becomes idle.  **Returned:** changed  **Sample:** `3600` |
| **pba_block_lifetime**  integer | The timeout for the port block.  **Returned:** changed  **Sample:** `7200` |
| **pba_block_size**  integer | The number of ports in a block.  **Returned:** changed  **Sample:** `128` |
| **pba_client_block_limit**  integer | The number of blocks that can be assigned to a single subscriber IP address.  **Returned:** changed  **Sample:** `3` |
| **pba_zombie_timeout**  integer | The timeout duration for a zombie port block.  **Returned:** changed  **Sample:** `180` |
| **persistence_mode**  string | Specifies the persistence settings for LSN translation entries.  **Returned:** changed  **Sample:** `"address"` |
| **persistence_timeout**  integer | Specifies the persistence timeout value for LSN translation entries.  **Returned:** changed  **Sample:** `500` |
| **port_range_high**  integer | The high end of the range of port numbers available for use with translation IP addresses.  **Returned:** changed  **Sample:** `65535` |
| **port_range_low**  integer | The low end of the range of port numbers available for use with translation IP addresses.  **Returned:** changed  **Sample:** `1025` |
| **route_advertisement**  boolean | Specifies whether the translation addresses are advertised through dynamic routing protocols.  **Returned:** changed  **Sample:** `true` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
