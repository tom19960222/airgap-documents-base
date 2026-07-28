---
collection: ansible
version: "8"
title: "community.general.pamd module – Manage PAM Modules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pamd_module.html
fetched_at: 2026-07-28T01:48:57+00:00
---
# community.general.pamd module – Manage PAM Modules

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.pamd`.

- [Synopsis](pamd_module.md#synopsis)
- [Parameters](pamd_module.md#parameters)
- [Attributes](pamd_module.md#attributes)
- [Notes](pamd_module.md#notes)
- [Examples](pamd_module.md#examples)
- [Return Values](pamd_module.md#return-values)

## [Synopsis](pamd_module.md#id1)

- Edit PAM service’s type, control, module path and module arguments.
- In order for a PAM rule to be modified, the type, control and module_path must match an existing rule. See man(5) pam.d for details.

Aliases: system.pamd

## [Parameters](pamd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **control**  string / required | The control of the PAM rule being modified.  This may be a complicated control with brackets. If this is the case, be sure to put “[bracketed controls]” in quotes.  The `type`, `control`, and `module_path` options all must match a rule to be modified. |
| **module_arguments**  list / elements=string | When `state=updated`, the `module_arguments` will replace existing module_arguments.  When `state=args_absent` args matching those listed in `module_arguments` will be removed.  When `state=args_present` any args listed in `module_arguments` are added if missing from the existing rule.  Furthermore, if the module argument takes a value denoted by `=`, the value will be changed to that specified in module_arguments. |
| **module_path**  string / required | The module path of the PAM rule being modified.  The `type`, `control`, and `module_path` options all must match a rule to be modified. |
| **name**  string / required | The name generally refers to the PAM service file to change, for example system-auth. |
| **new_control**  string | The new control to assign to the new rule. |
| **new_module_path**  string | The new module path to be assigned to the new rule. |
| **new_type**  string | The new type to assign to the new rule.  **Choices:**   - `"account"` - `"-account"` - `"auth"` - `"-auth"` - `"password"` - `"-password"` - `"session"` - `"-session"` |
| **path**  path | This is the path to the PAM service files.  **Default:** `"/etc/pam.d"` |
| **state**  string | The default of `updated` will modify an existing rule if type, control and module_path all match an existing rule.  With `before`, the new rule will be inserted before a rule matching type, control and module_path.  Similarly, with `after`, the new rule will be inserted after an existing rulematching type, control and module_path.  With either `before` or `after` `new_type`, `new_control`, and `new_module_path` must all be specified.  If state is `args_absent` or `args_present`, `new_type`, `new_control`, and `new_module_path` will be ignored.  State `absent` will remove the rule. The `absent` state was added in Ansible 2.4.  **Choices:**   - `"absent"` - `"before"` - `"after"` - `"args_absent"` - `"args_present"` - `"updated"` ← (default) |
| **type**  string / required | The type of the PAM rule being modified.  The `type`, `control`, and `module_path` options all must match a rule to be modified.  **Choices:**   - `"account"` - `"-account"` - `"auth"` - `"-auth"` - `"password"` - `"-password"` - `"session"` - `"-session"` |

## [Attributes](pamd_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pamd_module.md#id4)

> **Note:**
>
> - This module does not handle authselect profiles.

## [Examples](pamd_module.md#id5)

```yaml+jinja
- name: Update pamd rule's control in /etc/pam.d/system-auth
  community.general.pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    new_control: sufficient

- name: Update pamd rule's complex control in /etc/pam.d/system-auth
  community.general.pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    new_control: '[success=2 default=ignore]'

- name: Insert a new rule before an existing rule
  community.general.pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    new_type: auth
    new_control: sufficient
    new_module_path: pam_faillock.so
    state: before

- name: Insert a new rule pam_wheel.so with argument 'use_uid' after an \
        existing rule pam_rootok.so
  community.general.pamd:
    name: su
    type: auth
    control: sufficient
    module_path: pam_rootok.so
    new_type: auth
    new_control: required
    new_module_path: pam_wheel.so
    module_arguments: 'use_uid'
    state: after

- name: Remove module arguments from an existing rule
  community.general.pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    module_arguments: ''
    state: updated

- name: Replace all module arguments in an existing rule
  community.general.pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    module_arguments: 'preauth
        silent
        deny=3
        unlock_time=604800
        fail_interval=900'
    state: updated

- name: Remove specific arguments from a rule
  community.general.pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    module_arguments: crond,quiet
    state: args_absent

- name: Ensure specific arguments are present in a rule
  community.general.pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    module_arguments: crond,quiet
    state: args_present

- name: Ensure specific arguments are present in a rule (alternative)
  community.general.pamd:
    name: system-auth
    type: session
    control: '[success=1 default=ignore]'
    module_path: pam_succeed_if.so
    module_arguments:
    - crond
    - quiet
    state: args_present

- name: Module arguments requiring commas must be listed as a Yaml list
  community.general.pamd:
    name: special-module
    type: account
    control: required
    module_path: pam_access.so
    module_arguments:
    - listsep=,
    state: args_present

- name: Update specific argument value in a rule
  community.general.pamd:
    name: system-auth
    type: auth
    control: required
    module_path: pam_faillock.so
    module_arguments: 'fail_interval=300'
    state: args_present

- name: Add pam common-auth rule for duo
  community.general.pamd:
    name: common-auth
    new_type: auth
    new_control: '[success=1 default=ignore]'
    new_module_path: '/lib64/security/pam_duo.so'
    state: after
    type: auth
    module_path: pam_sss.so
    control: 'requisite'
```

## [Return Values](pamd_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backupdest**  string | The file name of the backup file, if created.  **Returned:** success |
| **change_count**  integer | How many rules were changed.  **Returned:** success  **Sample:** `1` |

### Authors

- Kenneth D. Evensen (@kevensen)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
