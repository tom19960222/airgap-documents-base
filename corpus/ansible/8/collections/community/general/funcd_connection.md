---
collection: ansible
version: "8"
title: "community.general.funcd connection – Use funcd to connect to target"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/funcd_connection.html
fetched_at: 2026-07-28T01:52:10+00:00
---
# community.general.funcd connection – Use funcd to connect to target

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
> To use it in a playbook, specify: `community.general.funcd`.

- [Synopsis](funcd_connection.md#synopsis)
- [Parameters](funcd_connection.md#parameters)

## [Synopsis](funcd_connection.md#id1)

- This transport permits you to use Ansible over Func.
- For people who have already setup func and that wish to play with ansible, this permit to move gradually to ansible without having to redo completely the setup of the network.

## [Parameters](funcd_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **remote_addr**  string | The path of the chroot you want to access.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: ansible_host - Variable: ansible_func_host |

### Authors

- Michael Scherer (@mscherer)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
