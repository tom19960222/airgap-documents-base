---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_nat_rule module – Manages nat-rule objects on Checkpoint over Web Services API."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_nat_rule_module.html
fetched_at: 2026-07-28T01:16:51+00:00
---
# check_point.mgmt.cp_mgmt_nat_rule module – Manages nat-rule objects on Checkpoint over Web Services API.

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_nat_rule`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_nat_rule_module.md#synopsis)
- [Parameters](cp_mgmt_nat_rule_module.md#parameters)
- [Examples](cp_mgmt_nat_rule_module.md#examples)
- [Return Values](cp_mgmt_nat_rule_module.md#return-values)

## [Synopsis](cp_mgmt_nat_rule_module.md#id1)

- Manages nat-rule objects on Checkpoint devices including creating, updating and removing objects.
- Minimum version required is 1.7.1 and JHF with PMTR-88097.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_nat_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Enable/Disable the rule.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **install_on**  list / elements=string | Which Gateways identified by the name or UID to install the policy on. |
| **method**  string | Nat method.  **Choices:**   - `"static"` - `"hide"` - `"nat64"` - `"nat46"` - `"cgnat"` |
| **name**  string / required | Rule name. |
| **original_destination**  string | Original destination. |
| **original_service**  string | Original service. |
| **original_source**  string | Original source. |
| **package**  string | Name of the package. |
| **position**  string | Position in the rulebase. The use of values “top” and “bottom” may not be idempotent. |
| **relative_position**  dictionary | Position in the rulebase.  Use of this field may not be idempotent. |
| **above**  string | Add rule above specific rule/section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **below**  string | Add rule below specific rule/section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **bottom**  string | Add rule to the bottom of a specific section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **top**  string | Add rule to the top of a specific section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **search_entire_rulebase**  boolean | Whether to search the entire rulebase for a rule that’s been edited in its relative_position field to make sure there indeed has been a change in its position or the section it might be in.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **translated_destination**  string | Translated destination. |
| **translated_service**  string | Translated service. |
| **translated_source**  string | Translated source. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_nat_rule_module.md#id3)

```yaml+jinja
- name: add-nat-rule
  cp_mgmt_nat_rule:
    name: nat_rule1
    comments: comment example1 nat999
    enabled: false
    install_on:
    - Policy Targets
    original_destination: All_Internet
    original_source: Any
    package: standard
    position: 1
    state: present

- name: set-nat-rule
  cp_mgmt_nat_rule:
    name: nat_rule1
    comments: rule for RND members  RNDNetwork-> RND to Internal Network
    enabled: false
    original_service: ssh_version_2
    original_source: Any
    package: standard
    state: present

- name: delete-nat-rule
  cp_mgmt_nat_rule:
    name: nat_rule1
    package: standard
    state: absent
```

## [Return Values](cp_mgmt_nat_rule_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_nat_rule**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
