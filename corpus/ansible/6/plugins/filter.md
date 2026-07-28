---
collection: ansible
version: "6"
title: "Filter plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/filter.html
fetched_at: 2026-07-27T16:40:40+00:00
---
# Filter plugins

- [Enabling filter plugins](filter.md#enabling-filter-plugins)
- [Using filter plugins](filter.md#using-filter-plugins)

Filter plugins manipulate data. With the right filter you can extract a particular value, transform data types and formats, perform mathematical calculations, split and concatenate strings, insert dates and times, and do much more. Ansible uses the [standard filters](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters "(in Jinja v3.1.x)") shipped with Jinja2 and adds some specialized filter plugins. You can [create custom Ansible filters as plugins](../dev_guide/developing_plugins.md#developing-filter-plugins).

## [Enabling filter plugins](filter.md#id2)

You can add a custom filter plugin by dropping it into a `filter_plugins` directory adjacent to your play, inside a role, or by putting it in one of the filter plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using filter plugins](filter.md#id3)

For information on using filter plugins, see [Using filters to manipulate data](../user_guide/playbooks_filters.md#playbooks-filters).

> **See also:**
>
> [Intro to playbooks](../user_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Inventory plugins](inventory.md#inventory-plugins)
> :   Inventory plugins
>
> [Callback plugins](callback.md#callback-plugins)
> :   Callback plugins
>
> [Test plugins](test.md#test-plugins)
> :   Test plugins
>
> [Lookup plugins](lookup.md#lookup-plugins)
> :   Lookup plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
