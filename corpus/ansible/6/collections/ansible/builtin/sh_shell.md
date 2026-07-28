---
collection: ansible
version: "6"
title: "ansible.builtin.sh shell – POSIX shell (/bin/sh)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/sh_shell.html
fetched_at: 2026-07-27T16:44:26+00:00
---
# ansible.builtin.sh shell – POSIX shell (/bin/sh)

> **Note:**
>
> This shell plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `sh` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same shell plugin name.

- [Synopsis](sh_shell.md#synopsis)
- [Parameters](sh_shell.md#parameters)

## [Synopsis](sh_shell.md#id1)

- This shell plugin is the one you want to use on most Unix systems, it is the most compatible and widely installed shell.

## [Parameters](sh_shell.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_users**  list / elements=string | list of users to be expected to have admin privileges. This is used by the controller to determine how to share temporary files between the remote user and the become user.  Default: `["root", "toor"]`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   admin_users = root, toor   ``` - Environment variable: [`ANSIBLE_ADMIN_USERS`](../../environment_variables.md#envvar-ANSIBLE_ADMIN_USERS) - Variable: ansible_admin_users |
| **async_dir**  string | Directory in which ansible will keep async job information  Default: `"~/.ansible_async"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   async_dir = ~/.ansible_async   ``` - Environment variable: [`ANSIBLE_ASYNC_DIR`](../../environment_variables.md#envvar-ANSIBLE_ASYNC_DIR) - Variable: ansible_async_dir |
| **common_remote_group**  string  added in ansible-base 2.10 | Checked when Ansible needs to execute a module as a different user.  If setfacl and chown both fail and do not let the different user access the module’s files, they will be chgrp’d to this group.  In order for this to work, the remote_user and become_user must share a common group and this setting must be set to that group.  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   common_remote_group = VALUE   ``` - Environment variable: [`ANSIBLE_COMMON_REMOTE_GROUP`](../../environment_variables.md#envvar-ANSIBLE_COMMON_REMOTE_GROUP) - Variable: ansible_common_remote_group |
| **environment**  list / elements=dictionary | List of dictionaries of environment variables and their values to use when executing commands.  Default: `[{}]` |
| **remote_tmp**  string | Temporary directory to use on targets when executing tasks.  Default: `"~/.ansible/tmp"`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   remote_tmp = ~/.ansible/tmp   ``` - Environment variable: [`ANSIBLE_REMOTE_TEMP`](../../environment_variables.md#envvar-ANSIBLE_REMOTE_TEMP) - Environment variable: [`ANSIBLE_REMOTE_TMP`](../../environment_variables.md#envvar-ANSIBLE_REMOTE_TMP) - Variable: ansible_remote_tmp |
| **system_tmpdirs**  list / elements=string | List of valid system temporary directories on the managed machine for Ansible to validate `remote_tmp` against, when specific permissions are needed. These must be world readable, writable, and executable. This list should only contain directories which the system administrator has pre-created with the proper ownership and permissions otherwise security issues can arise.  When `remote_tmp` is required to be a system temp dir and it does not match any in the list, the first one from the list will be used instead.  Default: `["/var/tmp", "/tmp"]`  Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   system_tmpdirs = /var/tmp, /tmp   ``` - Environment variable: [`ANSIBLE_SYSTEM_TMPDIRS`](../../environment_variables.md#envvar-ANSIBLE_SYSTEM_TMPDIRS) - Variable: ansible_system_tmpdirs |
| **world_readable_temp**  boolean  added in ansible-base 2.10 | This makes the temporary files created on the machine world-readable and will issue a warning instead of failing the task.  It is useful when becoming an unprivileged user.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   allow_world_readable_tmpfiles = false   ``` - Environment variable: [`ANSIBLE_SHELL_ALLOW_WORLD_READABLE_TEMP`](../../environment_variables.md#envvar-ANSIBLE_SHELL_ALLOW_WORLD_READABLE_TEMP) - Variable: ansible_shell_allow_world_readable_temp |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
