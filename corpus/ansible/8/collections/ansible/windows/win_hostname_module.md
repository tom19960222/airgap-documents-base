---
collection: ansible
version: "8"
title: "ansible.windows.win_hostname module – Manages local Windows computer name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_hostname_module.html
fetched_at: 2026-07-28T01:10:40+00:00
---
# ansible.windows.win_hostname module – Manages local Windows computer name

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_hostname`.

- [Synopsis](win_hostname_module.md#synopsis)
- [Parameters](win_hostname_module.md#parameters)
- [See Also](win_hostname_module.md#see-also)
- [Examples](win_hostname_module.md#examples)
- [Return Values](win_hostname_module.md#return-values)

## [Synopsis](win_hostname_module.md#id1)

- Manages local Windows computer name.
- A reboot is required for the computer name to take effect.

## [Parameters](win_hostname_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | The hostname to set for the computer. |

## [See Also](win_hostname_module.md#id3)

> **See also:**
>
> [ansible.windows.win_dns_client](win_dns_client_module.md#ansible-collections-ansible-windows-win-dns-client-module)
> :   Configures DNS lookup on Windows hosts.

## [Examples](win_hostname_module.md#id4)

```yaml+jinja
- name: Change the hostname to sample-hostname
  ansible.windows.win_hostname:
    name: sample-hostname
  register: res

- name: Reboot
  ansible.windows.win_reboot:
  when: res.reboot_required
```

## [Return Values](win_hostname_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **old_name**  string | The original hostname that was set before it was changed.  **Returned:** always  **Sample:** `"old_hostname"` |
| **reboot_required**  boolean | Whether a reboot is required to complete the hostname change.  **Returned:** always  **Sample:** `true` |

### Authors

- Ripon Banik (@riponbanik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
