---
collection: ansible
version: "6"
title: "community.general.modprobe module – Load or unload kernel modules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/modprobe_module.html
fetched_at: 2026-07-27T17:10:59+00:00
---
# community.general.modprobe module – Load or unload kernel modules

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
> To use it in a playbook, specify: `community.general.modprobe`.

- [Synopsis](modprobe_module.md#synopsis)
- [Parameters](modprobe_module.md#parameters)
- [Examples](modprobe_module.md#examples)

## [Synopsis](modprobe_module.md#id1)

- Load or unload kernel modules.

## [Parameters](modprobe_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of kernel module to manage. |
| **params**  string | Modules parameters.  Default: `""` |
| **state**  string | Whether the module should be present or absent.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](modprobe_module.md#id3)

```yaml+jinja
- name: Add the 802.1q module
  community.general.modprobe:
    name: 8021q
    state: present

- name: Add the dummy module
  community.general.modprobe:
    name: dummy
    state: present
    params: 'numdummies=2'
```

### Authors

- David Stygstra (@stygstra)
- Julien Dauphant (@jdauphant)
- Matt Jeffery (@mattjeffery)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
