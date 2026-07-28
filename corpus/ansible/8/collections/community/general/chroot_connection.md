---
collection: ansible
version: "8"
title: "community.general.chroot connection – Interact with local chroot"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/chroot_connection.html
fetched_at: 2026-07-28T01:52:09+00:00
---
# community.general.chroot connection – Interact with local chroot

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
> To use it in a playbook, specify: `community.general.chroot`.

- [Synopsis](chroot_connection.md#synopsis)
- [Parameters](chroot_connection.md#parameters)
- [Examples](chroot_connection.md#examples)

## [Synopsis](chroot_connection.md#id1)

- Run commands or put/fetch files to an existing chroot on the Ansible controller.

## [Parameters](chroot_connection.md#id2)

| Parameter | Comments |
| --- | --- |
| **chroot_exe**  string | User specified chroot binary  **Default:** `"chroot"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [chroot_connection]   exe = chroot   ``` - Environment variable: [`ANSIBLE_CHROOT_EXE`](../../environment_variables.md#envvar-ANSIBLE_CHROOT_EXE) - Variable: ansible_chroot_exe |
| **disable_root_check**  boolean  *added in community.general 7.3.0* | Do not check that the user is not root.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [chroot_connection]   disable_root_check = false   ``` - Environment variable: [`ANSIBLE_CHROOT_DISABLE_ROOT_CHECK`](../../environment_variables.md#envvar-ANSIBLE_CHROOT_DISABLE_ROOT_CHECK) - Variable: ansible_chroot_disable_root_check |
| **executable**  string | User specified executable shell  **Default:** `"/bin/sh"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   executable = /bin/sh   ``` - Environment variable: [`ANSIBLE_EXECUTABLE`](../../../reference_appendices/config.md#envvar-ANSIBLE_EXECUTABLE) - Variable: ansible_executable |
| **remote_addr**  string | The path of the chroot you want to access.  **Default:** `"inventory_hostname"`  **Configuration:**   - Variable: inventory_hostname - Variable: ansible_host |

## [Examples](chroot_connection.md#id3)

```yaml+jinja
# Plugin requires root privileges for chroot, -E preserves your env (and location of ~/.ansible):
# sudo -E ansible-playbook ...
#
# Static inventory file
# [chroots]
# /path/to/debootstrap
# /path/to/feboostrap
# /path/to/lxc-image
# /path/to/chroot

# playbook
---
- hosts: chroots
  connection: community.general.chroot
  tasks:
    - debug:
        msg: "This is coming from chroot environment"
```

### Authors

- Maykel Moya

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
