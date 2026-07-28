---
collection: ansible
version: "6"
title: "community.general.urpmi module – Urpmi manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/urpmi_module.html
fetched_at: 2026-07-27T17:13:42+00:00
---
# community.general.urpmi module – Urpmi manager

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
> To use it in a playbook, specify: `community.general.urpmi`.

- [Synopsis](urpmi_module.md#synopsis)
- [Parameters](urpmi_module.md#parameters)
- [Examples](urpmi_module.md#examples)

## [Synopsis](urpmi_module.md#id1)

- Manages packages with *urpmi* (such as for Mageia or Mandriva)

## [Parameters](urpmi_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Assume “yes” is the answer to any question urpmi has to ask. Corresponds to the `--force` option for *urpmi*.  Choices:   - `false` - `true` ← (default) |
| **name**  aliases: package, pkg  list / elements=string / required | A list of package names to install, upgrade or remove. |
| **no_recommends**  boolean | Corresponds to the `--no-recommends` option for *urpmi*.  Choices:   - `false` - `true` ← (default) |
| **root**  aliases: installroot  string | Specifies an alternative install root, relative to which all packages will be installed. Corresponds to the `--root` option for *urpmi*. |
| **state**  string | Indicates the desired package state.  Choices:   - `"absent"` - `"present"` ← (default) - `"installed"` - `"removed"` |
| **update_cache**  boolean | Update the package database first `urpmi.update -a`.  Choices:   - `false` ← (default) - `true` |

## [Examples](urpmi_module.md#id3)

```yaml+jinja
- name: Install package foo
  community.general.urpmi:
    pkg: foo
    state: present

- name: Remove package foo
  community.general.urpmi:
    pkg: foo
    state: absent

- name: Remove packages foo and bar
  community.general.urpmi:
    pkg: foo,bar
    state: absent

- name: Update the package database (urpmi.update -a -q) and install bar (bar will be the updated if a newer version exists)
- community.general.urpmi:
    name: bar
    state: present
    update_cache: true
```

### Authors

- Philippe Makowski (@pmakowski)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
