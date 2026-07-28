---
collection: ansible
version: "8"
title: "Filter plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/filter.html
fetched_at: 2026-07-28T01:00:15+00:00
---
# Filter plugins

- [Enabling filter plugins](filter.md#enabling-filter-plugins)
- [Using filter plugins](filter.md#using-filter-plugins)
- [Plugin list](filter.md#plugin-list)

Filter plugins manipulate data. With the right filter you can extract a particular value, transform data types and formats, perform mathematical calculations, split and concatenate strings, insert dates and times, and do much more. Ansible uses the standard filters shipped with Jinja2 and adds some specialized filter plugins. You can [create custom Ansible filters as plugins](../dev_guide/developing_plugins.md#developing-filter-plugins).

## [Enabling filter plugins](filter.md#id2)

You can add a custom filter plugin by dropping it into a `filter_plugins` directory adjacent to your play, inside a role, or by putting it in one of the filter plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using filter plugins](filter.md#id3)

You can use filters anywhere you can use templating in Ansible: in a play, in variables file, or in a Jinja2 template for the [template](../collections/ansible/builtin/template_module.md#template-module) module. For more information on using filter plugins, see [Using filters to manipulate data](../playbook_guide/playbooks_filters.md#playbooks-filters). Filters can return any type of data, but if you want to always return a boolean (`True` or `False`) you should be looking at a test instead.

```YAML+Jinja
vars:
   yaml_string: "{{ some_variable|to_yaml }}"
```

Filters are the preferred way to manipulate data in Ansible, you can identify a filter because it is normally preceded by a `|`, with the expression on the left of it being the first input of the filter. Additional parameters may be passed into the filter itself as you would to most programming functions. These parameters can be either `positional` (passed in order) or `named` (passed as key=value pairs). When passing both types, positional arguments should go first.

```YAML+Jinja
passing_positional: {{ (x == 32) | ternary('x is 32', 'x is not 32') }}
passing_extra_named_parameters: {{ some_variable | to_yaml(indent=8, width=1337) }}
passing_both: {{ some_variable| ternary('true value', 'false value', none_val='NULL') }}
```

In the documentation, filters will always have a C(_input) option that corresponds to the expression to the left of c(|). A C(positional:) field in the documentation will show which options are positional and in which order they are required.

## [Plugin list](filter.md#id4)

You can use `ansible-doc -t filter -l` to see the list of available plugins. Use `ansible-doc -t filter <plugin name>` to see plugin-specific documentation and examples.

> **See also:**
>
> [Ansible playbooks](../playbook_guide/playbooks_intro.md#about-playbooks)
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
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
