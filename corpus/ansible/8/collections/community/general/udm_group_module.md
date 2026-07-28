---
collection: ansible
version: "8"
title: "community.general.udm_group module – Manage of the posix group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/udm_group_module.html
fetched_at: 2026-07-28T01:51:02+00:00
---
# community.general.udm_group module – Manage of the posix group

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
> To use it in a playbook, specify: `community.general.udm_group`.

- [Synopsis](udm_group_module.md#synopsis)
- [Parameters](udm_group_module.md#parameters)
- [Attributes](udm_group_module.md#attributes)
- [Examples](udm_group_module.md#examples)

## [Synopsis](udm_group_module.md#id1)

- This module allows to manage user groups on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

Aliases: cloud.univention.udm_group

## [Parameters](udm_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Group description. |
| **name**  string / required | Name of the posix group. |
| **ou**  string | LDAP OU, e.g. school for LDAP OU `ou=school,dc=example,dc=com`.  **Default:** `""` |
| **position**  string | define the whole ldap position of the group, e.g. `cn=g123m-1A,cn=classes,cn=schueler,cn=groups,ou=schule,dc=example,dc=com`.  **Default:** `""` |
| **state**  string | Whether the group is present or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subpath**  string | Subpath inside the OU, e.g. `cn=classes,cn=students,cn=groups`.  **Default:** `"cn=groups"` |

## [Attributes](udm_group_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **partial** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](udm_group_module.md#id4)

```yaml+jinja
- name: Create a POSIX group
  community.general.udm_group:
    name: g123m-1A

# Create a POSIX group with the exact DN
# C(cn=g123m-1A,cn=classes,cn=students,cn=groups,ou=school,dc=school,dc=example,dc=com)
- name: Create a POSIX group with a DN
  community.general.udm_group:
    name: g123m-1A
    subpath: 'cn=classes,cn=students,cn=groups'
    ou: school

# or
- name: Create a POSIX group with a DN
  community.general.udm_group:
    name: g123m-1A
    position: 'cn=classes,cn=students,cn=groups,ou=school,dc=school,dc=example,dc=com'
```

### Authors

- Tobias Rüetschi (@keachi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
