---
collection: ansible
version: "8"
title: "ansible.builtin.runas become – Run As user"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/runas_become.html
fetched_at: 2026-07-28T01:05:10+00:00
---
# ansible.builtin.runas become – Run As user

> **Note:**
>
> This become plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `runas`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.runas` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same become plugin name.

New in Ansible 2.8

- [Synopsis](runas_become.md#synopsis)
- [Parameters](runas_become.md#parameters)
- [Notes](runas_become.md#notes)

## [Synopsis](runas_become.md#id1)

- This become plugin allows your remote/login user to execute commands as another user via the windows runas facility.

## [Parameters](runas_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_flags**  string | Options to pass to runas, a space delimited list of k=v pairs  **Default:** `""`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = ""   ```  ```YAML+Jinja   [runas_become_plugin]   flags = ""   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_RUNAS_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_RUNAS_FLAGS) - Variable: ansible_become_flags - Variable: ansible_runas_flags - Keyword: become_flags |
| **become_pass**  string | password  **Configuration:**   - INI entry:  ```YAML+Jinja   [runas_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_RUNAS_PASS`](../../environment_variables.md#envvar-ANSIBLE_RUNAS_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_runas_pass |
| **become_user**  string / required | User you ‘become’ to execute the task  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = VALUE   ```  ```YAML+Jinja   [runas_become_plugin]   user = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_RUNAS_USER`](../../environment_variables.md#envvar-ANSIBLE_RUNAS_USER) - Variable: ansible_become_user - Variable: ansible_runas_user - Keyword: become_user |

## [Notes](runas_become.md#id3)

> **Note:**
>
> - runas is really implemented in the powershell module handler and as such can only be used with winrm connections.
> - This plugin ignores the ‘become_exe’ setting as it uses an API and not an executable.
> - The Secondary Logon service (seclogon) must be running to use runas

### Authors

- ansible (@core)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
