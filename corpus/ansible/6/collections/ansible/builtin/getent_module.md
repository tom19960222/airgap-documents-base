---
collection: ansible
version: "6"
title: "ansible.builtin.getent module – A wrapper to the unix getent utility"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/getent_module.html
fetched_at: 2026-07-27T16:44:01+00:00
---
# ansible.builtin.getent module – A wrapper to the unix getent utility

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `getent` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](getent_module.md#synopsis)
- [Parameters](getent_module.md#parameters)
- [Attributes](getent_module.md#attributes)
- [Notes](getent_module.md#notes)
- [Examples](getent_module.md#examples)
- [Returned Facts](getent_module.md#returned-facts)

## [Synopsis](getent_module.md#id1)

- Runs getent against one of it’s various databases and returns information into the host’s facts, in a getent_<database> prefixed variable.

## [Parameters](getent_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **database**  string / required | The name of a getent database supported by the target system (passwd, group, hosts, etc). |
| **fail_key**  boolean | If a supplied key is missing this will make the task fail if `yes`.  Choices:   - `false` - `true` ← (default) |
| **key**  string | Key from which to return values from the specified database, otherwise the full contents are returned.  Default: `""` |
| **service**  string  added in Ansible 2.9 | Override all databases with the specified service  The underlying system must support the service flag which is not always available. |
| **split**  string | Character used to split the database values into lists/arrays such as `:` or `\t`, otherwise it will try to pick one depending on the database. |

## [Attributes](getent_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Notes](getent_module.md#id4)

> **Note:**
>
> - Not all databases support enumeration, check system documentation for details.

## [Examples](getent_module.md#id5)

```yaml+jinja
- name: Get root user info
  ansible.builtin.getent:
    database: passwd
    key: root
- ansible.builtin.debug:
    var: ansible_facts.getent_passwd

- name: Get all groups
  ansible.builtin.getent:
    database: group
    split: ':'
- ansible.builtin.debug:
    var: ansible_facts.getent_group

- name: Get all hosts, split by tab
  ansible.builtin.getent:
    database: hosts
- ansible.builtin.debug:
    var: ansible_facts.getent_hosts

- name: Get http service info, no error if missing
  ansible.builtin.getent:
    database: services
    key: http
    fail_key: False
- ansible.builtin.debug:
    var: ansible_facts.getent_services

- name: Get user password hash (requires sudo/root)
  ansible.builtin.getent:
    database: shadow
    key: www-data
    split: ':'
- ansible.builtin.debug:
    var: ansible_facts.getent_shadow
```

## [Returned Facts](getent_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **getent_<database>**  list / elements=string | A list of results or a single result as a list of the fields the db provides  The list elements depend on the database queried, see getent man page for the structure  Starting at 2.11 it now returns multiple duplicate entries, previouslly it only returned the last one  Returned: always |

### Authors

- Brian Coca (@bcoca)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
