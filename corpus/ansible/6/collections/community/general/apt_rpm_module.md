---
collection: ansible
version: "6"
title: "community.general.apt_rpm module – APT-RPM package manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/apt_rpm_module.html
fetched_at: 2026-07-27T17:08:09+00:00
---
# community.general.apt_rpm module – APT-RPM package manager

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
> To use it in a playbook, specify: `community.general.apt_rpm`.

- [Synopsis](apt_rpm_module.md#synopsis)
- [Parameters](apt_rpm_module.md#parameters)
- [Examples](apt_rpm_module.md#examples)

## [Synopsis](apt_rpm_module.md#id1)

- Manages packages with *apt-rpm*. Both low-level (*rpm*) and high-level (*apt-get*) package manager binaries required.

## [Parameters](apt_rpm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **package**  aliases: name, pkg  list / elements=string / required | list of packages to install, upgrade or remove. |
| **state**  string | Indicates the desired package state.  Choices:   - `"absent"` - `"present"` ← (default) - `"installed"` - `"removed"` |
| **update_cache**  boolean | update the package database first `apt-get update`.  Choices:   - `false` ← (default) - `true` |

## [Examples](apt_rpm_module.md#id3)

```yaml+jinja
- name: Install package foo
  community.general.apt_rpm:
    pkg: foo
    state: present

- name: Install packages foo and bar
  community.general.apt_rpm:
    pkg:
      - foo
      - bar
    state: present

- name: Remove package foo
  community.general.apt_rpm:
    pkg: foo
    state: absent

- name: Remove packages foo and bar
  community.general.apt_rpm:
    pkg: foo,bar
    state: absent

# bar will be the updated if a newer version exists
- name: Update the package database and install bar
  community.general.apt_rpm:
    name: bar
    state: present
    update_cache: true
```

### Authors

- Evgenii Terechkov (@evgkrsk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
