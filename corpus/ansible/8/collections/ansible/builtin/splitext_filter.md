---
collection: ansible
version: "8"
title: "ansible.builtin.splitext filter – split a path into root and file extension"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/splitext_filter.html
fetched_at: 2026-07-28T01:05:03+00:00
---
# ansible.builtin.splitext filter – split a path into root and file extension

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `splitext`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.splitext` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](splitext_filter.md#synopsis)
- [Input](splitext_filter.md#input)
- [Examples](splitext_filter.md#examples)
- [Return Value](splitext_filter.md#return-value)

## [Synopsis](splitext_filter.md#id1)

- Returns a list of two, with the elements consisting of filename root and extension.

## [Input](splitext_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.splitext`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A path. |

## [Examples](splitext_filter.md#id3)

```yaml+jinja
# gobble => [ '/etc/make', 'conf' ]
gobble: "{{ '/etc/make.conf' | splitext }}"

# file_n_ext => [ 'ansible', 'cfg' ]
file_n_ext: "{{ 'ansible.cfg' | splitext }}"

# hoax => ['/etc/hoasdf', '']
hoax: '{{ "/etc//hoasdf/"|splitext }}'
```

## [Return Value](splitext_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list consisting of root of the path and the extension.  **Returned:** success |

### Authors

- Matt Martz (@sivel)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
