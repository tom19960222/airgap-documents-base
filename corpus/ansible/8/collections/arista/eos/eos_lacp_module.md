---
collection: ansible
version: "8"
title: "arista.eos.eos_lacp module – LACP resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_lacp_module.html
fetched_at: 2026-07-28T01:11:04+00:00
---
# arista.eos.eos_lacp module – LACP resource module

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
> To use it in a playbook, specify: `arista.eos.eos_lacp`.

New in arista.eos 1.0.0

- [Synopsis](eos_lacp_module.md#synopsis)
- [Parameters](eos_lacp_module.md#parameters)
- [Notes](eos_lacp_module.md#notes)
- [Examples](eos_lacp_module.md#examples)
- [Return Values](eos_lacp_module.md#return-values)

## [Synopsis](eos_lacp_module.md#id1)

- This module manages Global Link Aggregation Control Protocol (LACP) on Arista EOS devices.

Aliases: lacp

## [Parameters](eos_lacp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | LACP global options. |
| **system**  dictionary | LACP system options. |
| **priority**  integer | The system priority to use in LACP negotiations.  Lower value is higher priority.  Refer to vendor documentation for valid values. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ^lacp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](eos_lacp_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_lacp_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# veos# show running-config | include lacp
# lacp system-priority 10

- name: Merge provided global LACP attributes with device attributes
  arista.eos.eos_lacp:
    config:
      system:
        priority: 20
    state: merged

# After state:
# ------------
# veos# show running-config | include lacp
# lacp system-priority 20
#

# Using replaced

# Before state:
# -------------
# veos# show running-config | include lacp
# lacp system-priority 10

- name: Replace device global LACP attributes with provided attributes
  arista.eos.eos_lacp:
    config:
      system:
        priority: 20
    state: replaced

# After state:
# ------------
# veos# show running-config | include lacp
# lacp system-priority 20
#

# Using deleted

# Before state:
# -------------
# veos# show running-config | include lacp
# lacp system-priority 10

- name: Delete global LACP attributes
  arista.eos.eos_lacp:
    state: deleted

# After state:
# ------------
# veos# show running-config | include lacp
#

# Using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lacp:
    config:
      system:
        priority: 20
    state: rendered

# Output:
# ------------
# rendered:
#   - "lacp system-priority 20"
#

# Using parsed:

# parsed.cfg
# lacp system-priority 20

- name: Use parsed to convert native configs to structured data
  arista.eos.eos_lacp:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output:
# parsed:
#   system:
#     priority: 20

# Using gathered:
# nathive config:
# -------------
# lacp system-priority 10

- name: Gather lacp facts from the device
  arista.eos.eos_lacp:
    state: gathered

# Output:
# gathered:
#   system:
#     priority: 10
#
```

## [Return Values](eos_lacp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["lacp system-priority 10"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
