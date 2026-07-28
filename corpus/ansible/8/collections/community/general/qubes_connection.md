---
collection: ansible
version: "8"
title: "community.general.qubes connection – Interact with an existing QubesOS AppVM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/qubes_connection.html
fetched_at: 2026-07-28T01:52:13+00:00
---
# community.general.qubes connection – Interact with an existing QubesOS AppVM

> **Note:**
>
> This connection plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.qubes`.

- [Synopsis](qubes_connection.md#synopsis)
- [Parameters](qubes_connection.md#parameters)

## [Synopsis](qubes_connection.md#id1)

- Run commands or put/fetch files to an existing Qubes AppVM using qubes tools.

## [Parameters](qubes_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **remote_addr**  string | vm name  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: ansible_host |
| **remote_user**  string | The user to execute as inside the vm.  **Default:** `"The *user* account as default in Qubes OS."`  **Configuration:**   - Variable: ansible_user |

### Authors

- Kushal Das (@kushaldas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
