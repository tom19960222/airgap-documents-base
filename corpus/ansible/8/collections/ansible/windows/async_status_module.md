---
collection: ansible
version: "8"
title: "ansible.windows.async_status module – Obtain status of asynchronous task"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/async_status_module.html
fetched_at: 2026-07-28T01:10:25+00:00
---
# ansible.windows.async_status module – Obtain status of asynchronous task

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
> To use it in a playbook, specify: `ansible.windows.async_status`.

- [Synopsis](async_status_module.md#synopsis)
- [Parameters](async_status_module.md#parameters)
- [See Also](async_status_module.md#see-also)
- [Examples](async_status_module.md#examples)
- [Return Values](async_status_module.md#return-values)

## [Synopsis](async_status_module.md#id1)

- This module gets the status of an asynchronous task.

## [Parameters](async_status_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **jid**  string / required | Job or task identifier |
| **mode**  string | If `status`, obtain the status.  If `cleanup`, clean up the async job cache (by default in `~/.ansible_async/`) for the specified job *jid*.  **Choices:**   - `"cleanup"` - `"status"` ← (default) |

## [See Also](async_status_module.md#id3)

> **See also:**
>
> [ansible.builtin.async_status](../builtin/async_status_module.md#ansible-collections-ansible-builtin-async-status-module)
> :   Obtain status of asynchronous task.

## [Examples](async_status_module.md#id4)

```yaml+jinja
- name: Asynchronous yum task
  ansible.windows.win_command: my.exe
  async: 1000
  poll: 0
  register: long_cmd

- name: Wait for asynchronous job to end
  ansible.builtin.async_status:
    jid: '{{ long_cmd.ansible_job_id }}'
  register: job_result
  until: job_result.finished
  retries: 100
  delay: 10
```

## [Return Values](async_status_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_job_id**  string | The asynchronous job id  **Returned:** success  **Sample:** `"360874038559.4169"` |
| **erased**  string | Path to erased job file  **Returned:** when file is erased |
| **finished**  integer | Whether the asynchronous job has finished (`1`) or not (`0`)  **Returned:** always  **Sample:** `1` |
| **started**  integer | Whether the asynchronous job has started (`1`) or not (`0`)  **Returned:** always  **Sample:** `1` |
| **stderr**  string | Any errors returned by async_wrapper  **Returned:** always |
| **stdout**  string | Any output returned by async_wrapper  **Returned:** always |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
