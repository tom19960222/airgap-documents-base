---
collection: ansible
version: "6"
title: "ansible.builtin.tree callback – Save host events to files"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/tree_callback.html
fetched_at: 2026-07-27T16:44:16+00:00
---
# ansible.builtin.tree callback – Save host events to files

> **Note:**
>
> This callback plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `tree` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same callback plugin name.

- [Callback plugin](tree_callback.md#callback-plugin)
- [Synopsis](tree_callback.md#synopsis)
- [Requirements](tree_callback.md#requirements)
- [Parameters](tree_callback.md#parameters)

## [Callback plugin](tree_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](tree_callback.md#id2)

- This callback is used by the Ansible (adhoc) command line option `-t|--tree`.
- This produces a JSON dump of events in a directory, a file for each host, the directory used MUST be passed as a command line option.

## [Requirements](tree_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- invoked in the command line

## [Parameters](tree_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **directory**  path  added in ansible-core 2.11 | directory that will contain the per host JSON files. Also set by the `--tree` option when using adhoc.  Default: `"~/.ansible/tree"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_tree]   directory = ~/.ansible/tree   ``` - Environment variable: [`ANSIBLE_CALLBACK_TREE_DIR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_TREE_DIR) |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
