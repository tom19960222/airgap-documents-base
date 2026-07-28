---
collection: ansible
version: "6"
title: "ansible.builtin.unvault lookup – read vaulted file(s) contents"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/unvault_lookup.html
fetched_at: 2026-07-27T16:44:24+00:00
---
# ansible.builtin.unvault lookup – read vaulted file(s) contents

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `unvault` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

New in ansible-base 2.10

- [Synopsis](unvault_lookup.md#synopsis)
- [Terms](unvault_lookup.md#terms)
- [Notes](unvault_lookup.md#notes)
- [Examples](unvault_lookup.md#examples)
- [Return Value](unvault_lookup.md#return-value)

## [Synopsis](unvault_lookup.md#id1)

- This lookup returns the contents from vaulted (or not) file(s) on the Ansible controller’s file system.

## [Terms](unvault_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | path(s) of files to read |

## [Notes](unvault_lookup.md#id3)

> **Note:**
>
> - This lookup does not understand ‘globbing’ nor shell environment variables.

## [Examples](unvault_lookup.md#id4)

```yaml+jinja
- ansible.builtin.debug: msg="the value of foo.txt is {{lookup('ansible.builtin.unvault', '/etc/foo.txt')|to_string }}"
```

## [Return Value](unvault_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | content of file(s) as bytes  Returned: success |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
