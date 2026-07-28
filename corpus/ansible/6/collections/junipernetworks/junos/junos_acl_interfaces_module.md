---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_acl_interfaces module – ACL interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_acl_interfaces_module.html
fetched_at: 2026-07-27T17:54:09+00:00
---
# junipernetworks.junos.junos_acl_interfaces module – ACL interfaces resource module

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
> see [Requirements](junos_acl_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-acl-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_acl_interfaces`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_acl_interfaces_module.md#synopsis)
- [Requirements](junos_acl_interfaces_module.md#requirements)
- [Parameters](junos_acl_interfaces_module.md#parameters)
- [Notes](junos_acl_interfaces_module.md#notes)
- [Examples](junos_acl_interfaces_module.md#examples)
- [Return Values](junos_acl_interfaces_module.md#return-values)

## [Synopsis](junos_acl_interfaces_module.md#id1)

- This module manages adding and removing Access Control Lists (ACLs) from interfaces on devices running Juniper JUNOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_acl_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_acl_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of ACL options for interfaces. |
| **access_groups**  list / elements=dictionary | Specifies ACLs attached to the interface. |
| **acls**  list / elements=dictionary | Specifies the ACLs for the provided AFI. |
| **direction**  string | Specifies the direction of packets that the ACL will be applied on.  Choices:   - `"in"` - `"out"` |
| **name**  string | Specifies the name of the IPv4/IPv4 ACL for the interface. |
| **afi**  string | Specifies the AFI for the ACL(s) to be configured on this interface.  Choices:   - `"ipv4"` - `"ipv6"` |
| **name**  string | Name/Identifier for the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_acl_interfaces_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_acl_interfaces_module.md#id5)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Delete JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
        - name: outbound_acl
          direction: out
      state: deleted

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

# Using merged

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface without filter";
#     unit 0 {
#         family inet {
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Merge JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
        - name: outbound_acl
          direction: out
      state: merged

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

# Using overridden

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface without filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input foo_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Override JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
        - name: outbound_acl
          direction: out
      state: overridden

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

# Using replaced

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface without filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input foo_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Replace JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
      state: replaced

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }
```

## [Return Values](junos_acl_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Daniel Mellado (@dmellado)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
