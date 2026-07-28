---
collection: ansible
version: "8"
title: "ovirt.ovirt.removesensitivevmdata filter – removesensitivevmdata internal filter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/removesensitivevmdata_filter.html
fetched_at: 2026-07-28T02:50:32+00:00
---
# ovirt.ovirt.removesensitivevmdata filter – removesensitivevmdata internal filter

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
> To use it in a playbook, specify: `ovirt.ovirt.removesensitivevmdata`.

- [Synopsis](removesensitivevmdata_filter.md#synopsis)
- [Input](removesensitivevmdata_filter.md#input)
- [Examples](removesensitivevmdata_filter.md#examples)
- [Return Value](removesensitivevmdata_filter.md#return-value)

## [Synopsis](removesensitivevmdata_filter.md#id1)

- removesensitivevmdata internal filter

## [Input](removesensitivevmdata_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.removesensitivevmdata`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | List of VMs |

## [Examples](removesensitivevmdata_filter.md#id3)

```yaml+jinja
- name: Print VM
  debug:
    msg: "{{ vms | ovirt.ovirt.removesensitivevmdata }}"
```

## [Return Value](removesensitivevmdata_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of VMs  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
