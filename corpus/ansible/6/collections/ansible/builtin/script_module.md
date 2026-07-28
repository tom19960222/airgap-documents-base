---
collection: ansible
version: "6"
title: "ansible.builtin.script module – Runs a local script on a remote node after transferring it"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/script_module.html
fetched_at: 2026-07-27T16:43:06+00:00
---
# ansible.builtin.script module – Runs a local script on a remote node after transferring it

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `script` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](script_module.md#synopsis)
- [Parameters](script_module.md#parameters)
- [Attributes](script_module.md#attributes)
- [Notes](script_module.md#notes)
- [See Also](script_module.md#see-also)
- [Examples](script_module.md#examples)

## [Synopsis](script_module.md#id1)

- The `script` module takes the script name followed by a list of space-delimited arguments.
- Either a free form command or `cmd` parameter is required, see the examples.
- The local script at path will be transferred to the remote node and then executed.
- The given script will be processed through the shell environment on the remote node.
- This module does not require python on the remote system, much like the [ansible.builtin.raw](raw_module.md#ansible-collections-ansible-builtin-raw-module) module.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **chdir**  string | Change into this directory on the remote node before running the script. |
| **cmd**  string | Path to the local script to run followed by optional arguments. |
| **creates**  string | A filename on the remote node, when it already exists, this step will **not** be run. |
| **decrypt**  boolean | This option controls the autodecryption of source files using vault.  Choices:   - `false` - `true` ← (default) |
| **executable**  string | Name or path of a executable to invoke the script with. |
| **free_form**  string | Path to the local script file followed by optional arguments. |
| **removes**  string | A filename on the remote node, when it does not exist, this step will **not** be run. |

## [Attributes](script_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: partial  while the script itself is arbitrary and cannot be subject to the check mode semantics it adds `creates`/`removes` options as a workaround | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platforms: all  This action is one of the few that requires no Python on the remote as it passes the command directly into the connection string | Target OS/families that can be operated against |
| **raw** | Support: full | Indicates if an action takes a ‘raw’ or ‘free form’ string as an option and has it’s own special parsing of it |
| **safe_file_operations** | Support: none | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | Support: full | Can automatically decrypt Ansible vaulted files |

## [Notes](script_module.md#id4)

> **Note:**
>
> - It is usually preferable to write Ansible modules rather than pushing scripts. Convert your script to an Ansible module for bonus points!
> - The `ssh` connection plugin will force pseudo-tty allocation via `-tt` when scripts are executed. Pseudo-ttys do not have a stderr channel and all stderr is sent to stdout. If you depend on separated stdout and stderr result keys, please switch to a copy+command set of tasks instead of using script.
> - If the path to the local script contains spaces, it needs to be quoted.
> - This module is also supported for Windows targets.

## [See Also](script_module.md#id5)

> **See also:**
>
> [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module)
> :   Execute shell commands on targets.
>
> [ansible.windows.win_shell](../windows/win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](script_module.md#id6)

```yaml+jinja
- name: Run a script with arguments (free form)
  ansible.builtin.script: /some/local/script.sh --some-argument 1234

- name: Run a script with arguments (using 'cmd' parameter)
  ansible.builtin.script:
    cmd: /some/local/script.sh --some-argument 1234

- name: Run a script only if file.txt does not exist on the remote node
  ansible.builtin.script: /some/local/create_file.sh --some-argument 1234
  args:
    creates: /the/created/file.txt

- name: Run a script only if file.txt exists on the remote node
  ansible.builtin.script: /some/local/remove_file.sh --some-argument 1234
  args:
    removes: /the/removed/file.txt

- name: Run a script using an executable in a non-system path
  ansible.builtin.script: /some/local/script
  args:
    executable: /some/remote/executable

- name: Run a script using an executable in a system path
  ansible.builtin.script: /some/local/script.py
  args:
    executable: python3

- name: Run a Powershell script on a windows host
  script: subdirectories/under/path/with/your/playbook/script.ps1
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
