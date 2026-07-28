---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_delete_rules_batch module – Delete rules in batch from the same layer. Use this API to achieve optimum performance when removing more than one rule."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_delete_rules_batch_module.html
fetched_at: 2026-07-28T01:16:04+00:00
---
# check_point.mgmt.cp_mgmt_delete_rules_batch module – Delete rules in batch from the same layer. Use this API to achieve optimum performance when removing more than one rule.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_delete_rules_batch`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_delete_rules_batch_module.md#synopsis)
- [Parameters](cp_mgmt_delete_rules_batch_module.md#parameters)
- [Examples](cp_mgmt_delete_rules_batch_module.md#examples)
- [Return Values](cp_mgmt_delete_rules_batch_module.md#return-values)

## [Synopsis](cp_mgmt_delete_rules_batch_module.md#id1)

- Delete rules in batch from the same layer. Use this API to achieve optimum performance when removing more than one rule.
- Warnings are ignored when using this API, operation will apply changes while ignoring warnings.
- Supported rules types are access-rule, nat-rule, https-rule and threat-exception.
- This module is not idempotent.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_delete_rules_batch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **objects**  list / elements=dictionary | Batch of rules separated by types. |
| **layer**  string | Layer name or uid. |
| **list**  list / elements=dictionary | List of rules from the same type to be deleted. <br>Use the “delete” API reference documentation for a single rule command to find the expected fields for the request.<br>For example, to delete access-rule, use the “delete-access-rule” command found in the API reference documentation (under Access Control & NAT). <br>Note, “ignore-errors”, “ignore-warnings” and “details-level” options are not supported when deleting a batch of objects. |
| **type**  string | Type of rules to be deleted. <br>Only types from above are supported. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_delete_rules_batch_module.md#id3)

```yaml+jinja
- name: delete-rules-batch
  cp_mgmt_delete_rules_batch:
    objects:
    - layer: Network
      list:
      - rule_number: 1
      - rule_number: 2
      type: access-rule
    - layer: Standard
      list:
      - rule_number: 1
      - rule_number: 2
      type: nat-rule
    - layer: Default Layer
      list:
      - rule_number: 1
      - rule_number: 2
      type: https-rule
```

## [Return Values](cp_mgmt_delete_rules_batch_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_delete_rules_batch**  dictionary | The checkpoint delete-rules-batch output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
