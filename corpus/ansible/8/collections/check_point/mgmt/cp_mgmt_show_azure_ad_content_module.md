---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_show_azure_ad_content module – Retrieve AzureAD Objects from Azure AD Server."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_show_azure_ad_content_module.html
fetched_at: 2026-07-28T01:17:38+00:00
---
# check_point.mgmt.cp_mgmt_show_azure_ad_content module – Retrieve AzureAD Objects from Azure AD Server.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_azure_ad_content`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_show_azure_ad_content_module.md#synopsis)
- [Parameters](cp_mgmt_show_azure_ad_content_module.md#parameters)
- [Examples](cp_mgmt_show_azure_ad_content_module.md#examples)
- [Return Values](cp_mgmt_show_azure_ad_content_module.md#return-values)

## [Synopsis](cp_mgmt_show_azure_ad_content_module.md#id1)

- Retrieve AzureAD Objects from Azure AD Server.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_azure_ad_content_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **azure_ad_name**  string | Name of the Azure AD Server where to search for objects. |
| **azure_ad_uid**  string | Unique identifier of the Azure AD Server where to search for objects. |
| **details_level**  string | Standard and Full description are the same.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **filter**  dictionary | Return results matching the specified filter. |
| **parent_uid_in_data_center**  string | Return results under the specified Data Center Object (identified by UID). |
| **text**  string | Return results containing the specified text value. |
| **uri**  string | Return results under the specified Data Center Object (identified by URI). |
| **limit**  integer | The maximal number of returned results. |
| **offset**  integer | Number of the results to initially skip. |
| **order**  list / elements=dictionary | Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **uid_in_azure_ad**  string | Return result matching the unique identifier of the object on the Azure AD Server. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_show_azure_ad_content_module.md#id3)

```yaml+jinja
- name: show-azure-ad-content
  cp_mgmt_show_azure_ad_content:
    name: my_azureAD
```

## [Return Values](cp_mgmt_show_azure_ad_content_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_azure_ad_content**  dictionary | The checkpoint show-azure-ad-content output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
