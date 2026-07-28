---
collection: ansible
version: "6"
title: "community.windows.win_audit_rule module – Adds an audit rule to files, folders, or registry keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_audit_rule_module.html
fetched_at: 2026-07-27T17:23:09+00:00
---
# community.windows.win_audit_rule module – Adds an audit rule to files, folders, or registry keys

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
> To use it in a playbook, specify: `community.windows.win_audit_rule`.

- [Synopsis](win_audit_rule_module.md#synopsis)
- [Parameters](win_audit_rule_module.md#parameters)
- [See Also](win_audit_rule_module.md#see-also)
- [Examples](win_audit_rule_module.md#examples)
- [Return Values](win_audit_rule_module.md#return-values)

## [Synopsis](win_audit_rule_module.md#id1)

- Used to apply audit rules to files, folders or registry keys.
- Once applied, it will begin recording the user who performed the operation defined into the Security Log in the Event viewer.
- The behavior is designed to ignore inherited rules since those cannot be adjusted without first disabling the inheritance behavior. It will still print inherited rules in the output though for debugging purposes.

## [Parameters](win_audit_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **audit_flags**  list / elements=string / required | Defines whether to log on failure, success, or both.  To log both define as comma separated list “Success, Failure”.  Choices:   - `"Failure"` - `"Success"` |
| **inheritance_flags**  list / elements=string | Defines what objects inside of a folder or registry key will inherit the settings.  If you are setting a rule on a file, this value has to be changed to `none`.  For more information on the choices see MSDN PropagationFlags enumeration at <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.inheritanceflags.aspx>.  Choices:   - `"ContainerInherit"` ← (default) - `"ObjectInherit"` ← (default)   Default: `["ContainerInherit", "ObjectInherit"]` |
| **path**  aliases: dest, destination  path / required | Path to the file, folder, or registry key.  Registry paths should be in Powershell format, beginning with an abbreviation for the root such as, `HKLM:\Software`. |
| **propagation_flags**  string | Propagation flag on the audit rules.  This value is ignored when the path type is a file.  For more information on the choices see MSDN PropagationFlags enumeration at <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.propagationflags.aspx>.  Choices:   - `"None"` ← (default) - `"InherityOnly"` - `"NoPropagateInherit"` |
| **rights**  list / elements=string / required | Comma separated list of the rights desired. Only required for adding a rule.  If *path* is a file or directory, rights can be any right under MSDN FileSystemRights <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.filesystemrights.aspx>.  If *path* is a registry key, rights can be any right under MSDN RegistryRights <https://msdn.microsoft.com/en-us/library/system.security.accesscontrol.registryrights.aspx>. |
| **state**  string | Whether the rule should be `present` or `absent`.  For absent, only *path*, *user*, and *state* are required.  Specifying `absent` will remove all rules matching the defined *user*.  Choices:   - `"absent"` - `"present"` ← (default) |
| **user**  string / required | The user or group to adjust rules for. |

## [See Also](win_audit_rule_module.md#id3)

> **See also:**
>
> [community.windows.win_audit_policy_system](win_audit_policy_system_module.md#ansible-collections-community-windows-win-audit-policy-system-module)
> :   Used to make changes to the system wide Audit Policy.

## [Examples](win_audit_rule_module.md#id4)

```yaml+jinja
- name: Add filesystem audit rule for a folder
  community.windows.win_audit_rule:
    path: C:\inetpub\wwwroot\website
    user: BUILTIN\Users
    rights: write,delete,changepermissions
    audit_flags: success,failure
    inheritance_flags: ContainerInherit,ObjectInherit

- name: Add filesystem audit rule for a file
  community.windows.win_audit_rule:
    path: C:\inetpub\wwwroot\website\web.config
    user: BUILTIN\Users
    rights: write,delete,changepermissions
    audit_flags: success,failure
    inheritance_flags: None

- name: Add registry audit rule
  community.windows.win_audit_rule:
    path: HKLM:\software
    user: BUILTIN\Users
    rights: delete
    audit_flags: 'success'

- name: Remove filesystem audit rule
  community.windows.win_audit_rule:
    path: C:\inetpub\wwwroot\website
    user: BUILTIN\Users
    state: absent

- name: Remove registry audit rule
  community.windows.win_audit_rule:
    path: HKLM:\software
    user: BUILTIN\Users
    state: absent
```

## [Return Values](win_audit_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **current_audit_rules**  dictionary | The current rules on the defined *path*  Will return “No audit rules defined on *path*“  Returned: always  Sample: `{"audit_flags": "Success", "inheritance_flags": "False", "is_inherited": "False", "propagation_flags": "None", "rights": "Delete", "user": "Everyone"}` |
| **path_type**  string | The type of *path* being targetted.  Will be one of file, directory, registry.  Returned: always |

### Authors

- Noah Sparks (@nwsparks)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
