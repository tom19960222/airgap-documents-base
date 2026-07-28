---
collection: ansible
version: "8"
title: "cisco.aci.interface_range lookup – query interfaces from a range or comma separated list of ranges"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/interface_range_lookup.html
fetched_at: 2026-07-28T01:21:06+00:00
---
# cisco.aci.interface_range lookup – query interfaces from a range or comma separated list of ranges

> **Note:**
>
> This lookup plugin is part of the [cisco.aci collection](https://galaxy.ansible.com/ui/repo/published/cisco/aci/) (version 2.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.aci`.
>
> To use it in a playbook, specify: `cisco.aci.interface_range`.

- [Synopsis](interface_range_lookup.md#synopsis)
- [Terms](interface_range_lookup.md#terms)
- [Notes](interface_range_lookup.md#notes)
- [Examples](interface_range_lookup.md#examples)
- [Return Value](interface_range_lookup.md#return-value)

## [Synopsis](interface_range_lookup.md#id1)

- this lookup returns interfaces from a range or comma separated list of ranges given to it

## [Terms](interface_range_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | comma separated strings of interface ranges |

## [Notes](interface_range_lookup.md#id3)

> **Note:**
>
> - duplicate interfaces from overlapping ranges will only be returned once

## [Examples](interface_range_lookup.md#id4)

```yaml+jinja
- name: "loop through range of interfaces"
  ansible.builtin.debug:
    msg: "{{ item }}"
  with_items: "{{ query('cisco.aci.interface_range', '1/1-4,1/20-25', '1/5', '1/2/3/8-10', '5/0-2') }}"
```

## [Return Value](interface_range_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | list of interfaces  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)
