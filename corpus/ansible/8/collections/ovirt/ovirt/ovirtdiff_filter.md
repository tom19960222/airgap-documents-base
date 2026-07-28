---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirtdiff filter – Show what will be changed in next run of the VM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirtdiff_filter.html
fetched_at: 2026-07-28T02:50:25+00:00
---
# ovirt.ovirt.ovirtdiff filter – Show what will be changed in next run of the VM

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
> To use it in a playbook, specify: `ovirt.ovirt.ovirtdiff`.

- [Synopsis](ovirtdiff_filter.md#synopsis)
- [Input](ovirtdiff_filter.md#input)
- [Examples](ovirtdiff_filter.md#examples)
- [Return Value](ovirtdiff_filter.md#return-value)

## [Synopsis](ovirtdiff_filter.md#id1)

- Show what will be changed in next run of the VM

## [Input](ovirtdiff_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.ovirtdiff`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | VM |

## [Examples](ovirtdiff_filter.md#id3)

```yaml+jinja
- name: Get VM myvm
  ovirt_vm_info:
    auth: "{{ ovirt_auth }}"
    pattern: 'name={{ myvm }}'
    next_run: false
  register: vm

- name: Get next_run of VM myvm
  ovirt_vm_info:
    auth: "{{ ovirt_auth }}"
    pattern: 'name={{ myvm }}'
    next_run: true
  register: vm_next_run

- name: Print what will be changed in next run of the VM
  debug:
    msg: "{{ vm.ovirt_vms[0] | ovirt.ovirt.ovirtdiff(vm_next_run.ovirt_vms[0]) }}"
```

## [Return Value](ovirtdiff_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | VM  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
