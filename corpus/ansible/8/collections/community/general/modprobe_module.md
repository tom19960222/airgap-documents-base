---
collection: ansible
version: "8"
title: "community.general.modprobe module – Load or unload kernel modules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/modprobe_module.html
fetched_at: 2026-07-28T01:48:01+00:00
---
# community.general.modprobe module – Load or unload kernel modules

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
> To use it in a playbook, specify: `community.general.modprobe`.

- [Synopsis](modprobe_module.md#synopsis)
- [Parameters](modprobe_module.md#parameters)
- [Attributes](modprobe_module.md#attributes)
- [Examples](modprobe_module.md#examples)

## [Synopsis](modprobe_module.md#id1)

- Load or unload kernel modules.

Aliases: system.modprobe

## [Parameters](modprobe_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of kernel module to manage. |
| **params**  string | Modules parameters.  **Default:** `""` |
| **persistent**  string | Persistency between reboots for configured module.  This option creates files in `/etc/modules-load.d/` and `/etc/modprobe.d/` that make your module configuration persistent during reboots.  If `present`, adds module name to `/etc/modules-load.d/` and params to `/etc/modprobe.d/` so the module will be loaded on next reboot.  If `absent`, will comment out module name from `/etc/modules-load.d/` and comment out params from `/etc/modprobe.d/` so the module will not be loaded on next reboot.  If `disabled`, will not touch anything and leave `/etc/modules-load.d/` and `/etc/modprobe.d/` as it is.  Note that it is usually a better idea to rely on the automatic module loading by PCI IDs, USB IDs, DMI IDs or similar triggers encoded in the kernel modules themselves instead of configuration like this.  In fact, most modern kernel modules are prepared for automatic loading already.  **Note:** This option works only with distributions that use `systemd` when set to values other than `disabled`.  **Choices:**   - `"disabled"` ← (default) - `"absent"` - `"present"` |
| **state**  string | Whether the module should be present or absent.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](modprobe_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](modprobe_module.md#id4)

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

- name: Add the dummy module and make sure it is loaded after reboots
  community.general.modprobe:
    name: dummy
    state: present
    params: 'numdummies=2'
    persistent: present
```

### Authors

- David Stygstra (@stygstra)
- Julien Dauphant (@jdauphant)
- Matt Jeffery (@mattjeffery)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
