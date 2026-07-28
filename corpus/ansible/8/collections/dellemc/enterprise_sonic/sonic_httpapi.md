---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic httpapi – HttpApi Plugin for devices supporting Restconf SONIC API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_httpapi.html
fetched_at: 2026-07-28T02:03:56+00:00
---
# dellemc.enterprise_sonic.sonic httpapi – HttpApi Plugin for devices supporting Restconf SONIC API

> **Note:**
>
> This httpapi plugin is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_httpapi.md#synopsis)
- [Parameters](sonic_httpapi.md#parameters)

## [Synopsis](sonic_httpapi.md#id1)

- This HttpApi plugin provides methods to connect to Restconf SONIC API endpoints.

## [Parameters](sonic_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **root_path**  string | Specifies the location of the Restconf root.  **Default:** `"/restconf"`  **Configuration:**   - Variable: ansible_httpapi_restconf_root |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
