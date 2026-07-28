---
collection: ansible
version: "8"
title: "ansible.builtin.sha1 filter – SHA-1 hash of input data"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/sha1_filter.html
fetched_at: 2026-07-28T01:08:17+00:00
---
# ansible.builtin.sha1 filter – SHA-1 hash of input data

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `sha1`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.sha1` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](sha1_filter.md#synopsis)
- [Input](sha1_filter.md#input)
- [Notes](sha1_filter.md#notes)
- [Examples](sha1_filter.md#examples)
- [Return Value](sha1_filter.md#return-value)

## [Synopsis](sha1_filter.md#id1)

- Returns a [SHA-1 hash](https://en.wikipedia.org/wiki/SHA-1) of the input data.

## [Input](sha1_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.sha1`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | Data to hash. |

## [Notes](sha1_filter.md#id3)

> **Note:**
>
> - This requires the SHA-1 algorithm to be available on the system, security contexts like FIPS might prevent this.
> - SHA-1 has been deemed insecure and is not recommended for security related uses.

## [Examples](sha1_filter.md#id4)

```yaml+jinja
# sha1hash => "dc724af18fbdd4e59189f5fe768a5f8311527050"
sha1hash: "{{ 'testing' | sha1 }}"
```

## [Return Value](sha1_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The SHA-1 hash of the input.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
