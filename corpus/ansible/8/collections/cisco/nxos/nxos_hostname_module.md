---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_hostname module – Hostname resource module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_hostname_module.html
fetched_at: 2026-07-28T01:38:41+00:00
---
# cisco.nxos.nxos_hostname module – Hostname resource module.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_hostname`.

New in cisco.nxos 2.9.0

- [Synopsis](nxos_hostname_module.md#synopsis)
- [Parameters](nxos_hostname_module.md#parameters)
- [Notes](nxos_hostname_module.md#notes)
- [Examples](nxos_hostname_module.md#examples)
- [Return Values](nxos_hostname_module.md#return-values)

## [Synopsis](nxos_hostname_module.md#id1)

- This module manages hostname configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: hostname

## [Parameters](nxos_hostname_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of hostname configuration. |
| **hostname**  string | Hostname of the device. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section hostname**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *merged*, *replaced* and *overridden* have identical behaviour for this module.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_hostname_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6.
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_hostname_module.md#id4)

```yaml+jinja
# Using merged (replaced, overridden has the same behaviour)

# Before state:
# -------------
# nxos-9k-rdo# show running-config | section ^hostname
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_hostname:
    config:
      hostname: NXOSv-9k

# Task output
# -------------
# before: {}
#
# commands:
#   - hostname NXOSv-9k
#
# after:
#   hostname: NXOSv-9k

# After state:
# ------------
# nxos-9k-rdo# show running-config | section ^hostname
# hostname NXOSv-9k
#

# Using deleted

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section ^hostname
# hostname NXOSv-9k

- name: Delete hostname from running-config
  cisco.nxos.nxos_hostname:
    state: deleted

# Task output
# -------------
# before:
#   hostname: NXOSv-9k
#
# commands:
#   - no hostname NXOSv-9k
#
# after: {}

# Using gathered

- name: Gather hostname facts using gathered
  cisco.nxos.nxos_hostname:
    state: gathered

# Task output (redacted)
# -----------------------
#  gathered:
#    hostname: NXOSv-9k

# Using rendered

- name: Render platform specific configuration lines (without connecting to the device)
  cisco.nxos.nxos_hostname:
    config:
      hostname: NXOSv-9k

# Task Output (redacted)
# -----------------------
# rendered:
#   - hostname NXOSv-9k

# Using parsed

# parsed.cfg
# ------------
# hostname NXOSv-9k

- name: Parse externally provided hostname config
  cisco.nxos.nxos_hostname:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#   hostname: NXOSv-9k
```

## [Return Values](nxos_hostname_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["hostname switch01"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["hostname switch01"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
