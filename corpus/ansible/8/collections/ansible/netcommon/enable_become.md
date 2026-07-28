---
collection: ansible
version: "8"
title: "ansible.netcommon.enable become – Switch to elevated permissions on a network device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/enable_become.html
fetched_at: 2026-07-28T01:09:14+00:00
---
# ansible.netcommon.enable become – Switch to elevated permissions on a network device

> **Note:**
>
> This become plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.enable`.

New in ansible.netcommon 1.0.0

- [Synopsis](enable_become.md#synopsis)
- [Parameters](enable_become.md#parameters)
- [Notes](enable_become.md#notes)

## [Synopsis](enable_become.md#id1)

- This become plugins allows elevated permissions on a remote network device.

## [Parameters](enable_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_pass**  string | password  **Configuration:**   - INI entry:  ```YAML+Jinja   [enable_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_ENABLE_PASS`](../../environment_variables.md#envvar-ANSIBLE_ENABLE_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_enable_pass |

## [Notes](enable_become.md#id3)

> **Note:**
>
> - enable is really implemented in the network connection handler and as such can only be used with network connections.
> - This plugin ignores the ‘become_exe’ and ‘become_user’ settings as it uses an API and not an executable.

### Authors

- Ansible Networking Team (@ansible-network)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
