---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirtvmip filter – Return first IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirtvmip_filter.html
fetched_at: 2026-07-28T02:50:26+00:00
---
# ovirt.ovirt.ovirtvmip filter – Return first IP

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
> To use it in a playbook, specify: `ovirt.ovirt.ovirtvmip`.

- [Synopsis](ovirtvmip_filter.md#synopsis)
- [Input](ovirtvmip_filter.md#input)
- [Positional parameters](ovirtvmip_filter.md#positional-parameters)
- [Examples](ovirtvmip_filter.md#examples)
- [Return Value](ovirtvmip_filter.md#return-value)

## [Synopsis](ovirtvmip_filter.md#id1)

- Return first IP

## [Input](ovirtvmip_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.ovirtvmip`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | List of VMs |

## [Positional parameters](ovirtvmip_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ovirt.ovirt.ovirtvmip(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **attr**  list / elements=string | Attribute by which the |
| **network_ip**  string | Filter the IPs by network address |

## [Examples](ovirtvmip_filter.md#id4)

```yaml+jinja
- name: Print VM IP
  debug:
    msg: "{{ vms.ovirt_vms | ovirt.ovirt.ovirtvmip }}"
- name: Print VM IP
  debug:
    msg: "{{ vms.ovirt_vms | ovirt.ovirt.ovirtvmip(attr='name') }}"
```

## [Return Value](ovirtvmip_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | First IP  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
