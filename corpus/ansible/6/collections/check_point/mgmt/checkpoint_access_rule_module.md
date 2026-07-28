---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_access_rule module – Manages access rules on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_access_rule_module.html
fetched_at: 2026-07-27T16:47:29+00:00
---
# check_point.mgmt.checkpoint_access_rule module – Manages access rules on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_access_rule`.

- [Synopsis](checkpoint_access_rule_module.md#synopsis)
- [Parameters](checkpoint_access_rule_module.md#parameters)
- [Examples](checkpoint_access_rule_module.md#examples)
- [Return Values](checkpoint_access_rule_module.md#return-values)

## [Synopsis](checkpoint_access_rule_module.md#id1)

- Manages access rules on Check Point devices including creating, updating, removing access rules objects, All operations are performed over Web Services API.

## [Parameters](checkpoint_access_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Action of the access rule (accept, drop, inform, etc).  Default: `"drop"` |
| **auto_install_policy**  boolean | Install the package policy if changes have been performed after the task completes.  Choices:   - `false` - `true` ← (default) |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` ← (default) |
| **destination**  string | Destination object of the access rule. |
| **enabled**  boolean | Enabled or disabled flag.  Choices:   - `false` - `true` ← (default) |
| **layer**  string | Layer to attach the access rule to. |
| **name**  string / required | Name of the access rule. |
| **policy_package**  string | Package policy name to be installed.  Default: `"standard"` |
| **position**  string | Position of the access rule. |
| **source**  string | Source object of the access rule. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Default: `"present"` |
| **targets**  list / elements=string | Targets to install the package policy on. |

## [Examples](checkpoint_access_rule_module.md#id3)

```yaml+jinja
- name: Create access rule
  checkpoint_access_rule:
    layer: Network
    name: "Drop attacker"
    position: top
    source: attacker
    destination: Any
    action: Drop

- name: Delete access rule
  checkpoint_access_rule:
    layer: Network
    name: "Drop attacker"
```

## [Return Values](checkpoint_access_rule_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checkpoint_access_rules**  list / elements=string | The checkpoint access rule object created or updated.  Returned: always, except when deleting the access rule. |

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
