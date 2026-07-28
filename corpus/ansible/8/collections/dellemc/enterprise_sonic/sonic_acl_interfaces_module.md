---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_acl_interfaces module – Manage access control list (ACL) to interface binding on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_acl_interfaces_module.html
fetched_at: 2026-07-28T02:03:25+00:00
---
# dellemc.enterprise_sonic.sonic_acl_interfaces module – Manage access control list (ACL) to interface binding on SONiC

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_acl_interfaces`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_acl_interfaces_module.md#synopsis)
- [Parameters](sonic_acl_interfaces_module.md#parameters)
- [Examples](sonic_acl_interfaces_module.md#examples)
- [Return Values](sonic_acl_interfaces_module.md#return-values)

## [Synopsis](sonic_acl_interfaces_module.md#id1)

- This module provides configuration management of applying access control lists (ACL) to interfaces in devices running SONiC.
- ACL needs to be created earlier in the device.

## [Parameters](sonic_acl_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies interface access-group configurations. |
| **access_groups**  list / elements=dictionary | Access-group configurations to be set for the interface. |
| **acls**  list / elements=dictionary | List of ACLs for the given type. |
| **direction**  string / required | Specifies the direction of the packets that the ACL will be applied on.  **Choices:**   - `"in"` - `"out"` |
| **name**  string / required | Name of the ACL to be applied on the interface. |
| **type**  string / required | Type of the ACLs to be applied on the interface.  **Choices:**   - `"mac"` - `"ipv4"` - `"ipv6"` |
| **name**  string / required | Full name of the interface, i.e. Eth1/1. |
| **state**  string | The state of the configuration after module completion.  *merged* - Merges provided interface access-group configuration with on-device configuration.  *replaced* - Replaces on-device access-group configuration of the specified interfaces with provided configuration.  *overridden* - Overrides all on-device interface access-group configurations with the provided configuration.  *deleted* - Deletes on-device interface access-group configuration.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_acl_interfaces_module.md#id3)

```yaml+jinja
# Using merged
#
# Before State:
# -------------
#
# sonic# show mac access-group
# sonic#
# sonic# show ip access-group
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# sonic#

  - name: Merge provided interface access-group configurations
    dellemc.enterprise_sonic.sonic_acl_interfaces:
      config:
        - name: 'Eth1/1'
          access_groups:
            - type: 'mac'
              acls:
                - name: 'mac-acl-1'
                  direction: 'in'
                - name: 'mac-acl-2'
                  direction: 'out'
            - type: 'ipv6'
              acls:
                - name: 'ipv6-acl-2'
                  direction: 'out'
        - name: 'Eth1/2'
          access_groups:
            - type: 'ipv4'
              acls:
                - name: 'ip-acl-1'
                  direction: 'in'
      state: merged

# After State:
# ------------
#
# sonic# show mac access-group
# Ingress MAC access-list mac-acl-1 on Eth1/1
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Ingress IP access-list ip-acl-1 on Eth1/2
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/1
# sonic#

# Using replaced
#
# Before State:
# -------------
#
# sonic# show mac access-group
# Ingress MAC access-list mac-acl-1 on Eth1/1
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Ingress IP access-list ip-acl-1 on Eth1/2
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/1
# sonic#

  - name: Replace device access-group configuration of specified interfaces with provided configuration
    dellemc.enterprise_sonic.sonic_acl_interfaces:
      config:
        - name: 'Eth1/2'
          access_groups:
            - type: 'ipv6'
              acls:
                - name: 'ipv6-acl-2'
                  direction: 'out'
        - name: 'Eth1/3'
          access_groups:
            - type: 'ipv4'
              acls:
                - name: 'ip-acl-2'
                  direction: 'out'
      state: replaced

# After State:
# ------------
#
# sonic# show mac access-group
# Ingress MAC access-list mac-acl-1 on Eth1/1
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Egress IP access-list ip-acl-2 on Eth1/3
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/2
# sonic#

# Using overridden
#
# Before State:
# -------------
#
# sonic# show mac access-group
# Ingress MAC access-list mac-acl-1 on Eth1/1
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Egress IP access-list ip-acl-2 on Eth1/3
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/2
# sonic#

  - name: Override all interfaces access-group device configuration with provided configuration
    dellemc.enterprise_sonic.sonic_acl_interfaces:
      config:
        - name: 'Eth1/1'
          access_groups:
            - type: 'ip'
              acls:
                - name: 'ip-acl-2'
                  direction: 'out'
        - name: 'Eth1/2'
          access_groups:
            - type: 'ip'
              acls:
                - name: 'ip-acl-2'
                  direction: 'out'
      state: overridden

# After State:
# ------------
#
# sonic# show mac access-group
# sonic#
# sonic# show ip access-group
# Egress IP access-list ip-acl-2 on Eth1/1
# Egress IP access-list ip-acl-2 on Eth1/2
# sonic#
# sonic# show ipv6 access-group
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show mac access-group
# Ingress MAC access-list mac-acl-1 on Eth1/1
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Egress IP access-list ip-acl-2 on Eth1/3
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/2
# sonic#

  - name: Delete specified interfaces access-group configurations
    dellemc.enterprise_sonic.sonic_l2_acls:
      config:
        - name: 'Eth1/1'
          access_groups:
            - type: 'mac'
              acls:
                - name: 'mac-acl-1'
                  direction: 'in'
            - type: 'ipv6'
        - name: 'Eth1/2'
      state: deleted

# After State:
# ------------
#
# sonic# show mac access-group
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Egress IP access-list ip-acl-2 on Eth1/3
# sonic#
# sonic# show ipv6 access-group
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show mac access-group
# Ingress MAC access-list mac-acl-1 on Eth1/1
# Egress MAC access-list mac-acl-2 on Eth1/1
# sonic#
# sonic# show ip access-group
# Egress IP access-list ip-acl-2 on Eth1/3
# sonic#
# sonic# show ipv6 access-group
# Ingress IPV6 access-list ipv6-acl-1 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/1
# Egress IPV6 access-list ipv6-acl-2 on Eth1/2
# sonic#

  - name: Delete all interface access-group configurations
    dellemc.enterprise_sonic.sonic_acl_interfaces:
      config:
      state: deleted

# After State:
# ------------
#
# sonic# show mac access-group
# sonic#
# sonic# show ip access-group
# sonic#
# sonic# show ipv6 access-group
# sonic#
```

## [Return Values](sonic_acl_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
