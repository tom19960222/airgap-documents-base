---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_vlans module – VLANs resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_vlans_module.html
fetched_at: 2026-07-27T17:54:44+00:00
---
# junipernetworks.junos.junos_vlans module – VLANs resource module

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
> see [Requirements](junos_vlans_module.md#ansible-collections-junipernetworks-junos-junos-vlans-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_vlans`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_vlans_module.md#synopsis)
- [Requirements](junos_vlans_module.md#requirements)
- [Parameters](junos_vlans_module.md#parameters)
- [Notes](junos_vlans_module.md#notes)
- [Examples](junos_vlans_module.md#examples)
- [Return Values](junos_vlans_module.md#return-values)

## [Synopsis](junos_vlans_module.md#id1)

- This module creates and manages VLAN configurations on Junos OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_vlans_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_vlans_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Vlan options |
| **description**  string | Text description of VLANs |
| **l3_interface**  string | Name of logical layer 3 interface. |
| **name**  string / required | Name of VLAN. |
| **vlan_id**  integer | IEEE 802.1q VLAN identifier for VLAN (1..4094). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show vlans**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](junos_vlans_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed
> - Tested against Junos OS 18.4R1
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).

## [Examples](junos_vlans_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show vlans
#
# [edit]

- name: Merge provided Junos vlans config with running-config
  junipernetworks.junos.junos_vlans:
    config:
    - name: vlan1
      vlan_id: 1
    - name: vlan2
      vlan_id: 2
      l3_interface: irb.12
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": [
#         {
#             "name": "vlan1",
#             "vlan_id": 1
#         },
#         {
#             "l3_interface": "irb.12",
#             "name": "vlan2",
#             "vlan_id": 2
#         }
#     ],
#     "before": [],
#     "changed": true,
#     "commands": [
#         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id></nc:vlan>"
#         "<nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id><nc:l3-interface>irb.12</nc:l3-interface>"
#         "</nc:vlan></nc:vlans>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show vlans
# vlan1 {
#     vlan-id 1;
# }
# vlan2 {
#     vlan-id 2;
#     l3-interface irb.12;
# }

# Using replaced
#
# Before state
# ------------
#
# vagrant@vsrx# show vlans
# vlan1 {
#     vlan-id 1;
# }
# vlan2 {
#     vlan-id 2;
#     l3-interface irb.12;
# }

- name: Replace Junos vlans running-config with the provided config
  junipernetworks.junos.junos_vlans:
    config:
    - name: vlan1
      vlan_id: 11
      l3_interface: irb.10

    - name: vlan2
      vlan_id: 2
    state: replaced
# -------------------------
# Module Execution Result
# -------------------------
#     "after": [
#         {
#             "l3_interface": "irb.10",
#             "name": "vlan1",
#             "vlan_id": 11
#         },
#         {
#             "name": "vlan2",
#             "vlan_id": 2
#         }
#     ],
#     "before": [
#         {
#             "name": "vlan1",
#             "vlan_id": 1
#         },
#         {
#             "l3_interface": "irb.12",
#             "name": "vlan2",
#             "vlan_id": 2
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan>"
#         "<nc:vlan delete="delete"><nc:name>vlan2</nc:name></nc:vlan>"
#         "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>11</nc:vlan-id>"
#         "<nc:l3-interface>irb.10</nc:l3-interface></nc:vlan><nc:vlan>"
#         "<nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id></nc:vlan></nc:vlans>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show vlans
# vlan1 {
#     vlan-id 11;
#     l3-interface irb.10;
# }
# vlan2 {
#     vlan-id 2;
# }
#
# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show vlans
# vlan1 {
#     vlan-id 11;
#     l3-interface irb.10;
# }
# vlan2 {
#     vlan-id 2;
# }
- name: Override Junos running-config with provided config
  junipernetworks.junos.junos_vlans:
    config:
    - name: vlan3
      vlan_id: 3
      l3_interface: irb.13
    state: overridden
# -------------------------
# Module Execution Result
# -------------------------
#     "after": [
#         {
#             "l3_interface": "irb.13",
#             "name": "vlan3",
#             "vlan_id": 3
#         }
#     ],
#     "before": [
#         {
#             "l3_interface": "irb.10",
#             "name": "vlan1",
#             "vlan_id": 11
#         },
#         {
#             "name": "vlan2",
#             "vlan_id": 2
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:vlan delete="delete"><nc:name>vlan1</nc:name></nc:vlan><nc:vlan delete="delete">"
#         "<nc:name>vlan2</nc:name></nc:vlan><nc:vlan><nc:name>vlan3</nc:name><nc:vlan-id>3</nc:vlan-id>"
#         "<nc:l3-interface>irb.13</nc:l3-interface></nc:vlan></nc:vlans>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show vlans
# vlan3 {
#     vlan-id 3;
#     l3-interface irb.13;
# }
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show vlans
# vlan3 {
#     vlan-id 3;
#     l3-interface irb.13;
# }
- name: Delete specific vlan
  junipernetworks.junos.junos_vlans:
    config:
    - name: vlan3
    state: deleted
# -------------------------
# Module Execution Result
# -------------------------
#     "after": [],
#     "changed": true,
#     "commands": [
#         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#         "<nc:vlan delete="delete"><nc:name>vlan3</nc:name></nc:vlan></nc:vlans>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show vlans
# vlan1 {
#     vlan-id 11;
#     l3-interface irb.10;
# }
# vlan2 {
#     vlan-id 2;
# }

- name: Gather running vlans configuration
  junipernetworks.junos.junos_vlans:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": [
#         {
#             "l3_interface": "irb.10",
#             "name": "vlan1",
#             "vlan_id": 11
#         },
#         {
#             "name": "vlan2",
#             "vlan_id": 2
#         }
#     ],
#     "changed": false,
#
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_vlans:
    config:
    - name: vlan1
      vlan_id: 1

    - name: vlan2
      vlan_id: 2
      l3_interface: irb.12
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#         "<nc:vlans xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id></nc:vlan>"
#         "<nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id><nc:l3-interface>irb.12</nc:l3-interface>"
#         "</nc:vlan></nc:vlans>"
#     ]
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <vlans>
#           <vlan>
#             <name>vlan1</name>
#             <vlan-id>1</vlan-id>
#           </vlan>
#           <vlan>
#             <name>vlan2</name>
#             <vlan-id>2</vlan-id>
#             <l3-interface>irb.12</l3-interface>
#           </vlan>
#        </vlans>
#     </configuration>
# </rpc-reply>

- name: Parse routing instance running config
  junipernetworks.junos.junos_vlans:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  [
#         {
#             "name": "vlan1",
#             "vlan_id": 1
#         },
#         {
#             "l3_interface": "irb.12",
#             "name": "vlan2",
#             "vlan_id": 2
#         }
#     ]
#
```

## [Return Values](junos_vlans_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:vlans xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:vlan><nc:name>vlan1</nc:name><nc:vlan-id>1</nc:vlan-id> </nc:vlan><nc:vlan><nc:name>vlan2</nc:name><nc:vlan-id>2</nc:vlan-id> <nc:l3-interface>irb.12</nc:l3-interface></nc:vlan></nc:vlans>", "xml 2", "xml 3"]` |

### Authors

- Daniel Mellado (@dmellado)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
