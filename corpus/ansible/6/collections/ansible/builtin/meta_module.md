---
collection: ansible
version: "6"
title: "ansible.builtin.meta module – Execute Ansible ‘actions’"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/meta_module.html
fetched_at: 2026-07-27T16:42:52+00:00
---
# ansible.builtin.meta module – Execute Ansible ‘actions’

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `meta` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](meta_module.md#synopsis)
- [Parameters](meta_module.md#parameters)
- [Attributes](meta_module.md#attributes)
- [Notes](meta_module.md#notes)
- [See Also](meta_module.md#see-also)
- [Examples](meta_module.md#examples)

## [Synopsis](meta_module.md#id1)

- Meta tasks are a special kind of task which can influence Ansible internal execution or state.
- Meta tasks can be used anywhere within your playbook.
- This module is also supported for Windows targets.

## [Parameters](meta_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **free_form**  string / required | This module takes a free form command, as a string. There is not an actual option named “free form”. See the examples!  `flush_handlers` makes Ansible run any handler tasks which have thus far been notified. Ansible inserts these tasks internally at certain points to implicitly trigger handler runs (after pre/post tasks, the final role execution, and the main tasks section of your plays).  `refresh_inventory` (added in Ansible 2.0) forces the reload of the inventory, which in the case of dynamic inventory scripts means they will be re-executed. If the dynamic inventory script is using a cache, Ansible cannot know this and has no way of refreshing it (you can disable the cache or, if available for your specific inventory datasource (e.g. aws), you can use the an inventory plugin instead of an inventory script). This is mainly useful when additional hosts are created and users wish to use them instead of using the [ansible.builtin.add_host](add_host_module.md#ansible-collections-ansible-builtin-add-host-module) module.  `noop` (added in Ansible 2.0) This literally does ‘nothing’. It is mainly used internally and not recommended for general use.  `clear_facts` (added in Ansible 2.1) causes the gathered facts for the hosts specified in the play’s list of hosts to be cleared, including the fact cache.  `clear_host_errors` (added in Ansible 2.1) clears the failed state (if any) from hosts specified in the play’s list of hosts.  `end_play` (added in Ansible 2.2) causes the play to end without failing the host(s). Note that this affects all hosts.  `reset_connection` (added in Ansible 2.3) interrupts a persistent connection (i.e. ssh + control persist)  `end_host` (added in Ansible 2.8) is a per-host variation of `end_play`. Causes the play to end for the current host without failing it.  `end_batch` (added in Ansible 2.12) causes the current batch (see `serial`) to end without failing the host(s). Note that with `serial=0` or undefined this behaves the same as `end_play`.  Choices:   - `"clear_facts"` - `"clear_host_errors"` - `"end_host"` - `"end_play"` - `"flush_handlers"` - `"noop"` - `"refresh_inventory"` - `"reset_connection"` - `"end_batch"` |

## [Attributes](meta_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: none | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: partial  Some of the subactions ignore the host loop, see the description above for each specific action for the exceptions | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: partial  Most of the subactions ignore the task loop, see the description above for each specific action for the exceptions | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: partial  While these actions don’t modify the targets directly they do change possible states of the target within the run | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: partial  Most options in this action do not use a connection, except `reset_connection` which still does not connect to the remote | Uses the target’s configured connection information to execute code on it |
| **core** | Support: full | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: none | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: partial  Only some options support conditionals and when they do they act ‘bypassing the host loop’, taking the values from first available host | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [Notes](meta_module.md#id4)

> **Note:**
>
> - `clear_facts` will remove the persistent facts from [ansible.builtin.set_fact](set_fact_module.md#ansible-collections-ansible-builtin-set-fact-module) using `cacheable=True`, but not the current host variable it creates for the current run.
> - Skipping `meta` tasks with tags is not supported before Ansible 2.11.

## [See Also](meta_module.md#id5)

> **See also:**
>
> [ansible.builtin.assert](assert_module.md#ansible-collections-ansible-builtin-assert-module)
> :   Asserts given expressions are true.
>
> [ansible.builtin.fail](fail_module.md#ansible-collections-ansible-builtin-fail-module)
> :   Fail with custom message.

## [Examples](meta_module.md#id6)

```yaml+jinja
# Example showing flushing handlers on demand, not at end of play
- ansible.builtin.template:
    src: new.j2
    dest: /etc/config.txt
  notify: myhandler

- name: Force all notified handlers to run at this point, not waiting for normal sync points
  ansible.builtin.meta: flush_handlers

# Example showing how to refresh inventory during play
- name: Reload inventory, useful with dynamic inventories when play makes changes to the existing hosts
  cloud_guest:            # this is fake module
    name: newhost
    state: present

- name: Refresh inventory to ensure new instances exist in inventory
  ansible.builtin.meta: refresh_inventory

# Example showing how to clear all existing facts of targeted hosts
- name: Clear gathered facts from all currently targeted hosts
  ansible.builtin.meta: clear_facts

# Example showing how to continue using a failed target
- name: Bring host back to play after failure
  ansible.builtin.copy:
    src: file
    dest: /etc/file
  remote_user: imightnothavepermission

- ansible.builtin.meta: clear_host_errors

# Example showing how to reset an existing connection
- ansible.builtin.user:
    name: '{{ ansible_user }}'
    groups: input

- name: Reset ssh connection to allow user changes to affect 'current login user'
  ansible.builtin.meta: reset_connection

# Example showing how to end the play for specific targets
- name: End the play for hosts that run CentOS 6
  ansible.builtin.meta: end_host
  when:
  - ansible_distribution == 'CentOS'
  - ansible_distribution_major_version == '6'
```

### Authors

- Ansible Core Team

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
