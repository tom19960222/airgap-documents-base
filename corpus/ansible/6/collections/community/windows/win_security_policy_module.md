---
collection: ansible
version: "6"
title: "community.windows.win_security_policy module – Change local security policy settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_security_policy_module.html
fetched_at: 2026-07-27T17:23:58+00:00
---
# community.windows.win_security_policy module – Change local security policy settings

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
> To use it in a playbook, specify: `community.windows.win_security_policy`.

- [Synopsis](win_security_policy_module.md#synopsis)
- [Parameters](win_security_policy_module.md#parameters)
- [Notes](win_security_policy_module.md#notes)
- [See Also](win_security_policy_module.md#see-also)
- [Examples](win_security_policy_module.md#examples)
- [Return Values](win_security_policy_module.md#return-values)

## [Synopsis](win_security_policy_module.md#id1)

- Allows you to set the local security policies that are configured by SecEdit.exe.

## [Parameters](win_security_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **key**  string / required | The ini key of the section or policy name to modify.  The module will return an error if this key is invalid. |
| **section**  string / required | The ini section the key exists in.  If the section does not exist then the module will return an error.  Example sections to use are ‘Account Policies’, ‘Local Policies’, ‘Event Log’, ‘Restricted Groups’, ‘System Services’, ‘Registry’ and ‘File System’  If wanting to edit the `Privilege Rights` section, use the [ansible.windows.win_user_right](../../ansible/windows/win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module) module instead. |
| **value**  string / required | The value for the ini key or policy name.  If the key takes in a boolean value then 0 = False and 1 = True. |

## [Notes](win_security_policy_module.md#id3)

> **Note:**
>
> - This module uses the SecEdit.exe tool to configure the values, more details of the areas and keys that can be configured can be found here <https://msdn.microsoft.com/en-us/library/bb742512.aspx>.
> - If you are in a domain environment these policies may be set by a GPO policy, this module can temporarily change these values but the GPO will override it if the value differs.
> - You can also run `SecEdit.exe /export /cfg C:\temp\output.ini` to view the current policies set on your system.
> - When assigning user rights, use the [ansible.windows.win_user_right](../../ansible/windows/win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module) module instead.

## [See Also](win_security_policy_module.md#id4)

> **See also:**
>
> [ansible.windows.win_user_right](../../ansible/windows/win_user_right_module.md#ansible-collections-ansible-windows-win-user-right-module)
> :   Manage Windows User Rights.

## [Examples](win_security_policy_module.md#id5)

```yaml+jinja
- name: Change the guest account name
  community.windows.win_security_policy:
    section: System Access
    key: NewGuestName
    value: Guest Account

- name: Set the maximum password age
  community.windows.win_security_policy:
    section: System Access
    key: MaximumPasswordAge
    value: 15

- name: Do not store passwords using reversible encryption
  community.windows.win_security_policy:
    section: System Access
    key: ClearTextPassword
    value: 0

- name: Enable system events
  community.windows.win_security_policy:
    section: Event Audit
    key: AuditSystemEvents
    value: 1
```

## [Return Values](win_security_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **import_log**  string | The log of the SecEdit.exe /configure job that configured the local policies. This is used for debugging purposes on failures.  Returned: secedit.exe /import run and change occurred  Sample: `"Completed 6 percent (0/15) \\tProcess Privilege Rights area."` |
| **key**  string | The key in the section passed to the module to modify.  Returned: success  Sample: `"NewGuestName"` |
| **rc**  integer | The return code after a failure when running SecEdit.exe.  Returned: failure with secedit calls  Sample: `-1` |
| **section**  string | The section passed to the module to modify.  Returned: success  Sample: `"System Access"` |
| **stderr**  string | The output of the STDERR buffer after a failure when running SecEdit.exe.  Returned: failure with secedit calls  Sample: `"failed to import security policy"` |
| **stdout**  string | The output of the STDOUT buffer after a failure when running SecEdit.exe.  Returned: failure with secedit calls  Sample: `"check log for error details"` |
| **value**  string | The value passed to the module to modify to.  Returned: success  Sample: `"Guest Account"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
