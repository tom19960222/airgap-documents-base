---
collection: ansible
version: "8"
title: "community.windows.win_wait_for_process module – Waits for a process to exist or not exist before continuing."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_wait_for_process_module.html
fetched_at: 2026-07-28T02:02:34+00:00
---
# community.windows.win_wait_for_process module – Waits for a process to exist or not exist before continuing.

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_wait_for_process`.

- [Synopsis](win_wait_for_process_module.md#synopsis)
- [Parameters](win_wait_for_process_module.md#parameters)
- [See Also](win_wait_for_process_module.md#see-also)
- [Examples](win_wait_for_process_module.md#examples)
- [Return Values](win_wait_for_process_module.md#return-values)

## [Synopsis](win_wait_for_process_module.md#id1)

- Waiting for a process to start or stop.
- This is useful when Windows services behave poorly and do not enumerate external dependencies in their manifest.

## [Parameters](win_wait_for_process_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **owner**  string | The owner of the process.  Requires PowerShell version 4.0 or newer. |
| **pid**  integer | The PID of the process.  **Default:** `0` |
| **post_wait_delay**  integer | Seconds to wait after checking for processes.  **Default:** `0` |
| **pre_wait_delay**  integer | Seconds to wait before checking processes.  **Default:** `0` |
| **process_min_count**  integer | Minimum number of process matching the supplied pattern to satisfy `present` condition.  Only applies to `present`.  **Default:** `1` |
| **process_name_exact**  list / elements=string | The name of the process(es) for which to wait. The name of the process(es) should not include the file extension suffix. |
| **process_name_pattern**  string | RegEx pattern matching desired process(es). |
| **sleep**  integer | Number of seconds to sleep between checks.  Only applies when waiting for a process to start. Waiting for a process to start does not have a native non-polling mechanism. Waiting for a stop uses native PowerShell and does not require polling.  **Default:** `1` |
| **state**  string | When checking for a running process `present` will block execution until the process exists, or until the timeout has been reached. `absent` will block execution until the process no longer exists, or until the timeout has been reached.  When waiting for `present`, the module will return changed only if the process was not present on the initial check but became present on subsequent checks.  If, while waiting for `absent`, new processes matching the supplied pattern are started, these new processes will not be included in the action.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | The maximum number of seconds to wait for a for a process to start or stop before erroring out.  **Default:** `300` |

## [See Also](win_wait_for_process_module.md#id3)

> **See also:**
>
> [ansible.builtin.wait_for](../../ansible/builtin/wait_for_module.md#ansible-collections-ansible-builtin-wait-for-module)
> :   Waits for a condition before continuing.
>
> [ansible.windows.win_wait_for](../../ansible/windows/win_wait_for_module.md#ansible-collections-ansible-windows-win-wait-for-module)
> :   Waits for a condition before continuing.

## [Examples](win_wait_for_process_module.md#id4)

```yaml+jinja
- name: Wait 300 seconds for all Oracle VirtualBox processes to stop. (VBoxHeadless, VirtualBox, VBoxSVC)
  community.windows.win_wait_for_process:
    process_name_pattern: 'v(irtual)?box(headless|svc)?'
    state: absent
    timeout: 500

- name: Wait 300 seconds for 3 instances of cmd to start, waiting 5 seconds between each check
  community.windows.win_wait_for_process:
    process_name_exact: cmd
    state: present
    timeout: 500
    sleep: 5
    process_min_count: 3
```

## [Return Values](win_wait_for_process_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  float | The elapsed seconds between the start of poll and the end of the module.  **Returned:** always  **Sample:** `3.14159265` |
| **matched_processes**  complex | List of matched processes (either stopped or started).  **Returned:** always |
| **name**  string | The name of the matched process.  **Returned:** always  **Sample:** `"svchost"` |
| **owner**  string | The owner of the matched process.  **Returned:** when supported by PowerShell  **Sample:** `"NT AUTHORITY\\SYSTEM"` |
| **pid**  integer | The PID of the matched process.  **Returned:** always  **Sample:** `7908` |

### Authors

- Charles Crossan (@crossan007)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
