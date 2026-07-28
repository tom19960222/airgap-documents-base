---
collection: ansible
version: "8"
title: "ansible.builtin.debug module – Print statements during execution"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/debug_module.html
fetched_at: 2026-07-28T01:04:27+00:00
---
# ansible.builtin.debug module – Print statements during execution

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `debug` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.debug` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](debug_module.md#synopsis)
- [Parameters](debug_module.md#parameters)
- [Attributes](debug_module.md#attributes)
- [See Also](debug_module.md#see-also)
- [Examples](debug_module.md#examples)

## [Synopsis](debug_module.md#id1)

- This module prints statements during execution and can be useful for debugging variables or expressions without necessarily halting the playbook.
- Useful for debugging together with the ‘when:’ directive.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](debug_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **msg**  string | The customized message that is printed. If omitted, prints a generic message.  **Default:** `"Hello world!"` |
| **var**  string | A variable name to debug.  Mutually exclusive with the `msg` option.  Be aware that this option already runs in Jinja2 context and has an implicit `{{ }}` wrapping, so you should not be using Jinja2 delimiters unless you are looking for double interpolation. |
| **verbosity**  integer | A number that controls when the debug is run, if you set to 3 it will only run debug when -vvv or above.  **Default:** `0` |

## [Attributes](debug_module.md#id3)

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

## [See Also](debug_module.md#id4)

> **See also:**
>
> [ansible.builtin.assert](assert_module.md#ansible-collections-ansible-builtin-assert-module)
> :   Asserts given expressions are true.
>
> [ansible.builtin.fail](fail_module.md#ansible-collections-ansible-builtin-fail-module)
> :   Fail with custom message.

## [Examples](debug_module.md#id5)

```yaml+jinja
- name: Print the gateway for each host when defined
  ansible.builtin.debug:
    msg: System {{ inventory_hostname }} has gateway {{ ansible_default_ipv4.gateway }}
  when: ansible_default_ipv4.gateway is defined

- name: Get uptime information
  ansible.builtin.shell: /usr/bin/uptime
  register: result

- name: Print return information from the previous task
  ansible.builtin.debug:
    var: result
    verbosity: 2

- name: Display all variables/facts known for a host
  ansible.builtin.debug:
    var: hostvars[inventory_hostname]
    verbosity: 4

- name: Prints two lines of messages, but only if there is an environment value set
  ansible.builtin.debug:
    msg:
    - "Provisioning based on YOUR_KEY which is: {{ lookup('ansible.builtin.env', 'YOUR_KEY') }}"
    - "These servers were built using the password of '{{ password_used }}'. Please retain this for later use."
```

### Authors

- Dag Wieers (@dagwieers)
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
