---
collection: ansible
version: "6"
title: "community.general.ksu become – Kerberos substitute user"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ksu_become.html
fetched_at: 2026-07-27T17:14:17+00:00
---
# community.general.ksu become – Kerberos substitute user

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
> To use it in a playbook, specify: `community.general.ksu`.

- [Synopsis](ksu_become.md#synopsis)
- [Parameters](ksu_become.md#parameters)

## [Synopsis](ksu_become.md#id1)

- This become plugins allows your remote/login user to execute commands as another user via the ksu utility.

## [Parameters](ksu_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Su executable  Default: `"ksu"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = ksu   ```  ```YAML+Jinja   [ksu_become_plugin]   executable = ksu   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_KSU_EXE`](../../environment_variables.md#envvar-ANSIBLE_KSU_EXE) - Variable: ansible_become_exe - Variable: ansible_ksu_exe |
| **become_flags**  string | Options to pass to ksu  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = ""   ```  ```YAML+Jinja   [ksu_become_plugin]   flags = ""   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_KSU_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_KSU_FLAGS) - Variable: ansible_become_flags - Variable: ansible_ksu_flags |
| **become_pass**  string | ksu password  Configuration:   - INI entry:  ```YAML+Jinja   [ksu_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_KSU_PASS`](../../environment_variables.md#envvar-ANSIBLE_KSU_PASS) - Variable: ansible_ksu_pass - Variable: ansible_become_pass - Variable: ansible_become_password |
| **become_user**  string / required | User you ‘become’ to execute the task  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = VALUE   ```  ```YAML+Jinja   [ksu_become_plugin]   user = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_KSU_USER`](../../environment_variables.md#envvar-ANSIBLE_KSU_USER) - Variable: ansible_become_user - Variable: ansible_ksu_user |
| **prompt_l10n**  string | List of localized strings to match for prompt detection  If empty we’ll use the built in one  Default: `[]`  Configuration:   - INI entry:  ```YAML+Jinja   [ksu_become_plugin]   localized_prompts =   ``` - Environment variable: [`ANSIBLE_KSU_PROMPT_L10N`](../../environment_variables.md#envvar-ANSIBLE_KSU_PROMPT_L10N) - Variable: ansible_ksu_prompt_l10n |

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
