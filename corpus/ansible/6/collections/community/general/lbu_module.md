---
collection: ansible
version: "6"
title: "community.general.lbu module – Local Backup Utility for Alpine Linux"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lbu_module.html
fetched_at: 2026-07-27T17:10:27+00:00
---
# community.general.lbu module – Local Backup Utility for Alpine Linux

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.lbu`.

New in community.general 0.2.0

- [Synopsis](lbu_module.md#synopsis)
- [Parameters](lbu_module.md#parameters)
- [Examples](lbu_module.md#examples)
- [Return Values](lbu_module.md#return-values)

## [Synopsis](lbu_module.md#id1)

- Manage Local Backup Utility of Alpine Linux in run-from-RAM mode

## [Parameters](lbu_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commit**  boolean | Control whether to commit changed files.  Choices:   - `false` - `true` |
| **exclude**  list / elements=string | List of paths to exclude. |
| **include**  list / elements=string | List of paths to include. |

## [Examples](lbu_module.md#id3)

```yaml+jinja
# Commit changed files (if any)
- name: Commit
  community.general.lbu:
    commit: true

# Exclude path and commit
- name: Exclude directory
  community.general.lbu:
    commit: true
    exclude:
    - /etc/opt

# Include paths without committing
- name: Include file and directory
  community.general.lbu:
    include:
    - /root/.ssh/authorized_keys
    - /var/lib/misc
```

## [Return Values](lbu_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Error message  Returned: on failure |

### Authors

- Kaarle Ritvanen (@kunkku)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
