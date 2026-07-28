---
collection: ansible
version: "6"
title: "community.fortios.fmgr_fwobj_ippool6 module – Allows the editing of IP Pool Objects within FortiManager."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_fwobj_ippool6_module.html
fetched_at: 2026-07-27T17:07:41+00:00
---
# community.fortios.fmgr_fwobj_ippool6 module – Allows the editing of IP Pool Objects within FortiManager.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_fwobj_ippool6`.

- [Synopsis](fmgr_fwobj_ippool6_module.md#synopsis)
- [Parameters](fmgr_fwobj_ippool6_module.md#parameters)
- [Notes](fmgr_fwobj_ippool6_module.md#notes)
- [Examples](fmgr_fwobj_ippool6_module.md#examples)
- [Return Values](fmgr_fwobj_ippool6_module.md#return-values)

## [Synopsis](fmgr_fwobj_ippool6_module.md#id1)

- Allows users to add/edit/delete IPv6 Pool Objects.

## [Parameters](fmgr_fwobj_ippool6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **comments**  string | Comment. |
| **dynamic_mapping**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **dynamic_mapping_comments**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_endip**  string | Dynamic Mapping clone of original suffixed parameter. |
| **dynamic_mapping_startip**  string | Dynamic Mapping clone of original suffixed parameter. |
| **endip**  string | Final IPv6 address (inclusive) in the range for the address pool. |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | IPv6 IP pool name. |
| **startip**  string | First IPv6 address (inclusive) in the range for the address pool. |

## [Notes](fmgr_fwobj_ippool6_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_fwobj_ippool6_module.md#id4)

```yaml+jinja
- name: ADD FMGR_FIREWALL_IPPOOL6
  fmgr_firewall_ippool6:
    mode: "add"
    adom: "ansible"
    startip:
    name: "IPv6 IPPool"
    endip:
    comments: "Created by Ansible"

- name: DELETE FMGR_FIREWALL_IPPOOL6
  fmgr_firewall_ippool6:
    mode: "delete"
    adom: "ansible"
    name: "IPv6 IPPool"
```

## [Return Values](fmgr_fwobj_ippool6_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
