---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_access_rule_facts module – Get access rules objects facts on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_access_rule_facts_module.html
fetched_at: 2026-07-27T16:47:30+00:00
---
# check_point.mgmt.checkpoint_access_rule_facts module – Get access rules objects facts on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_access_rule_facts`.

- [Synopsis](checkpoint_access_rule_facts_module.md#synopsis)
- [Parameters](checkpoint_access_rule_facts_module.md#parameters)
- [Examples](checkpoint_access_rule_facts_module.md#examples)

## [Synopsis](checkpoint_access_rule_facts_module.md#id1)

- Get access rules objects facts on Check Point devices. All operations are performed over Web Services API.

## [Parameters](checkpoint_access_rule_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **layer**  string / required | Layer the access rule is attached to. |
| **name**  string | Name of the access rule. If not provided, UID is required. |
| **uid**  string | UID of the access rule. If not provided, name is required. |

## [Examples](checkpoint_access_rule_facts_module.md#id3)

```yaml+jinja
- name: Get access rule facts
  checkpoint_access_rule_facts:
    layer: Network
    name: "Drop attacker"
```

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
