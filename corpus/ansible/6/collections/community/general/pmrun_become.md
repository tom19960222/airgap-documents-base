---
collection: ansible
version: "6"
title: "community.general.pmrun become – Privilege Manager run"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pmrun_become.html
fetched_at: 2026-07-27T17:14:19+00:00
---
# community.general.pmrun become – Privilege Manager run

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
> To use it in a playbook, specify: `community.general.pmrun`.

- [Synopsis](pmrun_become.md#synopsis)
- [Parameters](pmrun_become.md#parameters)
- [Notes](pmrun_become.md#notes)

## [Synopsis](pmrun_become.md#id1)

- This become plugins allows your remote/login user to execute commands as another user via the pmrun utility.

## [Parameters](pmrun_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Sudo executable  Default: `"pmrun"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = pmrun   ```  ```YAML+Jinja   [pmrun_become_plugin]   executable = pmrun   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_PMRUN_EXE`](../../environment_variables.md#envvar-ANSIBLE_PMRUN_EXE) - Variable: ansible_become_exe - Variable: ansible_pmrun_exe |
| **become_flags**  string | Options to pass to pmrun  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = ""   ```  ```YAML+Jinja   [pmrun_become_plugin]   flags = ""   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_PMRUN_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_PMRUN_FLAGS) - Variable: ansible_become_flags - Variable: ansible_pmrun_flags |
| **become_pass**  string | pmrun password  Configuration:   - INI entry:  ```YAML+Jinja   [pmrun_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_PMRUN_PASS`](../../environment_variables.md#envvar-ANSIBLE_PMRUN_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_pmrun_pass |

## [Notes](pmrun_become.md#id3)

> **Note:**
>
> - This plugin ignores the become_user supplied and uses pmrun’s own configuration to select the user.

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
