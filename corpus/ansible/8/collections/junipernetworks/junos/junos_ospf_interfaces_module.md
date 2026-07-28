---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_ospf_interfaces module – OSPF Interfaces Resource Module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_ospf_interfaces_module.html
fetched_at: 2026-07-28T02:39:46+00:00
---
# junipernetworks.junos.junos_ospf_interfaces module – OSPF Interfaces Resource Module.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_ospf_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-ospf-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_ospf_interfaces`.

New in junipernetworks.junos 1.3.0

- [Synopsis](junos_ospf_interfaces_module.md#synopsis)
- [Requirements](junos_ospf_interfaces_module.md#requirements)
- [Parameters](junos_ospf_interfaces_module.md#parameters)
- [Notes](junos_ospf_interfaces_module.md#notes)
- [Examples](junos_ospf_interfaces_module.md#examples)
- [Return Values](junos_ospf_interfaces_module.md#return-values)

## [Synopsis](junos_ospf_interfaces_module.md#id1)

- This module manages OSPF(v2/v3) configuration of interfaces on devices running Juniper JUNOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ospf_interfaces

## [Requirements](junos_ospf_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_ospf_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPF configuration for interfaces. |
| **address_family**  list / elements=dictionary | OSPF settings on the interfaces in address-family context. |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF settings on the interfaces.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **processes**  dictionary | Interfaces configuration for an OSPF process. |
| **area**  dictionary | Specify the area-id |
| **area_id**  string | Specify area id. |
| **authentication**  dictionary | Specify authentication type |
| **md5**  list / elements=dictionary | Specify md5 based authentication. |
| **key_id**  integer | Specify md5 key-id |
| **key_value**  string | Specify key value |
| **start_time**  string | Specify start time for key transmission |
| **simple_password**  string | Specify password for authentication. |
| **bandwidth_based_metrics**  list / elements=dictionary | Specify list of bandwidth based metrics |
| **bandwidth**  string | BW to apply metric to.  **Choices:**   - `"1g"` - `"10g"` |
| **metric**  integer | Specify metric |
| **dead_interval**  integer | Dead interval (seconds). |
| **demand_circuit**  boolean | Interface functions as a demand circuit.  **Choices:**   - `false` - `true` |
| **flood_reduction**  boolean | Enable flood reduction.  **Choices:**   - `false` - `true` |
| **hello_interval**  integer | Hello interval (seconds). |
| **interface_type**  string | Specify type of interface  **Choices:**   - `"nbma"` - `"p2mp"` - `"p2p"` |
| **ipsec_sa**  string | IPSec security association name |
| **metric**  integer | Metric applied to the interface. |
| **mtu**  integer | Maximum OSPF packet size |
| **no_advertise_adjacency_segment**  boolean | Do not advertise an adjacency segment for this interface.  **Choices:**   - `false` - `true` |
| **no_eligible_backup**  boolean | Not eligible to backup traffic from protected interfaces.  **Choices:**   - `false` - `true` |
| **no_eligible_remote_backup**  boolean | Not eligible for Remote-LFA backup traffic from protected interfaces.  **Choices:**   - `false` - `true` |
| **no_interface_state_traps**  boolean | Do not send interface state change traps.  **Choices:**   - `false` - `true` |
| **no_neighbor_down_notification**  boolean | Don’t inform other protocols about neighbor down events.  **Choices:**   - `false` - `true` |
| **node_link_protection**  boolean | Protect interface from both link and node faults.  **Choices:**   - `false` - `true` |
| **passive**  boolean | Do not run OSPF, but advertise it.  **Choices:**   - `false` - `true` |
| **poll_interval**  integer | Poll interval (seconds). |
| **priority**  integer | Priority for the interface. |
| **retransmit_interval**  integer | Retransmit interval (seconds). |
| **secondary**  boolean | Treat interface as secondary  **Choices:**   - `false` - `true` |
| **te_metric**  integer | Traffic engineering metric applied to the interface. |
| **transit_delay**  integer | Transit delay (seconds). |
| **name**  string / required | Name/Identifier of the interface. |
| **router_id**  string | The OSPF router id. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show protocols ospf**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_ospf_interfaces_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_ospf_interfaces_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# admin# show protocols ospf

- name: Merge Junos OSPF interfaces config
  junipernetworks.junos.junos_ospf_interfaces:
    config:
      - name: 'ge-0/0/2.0'
        address_family:
          - afi: 'ipv4'
            processes:
              area:
                area_id: '0.0.0.2'
              priority: 3
              metric: 5
    state: merged

# After state
# -----------
#
# admin# show protocols ospf
# area 0.0.0.2 {
#     interface ge-0/0/2.0 {
#         metric 5;
#         priority 3;
#     }
# }

# Using replaced
#
# Before state
# ------------
#
# admin# show protocols ospf
# area 0.0.0.2 {
#     interface ge-0/0/2.0 {
#         metric 5;
#         priority 3;
#     }
# }
- name: Replace Junos OSPF interfaces config
  junipernetworks.junos.junos_ospf_interfaces:
    config:
      - name: 'ge-0/0/2.0'
        address_family:
          - afi: 'ipv4'
            processes:
              area:
                area_id: '0.0.0.1'
              priority: 6
              metric: 6
    state: replaced

# After state
# -----------
#
# admin# show protocols ospf
# area 0.0.0.1 {
#     interface ge-0/0/2.0 {
#         metric 6;
#         priority 6;
#     }
# }

# Using overridden
#
# Before state
# ------------
#
# admin# show protocols ospf
# area 0.0.0.3 {
#     interface ge-0/0/3.0 {
#         metric 5;
#         priority 3;
#     }
# }
# area 0.0.0.2 {
#     interface ge-0/0/2.0 {
#         metric 5;
#         priority 3;
#     }
# }

- name: Override Junos OSPF interfaces config
  junipernetworks.junos.junos_ospf_interfaces:
  config:
    - name: 'ge-0/0/1.0'
      address_family:
        - afi: 'ipv4'
          processes:
            area:
              area_id: '0.0.0.1'
            priority: 3
            metric: 5
  state: overridden

# After state
# -----------
#
# admin# show protocols ospf
# area 0.0.0.1 {
#     interface ge-0/0/1.0 {
#         metric 5;
#         priority 3;
#     }
# }

#
# Using deleted
#
# Before state
# ------------
#
# admin# show protocols ospf
# area 0.0.0.1 {
#     interface ge-0/0/1.0 {
#         metric 5;
#         priority 3;
#     }
# }

- name: Delete Junos OSPF interfaces config
  junipernetworks.junos.junos_ospf_interfaces:
    config:
      - name: 'ge-0/0/1.0'
    state: deleted

# After state
# -----------
#
# admin# show protocols ospf
# Using gathered
#
# Before state
# ------------
#
# admin# show protocols ospf
# area 0.0.0.3 {
#     interface ge-0/0/3.0 {
#         metric 5;
#         priority 3;
#     }
# }
# area 0.0.0.2 {
#     interface ge-0/0/2.0 {
#         metric 5;
#         priority 3;
#     }
# }

- name: Gather Junos OSPF interfaces config
  junipernetworks.junos.junos_ospf_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "processes": {
#                         "area": {
#                             "area_id": "0.0.0.3"
#                         },
#                         "metric": 5,
#                         "priority": 3
#                     }
#                 }
#             ],
#             "name": "ge-0/0/3.0",
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "processes": {
#                         "area": {
#                             "area_id": "0.0.0.2"
#                         },
#                         "metric": 5,
#                         "priority": 3
#                     }
#                 }
#             ],
#             "name": "ge-0/0/2.0",
#         }
#     ]
#
# Using rendered
#
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_ospf_interfaces:
    config:
      - name: 'ge-0/0/2.0'
        address_family:
          - afi: 'ipv4'
            processes:
              area:
                area_id: '0.0.0.2'
              priority: 3
              metric: 5
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "
# <nc:protocols
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:ospf>
#         <nc:area>
#             <nc:name>0.0.0.2</nc:name>
#             <nc:interface>
#                 <nc:name>ge-0/0/2.0</nc:name>
#                 <nc:priority>3</nc:priority>
#                 <nc:metric>5</nc:metric>
#             </nc:interface>
#         </nc:area>
#     </nc:ospf>
# </nc:protocols>"
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <protocols>
#             <ospf>
#                 <area>
#                     <name>0.0.0.2</name>
#                     <stub>
#                         <default-metric>200</default-metric>
#                     </stub>
#                     <interface>
#                         <name>ge-0/0/2.0</name>
#                         <metric>5</metric>
#                         <priority>3</priority>
#                     </interface>
#                 </area>
#             </ospf>
#         </protocols>
#         <routing-options>
#             <router-id>10.200.16.75</router-id>
#         </routing-options>
#     </configuration>
# </rpc-reply>

- name: Parsed the device configuration to get output commands
  junipernetworks.junos.junos_ospf_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "processes": {
#                         "area": {
#                             "area_id": "0.0.0.2"
#                         },
#                         "metric": 5,
#                         "priority": 3
#                     }
#                 }
#             ],
#             "name": "ge-0/0/2.0",
#         }
#     ]
#
```

## [Return Values](junos_ospf_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:ospf> <nc:area> <nc:name>0.0.0.3</nc:name> <nc:interface> <nc:name>ge-0/0/3.0</nc:name> <nc:priority>3</nc:priority> <nc:metric>5</nc:metric> </nc:interface> </nc:area> <nc:area> <nc:name>0.0.0.2</nc:name> <nc:interface> <nc:name>ge-0/0/2.0</nc:name> <nc:priority>3</nc:priority> <nc:metric>5</nc:metric> </nc:interface> </nc:area> </nc:ospf> </nc:protocols>\", \" <nc:routing-options xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:router-id>10.200.16.75</nc:router-id> <nc:router-id>10.200.16.75</nc:router-id> </nc:routing-options>", "xml 2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
