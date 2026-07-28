---
collection: ansible
version: "6"
title: "community.general.opkg module – Package manager for OpenWrt"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/opkg_module.html
fetched_at: 2026-07-27T17:11:36+00:00
---
# community.general.opkg module – Package manager for OpenWrt

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
> see [Requirements](opkg_module.md#ansible-collections-community-general-opkg-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.opkg`.

- [Synopsis](opkg_module.md#synopsis)
- [Requirements](opkg_module.md#requirements)
- [Parameters](opkg_module.md#parameters)
- [Examples](opkg_module.md#examples)

## [Synopsis](opkg_module.md#id1)

- Manages OpenWrt packages

## [Requirements](opkg_module.md#id2)

The below requirements are needed on the host that executes this module.

- opkg
- python

## [Parameters](opkg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  string | The `opkg --force` parameter used.  Choices:   - `""` ← (default) - `"depends"` - `"maintainer"` - `"reinstall"` - `"overwrite"` - `"downgrade"` - `"space"` - `"postinstall"` - `"remove"` - `"checksum"` - `"removal-of-dependent-packages"` |
| **name**  aliases: pkg  list / elements=string / required | Name of package(s) to install/remove. |
| **state**  string | State of the package.  Choices:   - `"present"` ← (default) - `"absent"` - `"installed"` - `"removed"` |
| **update_cache**  boolean | Update the package DB first.  Choices:   - `false` ← (default) - `true` |

## [Examples](opkg_module.md#id4)

```yaml+jinja
- name: Install foo
  community.general.opkg:
    name: foo
    state: present

- name: Update cache and install foo
  community.general.opkg:
    name: foo
    state: present
    update_cache: true

- name: Remove foo
  community.general.opkg:
    name: foo
    state: absent

- name: Remove foo and bar
  community.general.opkg:
    name:
      - foo
      - bar
    state: absent

- name: Install foo using overwrite option forcibly
  community.general.opkg:
    name: foo
    state: present
    force: overwrite
```

### Authors

- Patrick Pelletier (@skinp)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
