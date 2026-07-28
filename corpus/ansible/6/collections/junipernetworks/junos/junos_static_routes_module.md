---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_static_routes module – Static routes resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_static_routes_module.html
fetched_at: 2026-07-27T17:54:41+00:00
---
# junipernetworks.junos.junos_static_routes module – Static routes resource module

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_static_routes_module.md#ansible-collections-junipernetworks-junos-junos-static-routes-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_static_routes`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_static_routes_module.md#synopsis)
- [Requirements](junos_static_routes_module.md#requirements)
- [Parameters](junos_static_routes_module.md#parameters)
- [Notes](junos_static_routes_module.md#notes)
- [Examples](junos_static_routes_module.md#examples)
- [Return Values](junos_static_routes_module.md#return-values)

## [Synopsis](junos_static_routes_module.md#id1)

- This module provides declarative management of static routes on Juniper JUNOS devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_static_routes_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12)

## [Parameters](junos_static_routes_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of static routes options |
| **address_families**  list / elements=dictionary | Address family to use for the static routes |
| **afi**  string / required | afi to use for the static routes  Choices:   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | Static route configuration |
| **dest**  string | Static route destination including prefix |
| **metric**  integer | Metric value for the static route |
| **next_hop**  list / elements=dictionary | Next hop to destination |
| **forward_router_address**  string | List of next hops |
| **vrf**  string | Virtual Routing and Forwarding (VRF) name |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show routing-options**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_static_routes_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_static_routes_module.md#id5)

```yaml+jinja
# Using deleted

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
#     route 10.200.16.75/24 next-hop 10.200.16.2;
# }

- name: Delete provided configuration (default operation is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.200.16.75/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: deleted

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }

# Using merged

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }

- name: Merge provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.200.16.75/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: merged

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
#     route 10.200.16.75/24 next-hop 10.200.16.2;
# }

# Using overridden

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.0.1;
# }

- name: Override provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.200.16.75/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: overridden

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 10.200.16.75/24 next-hop 10.200.16.2;
# }

# Using replaced

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }

- name: Replace provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.168.47.0/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: replaced

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 10.200.16.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }
```

## [Return Values](junos_static_routes_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  string | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  string | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Daniel Mellado (@dmellado)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
