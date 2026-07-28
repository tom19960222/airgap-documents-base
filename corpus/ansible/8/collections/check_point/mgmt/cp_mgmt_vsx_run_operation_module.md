---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_vsx_run_operation module – Run the VSX operation by its name and parameters."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_vsx_run_operation_module.html
fetched_at: 2026-07-28T01:18:32+00:00
---
# check_point.mgmt.cp_mgmt_vsx_run_operation module – Run the VSX operation by its name and parameters.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_vsx_run_operation`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_vsx_run_operation_module.md#synopsis)
- [Parameters](cp_mgmt_vsx_run_operation_module.md#parameters)
- [Examples](cp_mgmt_vsx_run_operation_module.md#examples)
- [Return Values](cp_mgmt_vsx_run_operation_module.md#return-values)

## [Synopsis](cp_mgmt_vsx_run_operation_module.md#id1)

- Run the VSX operation by its name and parameters. <br><b>Important note:</b> An automatic session publish is part of all the operations in this API.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_vsx_run_operation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **add_member_params**  dictionary | Parameters for the operation to add a VSX Cluster member. |
| **ipv4_address**  string | The IPv4 address of the management interface of the VSX Cluster member. |
| **ipv4_sync_address**  string | The IPv4 address of the sync interface of the VSX Cluster member. |
| **member_name**  string | Name of the new VSX Cluster member object. |
| **vsx_name**  string | Name of the VSX Cluster object. |
| **vsx_uid**  string | UID of the VSX Cluster object. |
| **downgrade_params**  dictionary | Parameters for the operation to downgrade a VSX Gateway or VSX Cluster object to a lower version.<br>In case the current version is already the target version, or is lower than the target version, no change is done. |
| **target_version**  string | The target version. |
| **vsx_name**  string | Name of the VSX Gateway or VSX Cluster object. |
| **vsx_uid**  string | UID of the VSX Gateway or VSX Cluster object. |
| **operation**  string | The name of the operation to run. Each operation has its specific parameters.<br>The available operations are,<ul><li><i>upgrade</i> - Upgrades the VSX Gateway or VSX Cluster object to a higher version</li><li><i>downgrade</i> - Downgrades the VSX Gateway or VSX Cluster object to a lower version</li><li><i>add-member</i> - Adds a new VSX Cluster member object</li><li><i>remove-member</i> - Removes a VSX Cluster member object</li><li><i>reconf-gw</i> - Reconfigures a VSX Gateway after a clean install</li><li><i>reconf-member</i> - Reconfigures a VSX Cluster member after a clean install</li></ul>.  **Choices:**   - `"upgrade"` - `"downgrade"` - `"add-member"` - `"remove-member"` - `"reconf-gw"` - `"reconf-member"` |
| **reconf_gw_params**  dictionary | Parameters for the operation to reconfigure a VSX Gateway after a clean install. |
| **ipv4_corexl_number**  integer | Number of IPv4 CoreXL Firewall instances on the target VSX Gateway.<br>Valid values,<br><ul><li>To configure CoreXL Firewall instances, enter an integer greater or equal to 2.</li><li>To disable CoreXL, enter 1.</li></ul>. |
| **one_time_password**  string | A password required for establishing a Secure Internal Communication (SIC). Enter the same password you used during the First Time Configuration Wizard on the target VSX Gateway. |
| **vsx_name**  string | Name of the VSX Gateway object. |
| **vsx_uid**  string | UID of the VSX Gateway object. |
| **reconf_member_params**  dictionary | Parameters for the operation to reconfigure a VSX Cluster member after a clean install. |
| **ipv4_corexl_number**  integer | Number of IPv4 CoreXL Firewall instances on the target VSX Cluster member.<br>Valid values,<br><ul><li>To configure CoreXL Firewall instances, enter an integer greater or equal to 2.</li><li>To disable CoreXL, enter 1.</li></ul>Important - The CoreXL configuration must be the same on all the cluster members. |
| **member_name**  string | Name of the VSX Cluster member object. |
| **member_uid**  string | UID of the VSX Cluster member object. |
| **one_time_password**  string | A password required for establishing a Secure Internal Communication (SIC). Enter the same password you used during the First Time Configuration Wizard on the target VSX Cluster member. |
| **remove_member_params**  dictionary | Parameters for the operation to remove a VSX Cluster member object. |
| **member_name**  string | Name of the VSX Cluster member object. |
| **member_uid**  string | UID of the VSX Cluster member object. |
| **upgrade_params**  dictionary | Parameters for the operation to upgrade a VSX Gateway or VSX Cluster object to a higher version.<br>In case the current version is already the target version, or is higher than the target version, no change is done. |
| **target_version**  string | The target version. |
| **vsx_name**  string | Name of the VSX Gateway or VSX Cluster object. |
| **vsx_uid**  string | UID of the VSX Gateway or VSX Cluster object. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_vsx_run_operation_module.md#id3)

```yaml+jinja
- name: vsx-run-operation
  cp_mgmt_vsx_run_operation:
    add_member_params:
      ipv4_address: 25.25.25.223
      ipv4_sync_address: 20.20.20.223
      member_name: Mem3
      vsx_name: VSX_CLUSTER
    operation: add-member
```

## [Return Values](cp_mgmt_vsx_run_operation_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_vsx_run_operation**  dictionary | The checkpoint vsx-run-operation output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
