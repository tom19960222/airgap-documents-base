---
collection: ansible
version: "8"
title: "community.crypto.split_pem filter – Split PEM file contents into multiple objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/crypto/split_pem_filter.html
fetched_at: 2026-07-28T01:42:47+00:00
---
# community.crypto.split_pem filter – Split PEM file contents into multiple objects

> **Note:**
>
> This filter plugin is part of the [community.crypto collection](https://galaxy.ansible.com/ui/repo/published/community/crypto/) (version 2.16.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.crypto`.
>
> To use it in a playbook, specify: `community.crypto.split_pem`.

New in community.crypto 2.10.0

- [Synopsis](split_pem_filter.md#synopsis)
- [Input](split_pem_filter.md#input)
- [Examples](split_pem_filter.md#examples)
- [Return Value](split_pem_filter.md#return-value)

## [Synopsis](split_pem_filter.md#id1)

- Split PEM file contents into multiple PEM objects. Comments or invalid parts are ignored.

## [Input](split_pem_filter.md#id2)

This describes the input of the filter, the value before `| community.crypto.split_pem`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The PEM contents to split. |

## [Examples](split_pem_filter.md#id3)

```yaml+jinja
- name: Print all CA certificates
  ansible.builtin.debug:
    msg: '{{ item }}'
  loop: >-
    {{ lookup('ansible.builtin.file', '/path/to/ca-bundle.pem') | community.crypto.split_pem }}
```

## [Return Value](split_pem_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list of PEM file contents.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.crypto/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.crypto)
- [Submit a bug report](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.crypto/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-crypto)
