---
collection: ansible
version: "8"
title: "ansible.builtin.raw module – Executes a low-down and dirty command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/raw_module.html
fetched_at: 2026-07-28T01:04:16+00:00
---
# ansible.builtin.raw module – Executes a low-down and dirty command

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `raw` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.raw` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](raw_module.md#synopsis)
- [Parameters](raw_module.md#parameters)
- [Attributes](raw_module.md#attributes)
- [Notes](raw_module.md#notes)
- [See Also](raw_module.md#see-also)
- [Examples](raw_module.md#examples)

## [Synopsis](raw_module.md#id1)

- Executes a low-down and dirty SSH command, not going through the module subsystem.
- This is useful and should only be done in a few cases. A common case is installing `python` on a system without python installed by default. Another is speaking to any devices such as routers that do not have any Python installed. In any other case, using the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) or [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module) module is much more appropriate.
- Arguments given to `raw` are run directly through the configured remote shell.
- Standard output, error output and return code are returned when available.
- There is no change handler support for this module.
- This module does not require python on the remote system, much like the [ansible.builtin.script](script_module.md#ansible-collections-ansible-builtin-script-module) module.
- This module is also supported for Windows targets.
- If the command returns non UTF-8 data, it must be encoded to avoid issues. One option is to pipe the output through `base64`.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](raw_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **executable**  string | Change the shell used to execute the command. Should be an absolute path to the executable.  When using privilege escalation (`become`) a default shell will be assigned if one is not provided as privilege escalation requires a shell. |
| **free_form**  string / required | The raw module takes a free form command to run.  There is no parameter actually named ‘free form’; see the examples! |

## [Attributes](raw_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all**  This action is one of the few that requires no Python on the remote as it passes the command directly into the connection string | Target OS/families that can be operated against |
| **raw** | **Support:** **full** | Indicates if an action takes a ‘raw’ or ‘free form’ string as an option and has it’s own special parsing of it |

## [Notes](raw_module.md#id4)

> **Note:**
>
> - If using raw from a playbook, you may need to disable fact gathering using `gather_facts: no` if you’re using `raw` to bootstrap python onto the machine.
> - If you want to execute a command securely and predictably, it may be better to use the [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module) or [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) modules instead.
> - The `environment` keyword does not work with raw normally, it requires a shell which means it only works if `executable` is set or using the module with privilege escalation (`become`).

## [See Also](raw_module.md#id5)

> **See also:**
>
> [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module)
> :   Execute commands on targets.
>
> [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module)
> :   Execute shell commands on targets.
>
> [ansible.windows.win_command](../windows/win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.
>
> [ansible.windows.win_shell](../windows/win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](raw_module.md#id6)

```yaml+jinja
- name: Bootstrap a host without python2 installed
  ansible.builtin.raw: dnf install -y python2 python2-dnf libselinux-python

- name: Run a command that uses non-posix shell-isms (in this example /bin/sh doesn't handle redirection and wildcards together but bash does)
  ansible.builtin.raw: cat < /tmp/*txt
  args:
    executable: /bin/bash

- name: Safely use templated variables. Always use quote filter to avoid injection issues.
  ansible.builtin.raw: "{{ package_mgr|quote }} {{ pkg_flags|quote }} install {{ python|quote }}"

- name: List user accounts on a Windows system
  ansible.builtin.raw: Get-WmiObject -Class Win32_UserAccount
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
