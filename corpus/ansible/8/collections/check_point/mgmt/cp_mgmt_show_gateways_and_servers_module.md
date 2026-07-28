---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_show_gateways_and_servers module – Shows list of Gateways & Servers sorted by name."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_show_gateways_and_servers_module.html
fetched_at: 2026-07-28T01:17:40+00:00
---
# check_point.mgmt.cp_mgmt_show_gateways_and_servers module – Shows list of Gateways & Servers sorted by name.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_gateways_and_servers`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_show_gateways_and_servers_module.md#synopsis)
- [Parameters](cp_mgmt_show_gateways_and_servers_module.md#parameters)
- [Examples](cp_mgmt_show_gateways_and_servers_module.md#examples)
- [Return Values](cp_mgmt_show_gateways_and_servers_module.md#return-values)

## [Synopsis](cp_mgmt_show_gateways_and_servers_module.md#id1)

- Shows list of Gateways & Servers sorted by name.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_gateways_and_servers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **limit**  integer | The maximal number of returned results. This parameter is relevant only for getting few objects. |
| **offset**  integer | Number of the results to initially skip. This parameter is relevant only for getting few objects. |
| **order**  list / elements=dictionary | Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order. This parameter is relevant only for getting few objects. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_show_gateways_and_servers_module.md#id3)

```yaml+jinja
- name: show-gateways-and-servers
  cp_mgmt_show_gateways_and_servers:
    details_level: full
```

## [Return Values](cp_mgmt_show_gateways_and_servers_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_gateways_and_servers**  dictionary | The checkpoint show-gateways-and-servers output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
