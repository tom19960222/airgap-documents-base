---
collection: ansible
version: "8"
title: "ovirt.ovirt.convert_to_bytes filter – Convert units to bytes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/convert_to_bytes_filter.html
fetched_at: 2026-07-28T02:50:19+00:00
---
# ovirt.ovirt.convert_to_bytes filter – Convert units to bytes

> **Note:**
>
> This filter plugin is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
>
> To use it in a playbook, specify: `ovirt.ovirt.convert_to_bytes`.

- [Synopsis](convert_to_bytes_filter.md#synopsis)
- [Input](convert_to_bytes_filter.md#input)
- [Examples](convert_to_bytes_filter.md#examples)
- [Return Value](convert_to_bytes_filter.md#return-value)

## [Synopsis](convert_to_bytes_filter.md#id1)

- This method convert units to bytes, which follow IEC standard

## [Input](convert_to_bytes_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.convert_to_bytes`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Value to be converted |

## [Examples](convert_to_bytes_filter.md#id3)

```yaml+jinja
- name: Get number of bytes
  ansible.builtin.set_fact:
    disk_size: "{{ '1KiB' | ovirt.ovirt.convert_to_bytes }}"
```

## [Return Value](convert_to_bytes_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  integer | Amount of bytes  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
