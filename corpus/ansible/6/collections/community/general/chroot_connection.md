---
collection: ansible
version: "6"
title: "community.general.chroot connection – Interact with local chroot"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/chroot_connection.html
fetched_at: 2026-07-27T17:14:40+00:00
---
# community.general.chroot connection – Interact with local chroot

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
> To use it in a playbook, specify: `community.general.chroot`.

- [Synopsis](chroot_connection.md#synopsis)
- [Parameters](chroot_connection.md#parameters)

## [Synopsis](chroot_connection.md#id1)

- Run commands or put/fetch files to an existing chroot on the Ansible controller.

## [Parameters](chroot_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **chroot_exe**  string | User specified chroot binary  Default: `"chroot"`  Configuration:   - INI entry:  ```YAML+Jinja   [chroot_connection]   exe = chroot   ``` - Environment variable: [`ANSIBLE_CHROOT_EXE`](../../environment_variables.md#envvar-ANSIBLE_CHROOT_EXE) - Variable: ansible_chroot_exe |
| **executable**  string | User specified executable shell  Default: `"/bin/sh"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   executable = /bin/sh   ``` - Environment variable: [`ANSIBLE_EXECUTABLE`](../../../reference_appendices/config.md#envvar-ANSIBLE_EXECUTABLE) - Variable: ansible_executable |
| **remote_addr**  string | The path of the chroot you want to access.  Default: `"inventory_hostname"`  Configuration:   - Variable: inventory_hostname - Variable: ansible_host |

### Authors

- Maykel Moya

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
