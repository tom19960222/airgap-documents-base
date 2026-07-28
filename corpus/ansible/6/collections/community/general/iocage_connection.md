---
collection: ansible
version: "6"
title: "community.general.iocage connection – Run tasks in iocage jails"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/iocage_connection.html
fetched_at: 2026-07-27T17:14:41+00:00
---
# community.general.iocage connection – Run tasks in iocage jails

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
> To use it in a playbook, specify: `community.general.iocage`.

- [Synopsis](iocage_connection.md#synopsis)
- [Parameters](iocage_connection.md#parameters)

## [Synopsis](iocage_connection.md#id1)

- Run commands or put/fetch files to an existing iocage jail

## [Parameters](iocage_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **remote_addr**  string | Path to the jail  Configuration:   - Variable: ansible_host - Variable: ansible_iocage_host |
| **remote_user**  string | User to execute as inside the jail  Configuration:   - Variable: ansible_user - Variable: ansible_iocage_user |

### Authors

- Stephan Lohse

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
