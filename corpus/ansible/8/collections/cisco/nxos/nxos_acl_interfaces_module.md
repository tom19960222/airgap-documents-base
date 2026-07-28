---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_acl_interfaces module – ACL interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_acl_interfaces_module.html
fetched_at: 2026-07-28T01:38:26+00:00
---
# cisco.nxos.nxos_acl_interfaces module – ACL interfaces resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_acl_interfaces`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_acl_interfaces_module.md#synopsis)
- [Parameters](nxos_acl_interfaces_module.md#parameters)
- [Notes](nxos_acl_interfaces_module.md#notes)
- [Examples](nxos_acl_interfaces_module.md#examples)
- [Return Values](nxos_acl_interfaces_module.md#return-values)

## [Synopsis](nxos_acl_interfaces_module.md#id1)

- Add and remove Access Control Lists on interfaces in NX-OS platform

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: acl_interfaces

## [Parameters](nxos_acl_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of interfaces to be configured with ACLs |
| **access_groups**  list / elements=dictionary | List of address family indicators with ACLs to be configured on the interface |
| **acls**  list / elements=dictionary | List of Access Control Lists for the interface |
| **direction**  string / required | Direction to be applied for the ACL  **Choices:**   - `"in"` - `"out"` |
| **name**  string / required | Name of the ACL to be added/removed |
| **port**  boolean | Use ACL as port policy.  **Choices:**   - `false` - `true` |
| **afi**  string / required | Address Family Indicator of the ACLs to be configured  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **name**  string / required | Name of the interface |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^interface’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"deleted"` - `"gathered"` - `"merged"` ← (default) - `"overridden"` - `"rendered"` - `"replaced"` - `"parsed"` |

## [Notes](nxos_acl_interfaces_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS

## [Examples](nxos_acl_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# ------------
#

- name: Merge ACL interfaces configuration
  cisco.nxos.nxos_acl_interfaces:
    config:
    - name: Ethernet1/2
      access_groups:
      - afi: ipv6
        acls:
        - name: ACL1v6
          direction: in

    - name: Eth1/5
      access_groups:
      - afi: ipv4
        acls:
        - name: PortACL
          direction: in
          port: true

        - name: ACL1v4
          direction: out

      - afi: ipv6
        acls:
        - name: ACL1v6
          direction: in
    state: merged

# After state:
# ------------
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/5
#   ip port access-group PortACL in
#   ip access-group ACL1v4 out
#   ipv6 traffic-filter ACL1v6 in

# Using replaced

# Before state:
# ------------
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/5
#   ip port access-group PortACL in
#   ip access-group ACL1v4 out
#   ipv6 traffic-filter ACL1v6 in

- name: Replace interface configuration with given configuration
  cisco.nxos.nxos_acl_interfaces:
    config:
    - name: Eth1/5
      access_groups:
      - afi: ipv4
        acls:
        - name: NewACLv4
          direction: out

    - name: Ethernet1/3
      access_groups:
      - afi: ipv6
        acls:
        - name: NewACLv6
          direction: in
          port: true
    state: replaced

# After state:
# ------------
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/3
#   ipv6 port traffic-filter NewACLv6 in
# interface Ethernet1/5
#   ip access-group NewACLv4 out

# Using overridden

# Before state:
# ------------
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/5
#   ip port access-group PortACL in
#   ip access-group ACL1v4 out
#   ipv6 traffic-filter ACL1v6 in

- name: Override interface configuration with given configuration
  cisco.nxos.nxos_acl_interfaces:
    config:
    - name: Ethernet1/3
      access_groups:
      - afi: ipv4
        acls:
        - name: ACL1v4
          direction: out

        - name: PortACL
          port: true
          direction: in
      - afi: ipv6
        acls:
        - name: NewACLv6
          direction: in
          port: true
    state: overridden

# After state:
# ------------
# interface Ethernet1/3
#   ip access-group ACL1v4 out
#   ip port access-group PortACL in
#   ipv6 port traffic-filter NewACLv6 in

# Using deleted to remove ACL config from specified interfaces

# Before state:
# -------------
# interface Ethernet1/1
#   ip access-group ACL2v4 in
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/5
#   ip port access-group PortACL in
#   ip access-group ACL1v4 out
#   ipv6 traffic-filter ACL1v6 in

- name: Delete ACL configuration on interfaces
  cisco.nxos.nxos_acl_interfaces:
    config:
    - name: Ethernet1/5
    - name: Ethernet1/2
    state: deleted

# After state:
# -------------
# interface Ethernet1/1
#   ip access-group ACL2v4 in
# interface Ethernet1/2
# interface Ethernet1/5

# Using deleted to remove ACL config from all interfaces

# Before state:
# -------------
# interface Ethernet1/1
#   ip access-group ACL2v4 in
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/5
#   ip port access-group PortACL in
#   ip access-group ACL1v4 out
#   ipv6 traffic-filter ACL1v6 in

- name: Delete ACL configuration from all interfaces
  cisco.nxos.nxos_acl_interfaces:
    state: deleted

# After state:
# -------------
# interface Ethernet1/1
# interface Ethernet1/2
# interface Ethernet1/5

# Using parsed

- name: Parse given configuration into structured format
  cisco.nxos.nxos_acl_interfaces:
    running_config: |
      interface Ethernet1/2
      ipv6 traffic-filter ACL1v6 in
      interface Ethernet1/5
      ipv6 traffic-filter ACL1v6 in
      ip access-group ACL1v4 out
      ip port access-group PortACL in
    state: parsed

# returns
# parsed:
#   - name: Ethernet1/2
#     access_groups:
#       - afi: ipv6
#         acls:
#           - name: ACL1v6
#             direction: in
#  - name: Ethernet1/5
#    access_groups:
#      - afi: ipv4
#        acls:
#          - name: PortACL
#            direction: in
#            port: True
#          - name: ACL1v4
#            direction: out
#      - afi: ipv6
#        acls:
#          - name: ACL1v6
#             direction: in

# Using gathered:

# Before state:
# ------------
# interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
# interface Ethernet1/5
#   ipv6 traffic-filter ACL1v6 in
#   ip access-group ACL1v4 out
#   ip port access-group PortACL in

- name: Gather existing configuration from device
  cisco.nxos.nxos_acl_interfaces:
    config:
    state: gathered

# returns
# gathered:
#   - name: Ethernet1/2
#     access_groups:
#       - afi: ipv6
#         acls:
#           - name: ACL1v6
#             direction: in
#  - name: Ethernet1/5
#    access_groups:
#      - afi: ipv4
#        acls:
#          - name: PortACL
#            direction: in
#            port: True
#          - name: ACL1v4
#            direction: out
#      - afi: ipv6
#        acls:
#          - name: ACL1v6
#             direction: in

# Using rendered

- name: Render required configuration to be pushed to the device
  cisco.nxos.nxos_acl_interfaces:
    config:
    - name: Ethernet1/2
      access_groups:
      - afi: ipv6
        acls:
        - name: ACL1v6
          direction: in

    - name: Ethernet1/5
      access_groups:
      - afi: ipv4
        acls:
        - name: PortACL
          direction: in
          port: true
        - name: ACL1v4
          direction: out
      - afi: ipv6
        acls:
        - name: ACL1v6
          direction: in
    state: rendered

# returns
# rendered:
#   interface Ethernet1/2
#   ipv6 traffic-filter ACL1v6 in
#   interface Ethernet1/5
#   ipv6 traffic-filter ACL1v6 in
#   ip access-group ACL1v4 out
#   ip port access-group PortACL in
```

## [Return Values](nxos_acl_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface Ethernet1/2", "ipv6 traffic-filter ACL1v6 out", "ip port access-group PortACL in"]` |

### Authors

- Adharsh Srivats Rangarajan (@adharshsrivatsr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
