---
collection: ansible
version: "8"
title: "community.general.pfexec become – profile based execution"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pfexec_become.html
fetched_at: 2026-07-28T01:51:46+00:00
---
# community.general.pfexec become – profile based execution

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
> To use it in a playbook, specify: `community.general.pfexec`.

- [Synopsis](pfexec_become.md#synopsis)
- [Parameters](pfexec_become.md#parameters)
- [Notes](pfexec_become.md#notes)

## [Synopsis](pfexec_become.md#id1)

- This become plugins allows your remote/login user to execute commands as another user via the pfexec utility.

## [Parameters](pfexec_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Sudo executable  **Default:** `"pfexec"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = pfexec   ```  ```YAML+Jinja   [pfexec_become_plugin]   executable = pfexec   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_PFEXEC_EXE`](../../environment_variables.md#envvar-ANSIBLE_PFEXEC_EXE) - Variable: ansible_become_exe - Variable: ansible_pfexec_exe |
| **become_flags**  string | Options to pass to pfexec  **Default:** `"-H -S -n"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = -H -S -n   ```  ```YAML+Jinja   [pfexec_become_plugin]   flags = -H -S -n   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_PFEXEC_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_PFEXEC_FLAGS) - Variable: ansible_become_flags - Variable: ansible_pfexec_flags |
| **become_pass**  string | pfexec password  **Configuration:**   - INI entry:  ```YAML+Jinja   [pfexec_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_PFEXEC_PASS`](../../environment_variables.md#envvar-ANSIBLE_PFEXEC_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_pfexec_pass |
| **become_user**  string | User you ‘become’ to execute the task  This plugin ignores this setting as pfexec uses it’s own `exec_attr` to figure this out, but it is supplied here for Ansible to make decisions needed for the task execution, like file permissions.  **Default:** `"root"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = root   ```  ```YAML+Jinja   [pfexec_become_plugin]   user = root   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_PFEXEC_USER`](../../environment_variables.md#envvar-ANSIBLE_PFEXEC_USER) - Variable: ansible_become_user - Variable: ansible_pfexec_user |
| **wrap_exe**  boolean | Toggle to wrap the command pfexec calls in ‘shell -c’ or not  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [pfexec_become_plugin]   wrap_execution = false   ``` - Environment variable: [`ANSIBLE_PFEXEC_WRAP_EXECUTION`](../../environment_variables.md#envvar-ANSIBLE_PFEXEC_WRAP_EXECUTION) - Variable: ansible_pfexec_wrap_execution |

## [Notes](pfexec_become.md#id3)

> **Note:**
>
> - This plugin ignores `become_user` as pfexec uses it’s own `exec_attr` to figure this out.

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
