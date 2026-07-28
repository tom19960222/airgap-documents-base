---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_run_script module – Run scripts on Check Point devices over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_run_script_module.html
fetched_at: 2026-07-27T16:47:31+00:00
---
# check_point.mgmt.checkpoint_run_script module – Run scripts on Check Point devices over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_run_script`.

New in check_point.mgmt 2.7

- [Synopsis](checkpoint_run_script_module.md#synopsis)
- [Parameters](checkpoint_run_script_module.md#parameters)
- [Examples](checkpoint_run_script_module.md#examples)
- [Return Values](checkpoint_run_script_module.md#return-values)

## [Synopsis](checkpoint_run_script_module.md#id1)

- Run scripts on Check Point devices. All operations are performed over Web Services API.

## [Parameters](checkpoint_run_script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **script**  string / required | Script body contents. |
| **script_name**  string / required | Name of the script. |
| **targets**  list / elements=string / required | Targets the script should be run against. Can reference either name or UID. |

## [Examples](checkpoint_run_script_module.md#id3)

```yaml+jinja
- name: Run script
  checkpoint_run_script:
    script_name: "List root"
    script: ls -l /
    targets:
      - mycheckpointgw
```

## [Return Values](checkpoint_run_script_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checkpoint_run_script**  list / elements=string | The checkpoint run script output.  Returned: always. |

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
