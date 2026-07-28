---
collection: ansible
version: "6"
title: "ansible.builtin.add_host module – Add a host (and alternatively a group) to the ansible-playbook in-memory inventory"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/add_host_module.html
fetched_at: 2026-07-27T16:43:04+00:00
---
# ansible.builtin.add_host module – Add a host (and alternatively a group) to the ansible-playbook in-memory inventory

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `add_host` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](add_host_module.md#synopsis)
- [Parameters](add_host_module.md#parameters)
- [Attributes](add_host_module.md#attributes)
- [Notes](add_host_module.md#notes)
- [See Also](add_host_module.md#see-also)
- [Examples](add_host_module.md#examples)

## [Synopsis](add_host_module.md#id1)

- Use variables to create new hosts and groups in inventory for use in later plays of the same playbook.
- Takes variables so you can define the new hosts more fully.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](add_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **groups**  aliases: group, groupname  list / elements=string | The groups to add the hostname to. |
| **name**  aliases: host, hostname  string / required | The hostname/ip of the host to add to the inventory, can include a colon and a port number. |

## [Attributes](add_host_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: full | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: none | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: partial  While this makes no changes to target systems the ‘in memory’ inventory will still be altered | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **core** | Support: partial  While parts of this action are implemented in core, other parts are still available as normal plugins and can be partially overridden | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: none | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: none | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [Notes](add_host_module.md#id4)

> **Note:**
>
> - The alias `host` of the parameter `name` is only available on Ansible 2.4 and newer.
> - Since Ansible 2.4, the `inventory_dir` variable is now set to `None` instead of the ‘global inventory source’, because you can now have multiple sources. An example was added that shows how to partially restore the previous behaviour.
> - Though this module does not change the remote host, we do provide ‘changed’ status as it can be useful for those trying to track inventory changes.
> - The hosts added will not bypass the `--limit` from the command line, so both of those need to be in agreement to make them available as play targets. They are still available from hostvars and for delegation as a normal part of the inventory.

## [See Also](add_host_module.md#id5)

> **See also:**
>
> [ansible.builtin.group_by](group_by_module.md#ansible-collections-ansible-builtin-group-by-module)
> :   Create Ansible groups based on facts.

## [Examples](add_host_module.md#id6)

```yaml+jinja
- name: Add host to group 'just_created' with variable foo=42
  ansible.builtin.add_host:
    name: '{{ ip_from_ec2 }}'
    groups: just_created
    foo: 42

- name: Add host to multiple groups
  ansible.builtin.add_host:
    hostname: '{{ new_ip }}'
    groups:
    - group1
    - group2

- name: Add a host with a non-standard port local to your machines
  ansible.builtin.add_host:
    name: '{{ new_ip }}:{{ new_port }}'

- name: Add a host alias that we reach through a tunnel (Ansible 1.9 and older)
  ansible.builtin.add_host:
    hostname: '{{ new_ip }}'
    ansible_ssh_host: '{{ inventory_hostname }}'
    ansible_ssh_port: '{{ new_port }}'

- name: Add a host alias that we reach through a tunnel (Ansible 2.0 and newer)
  ansible.builtin.add_host:
    hostname: '{{ new_ip }}'
    ansible_host: '{{ inventory_hostname }}'
    ansible_port: '{{ new_port }}'

- name: Ensure inventory vars are set to the same value as the inventory_hostname has (close to pre Ansible 2.4 behaviour)
  ansible.builtin.add_host:
    hostname: charlie
    inventory_dir: '{{ inventory_dir }}'

- name: Add all hosts running this playbook to the done group
  ansible.builtin.add_host:
    name: '{{ item }}'
    groups: done
  loop: "{{ ansible_play_hosts }}"
```

### Authors

- Ansible Core Team
- Seth Vidal (@skvidal)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
