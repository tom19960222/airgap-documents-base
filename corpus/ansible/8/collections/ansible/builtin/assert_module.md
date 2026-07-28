---
collection: ansible
version: "8"
title: "ansible.builtin.assert module – Asserts given expressions are true"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/assert_module.html
fetched_at: 2026-07-28T01:04:07+00:00
---
# ansible.builtin.assert module – Asserts given expressions are true

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `assert` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.assert` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](assert_module.md#synopsis)
- [Parameters](assert_module.md#parameters)
- [Attributes](assert_module.md#attributes)
- [See Also](assert_module.md#see-also)
- [Examples](assert_module.md#examples)

## [Synopsis](assert_module.md#id1)

- This module asserts that given expressions are true with an optional custom message.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](assert_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fail_msg**  aliases: msg  string  *added in Ansible 2.7* | The customized message used for a failing assertion.  This argument was called ‘msg’ before Ansible 2.7, now it is renamed to ‘fail_msg’ with alias ‘msg’. |
| **quiet**  boolean  *added in Ansible 2.8* | Set this to `true` to avoid verbose output.  **Choices:**   - `false` ← (default) - `true` |
| **success_msg**  string  *added in Ansible 2.7* | The customized message used for a successful assertion. |
| **that**  list / elements=string / required | A list of string expressions of the same form that can be passed to the ‘when’ statement. |

## [Attributes](assert_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **become** | **Support:** **none** | Is usable alongside become keywords |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | **Support:** **none** | Uses the target’s configured connection information to execute code on it |
| **delegation** | **Support:** **none**  Aside from `register` and/or in combination with `delegate_facts`, it has little effect. | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against |

## [See Also](assert_module.md#id4)

> **See also:**
>
> [ansible.builtin.debug](debug_module.md#ansible-collections-ansible-builtin-debug-module)
> :   Print statements during execution.
>
> [ansible.builtin.fail](fail_module.md#ansible-collections-ansible-builtin-fail-module)
> :   Fail with custom message.
>
> [ansible.builtin.meta](meta_module.md#ansible-collections-ansible-builtin-meta-module)
> :   Execute Ansible ‘actions’.

## [Examples](assert_module.md#id5)

```yaml+jinja
- ansible.builtin.assert: { that: "ansible_os_family != 'RedHat'" }

- ansible.builtin.assert:
    that:
      - "'foo' in some_command_result.stdout"
      - number_of_the_counting == 3

- name: After version 2.7 both 'msg' and 'fail_msg' can customize failing assertion message
  ansible.builtin.assert:
    that:
      - my_param <= 100
      - my_param >= 0
    fail_msg: "'my_param' must be between 0 and 100"
    success_msg: "'my_param' is between 0 and 100"

- name: Please use 'msg' when ansible version is smaller than 2.7
  ansible.builtin.assert:
    that:
      - my_param <= 100
      - my_param >= 0
    msg: "'my_param' must be between 0 and 100"

- name: Use quiet to avoid verbose output
  ansible.builtin.assert:
    that:
      - my_param <= 100
      - my_param >= 0
    quiet: true
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
