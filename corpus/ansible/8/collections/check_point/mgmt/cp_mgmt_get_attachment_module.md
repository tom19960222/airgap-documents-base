---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_get_attachment module – Retrieves a packet capture or blob data, according to the attributes of a log record."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_get_attachment_module.html
fetched_at: 2026-07-28T01:16:15+00:00
---
# check_point.mgmt.cp_mgmt_get_attachment module – Retrieves a packet capture or blob data, according to the attributes of a log record.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_get_attachment`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_get_attachment_module.md#synopsis)
- [Parameters](cp_mgmt_get_attachment_module.md#parameters)
- [Examples](cp_mgmt_get_attachment_module.md#examples)
- [Return Values](cp_mgmt_get_attachment_module.md#return-values)

## [Synopsis](cp_mgmt_get_attachment_module.md#id1)

- Retrieves a packet capture or blob data, according to the attributes of a log record.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_get_attachment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attachment_id**  string | Attachment identifier from a log record. |
| **id**  string | Log id from a log record. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_get_attachment_module.md#id3)

```yaml+jinja
- name: get-attachment
  cp_mgmt_get_attachment:
    attachment_id: MjY5HlNtYXJ0RGVmZW5zZR5jbj1jcF9tZ210LG89aHVnbzEtYmxvYkFwaS1uZXctdGFrZS0yLmNoZWNrcG9pbnQuY29tLnM2MjdvMx57MHg1OTg4
```

## [Return Values](cp_mgmt_get_attachment_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_get_attachment**  dictionary | The checkpoint get-attachment output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
