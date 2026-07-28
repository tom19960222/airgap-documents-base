---
collection: ansible
version: "8"
title: "ansible.builtin.path_join filter – Join one or more path components"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/path_join_filter.html
fetched_at: 2026-07-28T01:08:11+00:00
---
# ansible.builtin.path_join filter – Join one or more path components

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `path_join`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.path_join` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-base 2.10

- [Synopsis](path_join_filter.md#synopsis)
- [Input](path_join_filter.md#input)
- [Examples](path_join_filter.md#examples)
- [Return Value](path_join_filter.md#return-value)

## [Synopsis](path_join_filter.md#id1)

- Returns a path obtained by joining one or more path components.

## [Input](path_join_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.path_join`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A path, or a list of paths. |

## [Examples](path_join_filter.md#id3)

```yaml+jinja
# If path == 'foo/bar' and file == 'baz.txt', the result is '/etc/foo/bar/subdir/baz.txt'
{{ ('/etc', path, 'subdir', file) | path_join }}

# equivalent to '/etc/subdir/{{filename}}'
wheremyfile: "{{ ['/etc', 'subdir', filename] | path_join }}"

# trustme => '/etc/apt/trusted.d/mykey.gpgp'
trustme: "{{ ['/etc', 'apt', 'trusted.d', 'mykey.gpg'] | path_join }}"
```

## [Return Value](path_join_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The concatenated path.  **Returned:** success |

### Authors

- Anthony Bourguignon (@Toniob)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
