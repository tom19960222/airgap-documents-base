---
collection: ansible
version: "6"
title: "community.general.kernel_blacklist module – Blacklist kernel modules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/kernel_blacklist_module.html
fetched_at: 2026-07-27T17:10:15+00:00
---
# community.general.kernel_blacklist module – Blacklist kernel modules

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
> To use it in a playbook, specify: `community.general.kernel_blacklist`.

- [Synopsis](kernel_blacklist_module.md#synopsis)
- [Parameters](kernel_blacklist_module.md#parameters)
- [Examples](kernel_blacklist_module.md#examples)

## [Synopsis](kernel_blacklist_module.md#id1)

- Add or remove kernel modules from blacklist.

## [Parameters](kernel_blacklist_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **blacklist_file**  string | If specified, use this blacklist file instead of `/etc/modprobe.d/blacklist-ansible.conf`.  Default: `"/etc/modprobe.d/blacklist-ansible.conf"` |
| **name**  string / required | Name of kernel module to black- or whitelist. |
| **state**  string | Whether the module should be present in the blacklist or absent.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Examples](kernel_blacklist_module.md#id3)

```yaml+jinja
- name: Blacklist the nouveau driver module
  community.general.kernel_blacklist:
    name: nouveau
    state: present
```

### Authors

- Matthias Vogelgesang (@matze)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
