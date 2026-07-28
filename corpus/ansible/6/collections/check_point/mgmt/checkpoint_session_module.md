---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_session module – Manages session objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_session_module.html
fetched_at: 2026-07-27T16:47:31+00:00
---
# check_point.mgmt.checkpoint_session module – Manages session objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_session`.

New in check_point.mgmt 2.7

- [Synopsis](checkpoint_session_module.md#synopsis)
- [Parameters](checkpoint_session_module.md#parameters)
- [Examples](checkpoint_session_module.md#examples)
- [Return Values](checkpoint_session_module.md#return-values)

## [Synopsis](checkpoint_session_module.md#id1)

- Manages session objects on Check Point devices performing actions like publish and discard. All operations are performed over Web Services API.

## [Parameters](checkpoint_session_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **state**  string | Action to perform on the session object. Valid choices are published and discarded.  Choices:   - `"published"` ← (default) - `"discarded"` |
| **uid**  string / required | UID of the session. |

## [Examples](checkpoint_session_module.md#id3)

```yaml+jinja
- name: Publish session
  checkpoint_session:
    uid: 7a13a360-9b24-40d7-acd3-5b50247be33e
    state: published

- name: Discard session
  checkpoint_session:
    uid: 7a13a360-9b24-40d7-acd3-5b50247be33e
    state: discarded
```

## [Return Values](checkpoint_session_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checkpoint_session**  list / elements=string | The checkpoint session output per return from API. It will differ depending on action.  Returned: always. |

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
