---
collection: ansible
version: "8"
title: "ansible.builtin.command module – Execute commands on targets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/command_module.html
fetched_at: 2026-07-28T01:04:11+00:00
---
# ansible.builtin.command module – Execute commands on targets

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `command` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.command` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](command_module.md#synopsis)
- [Parameters](command_module.md#parameters)
- [Attributes](command_module.md#attributes)
- [Notes](command_module.md#notes)
- [See Also](command_module.md#see-also)
- [Examples](command_module.md#examples)
- [Return Values](command_module.md#return-values)

## [Synopsis](command_module.md#id1)

- The `command` module takes the command name followed by a list of space-delimited arguments.
- The given command will be executed on all selected nodes.
- The command(s) will not be processed through the shell, so variables like `$HOSTNAME` and operations like `"*"`, `"<"`, `">"`, `"|"`, `";"` and `"&"` will not work. Use the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) module if you need these features.
- To create `command` tasks that are easier to read than the ones using space-delimited arguments, pass parameters using the `args` [task keyword](https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#task) or use `cmd` parameter.
- Either a free form command or `cmd` parameter is required, see the examples.
- For Windows targets, use the [ansible.windows.win_command](../windows/win_command_module.md#ansible-collections-ansible-windows-win-command-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **argv**  list / elements=string | Passes the command as a list rather than a string.  Use `argv` to avoid quoting values that would otherwise be interpreted incorrectly (for example “user name”).  Only the string (free form) or the list (argv) form can be provided, not both. One or the other must be provided. |
| **chdir**  path | Change into this directory before running the command. |
| **cmd**  string | The command to run. |
| **creates**  path | A filename or (since 2.0) glob pattern. If a matching file already exists, this step **will not** be run.  This is checked before *removes* is checked. |
| **free_form**  string | The command module takes a free form string as a command to run.  There is no actual parameter named ‘free form’. |
| **removes**  path | A filename or (since 2.0) glob pattern. If a matching file exists, this step **will** be run.  This is checked after *creates* is checked. |
| **stdin**  string | Set the stdin of the command directly to the specified value. |
| **stdin_add_newline**  boolean  *added in Ansible 2.8* | If set to `true`, append a newline to stdin data.  **Choices:**   - `false` - `true` ← (default) |
| **strip_empty_ends**  boolean  *added in Ansible 2.8* | Strip empty lines from the end of stdout/stderr in result.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  while the command itself is arbitrary and cannot be subject to the check mode semantics it adds `creates`/`removes` options as a workaround | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |
| **raw** | **Support:** **full** | Indicates if an action takes a ‘raw’ or ‘free form’ string as an option and has it’s own special parsing of it |

## [Notes](command_module.md#id4)

> **Note:**
>
> - If you want to run a command through the shell (say you are using `<`, `>`, `|`, and so on), you actually want the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) module instead. Parsing shell metacharacters can lead to unexpected commands being executed if quoting is not done correctly so it is more secure to use the `command` module when possible.
> - `creates`, `removes`, and `chdir` can be specified after the command. For instance, if you only want to run a command if a certain file does not exist, use this.
> - Check mode is supported when passing `creates` or `removes`. If running in check mode and either of these are specified, the module will check for the existence of the file and report the correct changed status. If these are not supplied, the task will be skipped.
> - The `executable` parameter is removed since version 2.4. If you have a need for this parameter, use the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) module instead.
> - For Windows targets, use the [ansible.windows.win_command](../windows/win_command_module.md#ansible-collections-ansible-windows-win-command-module) module instead.
> - For rebooting systems, use the [ansible.builtin.reboot](reboot_module.md#ansible-collections-ansible-builtin-reboot-module) or [ansible.windows.win_reboot](../windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) module.
> - If the command returns non UTF-8 data, it must be encoded to avoid issues. This may necessitate using [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) so the output can be piped through `base64`.

## [See Also](command_module.md#id5)

> **See also:**
>
> [ansible.builtin.raw](raw_module.md#ansible-collections-ansible-builtin-raw-module)
> :   Executes a low-down and dirty command.
>
> [ansible.builtin.script](script_module.md#ansible-collections-ansible-builtin-script-module)
> :   Runs a local script on a remote node after transferring it.
>
> [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module)
> :   Execute shell commands on targets.
>
> [ansible.windows.win_command](../windows/win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.

## [Examples](command_module.md#id6)

```yaml+jinja
- name: Return motd to registered var
  ansible.builtin.command: cat /etc/motd
  register: mymotd

# free-form (string) arguments, all arguments on one line
- name: Run command if /path/to/database does not exist (without 'args')
  ansible.builtin.command: /usr/bin/make_database.sh db_user db_name creates=/path/to/database

# free-form (string) arguments, some arguments on separate lines with the 'args' keyword
# 'args' is a task keyword, passed at the same level as the module
- name: Run command if /path/to/database does not exist (with 'args' keyword)
  ansible.builtin.command: /usr/bin/make_database.sh db_user db_name
  args:
    creates: /path/to/database

# 'cmd' is module parameter
- name: Run command if /path/to/database does not exist (with 'cmd' parameter)
  ansible.builtin.command:
    cmd: /usr/bin/make_database.sh db_user db_name
    creates: /path/to/database

- name: Change the working directory to somedir/ and run the command as db_owner if /path/to/database does not exist
  ansible.builtin.command: /usr/bin/make_database.sh db_user db_name
  become: yes
  become_user: db_owner
  args:
    chdir: somedir/
    creates: /path/to/database

# argv (list) arguments, each argument on a separate line, 'args' keyword not necessary
# 'argv' is a parameter, indented one level from the module
- name: Use 'argv' to send a command as a list - leave 'command' empty
  ansible.builtin.command:
    argv:
      - /usr/bin/make_database.sh
      - Username with whitespace
      - dbname with whitespace
    creates: /path/to/database

- name: Safely use templated variable to run command. Always use the quote filter to avoid injection issues
  ansible.builtin.command: cat {{ myfile|quote }}
  register: myoutput
```

## [Return Values](command_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  list / elements=string | The command executed by the task.  **Returned:** always  **Sample:** `["echo", "hello"]` |
| **delta**  string | The command execution delta time.  **Returned:** always  **Sample:** `"0:00:00.001529"` |
| **end**  string | The command execution end time.  **Returned:** always  **Sample:** `"2017-09-29 22:03:48.084657"` |
| **msg**  boolean | changed  **Returned:** always  **Sample:** `true` |
| **rc**  integer | The command return code (0 means success).  **Returned:** always  **Sample:** `0` |
| **start**  string | The command execution start time.  **Returned:** always  **Sample:** `"2017-09-29 22:03:48.083128"` |
| **stderr**  string | The command standard error.  **Returned:** always  **Sample:** `"ls cannot access foo: No such file or directory"` |
| **stderr_lines**  list / elements=string | The command standard error split in lines.  **Returned:** always  **Sample:** `[{"u'ls cannot access foo": "No such file or directory'"}, "u'ls \u2026'"]` |
| **stdout**  string | The command standard output.  **Returned:** always  **Sample:** `"Clustering node rabbit@slave1 with rabbit@master \u2026"` |
| **stdout_lines**  list / elements=string | The command standard output split in lines.  **Returned:** always  **Sample:** `["u'Clustering node rabbit@slave1 with rabbit@master \u2026'"]` |

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
