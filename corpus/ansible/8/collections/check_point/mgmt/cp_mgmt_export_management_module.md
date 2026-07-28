---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_export_management module – Export the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_export_management_module.html
fetched_at: 2026-07-28T01:16:14+00:00
---
# check_point.mgmt.cp_mgmt_export_management module – Export the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_export_management`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_export_management_module.md#synopsis)
- [Parameters](cp_mgmt_export_management_module.md#parameters)
- [Examples](cp_mgmt_export_management_module.md#examples)
- [Return Values](cp_mgmt_export_management_module.md#return-values)

## [Synopsis](cp_mgmt_export_management_module.md#id1)

- Export the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_export_management_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_name**  string | Domain name to be exported.<br><font color=”red”>Required only for</font> exporting a Domain from the Multi-Domain Server or backing up Domain. |
| **file_path**  string | Path in which the exported database file is saved.<br><font color=”red”>Required only</font> when not using pre-export-verification-only flag. |
| **ignore_warnings**  boolean | Ignoring the verification warnings. By Setting this parameter to ‘true’ export will not be blocked by warnings.  **Choices:**   - `false` - `true` |
| **include_endpoint_configuration**  boolean | Include export of the Endpoint Security Management configuration files.  **Choices:**   - `false` - `true` |
| **include_endpoint_database**  boolean | Include export of the Endpoint Security Management database.  **Choices:**   - `false` - `true` |
| **include_logs**  boolean | Export logs without log indexes.  **Choices:**   - `false` - `true` |
| **include_logs_indexes**  boolean | Export logs with log indexes.  **Choices:**   - `false` - `true` |
| **is_domain_backup**  boolean | If true, the exported Domain will be suitable for import on the same Multi-Domain Server only.  **Choices:**   - `false` - `true` |
| **is_smc_to_mds**  boolean | If true, the exported Security Management Server will be suitable for import on the Multi-Domain Server only.  **Choices:**   - `false` - `true` |
| **pre_export_verification_only**  boolean | If true, only runs the pre-export verifications instead of the full export.  **Choices:**   - `false` - `true` |
| **target_version**  string | Target version. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_export_management_module.md#id3)

```yaml+jinja
- name: export-management
  cp_mgmt_export_management:
    domain_name: domain1
    file_path: /var/log/domain1_backup.tgz
    is_domain_backup: true
```

## [Return Values](cp_mgmt_export_management_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_export_management**  dictionary | The checkpoint export-management output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
