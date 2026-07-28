---
collection: ansible
version: "6"
title: "arista.eos.eos_acl_interfaces module – ACL interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_acl_interfaces_module.html
fetched_at: 2026-07-27T16:45:06+00:00
---
# arista.eos.eos_acl_interfaces module – ACL interfaces resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_acl_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_acl_interfaces_module.md#synopsis)
- [Parameters](eos_acl_interfaces_module.md#parameters)
- [Examples](eos_acl_interfaces_module.md#examples)
- [Return Values](eos_acl_interfaces_module.md#return-values)

## [Synopsis](eos_acl_interfaces_module.md#id1)

- This module manages adding and removing Access Control Lists (ACLs) from interfaces on devices running EOS software.

## [Parameters](eos_acl_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of ACL options for interfaces. |
| **access_groups**  list / elements=dictionary | Specifies ACLs attached to the interfaces. |
| **acls**  list / elements=dictionary | Specifies the ACLs for the provided AFI. |
| **direction**  string / required | Specifies the direction of packets that the ACL will be applied on.  Choices:   - `"in"` - `"out"` |
| **name**  string / required | Specifies the name of the IPv4/IPv4 ACL for the interface. |
| **afi**  string / required | Specifies the AFI for the ACL(s) to be configured on this interface.  Choices:   - `"ipv4"` - `"ipv6"` |
| **name**  string / required | Name/Identifier for the interface. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Examples](eos_acl_interfaces_module.md#id3)

```yaml+jinja
# Using Merged

# Before state:
# -------------
#
# eos#sh running-config | include interface|access-group
# interface Ethernet1
# interface Ethernet2
# interface Ethernet3

- name: Merge module attributes of given access-groups
  arista.eos.eos_acl_interfaces:
    config:
    - name: Ethernet2
      access_groups:
      - afi: ipv4
        acls:
          name: acl01
          direction: in
      - afi: ipv6
        acls:
          name: acl03
          direction: out
    state: merged

# Commands Fired:
# ---------------
#
# interface Ethernet2
# ip access-group acl01 in
# ipv6 access-group acl03 out

# After state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Loopback888
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 in
#  ipv6 access-group acl03 out
# interface Ethernet3

# Using Replaced

# Before state:
# -------------
#
# eos#sh running-config | include interface|access-group
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 in
#  ipv6 access-group acl03 out
# interface Ethernet3
#  ip access-group acl01 in

- name: Replace module attributes of given access-groups
  arista.eos.eos_acl_interfaces:
    config:
    - name: Ethernet2
      access_groups:
      - afi: ipv4
        acls:
          name: acl01
          direction: out
    state: replaced

# Commands Fired:
# ---------------
#
# interface Ethernet2
# no ip access-group acl01 in
# no ipv6 access-group acl03 out
# ip access-group acl01 out

# After state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Loopback888
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 out
# interface Ethernet3
#  ip access-group acl01 in

# Using Overridden

# Before state:
# -------------
#
# eos#sh running-config | include interface|access-group
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 in
#  ipv6 access-group acl03 out
# interface Ethernet3
#  ip access-group acl01 in

- name: Override module attributes of given access-groups
  arista.eos.eos_acl_interfaces:
    config:
    - name: Ethernet2
      access_groups:
      - afi: ipv4
        acls:
          name: acl01
          direction: out
    state: overridden

# Commands Fired:
# ---------------
#
# interface Ethernet2
# no ip access-group acl01 in
# no ipv6 access-group acl03 out
# ip access-group acl01 out
# interface Ethernet3
# no ip access-group acl01 in

# After state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Loopback888
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 out
# interface Ethernet3

# Using Deleted

# Before state:
# -------------
#
# eos#sh running-config | include interface|access-group
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 in
#  ipv6 access-group acl03 out
# interface Ethernet3
#  ip access-group acl01 out

- name: Delete module attributes of given access-groups
  arista.eos.eos_acl_interfaces:
    config:
    - name: Ethernet2
      access_groups:
      - afi: ipv4
        acls:
          name: acl01
          direction: in
      - afi: ipv6
        acls:
          name: acl03
          direction: out
    state: deleted

# Commands Fired:
# ---------------
#
# interface Ethernet2
# no ip access-group acl01 in
# no ipv6 access-group acl03 out

# After state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Loopback888
# interface Ethernet1
# interface Ethernet2
# interface Ethernet3
#  ip access-group acl01 out

# Before state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 in
#  ipv6 access-group acl03 out
# interface Ethernet3
#  ip access-group acl01 out

- name: Delete module attributes of given access-groups from ALL Interfaces
  arista.eos.eos_acl_interfaces:
    config:
    state: deleted

# Commands Fired:
# ---------------
#
# interface Ethernet2
# no ip access-group acl01 in
# no ipv6 access-group acl03 out
# interface Ethernet3
# no ip access-group acl01 out

# After state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Loopback888
# interface Ethernet1
# interface Ethernet2
# interface Ethernet3

# Before state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Ethernet1
# interface Ethernet2
#  ip access-group acl01 in
#  ipv6 access-group acl03 out
# interface Ethernet3
#  ip access-group acl01 out

- name: Delete acls under afi
  arista.eos.eos_acl_interfaces:
    config:
    - name: Ethernet3
      access_groups:
      - afi: ipv4
    - name: Ethernet2
      access_groups:
      - afi: ipv6
    state: deleted

# Commands Fired:
# ---------------
#
# interface Ethernet2
# no ipv6 access-group acl03 out
# interface Ethernet3
# no ip access-group acl01 out

# After state:
# -------------
#
# eos#sh running-config | include interface| access-group
# interface Loopback888
# interface Ethernet1
# interface Ethernet2
#   ip access-group acl01 in
# interface Ethernet3
```

## [Return Values](eos_acl_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet2", "ip access-group acl01 in", "ipv6 access-group acl03 out", "interface Ethernet3", "ip access-group acl01 out"]` |

### Authors

- GomathiSelvi S (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
