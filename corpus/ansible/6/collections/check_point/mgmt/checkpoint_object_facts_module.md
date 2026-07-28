---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_object_facts module – Get object facts on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_object_facts_module.html
fetched_at: 2026-07-27T16:47:31+00:00
---
# check_point.mgmt.checkpoint_object_facts module – Get object facts on Check Point over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_object_facts`.

- [Synopsis](checkpoint_object_facts_module.md#synopsis)
- [Parameters](checkpoint_object_facts_module.md#parameters)
- [Examples](checkpoint_object_facts_module.md#examples)
- [Return Values](checkpoint_object_facts_module.md#return-values)

## [Synopsis](checkpoint_object_facts_module.md#id1)

- Get object facts on Check Point devices. All operations are performed over Web Services API.

## [Parameters](checkpoint_object_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ip_only**  boolean | Filter only by IP address.  Choices:   - `false` ← (default) - `true` |
| **object_filter**  string | Filter expression for search. It accepts AND/OR logical operators and performs a textual and IP address search. To search only by IP address, set ip_only argument to True. which can be filtered with the filter argument. |
| **object_type**  string | Type of the object to search. Must be a valid API resource name |
| **uid**  string | UID of the object. If UID is not provided, it will do a full search which can be filtered with the filter argument. |

## [Examples](checkpoint_object_facts_module.md#id3)

```yaml+jinja
- name: Get object facts
  checkpoint_object_facts:
    object_filter: 192.168.30.30
    ip_only: yes
```

## [Return Values](checkpoint_object_facts_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_hosts**  list / elements=string | The checkpoint object facts.  Returned: always. |

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
