---
collection: ansible
version: "8"
title: "community.general.snap_alias module – Manages snap aliases"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/snap_alias_module.html
fetched_at: 2026-07-28T01:50:40+00:00
---
# community.general.snap_alias module – Manages snap aliases

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.snap_alias`.

New in community.general 4.0.0

- [Synopsis](snap_alias_module.md#synopsis)
- [Parameters](snap_alias_module.md#parameters)
- [Attributes](snap_alias_module.md#attributes)
- [See Also](snap_alias_module.md#see-also)
- [Examples](snap_alias_module.md#examples)
- [Return Values](snap_alias_module.md#return-values)

## [Synopsis](snap_alias_module.md#id1)

- Manages snaps aliases.

Aliases: packaging.os.snap_alias

## [Parameters](snap_alias_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alias**  aliases: aliases  list / elements=string | Aliases to be created or removed. |
| **name**  string | Name of the snap. |
| **state**  string | Desired state of the alias.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](snap_alias_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](snap_alias_module.md#id4)

> **See also:**
>
> [community.general.snap](snap_module.md#ansible-collections-community-general-snap-module)
> :   Manages snaps.

## [Examples](snap_alias_module.md#id5)

```yaml+jinja
# Install "foo" and "bar" snap
- name: Create snap alias
  community.general.snap_alias:
    name: hello-world
    alias: hw

- name: Create multiple aliases
  community.general.snap_alias:
    name: hello-world
    aliases:
      - hw
      - hw2
      - hw3
    state: present   # optional

- name: Remove one specific aliases
  community.general.snap_alias:
    name: hw
    state: absent

- name: Remove all aliases for snap
  community.general.snap_alias:
    name: hello-world
    state: absent
```

## [Return Values](snap_alias_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snap_aliases**  list / elements=string | The snap aliases after execution. If called in check mode, then the list represents the state before execution.  **Returned:** always |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
