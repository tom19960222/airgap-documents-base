---
collection: ansible
version: "8"
title: "ovirt.ovirt.ovirtvmipsv6 filter – VM IPv4"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/ovirtvmipsv6_filter.html
fetched_at: 2026-07-28T02:50:29+00:00
---
# ovirt.ovirt.ovirtvmipsv6 filter – VM IPv4

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
> To use it in a playbook, specify: `ovirt.ovirt.ovirtvmipsv6`.

- [Synopsis](ovirtvmipsv6_filter.md#synopsis)
- [Input](ovirtvmipsv6_filter.md#input)
- [Keyword parameters](ovirtvmipsv6_filter.md#keyword-parameters)
- [Examples](ovirtvmipsv6_filter.md#examples)
- [Return Value](ovirtvmipsv6_filter.md#return-value)

## [Synopsis](ovirtvmipsv6_filter.md#id1)

- VM IPv4

## [Input](ovirtvmipsv6_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.ovirtvmipsv6`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | List of VMs |

## [Keyword parameters](ovirtvmipsv6_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ovirt.ovirt.ovirtvmipsv6(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **attr**  list / elements=string | Attribute by which the |
| **network_ip**  string | Filter the IPs by network address |

## [Examples](ovirtvmipsv6_filter.md#id4)

```yaml+jinja
- name: Print VM all IPv6
  debug:
    msg: "{{ vms.ovirt_vms | ovirt.ovirt.ovirtvmipsv6 }}"
- name: Print VM all IPv6
  debug:
    msg: "{{ vms.ovirt_vms | ovirt.ovirt.ovirtvmipsv6(attr='name') }}"
```

## [Return Value](ovirtvmipsv6_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | VM IPv4  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
