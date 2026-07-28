---
collection: ansible
version: "6"
title: "ansible.builtin.file lookup – read file contents"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/file_lookup.html
fetched_at: 2026-07-27T16:44:20+00:00
---
# ansible.builtin.file lookup – read file contents

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `file` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](file_lookup.md#synopsis)
- [Terms](file_lookup.md#terms)
- [Keyword parameters](file_lookup.md#keyword-parameters)
- [Notes](file_lookup.md#notes)
- [Examples](file_lookup.md#examples)
- [Return Value](file_lookup.md#return-value)

## [Synopsis](file_lookup.md#id1)

- This lookup returns the contents from a file on the Ansible controller’s file system.

## [Terms](file_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | path(s) of files to read |

## [Keyword parameters](file_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.file', key1=value1, key2=value2, ...)` and `query('ansible.builtin.file', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **lstrip**  boolean | whether or not to remove whitespace from the beginning of the looked-up file  Choices:   - `false` ← (default) - `true` |
| **rstrip**  boolean | whether or not to remove whitespace from the ending of the looked-up file  Choices:   - `false` - `true` ← (default) |

## [Notes](file_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.file', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.file', term1, term2, key1=value1, key2=value2)`
> - if read in variable context, the file can be interpreted as YAML if the content is valid to the parser.
> - this lookup does not understand ‘globbing’, use the fileglob lookup instead.

## [Examples](file_lookup.md#id5)

```yaml+jinja
- ansible.builtin.debug:
    msg: "the value of foo.txt is {{lookup('ansible.builtin.file', '/etc/foo.txt') }}"

- name: display multiple file contents
  ansible.builtin.debug: var=item
  with_file:
    - "/path/to/foo.txt"
    - "bar.txt"  # will be looked in files/ dir relative to play or in role
    - "/path/to/biz.txt"
```

## [Return Value](file_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | content of file(s)  Returned: success |

### Authors

- Daniel Hokka Zakrisson

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
