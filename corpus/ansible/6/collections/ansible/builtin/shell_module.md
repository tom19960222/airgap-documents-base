---
collection: ansible
version: "6"
title: "ansible.builtin.shell module – Execute shell commands on targets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/shell_module.html
fetched_at: 2026-07-27T16:43:03+00:00
---
# ansible.builtin.shell module – Execute shell commands on targets

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `shell` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](shell_module.md#synopsis)
- [Parameters](shell_module.md#parameters)
- [Attributes](shell_module.md#attributes)
- [Notes](shell_module.md#notes)
- [See Also](shell_module.md#see-also)
- [Examples](shell_module.md#examples)
- [Return Values](shell_module.md#return-values)

## [Synopsis](shell_module.md#id1)

- The `shell` module takes the command name followed by a list of space-delimited arguments.
- Either a free form command or `cmd` parameter is required, see the examples.
- It is almost exactly like the [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module) module but runs the command through a shell (`/bin/sh`) on the remote node.
- For Windows targets, use the [ansible.windows.win_shell](../windows/win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](shell_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **chdir**  path | Change into this directory before running the command. |
| **cmd**  string | The command to run followed by optional arguments. |
| **creates**  path | A filename, when it already exists, this step will **not** be run. |
| **executable**  path | Change the shell used to execute the command.  This expects an absolute path to the executable. |
| **free_form**  string | The shell module takes a free form command to run, as a string.  There is no actual parameter named ‘free form’.  See the examples on how to use this module. |
| **removes**  path | A filename, when it does not exist, this step will **not** be run. |
| **stdin**  string | Set the stdin of the command directly to the specified value. |
| **stdin_add_newline**  boolean  added in Ansible 2.8 | Whether to append a newline to stdin data.  Choices:   - `false` - `true` ← (default) |
| **warn**  boolean | Whether to enable task warnings.  Choices:   - `false` - `true` ← (default) |

## [Attributes](shell_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: partial  while the command itself is arbitrary and cannot be subject to the check mode semantics it adds `creates`/`removes` options as a workaround | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |
| **raw** | Support: full | Indicates if an action takes a ‘raw’ or ‘free form’ string as an option and has it’s own special parsing of it |

## [Notes](shell_module.md#id4)

> **Note:**
>
> - If you want to execute a command securely and predictably, it may be better to use the [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module) module instead. Best practices when writing playbooks will follow the trend of using [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module) unless the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) module is explicitly required. When running ad-hoc commands, use your best judgement.
> - To sanitize any variables passed to the shell module, you should use `{{ var | quote }}` instead of just `{{ var }}` to make sure they do not include evil things like semicolons.
> - An alternative to using inline shell scripts with this module is to use the [ansible.builtin.script](script_module.md#ansible-collections-ansible-builtin-script-module) module possibly together with the [ansible.builtin.template](template_module.md#ansible-collections-ansible-builtin-template-module) module.
> - For rebooting systems, use the [ansible.builtin.reboot](reboot_module.md#ansible-collections-ansible-builtin-reboot-module) or [ansible.windows.win_reboot](../windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) module.

## [See Also](shell_module.md#id5)

> **See also:**
>
> [ansible.builtin.command](command_module.md#ansible-collections-ansible-builtin-command-module)
> :   Execute commands on targets.
>
> [ansible.builtin.raw](raw_module.md#ansible-collections-ansible-builtin-raw-module)
> :   Executes a low-down and dirty command.
>
> [ansible.builtin.script](script_module.md#ansible-collections-ansible-builtin-script-module)
> :   Runs a local script on a remote node after transferring it.
>
> [ansible.windows.win_shell](../windows/win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](shell_module.md#id6)

```yaml+jinja
- name: Execute the command in remote shell; stdout goes to the specified file on the remote
  ansible.builtin.shell: somescript.sh >> somelog.txt

- name: Change the working directory to somedir/ before executing the command
  ansible.builtin.shell: somescript.sh >> somelog.txt
  args:
    chdir: somedir/

# You can also use the 'args' form to provide the options.
- name: This command will change the working directory to somedir/ and will only run when somedir/somelog.txt doesn't exist
  ansible.builtin.shell: somescript.sh >> somelog.txt
  args:
    chdir: somedir/
    creates: somelog.txt

# You can also use the 'cmd' parameter instead of free form format.
- name: This command will change the working directory to somedir/
  ansible.builtin.shell:
    cmd: ls -l | grep log
    chdir: somedir/

- name: Run a command that uses non-posix shell-isms (in this example /bin/sh doesn't handle redirection and wildcards together but bash does)
  ansible.builtin.shell: cat < /tmp/*txt
  args:
    executable: /bin/bash

- name: Run a command using a templated variable (always use quote filter to avoid injection)
  ansible.builtin.shell: cat {{ myfile|quote }}

# You can use shell to run other executables to perform actions inline
- name: Run expect to wait for a successful PXE boot via out-of-band CIMC
  ansible.builtin.shell: |
    set timeout 300
    spawn ssh admin@{{ cimc_host }}

    expect "password:"
    send "{{ cimc_password }}\n"

    expect "\n{{ cimc_name }}"
    send "connect host\n"

    expect "pxeboot.n12"
    send "\n"

    exit 0
  args:
    executable: /usr/bin/expect
  delegate_to: localhost

# Disabling warnings
- name: Using curl to connect to a host via SOCKS proxy (unsupported in uri). Ordinarily this would throw a warning
  ansible.builtin.shell: curl --socks5 localhost:9000 http://www.ansible.com
  args:
    warn: no
```

## [Return Values](shell_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | The command executed by the task.  Returned: always  Sample: `"rabbitmqctl join_cluster rabbit@master"` |
| **delta**  string | The command execution delta time.  Returned: always  Sample: `"0:00:00.325771"` |
| **end**  string | The command execution end time.  Returned: always  Sample: `"2016-02-25 09:18:26.755339"` |
| **msg**  boolean | changed  Returned: always  Sample: `true` |
| **rc**  integer | The command return code (0 means success).  Returned: always  Sample: `0` |
| **start**  string | The command execution start time.  Returned: always  Sample: `"2016-02-25 09:18:26.429568"` |
| **stderr**  string | The command standard error.  Returned: always  Sample: `"ls: cannot access foo: No such file or directory"` |
| **stderr_lines**  list / elements=string | The command standard error split in lines.  Returned: always  Sample: `[{"u'ls cannot access foo": "No such file or directory'"}, "u'ls \u2026'"]` |
| **stdout**  string | The command standard output.  Returned: always  Sample: `"Clustering node rabbit@slave1 with rabbit@master \u2026"` |
| **stdout_lines**  list / elements=string | The command standard output split in lines.  Returned: always  Sample: `["u'Clustering node rabbit@slave1 with rabbit@master \u2026'"]` |

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
