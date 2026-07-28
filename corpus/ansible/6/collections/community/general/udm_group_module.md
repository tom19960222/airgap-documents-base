---
collection: ansible
version: "6"
title: "community.general.udm_group module – Manage of the posix group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/udm_group_module.html
fetched_at: 2026-07-27T17:13:39+00:00
---
# community.general.udm_group module – Manage of the posix group

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](udm_group_module.md#ansible-collections-community-general-udm-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.udm_group`.

- [Synopsis](udm_group_module.md#synopsis)
- [Requirements](udm_group_module.md#requirements)
- [Parameters](udm_group_module.md#parameters)
- [Examples](udm_group_module.md#examples)

## [Synopsis](udm_group_module.md#id1)

- This module allows to manage user groups on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

## [Requirements](udm_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python >= 2.6

## [Parameters](udm_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Group description. |
| **name**  string / required | Name of the posix group. |
| **ou**  string | LDAP OU, e.g. school for LDAP OU `ou=school,dc=example,dc=com`.  Default: `""` |
| **position**  string | define the whole ldap position of the group, e.g. `cn=g123m-1A,cn=classes,cn=schueler,cn=groups,ou=schule,dc=example,dc=com`.  Default: `""` |
| **state**  string | Whether the group is present or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subpath**  string | Subpath inside the OU, e.g. `cn=classes,cn=students,cn=groups`.  Default: `"cn=groups"` |

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
