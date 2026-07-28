---
collection: ansible
version: "6"
title: "ansible.builtin.su become – Substitute User"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/su_become.html
fetched_at: 2026-07-27T16:44:13+00:00
---
# ansible.builtin.su become – Substitute User

> **Note:**
>
> This become plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `su` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same become plugin name.

New in Ansible 2.8

- [Synopsis](su_become.md#synopsis)
- [Parameters](su_become.md#parameters)

## [Synopsis](su_become.md#id1)

- This become plugin allows your remote/login user to execute commands as another user via the su utility.

## [Parameters](su_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Su executable  Default: `"su"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = su   ```  ```YAML+Jinja   [su_become_plugin]   executable = su   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_SU_EXE`](../../environment_variables.md#envvar-ANSIBLE_SU_EXE) - Variable: ansible_become_exe - Variable: ansible_su_exe - Keyword: become_exe |
| **become_flags**  string | Options to pass to su  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = ""   ```  ```YAML+Jinja   [su_become_plugin]   flags = ""   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_SU_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_SU_FLAGS) - Variable: ansible_become_flags - Variable: ansible_su_flags - Keyword: become_flags |
| **become_pass**  string | Password to pass to su  Configuration:   - INI entry:  ```YAML+Jinja   [su_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_SU_PASS`](../../environment_variables.md#envvar-ANSIBLE_SU_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_su_pass |
| **become_user**  string | User you ‘become’ to execute the task  Default: `"root"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = root   ```  ```YAML+Jinja   [su_become_plugin]   user = root   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_SU_USER`](../../environment_variables.md#envvar-ANSIBLE_SU_USER) - Variable: ansible_become_user - Variable: ansible_su_user - Keyword: become_user |
| **prompt_l10n**  list / elements=string | List of localized strings to match for prompt detection  If empty we’ll use the built in one  Do NOT add a colon (:) to your custom entries. Ansible adds a colon at the end of each prompt; if you add another one in your string, your prompt will fail with a “Timeout” error.  Default: `[]`  Configuration:   - INI entry:  ```YAML+Jinja   [su_become_plugin]   localized_prompts =   ``` - Environment variable: [`ANSIBLE_SU_PROMPT_L10N`](../../environment_variables.md#envvar-ANSIBLE_SU_PROMPT_L10N) - Variable: ansible_su_prompt_l10n |

### Authors

- ansible (@core)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
