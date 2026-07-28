---
collection: ansible
version: "6"
title: "ansible.builtin.script inventory – Executes an inventory script that returns JSON"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/script_inventory.html
fetched_at: 2026-07-27T16:42:53+00:00
---
# ansible.builtin.script inventory – Executes an inventory script that returns JSON

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `script` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](script_inventory.md#synopsis)
- [Parameters](script_inventory.md#parameters)
- [Notes](script_inventory.md#notes)

## [Synopsis](script_inventory.md#id1)

- The source provided must be an executable that returns Ansible inventory JSON
- The source must accept `--list` and `--host <hostname>` as arguments. `--host` will only be used if no `_meta` key is present. This is a performance optimization as the script would be called per host otherwise.

## [Parameters](script_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **always_show_stderr**  boolean | Toggle display of stderr even when script was successful  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [inventory_plugin_script]   always_show_stderr = true   ``` - Environment variable: [`ANSIBLE_INVENTORY_PLUGIN_SCRIPT_STDERR`](../../environment_variables.md#envvar-ANSIBLE_INVENTORY_PLUGIN_SCRIPT_STDERR) |

## [Notes](script_inventory.md#id3)

> **Note:**
>
> - Enabled in configuration by default.
> - The plugin does not cache results because external inventory scripts are responsible for their own caching.

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
