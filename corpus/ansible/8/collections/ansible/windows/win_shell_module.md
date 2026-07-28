---
collection: ansible
version: "8"
title: "ansible.windows.win_shell module – Execute shell commands on target hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_shell_module.html
fetched_at: 2026-07-28T01:10:49+00:00
---
# ansible.windows.win_shell module – Execute shell commands on target hosts

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_shell`.

- [Synopsis](win_shell_module.md#synopsis)
- [Parameters](win_shell_module.md#parameters)
- [Notes](win_shell_module.md#notes)
- [See Also](win_shell_module.md#see-also)
- [Examples](win_shell_module.md#examples)
- [Return Values](win_shell_module.md#return-values)

## [Synopsis](win_shell_module.md#id1)

- The [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) module takes the command name followed by a list of space-delimited arguments. It is similar to the [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module) module, but runs the command via a shell (defaults to PowerShell) on the target host.
- For non-Windows targets, use the [ansible.builtin.shell](../builtin/shell_module.md#ansible-collections-ansible-builtin-shell-module) module instead.

## [Parameters](win_shell_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **chdir**  path | Set the specified path as the current working directory before executing a command |
| **creates**  path | A path or path filter pattern; when the referenced path exists on the target host, the task will be skipped. |
| **executable**  path | Change the shell used to execute the command (eg, `cmd`).  The target shell must accept a `/c` parameter followed by the raw command line to be executed. |
| **free_form**  string / required | The [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) module takes a free form command to run.  There is no parameter actually named ‘free form’. See the examples! |
| **no_profile**  boolean | Do not load the user profile before running a command. This is only valid when using PowerShell as the executable.  **Choices:**   - `false` ← (default) - `true` |
| **output_encoding_override**  string | This option overrides the encoding of stdout/stderr output.  You can use this option when you need to run a command which ignore the console’s codepage.  You should only need to use this option in very rare circumstances.  This value can be any valid encoding `Name` based on the output of `[System.Text.Encoding]::GetEncodings(`). See <https://docs.microsoft.com/dotnet/api/system.text.encoding.getencodings>. |
| **removes**  path | A path or path filter pattern; when the referenced path **does not** exist on the target host, the task will be skipped. |
| **stdin**  string | Set the stdin of the command directly to the specified value. |

## [Notes](win_shell_module.md#id3)

> **Note:**
>
> - If you want to run an executable securely and predictably, it may be better to use the [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module) module instead. Best practices when writing playbooks will follow the trend of using [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module) unless `win_shell` is explicitly required. When running ad-hoc commands, use your best judgement.
> - WinRM will not return from a command execution until all child processes created have exited. Thus, it is not possible to use [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module) to spawn long-running child or background processes. Consider creating a Windows service for managing background processes. - Consider using [ansible.windows.win_powershell](win_powershell_module.md#ansible-collections-ansible-windows-win-powershell-module) if you want to capture the output from the PowerShell script as structured objects.

## [See Also](win_shell_module.md#id4)

> **See also:**
>
> [community.windows.psexec](../../community/windows/psexec_module.md#ansible-collections-community-windows-psexec-module)
> :   Runs commands on a remote Windows host based on the PsExec model.
>
> [ansible.builtin.raw](../builtin/raw_module.md#ansible-collections-ansible-builtin-raw-module)
> :   Executes a low-down and dirty command.
>
> [ansible.builtin.script](../builtin/script_module.md#ansible-collections-ansible-builtin-script-module)
> :   Runs a local script on a remote node after transferring it.
>
> [ansible.builtin.shell](../builtin/shell_module.md#ansible-collections-ansible-builtin-shell-module)
> :   Execute shell commands on targets.
>
> [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.
>
> [ansible.windows.win_powershell](win_powershell_module.md#ansible-collections-ansible-windows-win-powershell-module)
> :   Run PowerShell scripts.
>
> [community.windows.win_psexec](../../community/windows/win_psexec_module.md#ansible-collections-community-windows-win-psexec-module)
> :   Runs commands (remotely) as another (privileged) user.

## [Examples](win_shell_module.md#id5)

```yaml+jinja
- name: Execute a command in the remote shell, stdout goes to the specified file on the remote
  ansible.windows.win_shell: C:\somescript.ps1 >> C:\somelog.txt

- name: Change the working directory to somedir/ before executing the command
  ansible.windows.win_shell: C:\somescript.ps1 >> C:\somelog.txt
  args:
    chdir: C:\somedir

- name: Run a command with an idempotent check on what it creates, will only run when somedir/somelog.txt does not exist
  ansible.windows.win_shell: C:\somescript.ps1 >> C:\somelog.txt
  args:
    chdir: C:\somedir
    creates: C:\somelog.txt

- name: Run a command under a non-Powershell interpreter (cmd in this case)
  ansible.windows.win_shell: echo %HOMEDIR%
  args:
    executable: cmd
  register: homedir_out

- name: Run multi-lined shell commands
  ansible.windows.win_shell: |
    $value = Test-Path -Path C:\temp
    if ($value) {
        Remove-Item -Path C:\temp -Force
    }
    New-Item -Path C:\temp -ItemType Directory

- name: Retrieve the input based on stdin
  ansible.windows.win_shell: '$string = [Console]::In.ReadToEnd(); Write-Output $string.Trim()'
  args:
    stdin: Input message
```

## [Return Values](win_shell_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | The command executed by the task.  **Returned:** always  **Sample:** `"rabbitmqctl join_cluster rabbit@main"` |
| **delta**  string | The command execution delta time.  **Returned:** always  **Sample:** `"0:00:00.325771"` |
| **end**  string | The command execution end time.  **Returned:** always  **Sample:** `"2016-02-25 09:18:26.755339"` |
| **msg**  boolean | Changed.  **Returned:** always  **Sample:** `true` |
| **rc**  integer | The command return code (0 means success).  **Returned:** always  **Sample:** `0` |
| **start**  string | The command execution start time.  **Returned:** always  **Sample:** `"2016-02-25 09:18:26.429568"` |
| **stderr**  string | The command standard error.  **Returned:** always  **Sample:** `"ls: cannot access foo: No such file or directory"` |
| **stdout**  string | The command standard output.  **Returned:** always  **Sample:** `"Clustering node rabbit@slave1 with rabbit@main ..."` |
| **stdout_lines**  list / elements=string | The command standard output split in lines.  **Returned:** always  **Sample:** `["u'Clustering node rabbit@slave1 with rabbit@main ...'"]` |

### Authors

- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
