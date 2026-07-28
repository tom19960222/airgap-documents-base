---
collection: ansible
version: "8"
title: "Docs fragments"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/docs_fragment.html
fetched_at: 2026-07-28T01:00:15+00:00
---
# Docs fragments

- [Enabling docs fragments](docs_fragment.md#enabling-docs-fragments)
- [Using docs fragments](docs_fragment.md#using-docs-fragments)

Docs fragments allow you to document common parameters of multiple plugins or modules in a single place.

## [Enabling docs fragments](docs_fragment.md#id3)

You can add a custom docs fragment by dropping it into a `doc_fragments` directory adjacent to your collection or role, just like any other plugin.

## [Using docs fragments](docs_fragment.md#id4)

Only collection developers and maintainers use docs fragments. For more information on using docs fragments, see [Documentation fragments](../dev_guide/developing_modules_documenting.md#module-docs-fragments) or [Using documentation fragments in collections](../dev_guide/developing_collections_shared.md#docfragments-collections).

> **See also:**
>
> [Developing modules](../dev_guide/developing_modules_general.md#developing-modules-general)
> :   An introduction to creating Ansible modules
>
> [Developing collections](../dev_guide/developing_collections.md#developing-collections)
> :   A guide to creating Ansible collections
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
