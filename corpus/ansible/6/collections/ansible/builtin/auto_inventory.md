---
collection: ansible
version: "6"
title: "ansible.builtin.auto inventory – Loads and executes an inventory plugin specified in a YAML config"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/auto_inventory.html
fetched_at: 2026-07-27T16:42:46+00:00
---
# ansible.builtin.auto inventory – Loads and executes an inventory plugin specified in a YAML config

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `auto` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](auto_inventory.md#synopsis)
- [Examples](auto_inventory.md#examples)

## [Synopsis](auto_inventory.md#id1)

- By enabling the `auto` inventory plugin, any YAML inventory config file with a `plugin` key at its root will automatically cause the named plugin to be loaded and executed with that config. This effectively provides automatic enabling of all installed/accessible inventory plugins.
- To disable this behavior, remove `auto` from the `INVENTORY_ENABLED` config element.

## [Examples](auto_inventory.md#id2)

```yaml+jinja
# This plugin is not intended for direct use; it is a fallback mechanism for automatic enabling of
# all installed inventory plugins.
```

### Authors

- Matt Davis (@nitzmahone)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
