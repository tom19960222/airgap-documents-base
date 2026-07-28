---
collection: ansible
version: "6"
title: "community.windows.win_audit_policy_system module – Used to make changes to the system wide Audit Policy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_audit_policy_system_module.html
fetched_at: 2026-07-27T17:23:09+00:00
---
# community.windows.win_audit_policy_system module – Used to make changes to the system wide Audit Policy

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_audit_policy_system`.

- [Synopsis](win_audit_policy_system_module.md#synopsis)
- [Parameters](win_audit_policy_system_module.md#parameters)
- [Notes](win_audit_policy_system_module.md#notes)
- [See Also](win_audit_policy_system_module.md#see-also)
- [Examples](win_audit_policy_system_module.md#examples)
- [Return Values](win_audit_policy_system_module.md#return-values)

## [Synopsis](win_audit_policy_system_module.md#id1)

- Used to make changes to the system wide Audit Policy.

## [Parameters](win_audit_policy_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **audit_type**  list / elements=string / required | The type of event you would like to audit for.  Accepts a list. See examples.  Choices:   - `"failure"` - `"none"` - `"success"` |
| **category**  string | Single string value for the category you would like to adjust the policy on.  Cannot be used with *subcategory*. You must define one or the other.  Changing this setting causes all subcategories to be adjusted to the defined *audit_type*. |
| **subcategory**  string | Single string value for the subcategory you would like to adjust the policy on.  Cannot be used with *category*. You must define one or the other. |

## [Notes](win_audit_policy_system_module.md#id3)

> **Note:**
>
> - It is recommended to take a backup of the policies before adjusting them for the first time.
> - See this page for in depth information <https://technet.microsoft.com/en-us/library/cc766468.aspx>.

## [See Also](win_audit_policy_system_module.md#id4)

> **See also:**
>
> [community.windows.win_audit_rule](win_audit_rule_module.md#ansible-collections-community-windows-win-audit-rule-module)
> :   Adds an audit rule to files, folders, or registry keys.

## [Examples](win_audit_policy_system_module.md#id5)

```yaml+jinja
- name: Enable failure auditing for the subcategory "File System"
  community.windows.win_audit_policy_system:
    subcategory: File System
    audit_type: failure

- name: Enable all auditing types for the category "Account logon events"
  community.windows.win_audit_policy_system:
    category: Account logon events
    audit_type: success, failure

- name: Disable auditing for the subcategory "File System"
  community.windows.win_audit_policy_system:
    subcategory: File System
    audit_type: none
```

## [Return Values](win_audit_policy_system_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **current_audit_policy**  dictionary | details on the policy being targetted  Returned: always  Sample: `{"File Share": "failure"}` |

### Authors

- Noah Sparks (@nwsparks)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
