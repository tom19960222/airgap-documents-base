---
collection: ansible
version: "8"
title: "ansible.builtin.reboot module – Reboot a machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/reboot_module.html
fetched_at: 2026-07-28T01:07:40+00:00
---
# ansible.builtin.reboot module – Reboot a machine

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `reboot` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.reboot` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

New in Ansible 2.7

- [Synopsis](reboot_module.md#synopsis)
- [Parameters](reboot_module.md#parameters)
- [Attributes](reboot_module.md#attributes)
- [Notes](reboot_module.md#notes)
- [See Also](reboot_module.md#see-also)
- [Examples](reboot_module.md#examples)
- [Return Values](reboot_module.md#return-values)

## [Synopsis](reboot_module.md#id1)

- Reboot a machine, wait for it to go down, come back up, and respond to commands.
- For Windows targets, use the [ansible.windows.win_reboot](../windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](reboot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **boot_time_command**  string  *added in ansible-base 2.10* | Command to run that returns a unique string indicating the last time the system was booted.  Setting this to a command that has different output each time it is run will cause the task to fail.  **Default:** `"cat /proc/sys/kernel/random/boot_id"` |
| **connect_timeout**  integer | Maximum seconds to wait for a successful connection to the managed hosts before trying again.  If unspecified, the default setting for the underlying connection plugin is used. |
| **msg**  string | Message to display to users before reboot.  **Default:** `"Reboot initiated by Ansible"` |
| **post_reboot_delay**  integer | Seconds to wait after the reboot command was successful before attempting to validate the system rebooted successfully.  This is useful if you want wait for something to settle despite your connection already working.  **Default:** `0` |
| **pre_reboot_delay**  integer | Seconds to wait before reboot. Passed as a parameter to the reboot command.  On Linux, macOS and OpenBSD, this is converted to minutes and rounded down. If less than 60, it will be set to 0.  On Solaris and FreeBSD, this will be seconds.  **Default:** `0` |
| **reboot_command**  string  *added in ansible-core 2.11* | Command to run that reboots the system, including any parameters passed to the command.  Can be an absolute path to the command or just the command name. If an absolute path to the command is not given, `search_paths` on the target system will be searched to find the absolute path.  This will cause `pre_reboot_delay`, `post_reboot_delay`, and `msg` to be ignored.  **Default:** `"[determined based on target OS]"` |
| **reboot_timeout**  integer | Maximum seconds to wait for machine to reboot and respond to a test command.  This timeout is evaluated separately for both reboot verification and test command success so the maximum execution time for the module is twice this amount.  **Default:** `600` |
| **search_paths**  list / elements=string  *added in Ansible 2.8* | Paths to search on the remote machine for the `shutdown` command.  *Only* these paths will be searched for the `shutdown` command. `PATH` is ignored in the remote node when searching for the `shutdown` command.  **Default:** `["/sbin", "/bin", "/usr/sbin", "/usr/bin", "/usr/local/sbin"]` |
| **test_command**  string | Command to run on the rebooted host and expect success from to determine the machine is ready for further tasks.  **Default:** `"whoami"` |

## [Attributes](reboot_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](reboot_module.md#id4)

> **Note:**
>
> - `PATH` is ignored on the remote node when searching for the `shutdown` command. Use `search_paths` to specify locations to search if the default paths do not work.

## [See Also](reboot_module.md#id5)

> **See also:**
>
> [ansible.windows.win_reboot](../windows/win_reboot_module.md#ansible-collections-ansible-windows-win-reboot-module)
> :   Reboot a windows machine.

## [Examples](reboot_module.md#id6)

```yaml+jinja
- name: Unconditionally reboot the machine with all defaults
  ansible.builtin.reboot:

- name: Reboot a slow machine that might have lots of updates to apply
  ansible.builtin.reboot:
    reboot_timeout: 3600

- name: Reboot a machine with shutdown command in unusual place
  ansible.builtin.reboot:
    search_paths:
     - '/lib/molly-guard'

- name: Reboot machine using a custom reboot command
  ansible.builtin.reboot:
    reboot_command: launchctl reboot userspace
    boot_time_command: uptime | cut -d ' ' -f 5
```

## [Return Values](reboot_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  integer | The number of seconds that elapsed waiting for the system to be rebooted.  **Returned:** always  **Sample:** `23` |
| **rebooted**  boolean | true if the machine was rebooted  **Returned:** always  **Sample:** `true` |

### Authors

- Matt Davis (@nitzmahone)
- Sam Doran (@samdoran)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
