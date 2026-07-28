---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_install_policy module – install policy on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_install_policy_module.html
fetched_at: 2026-07-27T16:48:04+00:00
---
# check_point.mgmt.cp_mgmt_install_policy module – install policy on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_install_policy`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_install_policy_module.md#synopsis)
- [Parameters](cp_mgmt_install_policy_module.md#parameters)
- [Examples](cp_mgmt_install_policy_module.md#examples)
- [Return Values](cp_mgmt_install_policy_module.md#return-values)

## [Synopsis](cp_mgmt_install_policy_module.md#id1)

- install policy on Check Point over Web Services API
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_install_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access**  boolean | Set to be true in order to install the Access Control policy. By default, the value is true if Access Control policy is enabled on the input policy package, otherwise false.  Choices:   - `false` - `true` |
| **desktop_security**  boolean | Set to be true in order to install the Desktop Security policy. By default, the value is true if desktop security policy is enabled on the input policy package, otherwise false.  Choices:   - `false` - `true` |
| **install_on_all_cluster_members_or_fail**  boolean | Relevant for the gateway clusters. If true, the policy is installed on all the cluster members. If the installation on a cluster member fails, don’t install on that cluster.  Choices:   - `false` - `true` |
| **policy_package**  string | The name of the Policy Package to be installed. |
| **prepare_only**  boolean | If true, prepares the policy for the installation, but doesn’t install it on an installation target.  Choices:   - `false` - `true` |
| **qos**  boolean | Set to be true in order to install the QoS policy. By default, the value is true if Quality-of-Service policy is enabled on the input policy package, otherwise false.  Choices:   - `false` - `true` |
| **revision**  string | The UID of the revision of the policy to install. |
| **targets**  list / elements=string | On what targets to execute this command. Targets may be identified by their name, or object unique identifier. |
| **threat_prevention**  boolean | Set to be true in order to install the Threat Prevention policy. By default, the value is true if Threat Prevention policy is enabled on the input policy package, otherwise false.  Choices:   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_install_policy_module.md#id3)

```yaml+jinja
- name: install-policy
  cp_mgmt_install_policy:
    access: true
    policy_package: standard
    targets:
    - corporate-gateway
    threat_prevention: true
```

## [Return Values](cp_mgmt_install_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_install_policy**  dictionary | The checkpoint install-policy output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
