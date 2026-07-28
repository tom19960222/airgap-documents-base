---
collection: ansible
version: "8"
title: "community.windows.win_snmp module – Configures the Windows SNMP service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_snmp_module.html
fetched_at: 2026-07-28T02:02:30+00:00
---
# community.windows.win_snmp module – Configures the Windows SNMP service

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_snmp`.

- [Synopsis](win_snmp_module.md#synopsis)
- [Parameters](win_snmp_module.md#parameters)
- [Examples](win_snmp_module.md#examples)
- [Return Values](win_snmp_module.md#return-values)

## [Synopsis](win_snmp_module.md#id1)

- This module configures the Windows SNMP service.

## [Parameters](win_snmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | `add` will add new SNMP community strings and/or SNMP managers  `set` will replace SNMP community strings and/or SNMP managers. An empty list for either `community_strings` or `permitted_managers` will result in the respective lists being removed entirely.  `remove` will remove SNMP community strings and/or SNMP managers  **Choices:**   - `"add"` - `"set"` ← (default) - `"remove"` |
| **community_strings**  list / elements=string | The list of read-only SNMP community strings. |
| **permitted_managers**  list / elements=string | The list of permitted SNMP managers. |

## [Examples](win_snmp_module.md#id3)

```yaml+jinja
- name: Replace SNMP communities and managers
  community.windows.win_snmp:
    community_strings:
    - public
    permitted_managers:
    - 192.168.1.2
    action: set

- name: Replace SNMP communities and clear managers
  community.windows.win_snmp:
    community_strings:
    - public
    permitted_managers: []
    action: set
```

## [Return Values](win_snmp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **community_strings**  list / elements=string | The list of community strings for this machine.  **Returned:** always  **Sample:** `["public", "snmp-ro"]` |
| **permitted_managers**  list / elements=string | The list of permitted managers for this machine.  **Returned:** always  **Sample:** `["192.168.1.1", "192.168.1.2"]` |

### Authors

- Michael Cassaniti (@mcassaniti)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
