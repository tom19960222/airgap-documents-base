---
collection: ansible
version: "6"
title: "community.general.dzdo become – Centrify’s Direct Authorize"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dzdo_become.html
fetched_at: 2026-07-27T17:14:16+00:00
---
# community.general.dzdo become – Centrify’s Direct Authorize

> **Note:**
>
> This become plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.dzdo`.

- [Synopsis](dzdo_become.md#synopsis)
- [Parameters](dzdo_become.md#parameters)

## [Synopsis](dzdo_become.md#id1)

- This become plugins allows your remote/login user to execute commands as another user via the dzdo utility.

## [Parameters](dzdo_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Dzdo executable  Default: `"dzdo"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = dzdo   ```  ```YAML+Jinja   [dzdo_become_plugin]   executable = dzdo   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_DZDO_EXE`](../../environment_variables.md#envvar-ANSIBLE_DZDO_EXE) - Variable: ansible_become_exe - Variable: ansible_dzdo_exe |
| **become_flags**  string | Options to pass to dzdo  Default: `"-H -S -n"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = -H -S -n   ```  ```YAML+Jinja   [dzdo_become_plugin]   flags = -H -S -n   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_DZDO_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_DZDO_FLAGS) - Variable: ansible_become_flags - Variable: ansible_dzdo_flags |
| **become_pass**  string | Options to pass to dzdo  Configuration:   - INI entry:  ```YAML+Jinja   [dzdo_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_DZDO_PASS`](../../environment_variables.md#envvar-ANSIBLE_DZDO_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_dzdo_pass |
| **become_user**  string | User you ‘become’ to execute the task  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = VALUE   ```  ```YAML+Jinja   [dzdo_become_plugin]   user = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_DZDO_USER`](../../environment_variables.md#envvar-ANSIBLE_DZDO_USER) - Variable: ansible_become_user - Variable: ansible_dzdo_user |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
