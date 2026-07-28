---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_add_nat_rule module – Create new object."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_add_nat_rule_module.html
fetched_at: 2026-07-28T01:15:43+00:00
---
# check_point.mgmt.cp_mgmt_add_nat_rule module – Create new object.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_add_nat_rule`.

New in check_point.mgmt 2.0.0

- [DEPRECATED](cp_mgmt_add_nat_rule_module.md#deprecated)
- [Synopsis](cp_mgmt_add_nat_rule_module.md#synopsis)
- [Parameters](cp_mgmt_add_nat_rule_module.md#parameters)
- [Examples](cp_mgmt_add_nat_rule_module.md#examples)
- [Return Values](cp_mgmt_add_nat_rule_module.md#return-values)
- [Status](cp_mgmt_add_nat_rule_module.md#status)

## [DEPRECATED](cp_mgmt_add_nat_rule_module.md#id1)

Removed in:
:   major release after 2024-11-01

Why:
:   Newer and updated module released with more functionality.

Alternative:
:   cp_mgmt_nat_rule

## [Synopsis](cp_mgmt_add_nat_rule_module.md#id2)

- Create new object.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_add_nat_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Enable/Disable the rule.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **install_on**  list / elements=string | Which Gateways identified by the name or UID to install the policy on. |
| **method**  string | Nat method.  **Choices:**   - `"static"` - `"hide"` - `"nat64"` - `"nat46"` |
| **original_destination**  string | Original destination. |
| **original_service**  string | Original service. |
| **original_source**  string | Original source. |
| **package**  string | Name of the package. |
| **position**  string | Position in the rulebase. |
| **translated_destination**  string | Translated destination. |
| **translated_service**  string | Translated service. |
| **translated_source**  string | Translated source. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_add_nat_rule_module.md#id4)

```yaml+jinja
- name: add-nat-rule
  cp_mgmt_add_nat_rule:
    comments: comment example1 nat999
    enabled: false
    install_on:
    - Policy Targets
    original_destination: All_Internet
    original_source: Any
    package: standard
    position: 1
```

## [Return Values](cp_mgmt_add_nat_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_add_nat_rule**  dictionary | The checkpoint add-nat-rule output.  **Returned:** always. |

## [Status](cp_mgmt_add_nat_rule_module.md#id6)

- This module will be removed in a major release after 2024-11-01.
  *[deprecated]*
- For more information see [DEPRECATED](cp_mgmt_add_nat_rule_module.md#deprecated).

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
