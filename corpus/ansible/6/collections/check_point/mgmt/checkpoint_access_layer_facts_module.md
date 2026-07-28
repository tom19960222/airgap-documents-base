---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_access_layer_facts module – Get access layer facts on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_access_layer_facts_module.html
fetched_at: 2026-07-27T16:47:29+00:00
---
# check_point.mgmt.checkpoint_access_layer_facts module – Get access layer facts on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_access_layer_facts`.

- [Synopsis](checkpoint_access_layer_facts_module.md#synopsis)
- [Parameters](checkpoint_access_layer_facts_module.md#parameters)
- [Examples](checkpoint_access_layer_facts_module.md#examples)

## [Synopsis](checkpoint_access_layer_facts_module.md#id1)

- Get access layer facts on Check Point devices. All operations are performed over Web Services API.

## [Parameters](checkpoint_access_layer_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | Name of the access layer object. |
| **uid**  string | UID of access layer object. |

## [Examples](checkpoint_access_layer_facts_module.md#id3)

```yaml+jinja
- name: Get object facts
  checkpoint_access_layer_facts:
```

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
