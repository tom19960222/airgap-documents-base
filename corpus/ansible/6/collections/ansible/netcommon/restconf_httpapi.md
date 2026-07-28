---
collection: ansible
version: "6"
title: "ansible.netcommon.restconf httpapi – HttpApi Plugin for devices supporting Restconf API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/restconf_httpapi.html
fetched_at: 2026-07-27T16:44:40+00:00
---
# ansible.netcommon.restconf httpapi – HttpApi Plugin for devices supporting Restconf API

> **Note:**
>
> This httpapi plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.restconf`.

New in ansible.netcommon 1.0.0

- [Synopsis](restconf_httpapi.md#synopsis)
- [Parameters](restconf_httpapi.md#parameters)

## [Synopsis](restconf_httpapi.md#id1)

- This HttpApi plugin provides methods to connect to Restconf API endpoints.

## [Parameters](restconf_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **root_path**  string | Specifies the location of the Restconf root.  Default: `"/restconf"`  Configuration:   - Variable: ansible_httpapi_restconf_root |

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
