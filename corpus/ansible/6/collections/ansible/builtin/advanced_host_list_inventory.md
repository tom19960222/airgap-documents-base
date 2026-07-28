---
collection: ansible
version: "6"
title: "ansible.builtin.advanced_host_list inventory – Parses a ‘host list’ with ranges"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/advanced_host_list_inventory.html
fetched_at: 2026-07-27T16:44:17+00:00
---
# ansible.builtin.advanced_host_list inventory – Parses a ‘host list’ with ranges

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `advanced_host_list` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](advanced_host_list_inventory.md#synopsis)
- [Examples](advanced_host_list_inventory.md#examples)

## [Synopsis](advanced_host_list_inventory.md#id1)

- Parses a host list string as a comma separated values of hosts and supports host ranges.
- This plugin only applies to inventory sources that are not paths and contain at least one comma.

## [Examples](advanced_host_list_inventory.md#id2)

```yaml+jinja
# simple range
# ansible -i 'host[1:10],' -m ping

# still supports w/o ranges also
# ansible-playbook -i 'localhost,' play.yml
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
