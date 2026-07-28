---
collection: ansible
version: "6"
title: "arista.eos.eos_lacp_interfaces module – LACP interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_lacp_interfaces_module.html
fetched_at: 2026-07-27T16:45:12+00:00
---
# arista.eos.eos_lacp_interfaces module – LACP interfaces resource module

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
> To use it in a playbook, specify: `arista.eos.eos_lacp_interfaces`.

New in arista.eos 1.0.0

- [Synopsis](eos_lacp_interfaces_module.md#synopsis)
- [Parameters](eos_lacp_interfaces_module.md#parameters)
- [Notes](eos_lacp_interfaces_module.md#notes)
- [Examples](eos_lacp_interfaces_module.md#examples)
- [Return Values](eos_lacp_interfaces_module.md#return-values)

## [Synopsis](eos_lacp_interfaces_module.md#id1)

- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces on Arista EOS devices.

## [Parameters](eos_lacp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of LACP interfaces options. |
| **name**  string | Full name of the interface (i.e. Ethernet1). |
| **port_priority**  integer | LACP port priority for the interface. Range 1-65535. |
| **timer**  aliases: rate  string | Rate at which PDUs are sent by LACP. At fast rate LACP is transmitted once every 1 second. At normal rate LACP is transmitted every 30 seconds after the link is bundled.  Choices:   - `"fast"` - `"normal"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^interfaces**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](eos_lacp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_lacp_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Merge provided configuration with device configuration
  arista.eos.eos_lacp_interfaces:
    config:
    - name: Ethernet1
      rate: fast
    - name: Ethernet2
      rate: normal
    state: merged

#
# -----------
# After state
# -----------
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
#    lacp rate fast
# interface Ethernet2

# Using replaced
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Replace existing LACP configuration of specified interfaces with provided
    configuration
  arista.eos.eos_lacp_interfaces:
    config:
    - name: Ethernet1
      rate: fast
    state: replaced

#
# -----------
# After state
# -----------
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp rate fast
# interface Ethernet2
#    lacp rate fast

# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Override the LACP configuration of all the interfaces with provided configuration
  arista.eos.eos_lacp_interfaces:
    config:
    - name: Ethernet1
      rate: fast
    state: overridden

#
# -----------
# After state
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp rate fast
# interface Ethernet2

# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Delete LACP attributes of given interfaces (or all interfaces if none specified).
  arista.eos.eos_lacp_interfaces:
    state: deleted

#
# -----------
# After state
# -----------
#
# veos#show run | section ^interface
# interface Ethernet1
# interface Ethernet2

# using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lacp_interfaces:
    config:
    - name: Ethernet1
      rate: fast
    - name: Ethernet2
      rate: normal
    state: rendered

#
# -----------
# Output
# -----------
# rendered:
#   - "interface Ethernet1"
#   - "lacp rate fast"

# Using parsed:

# parsed.cfg:
#    "interface Ethernet1"
#    "lacp rate fast"
#    "interface Ethernet2"

- name: Use parsed to convert native configs to structured data
  arista.eos.eos_lacp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output:
# parsed:
#   - name: Ethernet1
#     rate: fast
#   - name: Ethernet2
#     rate: normal

# Using gathered:
# native config:
#  veos#show run | section ^interface
# interface Ethernet1
#    lacp port-priority 30
# interface Ethernet2
#    lacp rate fast

- name: Gather LACP facts from the device
  arista.eos.eos_lacp_interfaces:
    state: gathered

# Output:
# gathered:
#   - name: Ethernet1
#   - name: Ethernet2
#     rate: fast
```

## [Return Values](eos_lacp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Ethernet1", "lacp rate fast"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
