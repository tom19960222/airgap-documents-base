---
collection: ansible
version: "8"
title: "ansible.builtin.host_list inventory – Parses a ‘host list’ string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/host_list_inventory.html
fetched_at: 2026-07-28T01:04:26+00:00
---
# ansible.builtin.host_list inventory – Parses a ‘host list’ string

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `host_list`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.host_list` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](host_list_inventory.md#synopsis)
- [Examples](host_list_inventory.md#examples)

## [Synopsis](host_list_inventory.md#id1)

- Parses a host list string as a comma separated values of hosts
- This plugin only applies to inventory strings that are not paths and contain a comma.

## [Examples](host_list_inventory.md#id2)

```yaml+jinja
# define 2 hosts in command line
# ansible -i '10.10.2.6, 10.10.2.4' -m ping all

# DNS resolvable names
# ansible -i 'host1.example.com, host2' -m user -a 'name=me state=absent' all

# just use localhost
# ansible-playbook -i 'localhost,' play.yml -c local
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
