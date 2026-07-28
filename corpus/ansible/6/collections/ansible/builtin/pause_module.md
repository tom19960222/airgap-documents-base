---
collection: ansible
version: "6"
title: "ansible.builtin.pause module – Pause playbook execution"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/pause_module.html
fetched_at: 2026-07-27T16:44:05+00:00
---
# ansible.builtin.pause module – Pause playbook execution

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `pause` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](pause_module.md#synopsis)
- [Parameters](pause_module.md#parameters)
- [Attributes](pause_module.md#attributes)
- [Notes](pause_module.md#notes)
- [Examples](pause_module.md#examples)
- [Return Values](pause_module.md#return-values)

## [Synopsis](pause_module.md#id1)

- Pauses playbook execution for a set amount of time, or until a prompt is acknowledged. All parameters are optional. The default behavior is to pause with a prompt.
- To pause/wait/sleep per host, use the [ansible.builtin.wait_for](wait_for_module.md#ansible-collections-ansible-builtin-wait-for-module) module.
- You can use `ctrl+c` if you wish to advance a pause earlier than it is set to expire or if you need to abort a playbook run entirely. To continue early press `ctrl+c` and then `c`. To abort a playbook press `ctrl+c` and then `a`.
- The pause module integrates into async/parallelized playbooks without any special considerations (see Rolling Updates). When using pauses with the `serial` playbook parameter (as in rolling updates) you are only prompted once for the current group of hosts.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](pause_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **echo**  boolean | Controls whether or not keyboard input is shown when typing.  Has no effect if ‘seconds’ or ‘minutes’ is set.  Choices:   - `false` - `true` ← (default) |
| **minutes**  string | A positive number of minutes to pause for. |
| **prompt**  string | Optional text to use for the prompt message. |
| **seconds**  string | A positive number of seconds to pause for. |

## [Attributes](pause_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: full | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **delegation** | Support: none | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platforms: all | Target OS/families that can be operated against |

## [Notes](pause_module.md#id4)

> **Note:**
>
> - Starting in 2.2, if you specify 0 or negative for minutes or seconds, it will wait for 1 second, previously it would wait indefinitely.
> - User input is not captured or echoed, regardless of echo setting, when minutes or seconds is specified.

## [Examples](pause_module.md#id5)

```yaml+jinja
- name: Pause for 5 minutes to build app cache
  ansible.builtin.pause:
    minutes: 5

- name: Pause until you can verify updates to an application were successful
  ansible.builtin.pause:

- name: A helpful reminder of what to look out for post-update
  ansible.builtin.pause:
    prompt: "Make sure org.foo.FooOverload exception is not present"

- name: Pause to get some sensitive input
  ansible.builtin.pause:
    prompt: "Enter a secret"
    echo: no
```

## [Return Values](pause_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **delta**  string | Time paused in seconds  Returned: always  Sample: `"2"` |
| **echo**  boolean | Value of echo setting  Returned: always  Sample: `true` |
| **start**  string | Time when started pausing  Returned: always  Sample: `"2017-02-23 14:35:07.298862"` |
| **stdout**  string | Output of pause module  Returned: always  Sample: `"Paused for 0.04 minutes"` |
| **stop**  string | Time when ended pausing  Returned: always  Sample: `"2017-02-23 14:35:09.552594"` |
| **user_input**  string | User input from interactive console  Returned: if no waiting time set  Sample: `"Example user input"` |

### Authors

- Tim Bielawa (@tbielawa)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
