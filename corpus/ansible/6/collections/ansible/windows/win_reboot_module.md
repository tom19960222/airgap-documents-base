---
collection: ansible
version: "6"
title: "ansible.windows.win_reboot module – Reboot a windows machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_reboot_module.html
fetched_at: 2026-07-27T16:45:00+00:00
---
# ansible.windows.win_reboot module – Reboot a windows machine

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
> To use it in a playbook, specify: `ansible.windows.win_reboot`.

- [Synopsis](win_reboot_module.md#synopsis)
- [Parameters](win_reboot_module.md#parameters)
- [Notes](win_reboot_module.md#notes)
- [See Also](win_reboot_module.md#see-also)
- [Examples](win_reboot_module.md#examples)
- [Return Values](win_reboot_module.md#return-values)

## [Synopsis](win_reboot_module.md#id1)

- Unconditionally reboot a Windows machine, wait for it to go down, come back up, and respond to commands.
- For non-Windows targets, use the [ansible.builtin.reboot](../builtin/reboot_module.md#ansible-collections-ansible-builtin-reboot-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](win_reboot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **boot_time_command**  string | Command to run that returns a unique string indicating the last time the system was booted.  Setting this to a command that has different output each time it is run will cause the task to fail.  Default: `"(Get-CimInstance -ClassName Win32_OperatingSystem -Property LastBootUpTime).LastBootUpTime.ToFileTime()"` |
| **connect_timeout**  aliases: connect_timeout_sec  float | Maximum seconds to wait for a single successful TCP connection to the WinRM endpoint before trying again.  Default: `5.0` |
| **msg**  string | Message to display to users.  Default: `"Reboot initiated by Ansible"` |
| **post_reboot_delay**  aliases: post_reboot_delay_sec  float | Seconds to wait after the reboot command was successful before attempting to validate the system rebooted successfully.  This is useful if you want wait for something to settle despite your connection already working.  Default: `0.0` |
| **pre_reboot_delay**  aliases: pre_reboot_delay_sec  float | Seconds to wait before reboot. Passed as a parameter to the reboot command.  The minimum version is `2` seconds and cannot be set lower.  Default: `2.0` |
| **reboot_timeout**  aliases: reboot_timeout_sec  float | Maximum seconds to wait for machine to re-appear on the network and respond to a test command.  This timeout is evaluated separately for both reboot verification and test command success so maximum clock time is actually twice this value.  Default: `600.0` |
| **test_command**  string | Command to expect success for to determine the machine is ready for management.  By default this test command is a custom one to detect when the Windows Logon screen is up and ready to accept credentials. Using a custom command will replace this behaviour and just run the command specified. |

## [Notes](win_reboot_module.md#id3)

> **Note:**
>
> - If a shutdown was already scheduled on the system, [ansible.windows.win_reboot](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) will abort the scheduled shutdown and enforce its own shutdown.
> - Beware that when [ansible.windows.win_reboot](win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) returns, the Windows system may not have settled yet and some base services could be in limbo. This can result in unexpected behavior. Check the examples for ways to mitigate this. This has been slightly mitigated in the `1.6.0` release of `ansible.windows` but it is not guranteed to always wait until the logon prompt is shown.
> - The connection user must have the `SeRemoteShutdownPrivilege` privilege enabled, see <https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/force-shutdown-from-a-remote-system> for more information.
> - This module is equivalent to using the /f forced option for reboot on a windows host

## [See Also](win_reboot_module.md#id4)

> **See also:**
>
> [ansible.builtin.reboot](../builtin/reboot_module.md#ansible-collections-ansible-builtin-reboot-module)
> :   Reboot a machine.

## [Examples](win_reboot_module.md#id5)

```yaml+jinja
- name: Reboot the machine with all defaults
  ansible.windows.win_reboot:

- name: Reboot a slow machine that might have lots of updates to apply
  ansible.windows.win_reboot:
    reboot_timeout: 3600

# Install a Windows feature and reboot if necessary
- name: Install IIS Web-Server
  ansible.windows.win_feature:
    name: Web-Server
  register: iis_install

- name: Reboot when Web-Server feature requires it
  ansible.windows.win_reboot:
  when: iis_install.reboot_required

# One way to ensure the system is reliable, is to set WinRM to a delayed startup
- name: Ensure WinRM starts when the system has settled and is ready to work reliably
  ansible.windows.win_service:
    name: WinRM
    start_mode: delayed

# Additionally, you can add a delay before running the next task
- name: Reboot a machine that takes time to settle after being booted
  ansible.windows.win_reboot:
    post_reboot_delay: 120

# Or you can make win_reboot validate exactly what you need to work before running the next task
- name: Validate that the netlogon service has started, before running the next task
  ansible.windows.win_reboot:
    test_command: 'exit (Get-Service -Name Netlogon).Status -ne "Running"'
```

## [Return Values](win_reboot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  float | The number of seconds that elapsed waiting for the system to be rebooted.  Returned: always  Sample: `23.2` |
| **rebooted**  boolean | True if the machine was rebooted.  Returned: always  Sample: `true` |

### Authors

- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
