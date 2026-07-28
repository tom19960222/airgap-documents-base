---
collection: ansible
version: "8"
title: "Lookup plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/lookup.html
fetched_at: 2026-07-28T01:00:17+00:00
---
# Lookup plugins

- [Enabling lookup plugins](lookup.md#enabling-lookup-plugins)
- [Using lookup plugins](lookup.md#using-lookup-plugins)
- [Forcing lookups to return lists: `query` and `wantlist=True`](lookup.md#forcing-lookups-to-return-lists-query-and-wantlist-true)
- [Plugin list](lookup.md#plugin-list)

Lookup plugins are an Ansible-specific extension to the Jinja2 templating language. You can use lookup plugins to access data from outside sources (files, databases, key/value stores, APIs, and other services) within your playbooks. Like all [templating](../playbook_guide/playbooks_templating.md#playbooks-templating), lookups execute and are evaluated on the Ansible control machine. Ansible makes the data returned by a lookup plugin available using the standard templating system. You can use lookup plugins to load variables or templates with information from external sources. You can [create custom lookup plugins](../dev_guide/developing_plugins.md#developing-lookup-plugins).

> **Note:**
>
> - Lookups are executed with a working directory relative to the role or play,
>   as opposed to local tasks, which are executed relative the executed script.
> - Pass `wantlist=True` to lookups to use in Jinja2 template “for” loops.
> - By default, lookup return values are marked as unsafe for security reasons. If you trust the outside source your lookup accesses, pass `allow_unsafe=True` to allow Jinja2 templates to evaluate lookup values.

> **Warning:**
>
> - Some lookups pass arguments to a shell. When using variables from a remote/untrusted source, use the |quote filter to ensure safe usage.

## [Enabling lookup plugins](lookup.md#id2)

Ansible enables all lookup plugins it can find. You can activate a custom lookup by either dropping it into a `lookup_plugins` directory adjacent to your play, inside the `plugins/lookup/` directory of a collection you have installed, inside a standalone role, or in one of the lookup directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using lookup plugins](lookup.md#id3)

You can use lookup plugins anywhere you can use templating in Ansible: in a play, in variables file, or in a Jinja2 template for the [template](../collections/ansible/builtin/template_module.md#template-module) module. For more information on using lookup plugins, see [Lookups](../playbook_guide/playbooks_lookups.md#playbooks-lookups).

```YAML+Jinja
vars:
  file_contents: "{{ lookup('file', 'path/to/file.txt') }}"
```

Lookups are an integral part of loops. Wherever you see `with_`, the part after the underscore is the name of a lookup. For this reason, lookups are expected to output lists; for example, `with_items` uses the [items](../collections/ansible/builtin/items_lookup.md#items-lookup) lookup:

```YAML+Jinja
tasks:
  - name: count to 3
    debug: msg={{ item }}
    with_items: [1, 2, 3]
```

You can combine lookups with [filters](../playbook_guide/playbooks_filters.md#playbooks-filters), [tests](../playbook_guide/playbooks_tests.md#playbooks-tests) and even each other to do some complex data generation and manipulation. For example:

```YAML+Jinja
tasks:
  - name: valid but useless and over complicated chained lookups and filters
    debug: msg="find the answer here:\n{{ lookup('url', 'https://google.com/search/?q=' + item|urlencode)|join(' ') }}"
    with_nested:
      - "{{ lookup('consul_kv', 'bcs/' + lookup('file', '/the/question') + ', host=localhost, port=2000')|shuffle }}"
      - "{{ lookup('sequence', 'end=42 start=2 step=2')|map('log', 4)|list) }}"
      - ['a', 'c', 'd', 'c']
```

New in version 2.6.

You can control how errors behave in all lookup plugins by setting `errors` to `ignore`, `warn`, or `strict`. The default setting is `strict`, which causes the task to fail if the lookup returns an error. For example:

To ignore lookup errors:

```YAML+Jinja
- name: if this file does not exist, I do not care .. file plugin itself warns anyway ...
  debug: msg="{{ lookup('file', '/nosuchfile', errors='ignore') }}"
```

```ansible-output
[WARNING]: Unable to find '/nosuchfile' in expected paths (use -vvvvv to see paths)

ok: [localhost] => {
    "msg": ""
}
```

To get a warning instead of a failure:

```YAML+Jinja
- name: if this file does not exist, let me know, but continue
  debug: msg="{{ lookup('file', '/nosuchfile', errors='warn') }}"
```

```ansible-output
[WARNING]: Unable to find '/nosuchfile' in expected paths (use -vvvvv to see paths)

[WARNING]: An unhandled exception occurred while running the lookup plugin 'file'. Error was a <class 'ansible.errors.AnsibleError'>, original message: could not locate file in lookup: /nosuchfile

ok: [localhost] => {
    "msg": ""
}
```

To get a fatal error (the default):

```YAML+Jinja
- name: if this file does not exist, FAIL (this is the default)
  debug: msg="{{ lookup('file', '/nosuchfile', errors='strict') }}"
```

```ansible-output
[WARNING]: Unable to find '/nosuchfile' in expected paths (use -vvvvv to see paths)

fatal: [localhost]: FAILED! => {"msg": "An unhandled exception occurred while running the lookup plugin 'file'. Error was a <class 'ansible.errors.AnsibleError'>, original message: could not locate file in lookup: /nosuchfile"}
```

## [Forcing lookups to return lists: `query` and `wantlist=True`](lookup.md#id4)

New in version 2.5.

In Ansible 2.5, a new Jinja2 function called `query` was added for invoking lookup plugins. The difference between `lookup` and `query` is largely that `query` will always return a list.
The default behavior of `lookup` is to return a string of comma separated values. `lookup` can be explicitly configured to return a list using `wantlist=True`.

This feature provides an easier and more consistent interface for interacting with the new `loop` keyword, while maintaining backwards compatibility with other uses of `lookup`.

The following examples are equivalent:

```jinja
lookup('dict', dict_variable, wantlist=True)

query('dict', dict_variable)
```

As demonstrated above, the behavior of `wantlist=True` is implicit when using `query`.

Additionally, `q` was introduced as a shortform of `query`:

```jinja
q('dict', dict_variable)
```

## [Plugin list](lookup.md#id5)

You can use `ansible-doc -t lookup -l` to see the list of available plugins. Use `ansible-doc -t lookup <plugin name>` to see plugin-specific documentation and examples.

> **See also:**
>
> [Ansible playbooks](../playbook_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Inventory plugins](inventory.md#inventory-plugins)
> :   Ansible inventory plugins
>
> [Callback plugins](callback.md#callback-plugins)
> :   Ansible callback plugins
>
> [Filter plugins](filter.md#filter-plugins)
> :   Jinja2 filter plugins
>
> [Test plugins](test.md#test-plugins)
> :   Jinja2 test plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
