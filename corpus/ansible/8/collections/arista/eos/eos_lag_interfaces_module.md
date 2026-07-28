---
collection: ansible
version: "8"
title: "arista.eos.eos_lag_interfaces module – LAG interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_lag_interfaces_module.html
fetched_at: 2026-07-28T01:11:05+00:00
---
# arista.eos.eos_lag_interfaces module – LAG interfaces resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_lag_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_lag_interfaces_module.md#synopsis)
- [Parameters](eos_lag_interfaces_module.md#parameters)
- [Notes](eos_lag_interfaces_module.md#notes)
- [Examples](eos_lag_interfaces_module.md#examples)
- [Return Values](eos_lag_interfaces_module.md#return-values)

## [Synopsis](eos_lag_interfaces_module.md#id1)

- This module manages attributes of link aggregation groups on Arista EOS devices.

Aliases: lag_interfaces

## [Parameters](eos_lag_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of link aggregation group configurations. |
| **members**  list / elements=dictionary | Ethernet interfaces that are part of the group. |
| **member**  string | Name of ethernet interface that is a member of the LAG. |
| **mode**  string | LAG mode for this interface.  **Choices:**   - `"active"` - `"on"` - `"passive"` |
| **name**  string / required | Name of the port-channel interface of the link aggregation group (LAG) e.g., Port-Channel5. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](eos_lag_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_lag_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2

- name: Merge provided LAG attributes with existing device configuration
  arista.eos.eos_lag_interfaces:
    config:
      - name: 5
        members:
          - member: Ethernet2
            mode: on
    state: merged

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

# Using replaced

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2

- name: Replace all device configuration of specified LAGs with provided configuration
  arista.eos.eos_lag_interfaces:
    config:
      - name: 5
        members:
          - member: Ethernet2
            mode: on
    state: replaced

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# interface Ethernet2
#   channel-group 5 mode on

# Using overridden

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2

- name: Override all device configuration of all LAG attributes with provided configuration
  arista.eos.eos_lag_interfaces:
    config:
      - name: 10
        members:
          - member: Ethernet2
            mode: on
    state: overridden

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# interface Ethernet2
#   channel-group 10 mode on

# Using deleted

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

- name: Delete LAG attributes of the given interfaces.
  arista.eos.eos_lag_interfaces:
    config:
      - name: 5
        members:
          - member: Ethernet1
    state: deleted

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# interface Ethernet2
#   channel-group 5 mode on

# Using parsed:

# parsed.cfg
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

- name: Use parsed to convert native configs to structured data
  arista.eos.lag_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output:
#   parsed:
#     - name: 5
#       members:
#         - member: Ethernet2
#           mode: on
#         - member: Ethernet1
#           mode: on

# using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lag_interfaces:
    config:
      - name: 5
        members:
          - member: Ethernet2
            mode: on
          - member: Ethernet1
            mode: on
    state: rendered
# -----------
# Output
# -----------
#
# rendered:

# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

# Using gathered:

# native config:
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

- name: Gather lldp_global facts from the device
  arista.eos.lldp_global:
    state: gathered

# Output:
#   gathered:
#     - name: 5
#       members:
#         - member: Ethernet2
#           mode: on
#         - member: Ethernet1
#           mode: on
```

## [Return Values](eos_lag_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
