---
collection: ansible
version: "6"
title: "community.general.pbrun become – PowerBroker run"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pbrun_become.html
fetched_at: 2026-07-27T17:14:18+00:00
---
# community.general.pbrun become – PowerBroker run

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
> To use it in a playbook, specify: `community.general.pbrun`.

- [Synopsis](pbrun_become.md#synopsis)
- [Parameters](pbrun_become.md#parameters)

## [Synopsis](pbrun_become.md#id1)

- This become plugins allows your remote/login user to execute commands as another user via the pbrun utility.

## [Parameters](pbrun_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Sudo executable  Default: `"pbrun"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = pbrun   ```  ```YAML+Jinja   [pbrun_become_plugin]   executable = pbrun   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_PBRUN_EXE`](../../environment_variables.md#envvar-ANSIBLE_PBRUN_EXE) - Variable: ansible_become_exe - Variable: ansible_pbrun_exe |
| **become_flags**  string | Options to pass to pbrun  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = ""   ```  ```YAML+Jinja   [pbrun_become_plugin]   flags = ""   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_PBRUN_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_PBRUN_FLAGS) - Variable: ansible_become_flags - Variable: ansible_pbrun_flags |
| **become_pass**  string | Password for pbrun  Configuration:   - INI entry:  ```YAML+Jinja   [pbrun_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_PBRUN_PASS`](../../environment_variables.md#envvar-ANSIBLE_PBRUN_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_pbrun_pass |
| **become_user**  string | User you ‘become’ to execute the task  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = ""   ```  ```YAML+Jinja   [pbrun_become_plugin]   user = ""   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_PBRUN_USER`](../../environment_variables.md#envvar-ANSIBLE_PBRUN_USER) - Variable: ansible_become_user - Variable: ansible_pbrun_user |
| **wrap_exe**  boolean | Toggle to wrap the command pbrun calls in ‘shell -c’ or not  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [pbrun_become_plugin]   wrap_execution = false   ``` - Environment variable: [`ANSIBLE_PBRUN_WRAP_EXECUTION`](../../environment_variables.md#envvar-ANSIBLE_PBRUN_WRAP_EXECUTION) - Variable: ansible_pbrun_wrap_execution |

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
