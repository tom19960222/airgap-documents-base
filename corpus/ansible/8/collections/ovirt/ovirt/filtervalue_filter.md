---
collection: ansible
version: "8"
title: "ovirt.ovirt.filtervalue filter – Filter to findall occurance of some value in dict"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/filtervalue_filter.html
fetched_at: 2026-07-28T02:50:20+00:00
---
# ovirt.ovirt.filtervalue filter – Filter to findall occurance of some value in dict

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
> To use it in a playbook, specify: `ovirt.ovirt.filtervalue`.

- [Synopsis](filtervalue_filter.md#synopsis)
- [Input](filtervalue_filter.md#input)
- [Positional parameters](filtervalue_filter.md#positional-parameters)
- [Examples](filtervalue_filter.md#examples)
- [Return Value](filtervalue_filter.md#return-value)

## [Synopsis](filtervalue_filter.md#id1)

- Filter to findall occurance of some value in dict

## [Input](filtervalue_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.filtervalue`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | List of VMs |

## [Positional parameters](filtervalue_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ovirt.ovirt.filtervalue(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **attr**  list / elements=string / required | Attribute to sotr by |
| **value**  list / elements=string / required | List of VMs |

## [Examples](filtervalue_filter.md#id4)

```yaml+jinja
- name: Set filtred ovirt_vms
  ansible.builtin.set_fact:
    ovirt_vms: "{{ vms | ovirt.ovirt.filtervalue('name', item.name) }}"
```

## [Return Value](filtervalue_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | Filtred VMs  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
