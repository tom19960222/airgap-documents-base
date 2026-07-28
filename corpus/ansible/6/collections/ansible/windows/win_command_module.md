---
collection: ansible
version: "6"
title: "ansible.windows.win_command module – Executes a command on a remote Windows node"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_command_module.html
fetched_at: 2026-07-27T16:44:52+00:00
---
# ansible.windows.win_command module – Executes a command on a remote Windows node

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_command`.

- [Synopsis](win_command_module.md#synopsis)
- [Parameters](win_command_module.md#parameters)
- [Notes](win_command_module.md#notes)
- [See Also](win_command_module.md#see-also)
- [Examples](win_command_module.md#examples)
- [Return Values](win_command_module.md#return-values)

## [Synopsis](win_command_module.md#id1)

- The `win_command` module takes the command name followed by a list of space-delimited arguments.
- The given command will be executed on all selected nodes. It will not be processed through the shell, so variables like `$env:HOME` and operations like `"<"`, `">"`, `"|"`, and `";"` will not work (use the [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) module if you need these features).
- For non-Windows targets, use the [ansible.builtin.command](../builtin/command_module.md#ansible-collections-ansible-builtin-command-module) module instead.

## [Parameters](win_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **_raw_params**  string | The `win_command` module takes a free form command to run.  This is mutually exclusive with the `cmd` and `argv` options.  There is no parameter actually named ‘_raw_params’. See the examples! |
| **argv**  list / elements=string  added in ansible.windows 1.11.0 | A list that contains the executable and arguments to run.  The module will attempt to quote the arguments specified based on the [Win32 C command-line argument rules](https://docs.microsoft.com/en-us/cpp/c-language/parsing-c-command-line-arguments).  Not all applications use the same quoting rules so the escaping may not work, for those scenarios use `cmd` instead. |
| **chdir**  path | Set the specified path as the current working directory before executing a command. |
| **cmd**  string  added in ansible.windows 1.11.0 | The command and arguments to run.  This is mutually exclusive with the `_raw_params` and `argv` options. |
| **creates**  path | A path or path filter pattern; when the referenced path exists on the target host, the task will be skipped. |
| **output_encoding_override**  string | This option overrides the encoding of stdout/stderr output.  You can use this option when you need to run a command which ignore the console’s codepage.  You should only need to use this option in very rare circumstances.  This value can be any valid encoding `Name` based on the output of `[System.Text.Encoding]::GetEncodings(`). See <https://docs.microsoft.com/dotnet/api/system.text.encoding.getencodings>. |
| **removes**  path | A path or path filter pattern; when the referenced path **does not** exist on the target host, the task will be skipped. |
| **stdin**  string | Set the stdin of the command directly to the specified value. |

## [Notes](win_command_module.md#id3)

> **Note:**
>
> - If you want to run a command through a shell (say you are using `<`, `>`, `|`, etc), you actually want the [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) module instead. The [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module) module is much more secure as it’s not affected by the user’s environment.
> - `creates`, `removes`, and `chdir` can be specified after the command. For instance, if you only want to run a command if a certain file does not exist, use this.
> - Do not try to use the older style free form format and the newer style cmd/argv format. See the examples for how both of these formats are defined.

## [See Also](win_command_module.md#id4)

> **See also:**
>
> [ansible.builtin.command](../builtin/command_module.md#ansible-collections-ansible-builtin-command-module)
> :   Execute commands on targets.
>
> [community.windows.psexec](../../community/windows/psexec_module.md#ansible-collections-community-windows-psexec-module)
> :   Runs commands on a remote Windows host based on the PsExec model.
>
> [ansible.builtin.raw](../builtin/raw_module.md#ansible-collections-ansible-builtin-raw-module)
> :   Executes a low-down and dirty command.
>
> [community.windows.win_psexec](../../community/windows/win_psexec_module.md#ansible-collections-community-windows-win-psexec-module)
> :   Runs commands (remotely) as another (privileged) user.
>
> [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](win_command_module.md#id5)

```yaml+jinja
# Older style using the free-form and args format. The command is on the same
# line as the module and 'args' is used to define the options for win_command.
- name: Save the result of 'whoami' in 'whoami_out'
  ansible.windows.win_command: whoami
  register: whoami_out

- name: Run command that only runs if folder exists and runs from a specific folder
  ansible.windows.win_command: wbadmin -backupTarget:C:\backup\
  args:
    chdir: C:\somedir\
    creates: C:\backup\

- name: Run an executable and send data to the stdin for the executable
  ansible.windows.win_command: powershell.exe -
  args:
    stdin: Write-Host test

# Newer style using module options. The command and other arguments are
# defined as module options and are indended like another other module.
- name: Run the 'whoami' executable with the '/all' argument
  ansible.windows.win_command:
    cmd: whoami.exe /all

- name: Run executable in 'C:\Program Files' with a custom chdir
  ansible.windows.win_command:
    # When using cmd, the arguments need to be quoted manually
    cmd: '"C:\Program Files\My Application\run.exe" "argument 1" -force'
    chdir: C:\Windows\TEMP

- name: Run executable using argv and have win_command escape the spaces as needed
  ansible.windows.win_command:
    # When using argv, each entry is quoted in the module
    argv:
    - C:\Program Files\My Application\run.exe
    - argument 1
    - -force
```

## [Return Values](win_command_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | The command executed by the task  Returned: always  Sample: `"rabbitmqctl join_cluster rabbit@main"` |
| **delta**  string | The command execution delta time  Returned: always  Sample: `"0:00:00.325771"` |
| **end**  string | The command execution end time  Returned: always  Sample: `"2016-02-25 09:18:26.755339"` |
| **msg**  boolean | changed  Returned: always  Sample: `true` |
| **rc**  integer | The command return code (0 means success)  Returned: always  Sample: `0` |
| **start**  string | The command execution start time  Returned: always  Sample: `"2016-02-25 09:18:26.429568"` |
| **stderr**  string | The command standard error  Returned: always  Sample: `"ls: cannot access foo: No such file or directory"` |
| **stdout**  string | The command standard output  Returned: always  Sample: `"Clustering node rabbit@slave1 with rabbit@main ..."` |
| **stdout_lines**  list / elements=string | The command standard output split in lines  Returned: always  Sample: `["u'Clustering node rabbit@slave1 with rabbit@main ...'"]` |

### Authors

- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
