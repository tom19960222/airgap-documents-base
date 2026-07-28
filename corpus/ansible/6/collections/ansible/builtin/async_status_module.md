---
collection: ansible
version: "6"
title: "ansible.builtin.async_status module – Obtain status of asynchronous task"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/async_status_module.html
fetched_at: 2026-07-27T16:43:09+00:00
---
# ansible.builtin.async_status module – Obtain status of asynchronous task

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `async_status` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](async_status_module.md#synopsis)
- [Parameters](async_status_module.md#parameters)
- [Attributes](async_status_module.md#attributes)
- [See Also](async_status_module.md#see-also)
- [Examples](async_status_module.md#examples)
- [Return Values](async_status_module.md#return-values)

## [Synopsis](async_status_module.md#id1)

- This module gets the status of an asynchronous task.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](async_status_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **jid**  string / required | Job or task identifier |
| **mode**  string | If `status`, obtain the status.  If `cleanup`, clean up the async job cache (by default in `~/.ansible_async/`) for the specified job *jid*.  Choices:   - `"cleanup"` - `"status"` ← (default) |

## [Attributes](async_status_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **bypass_host_loop** | Support: none | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | Support: none | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platforms: posix, windows | Target OS/families that can be operated against |

## [See Also](async_status_module.md#id4)

> **See also:**
>
> [Asynchronous actions and polling](../../../user_guide/playbooks_async.md#playbooks-async)
> :   Detailed information on how to use asynchronous actions and polling.

## [Examples](async_status_module.md#id5)

```yaml+jinja
---
- name: Asynchronous yum task
  ansible.builtin.yum:
    name: docker-io
    state: present
  async: 1000
  poll: 0
  register: yum_sleeper

- name: Wait for asynchronous job to end
  ansible.builtin.async_status:
    jid: '{{ yum_sleeper.ansible_job_id }}'
  register: job_result
  until: job_result.finished
  retries: 100
  delay: 10
```

## [Return Values](async_status_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_job_id**  string | The asynchronous job id  Returned: success  Sample: `"360874038559.4169"` |
| **erased**  string | Path to erased job file  Returned: when file is erased |
| **finished**  integer | Whether the asynchronous job has finished (`1`) or not (`0`)  Returned: always  Sample: `1` |
| **started**  integer | Whether the asynchronous job has started (`1`) or not (`0`)  Returned: always  Sample: `1` |
| **stderr**  string | Any errors returned by async_wrapper  Returned: always |
| **stdout**  string | Any output returned by async_wrapper  Returned: always |

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
