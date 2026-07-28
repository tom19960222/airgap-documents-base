---
collection: ansible
version: "6"
title: "ansible.builtin.inventory_hostnames lookup – list of inventory hosts matching a host pattern"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/inventory_hostnames_lookup.html
fetched_at: 2026-07-27T16:43:11+00:00
---
# ansible.builtin.inventory_hostnames lookup – list of inventory hosts matching a host pattern

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `inventory_hostnames` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](inventory_hostnames_lookup.md#synopsis)
- [Notes](inventory_hostnames_lookup.md#notes)
- [Examples](inventory_hostnames_lookup.md#examples)
- [Return Value](inventory_hostnames_lookup.md#return-value)

## [Synopsis](inventory_hostnames_lookup.md#id1)

- This lookup understands ‘host patterns’ as used by the `hosts:` keyword in plays and can return a list of matching hosts from inventory

## [Notes](inventory_hostnames_lookup.md#id2)

> **Note:**
>
> - this is only worth for ‘hostname patterns’ it is easier to loop over the group/group_names variables otherwise.

## [Examples](inventory_hostnames_lookup.md#id3)

```yaml+jinja
- name: show all the hosts matching the pattern, i.e. all but the group www
  ansible.builtin.debug:
    msg: "{{ item }}"
  with_inventory_hostnames:
    - all:!www
```

## [Return Value](inventory_hostnames_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | list of hostnames that matched the host pattern in inventory  Returned: success |

### Authors

- Michael DeHaan
- Steven Dossett

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
