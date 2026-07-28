---
collection: ansible
version: "6"
title: "ansible.windows.win_path module – Manage Windows path environment variables"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_path_module.html
fetched_at: 2026-07-27T16:44:59+00:00
---
# ansible.windows.win_path module – Manage Windows path environment variables

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_path`.

- [Synopsis](win_path_module.md#synopsis)
- [Parameters](win_path_module.md#parameters)
- [Notes](win_path_module.md#notes)
- [See Also](win_path_module.md#see-also)
- [Examples](win_path_module.md#examples)

## [Synopsis](win_path_module.md#id1)

- Allows element-based ordering, addition, and removal of Windows path environment variables.

## [Parameters](win_path_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **elements**  list / elements=string / required | A single path element, or a list of path elements (ie, directories) to add or remove.  When multiple elements are included in the list (and `state` is `present`), the elements are guaranteed to appear in the same relative order in the resultant path value.  Variable expansions (eg, `%VARNAME%`) are allowed, and are stored unexpanded in the target path element.  Any existing path elements not mentioned in `elements` are always preserved in their current order.  New path elements are appended to the path, and existing path elements may be moved closer to the end to satisfy the requested ordering.  Paths are compared in a case-insensitive fashion, and trailing backslashes are ignored for comparison purposes. However, note that trailing backslashes in YAML require quotes. |
| **name**  string | Target path environment variable name.  Default: `"PATH"` |
| **scope**  string | The level at which the environment variable specified by `name` should be managed (either for the current user or global machine scope).  Choices:   - `"machine"` ← (default) - `"user"` |
| **state**  string | Whether the path elements specified in `elements` should be present or absent.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](win_path_module.md#id3)

> **Note:**
>
> - This module is for modifying individual elements of path-like environment variables. For general-purpose management of other environment vars, use the [ansible.windows.win_environment](win_environment_module.md#ansible-collections-ansible-windows-win-environment-module) module.
> - This module does not broadcast change events. This means that the minority of windows applications which can have their environment changed without restarting will not be notified and therefore will need restarting to pick up new environment settings.
> - User level environment variables will require an interactive user to log out and in again before they become available.

## [See Also](win_path_module.md#id4)

> **See also:**
>
> [ansible.windows.win_environment](win_environment_module.md#ansible-collections-ansible-windows-win-environment-module)
> :   Modify environment variables on windows hosts.

## [Examples](win_path_module.md#id5)

```yaml+jinja
- name: Ensure that system32 and Powershell are present on the global system path, and in the specified order
  ansible.windows.win_path:
    elements:
    - '%SystemRoot%\system32'
    - '%SystemRoot%\system32\WindowsPowerShell\v1.0'

- name: Ensure that C:\Program Files\MyJavaThing is not on the current user's CLASSPATH
  ansible.windows.win_path:
    name: CLASSPATH
    elements: C:\Program Files\MyJavaThing
    scope: user
    state: absent
```

### Authors

- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
