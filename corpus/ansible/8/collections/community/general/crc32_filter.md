---
collection: ansible
version: "8"
title: "community.general.crc32 filter – Generate a CRC32 checksum"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/crc32_filter.html
fetched_at: 2026-07-28T01:52:16+00:00
---
# community.general.crc32 filter – Generate a CRC32 checksum

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.crc32`.

New in community.general 5.4.0

- [Synopsis](crc32_filter.md#synopsis)
- [Input](crc32_filter.md#input)
- [Examples](crc32_filter.md#examples)
- [Return Value](crc32_filter.md#return-value)

## [Synopsis](crc32_filter.md#id1)

- Checksum a string using CRC32 algorithm and return its hexadecimal representation.

## [Input](crc32_filter.md#id2)

This describes the input of the filter, the value before `| community.general.crc32`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | The string to checksum. |

## [Examples](crc32_filter.md#id3)

```yaml+jinja
- name: Checksum a test string
  ansible.builtin.debug:
    msg: "{{ 'test' | community.general.crc32 }}"
```

## [Return Value](crc32_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | CRC32 checksum.  **Returned:** success |

### Authors

- Julien Riou

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
