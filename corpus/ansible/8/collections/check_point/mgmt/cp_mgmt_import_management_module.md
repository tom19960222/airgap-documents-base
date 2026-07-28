---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_import_management module – Import the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_import_management_module.html
fetched_at: 2026-07-28T01:16:33+00:00
---
# check_point.mgmt.cp_mgmt_import_management module – Import the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_import_management`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_import_management_module.md#synopsis)
- [Parameters](cp_mgmt_import_management_module.md#parameters)
- [Examples](cp_mgmt_import_management_module.md#examples)
- [Return Values](cp_mgmt_import_management_module.md#return-values)

## [Synopsis](cp_mgmt_import_management_module.md#id1)

- Import the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration. <br/>After the import starts, the session expires and you must login again.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_import_management_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_ip_address**  string | IPv4 address for the imported Domain.<br><font color=”red”>Required only for</font> importing the Security Management Server into the Multi-Domain Server. |
| **domain_name**  string | Domain name to be imported. Must be unique in the Multi-Domain Server.<br><font color=”red”>Required only for</font> importing the Security Management Server into the Multi-Domain Server. |
| **domain_server_name**  string | Multi-Domain Server name for the imported Domain.<br><font color=”red”>Required only for</font> importing the Security Management Server into the Multi-Domain Server. |
| **file_path**  string / required | Path to the exported database file to be imported. |
| **ignore_warnings**  boolean | Ignoring the verification warnings. By Setting this parameter to ‘true’ import will not be blocked by warnings.  **Choices:**   - `false` - `true` |
| **include_endpoint_configuration**  boolean | Include import of the Endpoint Security Management configuration files.  **Choices:**   - `false` - `true` |
| **include_endpoint_database**  boolean | Include import of the Endpoint Security Management database.  **Choices:**   - `false` - `true` |
| **include_logs**  boolean | Import logs without log indexes.  **Choices:**   - `false` - `true` |
| **include_logs_indexes**  boolean | Import logs with log indexes.  **Choices:**   - `false` - `true` |
| **keep_cloud_sharing**  boolean | Preserve the connection of the Management Server to Check Point’s Infinity Portal.<br>Use this flag after ensuring that the original Management Server does not communicate with Infinity Portal.<br>Note, resuming the connection is also possible after import with set-cloud-services.  **Choices:**   - `false` - `true` |
| **pre_import_verification_only**  boolean | If true, only runs the pre-import verifications instead of the full import.  **Choices:**   - `false` - `true` |
| **verify_domain_restore**  boolean | If true, verify that the restore operation is valid for this input file and this environment. <br>Note, Restore operation will not be executed.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_import_management_module.md#id3)

```yaml+jinja
- name: import-management
  cp_mgmt_import_management:
    file_path: /var/log/domain1_exported.tgz
```

## [Return Values](cp_mgmt_import_management_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_import_management**  dictionary | The checkpoint import-management output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
