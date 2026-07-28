---
collection: ansible
version: "8"
title: "ovirt.ovirt.get_network_xml_to_dict filter – Get network bridge and uuid to dict"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/get_network_xml_to_dict_filter.html
fetched_at: 2026-07-28T02:50:21+00:00
---
# ovirt.ovirt.get_network_xml_to_dict filter – Get network bridge and uuid to dict

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
> To use it in a playbook, specify: `ovirt.ovirt.get_network_xml_to_dict`.

- [Synopsis](get_network_xml_to_dict_filter.md#synopsis)
- [Input](get_network_xml_to_dict_filter.md#input)
- [Examples](get_network_xml_to_dict_filter.md#examples)
- [Return Value](get_network_xml_to_dict_filter.md#return-value)

## [Synopsis](get_network_xml_to_dict_filter.md#id1)

- Get network bridge and uuid to dict

## [Input](get_network_xml_to_dict_filter.md#id2)

This describes the input of the filter, the value before `| ovirt.ovirt.get_network_xml_to_dict`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | xml |

## [Examples](get_network_xml_to_dict_filter.md#id3)

```yaml+jinja
- name: Set network_dict from default_net_xml
  ansible.builtin.set_fact:
    network_dict: "{{ default_net_xml['stdout'] | ovirt.ovirt.get_network_xml_to_dict }}"
```

## [Return Value](get_network_xml_to_dict_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | Dict of network  **Returned:** success |

### Authors

- Martin Necas (@mnecas)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
