---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_static_routes module – Manage static routes configuration on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_static_routes_module.html
fetched_at: 2026-07-28T02:03:49+00:00
---
# dellemc.enterprise_sonic.sonic_static_routes module – Manage static routes configuration on SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_static_routes`.

New in dellemc.enterprise_sonic 2.0.0

- [Synopsis](sonic_static_routes_module.md#synopsis)
- [Parameters](sonic_static_routes_module.md#parameters)
- [Examples](sonic_static_routes_module.md#examples)
- [Return Values](sonic_static_routes_module.md#return-values)

## [Synopsis](sonic_static_routes_module.md#id1)

- This module provides configuration management of static routes for devices running SONiC

## [Parameters](sonic_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Manages ‘static_routes’ configurations |
| **static_list**  list / elements=dictionary | A list of ‘static_routes’ configurations. |
| **next_hops**  list / elements=dictionary | A list of next-hops to be utilised for the static route being specified. |
| **index**  dictionary / required | An identifier utilised to uniquely reference the next-hop. |
| **blackhole**  boolean | Indicates that packets matching this route should be discarded.  **Choices:**   - `false` ← (default) - `true` |
| **interface**  string | The reference to a base interface. |
| **next_hop**  string | The next-hop that is to be used for the static route. |
| **nexthop_vrf**  string | Name of the next-hop network instance for leaked routes. |
| **metric**  integer | Specifies the preference of the next-hop entry when it is injected into the RIB. |
| **tag**  integer | The tag value for the static route. |
| **track**  integer | The IP SLA track ID for static route. |
| **prefix**  string / required | Destination prefix for the static route, either IPv4 or IPv6. |
| **vrf_name**  string / required | Name of the configured VRF on the device. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"overridden"` - `"replaced"` |

## [Examples](sonic_static_routes_module.md#id3)

```yaml+jinja
# Using merged
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep "ip route"
# (No "ip route" configuration present)

  - name: Merge static routes configurations
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      - vrf_name: 'default'
        static_list:
         - prefix: '2.0.0.0/8'
           next_hops:
             - index:
                 interface: 'Ethernet4'
               metric: 1
               tag: 2
               track: 3
             - index:
                next_hop: '3.0.0.0'
               metric: 2
               tag: 4
               track: 8
      - vrf_name: 'VrfReg1'
        static_list:
          - prefix: '3.0.0.0/8'
            next_hops:
              - index:
                  interface: 'eth0'
                  nexthop_vrf: 'VrfReg2'
                  next_hop: '4.0.0.0'
                metric: 4
                tag: 5
                track: 6
              - index:
                  blackhole: True
                metric: 10
                tag: 20
                track: 30
    state: merged

# After State:
# ------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
# ip route 2.0.0.0/8 interface Ethernet4 tag 2 track 3 1
# ip route vrf VrfReg1 3.0.0.0/8 4.0.0.0 interface Management 0 nexthop-vrf VrfReg2 tag 5 track 6 4
# ip route vrf VrfReg1 3.0.0.0/8 blackhole tag 20 track 30 10
#
#
# Modifying previous merge

  - name: Modify static routes configurations
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      - vrf_name: 'VrfReg1'
        static_list:
          - prefix: '3.0.0.0/8'
            next_hops:
              - index:
                  blackhole: True
                metric: 11
                tag: 22
                track: 33
    state: merged

# After State:
# ------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
# ip route 2.0.0.0/8 interface Ethernet4 tag 2 track 3 1
# ip route vrf VrfReg1 3.0.0.0/8 4.0.0.0 interface Management 0 nexthop-vrf VrfReg2 tag 5 track 6 4
# ip route vrf VrfReg1 3.0.0.0/8 blackhole tag 22 track 33 11

# Using overridden
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 4.0.0.0/8 2.0.0.0 tag 4 track 8 2

  - name: Override static routes configurations
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      - vrf_name: 'VrfReg2'
        static_list:
          - prefix: '3.0.0.0/8'
            next_hops:
              - index:
                  blackhole: True
                metric: 10
                tag: 20
                track: 30
    state: overridden

# After State:
# ------------
#
# sonic# show running-configuration | grep "ip route"
# ip route vrf VrfReg2 3.0.0.0/8 blackhole tag 20 track 30 10

# Using Replaced
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 4.0.0.0/8 2.0.0.0 tag 4 track 8 2

  - name: Replace static routes configurations
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      - vrf_name: 'default'
        static_list:
          - prefix: '4.0.0.0/8'
            next_hops:
              - index:
                  blackhole: True
                metric: 5
                tag: 10
                track: 15
    state: replaced

# After State:
# ------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 4.0.0.0/8 blackhole tag 10 track 15 5

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
# ip route 2.0.0.0/8 interface Ethernet4 tag 2 track 3 1
# ip route vrf VrfReg1 3.0.0.0/8 4.0.0.0 interface Management 0 nexthop-vrf VrfReg2 tag 5 track 6 4
# ip route vrf VrfReg1 3.0.0.0/8 blackhole tag 22 track 33 11

  - name: Delete static routes configurations
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      - vrf_name: 'default'
        static_list:
         - prefix: '2.0.0.0/8'
           next_hops:
             - index:
                 interface: 'Ethernet4'
      - vrf_name: 'VrfReg1'
    state: deleted

# After State:
# ------------
#
# sonic# show running-configuration | grep "ip route"
# ip route 2.0.0.0/8 3.0.0.0 tag 4 track 8 2
```

## [Return Values](sonic_static_routes_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Shade Talabi (@stalabi1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
