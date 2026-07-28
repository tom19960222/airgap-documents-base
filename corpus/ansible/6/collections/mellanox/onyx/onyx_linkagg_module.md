---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_linkagg module – Manage link aggregation groups on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_linkagg_module.html
fetched_at: 2026-07-27T17:55:30+00:00
---
# mellanox.onyx.onyx_linkagg module – Manage link aggregation groups on Mellanox ONYX network devices

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_linkagg`.

- [Synopsis](onyx_linkagg_module.md#synopsis)
- [Parameters](onyx_linkagg_module.md#parameters)
- [Examples](onyx_linkagg_module.md#examples)
- [Return Values](onyx_linkagg_module.md#return-values)

## [Synopsis](onyx_linkagg_module.md#id1)

- This module provides declarative management of link aggregation groups on Mellanox ONYX network devices.

## [Parameters](onyx_linkagg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of link aggregation definitions. |
| **members**  string / required | List of members interfaces of the link aggregation group. The value can be single interface or list of interfaces. |
| **mode**  string | Mode of the link aggregation group. A value of `on` will enable LACP. `active` configures the link to actively information about the state of the link, or it can be configured in `passive` mode ie. send link state information only when received them from another link.  Choices:   - `"on"` - `"active"` - `"passive"`   Default: `true` |
| **name**  string / required | Name of the link aggregation group. |
| **purge**  boolean | Purge link aggregation groups not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |

## [Examples](onyx_linkagg_module.md#id3)

```yaml+jinja
- name: Configure link aggregation group
  onyx_linkagg:
    name: Po1
    members:
      - Eth1/1
      - Eth1/2

- name: Remove configuration
  onyx_linkagg:
    name: Po1
    state: absent

- name: Create aggregate of linkagg definitions
  onyx_linkagg:
    aggregate:
        - { name: Po1, members: [Eth1/1] }
        - { name: Po2, members: [Eth1/2] }

- name: Remove aggregate of linkagg definitions
  onyx_linkagg:
    aggregate:
      - name: Po1
      - name: Po2
    state: absent
```

## [Return Values](onyx_linkagg_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["interface port-channel 1", "exit", "interface ethernet 1/1 channel-group 1 mode on", "interface ethernet 1/2 channel-group 1 mode on"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
