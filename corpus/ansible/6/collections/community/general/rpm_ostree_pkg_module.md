---
collection: ansible
version: "6"
title: "community.general.rpm_ostree_pkg module – Install or uninstall overlay additional packages"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rpm_ostree_pkg_module.html
fetched_at: 2026-07-27T17:12:47+00:00
---
# community.general.rpm_ostree_pkg module – Install or uninstall overlay additional packages

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
> To use it in a playbook, specify: `community.general.rpm_ostree_pkg`.

New in community.general 2.0.0

- [Synopsis](rpm_ostree_pkg_module.md#synopsis)
- [Parameters](rpm_ostree_pkg_module.md#parameters)
- [Notes](rpm_ostree_pkg_module.md#notes)
- [Examples](rpm_ostree_pkg_module.md#examples)
- [Return Values](rpm_ostree_pkg_module.md#return-values)

## [Synopsis](rpm_ostree_pkg_module.md#id1)

- Install or uninstall overlay additional packages using `rpm-ostree` command.

## [Parameters](rpm_ostree_pkg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pkg  list / elements=string / required | Name of overlay package to install or remove. |
| **state**  string | State of the overlay package.  `present` simply ensures that a desired package is installed.  `absent` removes the specified package.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](rpm_ostree_pkg_module.md#id3)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](rpm_ostree_pkg_module.md#id4)

```yaml+jinja
- name: Install overlay package
  community.general.rpm_ostree_pkg:
    name: nfs-utils
    state: present

- name: Remove overlay package
  community.general.rpm_ostree_pkg:
    name: nfs-utils
    state: absent
```

## [Return Values](rpm_ostree_pkg_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **action**  string | Action performed.  Returned: always  Sample: `"install"` |
| **changed**  boolean | State changes.  Returned: always  Sample: `true` |
| **cmd**  string | Full command used for performed action.  Returned: always  Sample: `"rpm-ostree uninstall --allow-inactive --idempotent --unchanged-exit-77 nfs-utils"` |
| **packages**  list / elements=string | A list of packages specified.  Returned: always  Sample: `["nfs-utils"]` |
| **rc**  integer | Return code of rpm-ostree command.  Returned: always  Sample: `0` |
| **stderr**  string | Stderr of rpm-ostree command.  Returned: always  Sample: `""` |
| **stdout**  string | Stdout of rpm-ostree command.  Returned: always  Sample: `"Staging deployment...done\\n..."` |

### Authors

- Dusty Mabe (@dustymabe)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
