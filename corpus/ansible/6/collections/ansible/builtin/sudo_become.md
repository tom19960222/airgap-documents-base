---
collection: ansible
version: "6"
title: "ansible.builtin.sudo become – Substitute User DO"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/sudo_become.html
fetched_at: 2026-07-27T16:44:13+00:00
---
# ansible.builtin.sudo become – Substitute User DO

> **Note:**
>
> This become plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `sudo` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same become plugin name.

New in Ansible 2.8

- [Synopsis](sudo_become.md#synopsis)
- [Parameters](sudo_become.md#parameters)

## [Synopsis](sudo_become.md#id1)

- This become plugin allows your remote/login user to execute commands as another user via the sudo utility.

## [Parameters](sudo_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Sudo executable  Default: `"sudo"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = sudo   ```  ```YAML+Jinja   [sudo_become_plugin]   executable = sudo   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_SUDO_EXE`](../../environment_variables.md#envvar-ANSIBLE_SUDO_EXE) - Variable: ansible_become_exe - Variable: ansible_sudo_exe - Keyword: become_exe |
| **become_flags**  string | Options to pass to sudo  Default: `"-H -S -n"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = -H -S -n   ```  ```YAML+Jinja   [sudo_become_plugin]   flags = -H -S -n   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_SUDO_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_SUDO_FLAGS) - Variable: ansible_become_flags - Variable: ansible_sudo_flags - Keyword: become_flags |
| **become_pass**  string | Password to pass to sudo  Configuration:   - INI entry:  ```YAML+Jinja   [sudo_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_SUDO_PASS`](../../environment_variables.md#envvar-ANSIBLE_SUDO_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_sudo_pass |
| **become_user**  string | User you ‘become’ to execute the task  Default: `"root"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = root   ```  ```YAML+Jinja   [sudo_become_plugin]   user = root   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_SUDO_USER`](../../environment_variables.md#envvar-ANSIBLE_SUDO_USER) - Variable: ansible_become_user - Variable: ansible_sudo_user - Keyword: become_user |

### Authors

- ansible (@core)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
