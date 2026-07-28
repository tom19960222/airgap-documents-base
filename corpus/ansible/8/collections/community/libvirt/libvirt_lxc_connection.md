---
collection: ansible
version: "8"
title: "community.libvirt.libvirt_lxc connection – Run tasks in lxc containers via libvirt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/libvirt/libvirt_lxc_connection.html
fetched_at: 2026-07-28T01:53:53+00:00
---
# community.libvirt.libvirt_lxc connection – Run tasks in lxc containers via libvirt

> **Note:**
>
> This connection plugin is part of the [community.libvirt collection](https://galaxy.ansible.com/ui/repo/published/community/libvirt/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.libvirt`.
>
> To use it in a playbook, specify: `community.libvirt.libvirt_lxc`.

- [Synopsis](libvirt_lxc_connection.md#synopsis)
- [Parameters](libvirt_lxc_connection.md#parameters)

## [Synopsis](libvirt_lxc_connection.md#id1)

- Run commands or put/fetch files to an existing lxc container using libvirt.

## [Parameters](libvirt_lxc_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **remote_addr**  string | Container identifier.  **Default:** `"The set user as per docker's configuration"`  **Configuration:**   - Variable: ansible_host - Variable: ansible_libvirt_lxc_host |

### Authors

- Michael Scherer (@mscherer)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.libvirt/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.libvirt)
