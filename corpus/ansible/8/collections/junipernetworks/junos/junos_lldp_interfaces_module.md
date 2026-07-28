---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_lldp_interfaces module – LLDP interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_lldp_interfaces_module.html
fetched_at: 2026-07-28T02:39:42+00:00
---
# junipernetworks.junos.junos_lldp_interfaces module – LLDP interfaces resource module

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_lldp_interfaces`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_lldp_interfaces_module.md#synopsis)
- [Parameters](junos_lldp_interfaces_module.md#parameters)
- [Examples](junos_lldp_interfaces_module.md#examples)
- [Return Values](junos_lldp_interfaces_module.md#return-values)

## [Synopsis](junos_lldp_interfaces_module.md#id1)

- This module manages link layer discovery protocol (LLDP) attributes of interfaces on Juniper JUNOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: lldp_interfaces

## [Parameters](junos_lldp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The list of link layer discovery protocol interface attribute configurations |
| **enabled**  boolean | This is a boolean value to control disabling of LLDP on the interface `name`  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the interface LLDP needs to be configured on. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show protocols lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Examples](junos_lldp_interfaces_module.md#id3)

```yaml+jinja
# Using merged
# Before state:
# -------------
# user@junos01# # show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;

- name: Merge provided configuration with device configuration
  junipernetworks.junos.junos_lldp_interfaces:
    config:
      - name: ge-0/0/1
      - name: ge-0/0/2
        enabled: false
    state: merged

# After state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }

# Using replaced
# Before state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }

- name: Replace provided configuration with device configuration
  junipernetworks.junos.junos_lldp_interfaces:
    config:
      - name: ge-0/0/2
        disable: false
      - name: ge-0/0/3
        enabled: false
    state: replaced

# After state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/1;
# interface ge-0/0/2;
# interface ge-0/0/3 {
#     disable;
# }

# Using overridden
# Before state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }

- name: Override provided configuration with device configuration
  junipernetworks.junos.junos_lldp_interfaces:
    config:
      - name: ge-0/0/2
        enabled: false
    state: overridden

# After state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/2 {
#     disable;
# }

# Using deleted
# Before state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/1;
# interface ge-0/0/2;
# interface ge-0/0/3 {
#     disable;
# }
- name: Delete lldp interface configuration (this will not delete other lldp configuration)
  junipernetworks.junos.junos_lldp_interfaces:
    config:
      - name: ge-0/0/1
      - name: ge-0/0/3
    state: deleted

# After state:
# -------------
# user@junos01# show protocols lldp
# management-address 10.1.1.1;
# advertisement-interval 10000;
# interface ge-0/0/2;
# interface ge-0/0/1;
# Using gathered
# Before state:
# ------------
#
# ansible@cm123456tr21# show protocols lldp
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }
- name: Gather junos lldp interfaces as in given arguments
  junipernetworks.junos.junos_lldp_interfaces:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "name": "ge-0/0/1"
#         },
#         {
#             "enabled": false,
#             "name": "ge-0/0/2"
#         }
#     ]
# After state:
# ------------
#
# ansible@cm123456tr21# show protocols lldp
# interface ge-0/0/1;
# interface ge-0/0/2 {
#     disable;
# }
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_lldp_interfaces:
    config:
      - name: ge-0/0/1
      - name: ge-0/0/2
        enabled: false
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:protocols
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:lldp>
#         <nc:interface>
#             <nc:name>ge-0/0/1</nc:name>
#             <nc:disable delete="delete"/>
#         </nc:interface>
#         <nc:interface>
#             <nc:name>ge-0/0/2</nc:name>
#             <nc:disable/>
#         </nc:interface>
#     </nc:lldp>
# </nc:protocols>"
# Using parsed
# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <protocols>
#             <ospf>
#                 <area>
#                     <name>0.0.0.0</name>
#                     <interface>
#                         <name>ge-0/0/0.0</name>
#                     </interface>
#                 </area>
#             </ospf>
#             <lldp>
#                 <interface>
#                     <name>ge-0/0/1</name>
#                 </interface>
#                 <interface>
#                     <name>ge-0/0/2</name>
#                     <disable/>
#                 </interface>
#             </lldp>
#         </protocols>
#     </configuration>
# </rpc-reply>
# - name: Convert lldp interfaces config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_lldp_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#         {
#             "name": "ge-0/0/1"
#         },
#         {
#             "enabled": false,
#             "name": "ge-0/0/2"
#         }
#     ]
```

## [Return Values](junos_lldp_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:lldp> <nc:interface> <nc:name>ge-0/0/1</nc:name> <nc:disable delete=\"delete\"/> </nc:interface> <nc:interface> <nc:name>ge-0/0/2</nc:name> <nc:disable/> </nc:interface> </nc:lldp> </nc:protocols>", "xml 2", "xml 3"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
