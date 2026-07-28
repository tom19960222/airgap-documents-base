---
collection: ansible
version: "6"
title: "community.windows.psexec module – Runs commands on a remote Windows host based on the PsExec model"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/psexec_module.html
fetched_at: 2026-07-27T17:23:08+00:00
---
# community.windows.psexec module – Runs commands on a remote Windows host based on the PsExec model

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
> see [Requirements](psexec_module.md#ansible-collections-community-windows-psexec-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.psexec`.

- [Synopsis](psexec_module.md#synopsis)
- [Requirements](psexec_module.md#requirements)
- [Parameters](psexec_module.md#parameters)
- [Notes](psexec_module.md#notes)
- [See Also](psexec_module.md#see-also)
- [Examples](psexec_module.md#examples)
- [Return Values](psexec_module.md#return-values)

## [Synopsis](psexec_module.md#id1)

- Runs a remote command from a Linux host to a Windows host without WinRM being set up.
- Can be run on the Ansible controller to bootstrap Windows hosts to get them ready for WinRM.

## [Requirements](psexec_module.md#id2)

The below requirements are needed on the host that executes this module.

- pypsexec
- smbprotocol[kerberos] for optional Kerberos authentication

## [Parameters](psexec_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arguments**  string | Any arguments as a single string to use when running the executable. |
| **asynchronous**  boolean | Will run the command as a detached process and the module returns immediately after starting the process while the process continues to run in the background.  The *stdout* and *stderr* return values will be null when this is set to `yes`.  The *stdin* option does not work with this type of process.  The *rc* return value is not set when this is `yes`  Choices:   - `false` ← (default) - `true` |
| **connection_password**  string | The password for *connection_user*.  Required if the Kerberos requirements are not installed or the username is a local account to the Windows host.  Can be omitted to use a Kerberos principal ticket for the principal set by *connection_user* if the Kerberos library is installed and the ticket has already been retrieved with the `kinit` command before. |
| **connection_timeout**  integer | The timeout in seconds to wait when receiving the initial SMB negotiate response from the server.  Default: `60` |
| **connection_username**  string | The username to use when connecting to the remote Windows host.  This user must be a member of the `Administrators` group of the Windows host.  Required if the Kerberos requirements are not installed or the username is a local account to the Windows host.  Can be omitted to use the default Kerberos principal ticket in the local credential cache if the Kerberos library is installed.  If *process_username* is not specified, then the remote process will run under a Network Logon under this account. |
| **encrypt**  boolean | Will use SMB encryption to encrypt the SMB messages sent to and from the host.  This requires the SMB 3 protocol which is only supported from Windows Server 2012 or Windows 8, older versions like Windows 7 or Windows Server 2008 (R2) must set this to `no` and use no encryption.  When setting to `no`, the packets are in plaintext and can be seen by anyone sniffing the network, any process options are included in this.  Choices:   - `false` - `true` ← (default) |
| **executable**  string / required | The executable to run on the Windows host. |
| **hostname**  string / required | The remote Windows host to connect to, can be either an IP address or a hostname. |
| **integrity_level**  string | The integrity level of the process when *process_username* is defined and is not equal to `System`.  When `default`, the default integrity level based on the system setup.  When `elevated`, the command will be run with Administrative rights.  When `limited`, the command will be forced to run with non-Administrative rights.  Choices:   - `"limited"` - `"default"` ← (default) - `"elevated"` |
| **interactive**  boolean | Will run the process as an interactive process that shows a process Window of the Windows session specified by *interactive_session*.  The *stdout* and *stderr* return values will be null when this is set to `yes`.  The *stdin* option does not work with this type of process.  Choices:   - `false` ← (default) - `true` |
| **interactive_session**  integer | The Windows session ID to use when displaying the interactive process on the remote Windows host.  This is only valid when *interactive* is `yes`.  The default is `0` which is the console session of the Windows host.  Default: `0` |
| **load_profile**  boolean | Runs the remote command with the user’s profile loaded.  Choices:   - `false` - `true` ← (default) |
| **port**  integer | The port that the remote SMB service is listening on.  Default: `445` |
| **priority**  string | Set the command’s priority on the Windows host.  See <https://msdn.microsoft.com/en-us/library/windows/desktop/ms683211.aspx> for more details.  Choices:   - `"above_normal"` - `"below_normal"` - `"high"` - `"idle"` - `"normal"` ← (default) - `"realtime"` |
| **process_password**  string | The password for *process_username*.  Required if *process_username* is defined and not `System`. |
| **process_timeout**  integer | The timeout in seconds that is placed upon the running process.  A value of `0` means no timeout.  Default: `0` |
| **process_username**  string | The user to run the process as.  This can be set to run the process under an Interactive logon of the specified account which bypasses limitations of a Network logon used when this isn’t specified.  If omitted then the process is run under the same account as *connection_username* with a Network logon.  Set to `System` to run as the builtin SYSTEM account, no password is required with this account.  If *encrypt* is `no`, the username and password are sent as a simple XOR scrambled byte string that is not encrypted. No special tools are required to get the username and password just knowledge of the protocol. |
| **show_ui_on_logon_screen**  boolean | Shows the process UI on the Winlogon secure desktop when *process_username* is `System`.  Choices:   - `false` ← (default) - `true` |
| **stdin**  string | Data to send on the stdin pipe once the process has started.  This option has no effect when *interactive* or *asynchronous* is `yes`. |
| **working_directory**  string | Changes the working directory set when starting the process.  Default: `"C:\\Windows\\System32"` |

## [Notes](psexec_module.md#id4)

> **Note:**
>
> - This module requires the Windows host to have SMB configured and enabled, and port 445 opened on the firewall.
> - This module will wait until the process is finished unless *asynchronous* is `yes`, ensure the process is run as a non-interactive command to avoid infinite hangs waiting for input.
> - The *connection_username* must be a member of the local Administrator group of the Windows host. For non-domain joined hosts, the `LocalAccountTokenFilterPolicy` should be set to `1` to ensure this works, see <https://support.microsoft.com/en-us/help/951016/description-of-user-account-control-and-remote-restrictions-in-windows>.
> - For more information on this module and the various host requirements, see <https://github.com/jborean93/pypsexec>.

## [See Also](psexec_module.md#id5)

> **See also:**
>
> [ansible.builtin.raw](../../ansible/builtin/raw_module.md#ansible-collections-ansible-builtin-raw-module)
> :   Executes a low-down and dirty command.
>
> [ansible.windows.win_command](../../ansible/windows/win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.
>
> [community.windows.win_psexec](win_psexec_module.md#ansible-collections-community-windows-win-psexec-module)
> :   Runs commands (remotely) as another (privileged) user.
>
> [ansible.windows.win_shell](../../ansible/windows/win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](psexec_module.md#id6)

```yaml+jinja
- name: Run a cmd.exe command
  community.windows.psexec:
    hostname: server
    connection_username: username
    connection_password: password
    executable: cmd.exe
    arguments: /c echo Hello World

- name: Run a PowerShell command
  community.windows.psexec:
    hostname: server.domain.local
    connection_username: username@DOMAIN.LOCAL
    connection_password: password
    executable: powershell.exe
    arguments: Write-Host Hello World

- name: Send data through stdin
  community.windows.psexec:
    hostname: 192.168.1.2
    connection_username: username
    connection_password: password
    executable: powershell.exe
    arguments: '-'
    stdin: |
      Write-Host Hello World
      Write-Error Error Message
      exit 0

- name: Run the process as a different user
  community.windows.psexec:
    hostname: server
    connection_user: username
    connection_password: password
    executable: whoami.exe
    arguments: /all
    process_username: anotheruser
    process_password: anotherpassword

- name: Run the process asynchronously
  community.windows.psexec:
    hostname: server
    connection_username: username
    connection_password: password
    executable: cmd.exe
    arguments: /c rmdir C:\temp
    asynchronous: yes

- name: Use Kerberos authentication for the connection (requires smbprotocol[kerberos])
  community.windows.psexec:
    hostname: host.domain.local
    connection_username: user@DOMAIN.LOCAL
    executable: C:\some\path\to\executable.exe
    arguments: /s

- name: Disable encryption to work with WIndows 7/Server 2008 (R2)
  community.windows.psexec:
    hostanme: windows-pc
    connection_username: Administrator
    connection_password: Password01
    encrypt: no
    integrity_level: elevated
    process_username: Administrator
    process_password: Password01
    executable: powershell.exe
    arguments: (New-Object -ComObject Microsoft.Update.Session).CreateUpdateInstaller().IsBusy

- name: Download and run ConfigureRemotingForAnsible.ps1 to setup WinRM
  community.windows.psexec:
    hostname: '{{ hostvars[inventory_hostname]["ansible_host"] | default(inventory_hostname) }}'
    connection_username: '{{ ansible_user }}'
    connection_password: '{{ ansible_password }}'
    encrypt: yes
    executable: powershell.exe
    arguments: '-'
    stdin: |
      $ErrorActionPreference = "Stop"
      $sec_protocols = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::SystemDefault
      $sec_protocols = $sec_protocols -bor [Net.SecurityProtocolType]::Tls12
      [Net.ServicePointManager]::SecurityProtocol = $sec_protocols
      $url = "https://github.com/ansible/ansible/raw/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
      Invoke-Expression ((New-Object Net.WebClient).DownloadString($url))
      exit
  delegate_to: localhost
```

## [Return Values](psexec_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Any exception details when trying to run the process  Returned: module failed  Sample: `"Received exception from remote PAExec service: Failed to start \"invalid.exe\". The system cannot find the file specified. [Err=0x2, 2]"` |
| **pid**  integer | The process ID of the asynchronous process that was created  Returned: success and asynchronous is ‘yes’  Sample: `719` |
| **rc**  integer | The return code of the remote process  Returned: success and asynchronous is ‘no’  Sample: `0` |
| **stderr**  string | The stderr from the remote process  Returned: success and interactive or asynchronous is ‘no’  Sample: `"Error [10] running process"` |
| **stdout**  string | The stdout from the remote process  Returned: success and interactive or asynchronous is ‘no’  Sample: `"Hello World"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
