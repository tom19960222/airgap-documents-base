---
collection: ansible
version: "6"
title: "community.general.lxc connection – Run tasks in lxc containers via lxc python library"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lxc_connection.html
fetched_at: 2026-07-27T17:14:43+00:00
---
# community.general.lxc connection – Run tasks in lxc containers via lxc python library

> **Note:**
>
> This connection plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.lxc`.

- [Synopsis](lxc_connection.md#synopsis)
- [Parameters](lxc_connection.md#parameters)

## [Synopsis](lxc_connection.md#id1)

- Run commands or put/fetch files to an existing lxc container using lxc python library

## [Parameters](lxc_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Shell executable  Default: `"/bin/sh"`  Configuration:   - Variable: ansible_executable - Variable: ansible_lxc_executable |
| **remote_addr**  string | Container identifier  Default: `"inventory_hostname"`  Configuration:   - Variable: ansible_host - Variable: ansible_lxc_host |

### Authors

- Joerg Thalheim

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
