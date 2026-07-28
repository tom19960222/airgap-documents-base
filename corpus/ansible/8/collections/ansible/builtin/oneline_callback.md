---
collection: ansible
version: "8"
title: "ansible.builtin.oneline callback – oneline Ansible screen output"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/oneline_callback.html
fetched_at: 2026-07-28T01:07:55+00:00
---
# ansible.builtin.oneline callback – oneline Ansible screen output

> **Note:**
>
> This callback plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `oneline`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.oneline` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same callback plugin name.

- [Callback plugin](oneline_callback.md#callback-plugin)
- [Synopsis](oneline_callback.md#synopsis)

## [Callback plugin](oneline_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](oneline_callback.md#id2)

- This is the output callback used by the -o/–one-line command line option.

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
