---
collection: ansible
version: "8"
title: "ovirt.ovirt.get_ovf_disk_size filter – Get OVF disk size"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/get_ovf_disk_size_filter.html
fetched_at: 2026-07-28T02:50:23+00:00
---
# ovirt.ovirt.get_ovf_disk_size filter – Get OVF disk size

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
> To use it in a playbook, specify: `ovirt.ovirt.get_ovf_disk_size`.

- [Synopsis](get_ovf_disk_size_filter.md#synopsis)
- [Input](get_ovf_disk_size_filter.md#input)
- [Examples](get_ovf_disk_size_filter.md#examples)
- [Return Value](get_ovf_disk_size_filter.md#return-value)

## [Synopsis](get_ovf_disk_size_filter.md#id1)

- Get OVF disk size.

## [Input](get_ovf_disk_size_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.get_ovf_disk_size`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | OVF data |

## [Examples](get_ovf_disk_size_filter.md#id3)

```yaml+jinja
- name: Get ovf data
  ansible.builtin.command: cat "{{ path }}"
  register: ovf_data
- name: Get disk size from ovf data
  ansible.builtin.set_fact:
    disk_size: "{{ ovf_data['stdout'] | ovirt.ovirt.get_ovf_disk_size }}"
```

## [Return Value](get_ovf_disk_size_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | OVF disk size  **Returned:** success |

### Authors

- Asaf Rachmani (@arachmani)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
