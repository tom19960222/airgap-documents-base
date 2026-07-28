---
collection: ansible
version: "8"
title: "ansible.posix.seboolean module – Toggles SELinux booleans"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/seboolean_module.html
fetched_at: 2026-07-28T01:09:31+00:00
---
# ansible.posix.seboolean module – Toggles SELinux booleans

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](seboolean_module.md#ansible-collections-ansible-posix-seboolean-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.seboolean`.

New in ansible.posix 1.0.0

- [Synopsis](seboolean_module.md#synopsis)
- [Requirements](seboolean_module.md#requirements)
- [Parameters](seboolean_module.md#parameters)
- [Notes](seboolean_module.md#notes)
- [Examples](seboolean_module.md#examples)

## [Synopsis](seboolean_module.md#id1)

- Toggles SELinux booleans.

## [Requirements](seboolean_module.md#id2)

The below requirements are needed on the host that executes this module.

- libselinux-python
- libsemanage-python
- python3-libsemanage

## [Parameters](seboolean_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ignore_selinux_state**  boolean | Useful for scenarios (chrooted environment) that you can’t get the real SELinux state.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the boolean to configure. |
| **persistent**  boolean | Set to `true` if the boolean setting should survive a reboot.  **Choices:**   - `false` ← (default) - `true` |
| **state**  boolean / required | Desired boolean value  **Choices:**   - `false` - `true` |

## [Notes](seboolean_module.md#id4)

> **Note:**
>
> - Not tested on any Debian based system.

## [Examples](seboolean_module.md#id5)

```yaml+jinja
- name: Set httpd_can_network_connect flag on and keep it persistent across reboots
  ansible.posix.seboolean:
    name: httpd_can_network_connect
    state: true
    persistent: true
```

### Authors

- Stephen Fromm (@sfromm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
