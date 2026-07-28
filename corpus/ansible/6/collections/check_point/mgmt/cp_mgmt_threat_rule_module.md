---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_threat_rule module – Manages threat-rule objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_threat_rule_module.html
fetched_at: 2026-07-27T16:48:48+00:00
---
# check_point.mgmt.cp_mgmt_threat_rule module – Manages threat-rule objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_threat_rule`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_threat_rule_module.md#synopsis)
- [Parameters](cp_mgmt_threat_rule_module.md#parameters)
- [Examples](cp_mgmt_threat_rule_module.md#examples)
- [Return Values](cp_mgmt_threat_rule_module.md#return-values)

## [Synopsis](cp_mgmt_threat_rule_module.md#id1)

- Manages threat-rule objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_threat_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Action-the enforced profile. |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` |
| **comments**  string | Comments string. |
| **destination**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **destination_negate**  boolean | True if negate is set for destination.  Choices:   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Enable/Disable the rule.  Choices:   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **install_on**  list / elements=string | Which Gateways identified by the name or UID to install the policy on. |
| **layer**  string | Layer that the rule belongs to identified by the name or UID. |
| **name**  string / required | Object name. |
| **position**  string | Position in the rulebase. |
| **protected_scope**  list / elements=string | Collection of objects defining Protected Scope identified by the name or UID. |
| **protected_scope_negate**  boolean | True if negate is set for Protected Scope.  Choices:   - `false` - `true` |
| **service**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **service_negate**  boolean | True if negate is set for Service.  Choices:   - `false` - `true` |
| **source**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **source_negate**  boolean | True if negate is set for source.  Choices:   - `false` - `true` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **track**  string | Packet tracking. |
| **track_settings**  dictionary | Threat rule track settings. |
| **packet_capture**  boolean | Packet capture.  Choices:   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_threat_rule_module.md#id3)

```yaml+jinja
- name: add-threat-rule
  cp_mgmt_threat_rule:
    comments: ''
    install_on: Policy Targets
    layer: New Layer 1
    name: First threat rule
    position: 1
    protected_scope: All_Internet
    state: present
    track: None

- name: set-threat-rule
  cp_mgmt_threat_rule:
    action: New Profile 1
    comments: commnet for the first rule
    install_on: Policy Targets
    layer: New Layer 1
    name: Rule Name
    position: 1
    protected_scope: All_Internet
    state: present

- name: delete-threat-rule
  cp_mgmt_threat_rule:
    layer: New Layer 1
    name: Rule Name
    state: absent
```

## [Return Values](cp_mgmt_threat_rule_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_threat_rule**  dictionary | The checkpoint object created or updated.  Returned: always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
