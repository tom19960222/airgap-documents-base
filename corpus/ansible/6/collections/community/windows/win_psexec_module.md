---
collection: ansible
version: "6"
title: "community.windows.win_psexec module – Runs commands (remotely) as another (privileged) user"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_psexec_module.html
fetched_at: 2026-07-27T17:23:42+00:00
---
# community.windows.win_psexec module – Runs commands (remotely) as another (privileged) user

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_psexec_module.md#ansible-collections-community-windows-win-psexec-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_psexec`.

- [Synopsis](win_psexec_module.md#synopsis)
- [Requirements](win_psexec_module.md#requirements)
- [Parameters](win_psexec_module.md#parameters)
- [Notes](win_psexec_module.md#notes)
- [See Also](win_psexec_module.md#see-also)
- [Examples](win_psexec_module.md#examples)
- [Return Values](win_psexec_module.md#return-values)

## [Synopsis](win_psexec_module.md#id1)

- Run commands (remotely) through the PsExec service.
- Run commands as another (domain) user (with elevated privileges).

## [Requirements](win_psexec_module.md#id2)

The below requirements are needed on the host that executes this module.

- Microsoft PsExec

## [Parameters](win_psexec_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chdir**  path | Run the command from this (remote) directory. |
| **command**  string / required | The command line to run through PsExec (limited to 260 characters). |
| **elevated**  boolean | Run the command with elevated privileges.  Choices:   - `false` ← (default) - `true` |
| **executable**  path | The location of the PsExec utility (in case it is not located in your PATH).  Default: `"psexec.exe"` |
| **hostnames**  list / elements=string | The hostnames to run the command.  If not provided, the command is run locally. |
| **interactive**  boolean | Run the program so that it interacts with the desktop on the remote system.  Choices:   - `false` ← (default) - `true` |
| **limited**  boolean | Run the command as limited user (strips the Administrators group and allows only privileges assigned to the Users group).  Choices:   - `false` ← (default) - `true` |
| **nobanner**  boolean | Do not display the startup banner and copyright message.  This only works for specific versions of the PsExec binary.  Choices:   - `false` ← (default) - `true` |
| **noprofile**  boolean | Run the command without loading the account’s profile.  Choices:   - `false` ← (default) - `true` |
| **password**  string | The password for the (remote) user to run the command as.  This is mandatory in order authenticate yourself. |
| **priority**  string | Used to run the command at a different priority.  Choices:   - `"abovenormal"` - `"background"` - `"belownormal"` - `"high"` - `"low"` - `"realtime"` |
| **session**  integer | Specifies the session ID to use.  This parameter works in conjunction with *interactive*.  It has no effect when *interactive* is set to `no`. |
| **system**  boolean | Run the remote command in the System account.  Choices:   - `false` ← (default) - `true` |
| **timeout**  integer | The connection timeout in seconds |
| **username**  string | The (remote) user to run the command as.  If not provided, the current user is used. |
| **wait**  boolean | Wait for the application to terminate.  Only use for non-interactive applications.  Choices:   - `false` - `true` ← (default) |

## [Notes](win_psexec_module.md#id4)

> **Note:**
>
> - More information related to Microsoft PsExec is available from <https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx>

## [See Also](win_psexec_module.md#id5)

> **See also:**
>
> [community.windows.psexec](psexec_module.md#ansible-collections-community-windows-psexec-module)
> :   Runs commands on a remote Windows host based on the PsExec model.
>
> [ansible.builtin.raw](../../ansible/builtin/raw_module.md#ansible-collections-ansible-builtin-raw-module)
> :   Executes a low-down and dirty command.
>
> [ansible.windows.win_command](../../ansible/windows/win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.
>
> [ansible.windows.win_shell](../../ansible/windows/win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](win_psexec_module.md#id6)

```yaml+jinja
- name: Test the PsExec connection to the local system (target node) with your user
  community.windows.win_psexec:
    command: whoami.exe

- name: Run regedit.exe locally (on target node) as SYSTEM and interactively
  community.windows.win_psexec:
    command: regedit.exe
    interactive: yes
    system: yes

- name: Run the setup.exe installer on multiple servers using the Domain Administrator
  community.windows.win_psexec:
    command: E:\setup.exe /i /IACCEPTEULA
    hostnames:
    - remote_server1
    - remote_server2
    username: DOMAIN\Administrator
    password: some_password
    priority: high

- name: Run PsExec from custom location C:\Program Files\sysinternals\
  community.windows.win_psexec:
    command: netsh advfirewall set allprofiles state off
    executable: C:\Program Files\sysinternals\psexec.exe
    hostnames: [ remote_server ]
    password: some_password
    priority: low
```

## [Return Values](win_psexec_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | The complete command line used by the module, including PsExec call and additional options.  Returned: always  Sample: `"psexec.exe -nobanner \\\\remote_server -u \"DOMAIN\\Administrator\" -p \"some_password\" -accepteula E:\\setup.exe"` |
| **pid**  integer | The PID of the async process created by PsExec.  Returned: when `wait=False`  Sample: `1532` |
| **rc**  integer | The return code for the command.  Returned: always  Sample: `0` |
| **stderr**  string | The error output from the command.  Returned: always  Sample: `"Error 15 running E:\\setup.exe"` |
| **stdout**  string | The standard output from the command.  Returned: always  Sample: `"Success."` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
