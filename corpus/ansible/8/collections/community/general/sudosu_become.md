---
collection: ansible
version: "8"
title: "community.general.sudosu become – Run tasks using sudo su -"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/sudosu_become.html
fetched_at: 2026-07-28T01:51:48+00:00
---
# community.general.sudosu become – Run tasks using sudo su -

> **Note:**
>
> This become plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.sudosu`.

New in community.general 2.4.0

- [Synopsis](sudosu_become.md#synopsis)
- [Parameters](sudosu_become.md#parameters)

## [Synopsis](sudosu_become.md#id1)

- This become plugin allows your remote/login user to execute commands as another user via the `sudo` and `su` utilities combined.

## [Parameters](sudosu_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_flags**  string | Options to pass to `sudo`.  **Default:** `"-H -S -n"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = -H -S -n   ```  ```YAML+Jinja   [sudo_become_plugin]   flags = -H -S -n   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_SUDO_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_SUDO_FLAGS) - Variable: ansible_become_flags - Variable: ansible_sudo_flags |
| **become_pass**  string | Password to pass to `sudo`.  **Configuration:**   - INI entry:  ```YAML+Jinja   [sudo_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_SUDO_PASS`](../../environment_variables.md#envvar-ANSIBLE_SUDO_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_sudo_pass |
| **become_user**  string | User you ‘become’ to execute the task.  **Default:** `"root"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = root   ```  ```YAML+Jinja   [sudo_become_plugin]   user = root   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_SUDO_USER`](../../environment_variables.md#envvar-ANSIBLE_SUDO_USER) - Variable: ansible_become_user - Variable: ansible_sudo_user |

### Authors

- Dag Wieers (@dagwieers)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
