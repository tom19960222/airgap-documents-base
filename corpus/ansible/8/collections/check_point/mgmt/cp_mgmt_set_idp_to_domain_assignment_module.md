---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_idp_to_domain_assignment module – Set Identity Provider assignment to domain, to allow administrator login to that domain using that identity provider, if there is no Identity Provider assigned to the domain the ‘idp-default-assignment’ will be used. This command only available  for Multi-Domain server."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_idp_to_domain_assignment_module.html
fetched_at: 2026-07-28T01:17:30+00:00
---
# check_point.mgmt.cp_mgmt_set_idp_to_domain_assignment module – Set Identity Provider assignment to domain, to allow administrator login to that domain using that identity provider, if there is no Identity Provider assigned to the domain the ‘idp-default-assignment’ will be used. This command only available for Multi-Domain server.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_idp_to_domain_assignment`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_set_idp_to_domain_assignment_module.md#synopsis)
- [Parameters](cp_mgmt_set_idp_to_domain_assignment_module.md#parameters)
- [Examples](cp_mgmt_set_idp_to_domain_assignment_module.md#examples)
- [Return Values](cp_mgmt_set_idp_to_domain_assignment_module.md#return-values)

## [Synopsis](cp_mgmt_set_idp_to_domain_assignment_module.md#id1)

- Set Identity Provider assignment to domain, to allow administrator login to that domain using that identity provider, if there is no Identity Provider assigned to the domain the ‘idp-default-assignment’ will be used. This command only available for Multi-Domain server.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_idp_to_domain_assignment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assigned_domain**  string | Represents the Domain assigned by ‘idp-to-domain-assignment’, need to be domain name or UID. |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **identity_provider**  string | Represents the Identity Provider to be used for Login by this assignment. Must be set when “using-default” was set to be false. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **using_default**  boolean | Is this assignment override by ‘idp-default-assignment’.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_idp_to_domain_assignment_module.md#id3)

```yaml+jinja
- name: set-idp-to-domain-assignment
  cp_mgmt_set_idp_to_domain_assignment:
    assigned_domain: BSMS
    identity_provider: okta
```

## [Return Values](cp_mgmt_set_idp_to_domain_assignment_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_idp_to_domain_assignment**  dictionary | The checkpoint set-idp-to-domain-assignment output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
