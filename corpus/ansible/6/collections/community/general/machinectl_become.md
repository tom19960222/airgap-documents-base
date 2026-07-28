---
collection: ansible
version: "6"
title: "community.general.machinectl become – Systemd’s machinectl privilege escalation"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/machinectl_become.html
fetched_at: 2026-07-27T17:14:17+00:00
---
# community.general.machinectl become – Systemd’s machinectl privilege escalation

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
> To use it in a playbook, specify: `community.general.machinectl`.

- [Synopsis](machinectl_become.md#synopsis)
- [Parameters](machinectl_become.md#parameters)
- [Notes](machinectl_become.md#notes)
- [Examples](machinectl_become.md#examples)

## [Synopsis](machinectl_become.md#id1)

- This become plugins allows your remote/login user to execute commands as another user via the machinectl utility.

## [Parameters](machinectl_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Machinectl executable  Default: `"machinectl"`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = machinectl   ```  ```YAML+Jinja   [machinectl_become_plugin]   executable = machinectl   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_MACHINECTL_EXE`](../../environment_variables.md#envvar-ANSIBLE_MACHINECTL_EXE) - Variable: ansible_become_exe - Variable: ansible_machinectl_exe |
| **become_flags**  string | Options to pass to machinectl  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_flags = ""   ```  ```YAML+Jinja   [machinectl_become_plugin]   flags = ""   ``` - Environment variable: [`ANSIBLE_BECOME_FLAGS`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_FLAGS) - Environment variable: [`ANSIBLE_MACHINECTL_FLAGS`](../../environment_variables.md#envvar-ANSIBLE_MACHINECTL_FLAGS) - Variable: ansible_become_flags - Variable: ansible_machinectl_flags |
| **become_pass**  string | Password for machinectl  Configuration:   - INI entry:  ```YAML+Jinja   [machinectl_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_MACHINECTL_PASS`](../../environment_variables.md#envvar-ANSIBLE_MACHINECTL_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_machinectl_pass |
| **become_user**  string | User you ‘become’ to execute the task  Default: `""`  Configuration:   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = ""   ```  ```YAML+Jinja   [machinectl_become_plugin]   user = ""   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_MACHINECTL_USER`](../../environment_variables.md#envvar-ANSIBLE_MACHINECTL_USER) - Variable: ansible_become_user - Variable: ansible_machinectl_user |

## [Notes](machinectl_become.md#id3)

> **Note:**
>
> - When not using this plugin with user `root`, it only works correctly with a polkit rule which will alter the behaviour of machinectl. This rule must alter the prompt behaviour to ask directly for the user credentials, if the user is allowed to perform the action (take a look at the examples section). If such a rule is not present the plugin only work if it is used in context with the root user, because then no further prompt will be shown by machinectl.

## [Examples](machinectl_become.md#id4)

```yaml+jinja
# A polkit rule needed to use the module with a non-root user.
# See the Notes section for details.
60-machinectl-fast-user-auth.rules: |
    polkit.addRule(function(action, subject) {
        if(action.id == "org.freedesktop.machine1.host-shell" && subject.isInGroup("wheel")) {
            return polkit.Result.AUTH_SELF_KEEP;
        }
    });
```

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
