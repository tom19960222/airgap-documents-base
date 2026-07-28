---
collection: ansible
version: "8"
title: "community.general.opkg module – Package manager for OpenWrt and Openembedded/Yocto based Linux distributions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/opkg_module.html
fetched_at: 2026-07-28T01:48:44+00:00
---
# community.general.opkg module – Package manager for OpenWrt and Openembedded/Yocto based Linux distributions

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
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
- [Attributes](opkg_module.md#attributes)
- [Examples](opkg_module.md#examples)

## [Synopsis](opkg_module.md#id1)

- Manages ipk packages for OpenWrt and Openembedded/Yocto based Linux distributions

Aliases: packaging.os.opkg

## [Requirements](opkg_module.md#id2)

The below requirements are needed on the host that executes this module.

- opkg
- python

## [Parameters](opkg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  path  *added in community.general 7.2.0* | The executable location for `opkg`. |
| **force**  string | The `opkg --force` parameter used.  Passing `""` as value and not passing any value at all have both the same effect of **not** using any `--force-` parameter.  **Choices:**   - `""` - `"depends"` - `"maintainer"` - `"reinstall"` - `"overwrite"` - `"downgrade"` - `"space"` - `"postinstall"` - `"remove"` - `"checksum"` - `"removal-of-dependent-packages"` |
| **name**  aliases: pkg  list / elements=string / required | Name of package(s) to install/remove.  `NAME=VERSION` syntax is also supported to install a package in a certain version. See the examples. This only works on Yocto based Linux distributions (opkg>=0.3.2) and not for OpenWrt. This is supported since community.general 6.2.0. |
| **state**  string | State of the package.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"installed"` - `"removed"` |
| **update_cache**  boolean | Update the package DB first.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](opkg_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](opkg_module.md#id5)

```yaml+jinja
- name: Install foo
  community.general.opkg:
    name: foo
    state: present

- name: Install foo in version 1.2 (opkg>=0.3.2 on Yocto based Linux distributions)
  community.general.opkg:
    name: foo=1.2
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

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
