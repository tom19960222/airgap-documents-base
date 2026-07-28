---
collection: ansible
version: "8"
title: "ansible.builtin.fail module – Fail with custom message"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/fail_module.html
fetched_at: 2026-07-28T01:07:28+00:00
---
# ansible.builtin.fail module – Fail with custom message

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `fail` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.fail` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](fail_module.md#synopsis)
- [Parameters](fail_module.md#parameters)
- [Attributes](fail_module.md#attributes)
- [See Also](fail_module.md#see-also)
- [Examples](fail_module.md#examples)

## [Synopsis](fail_module.md#id1)

- This module fails the progress with a custom message.
- It can be useful for bailing out when a certain condition is met using `when`.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](fail_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **msg**  string | The customized message used for failing execution.  If omitted, fail will simply bail out with a generic message.  **Default:** `"Failed as requested from task"` |

## [Attributes](fail_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **become** | **Support:** **none** | Is usable alongside become keywords |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | **Support:** **none** | Uses the target’s configured connection information to execute code on it |
| **delegation** | **Support:** **partial**  Aside from `register` and/or in combination with `delegate_facts`, it has little effect. | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against |

## [See Also](fail_module.md#id4)

> **See also:**
>
> [ansible.builtin.assert](assert_module.md#ansible-collections-ansible-builtin-assert-module)
> :   Asserts given expressions are true.
>
> [ansible.builtin.debug](debug_module.md#ansible-collections-ansible-builtin-debug-module)
> :   Print statements during execution.
>
> [ansible.builtin.meta](meta_module.md#ansible-collections-ansible-builtin-meta-module)
> :   Execute Ansible ‘actions’.

## [Examples](fail_module.md#id5)

```yaml+jinja
- name: Example using fail and when together
  ansible.builtin.fail:
    msg: The system may not be provisioned according to the CMDB status.
  when: cmdb_status != "to-be-staged"
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
