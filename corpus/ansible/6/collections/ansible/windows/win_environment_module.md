---
collection: ansible
version: "6"
title: "ansible.windows.win_environment module – Modify environment variables on windows hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_environment_module.html
fetched_at: 2026-07-27T16:44:55+00:00
---
# ansible.windows.win_environment module – Modify environment variables on windows hosts

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
> To use it in a playbook, specify: `ansible.windows.win_environment`.

- [Synopsis](win_environment_module.md#synopsis)
- [Parameters](win_environment_module.md#parameters)
- [Notes](win_environment_module.md#notes)
- [See Also](win_environment_module.md#see-also)
- [Examples](win_environment_module.md#examples)
- [Return Values](win_environment_module.md#return-values)

## [Synopsis](win_environment_module.md#id1)

- Uses .net Environment to set or remove environment variables and can set at User, Machine or Process level.
- User level environment variables will be set, but not available until the user has logged off and on again.

## [Parameters](win_environment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **level**  string / required | The level at which to set the environment variable.  Use `machine` to set for all users.  Use `user` to set for the current user that ansible is connected as.  Use `process` to set for the current process. Probably not that useful.  Choices:   - `"machine"` - `"process"` - `"user"` |
| **name**  string | The name of the environment variable. Required when *state=absent*. |
| **state**  string | Set to `present` to ensure environment variable is set.  Set to `absent` to ensure it is removed.  When using *variables*, do not set this option.  Choices:   - `"absent"` - `"present"` |
| **value**  string | The value to store in the environment variable.  Must be set when *state=present* and cannot be an empty string.  Should be omitted for *state=absent* and *variables*. |
| **variables**  dictionary  added in ansible.windows 1.3.0 | A dictionary where multiple environment variables can be defined at once.  Not valid when *state* is set. Variables with a value will be set (`present`) and variables with an empty value will be unset (`absent`).  *level* applies to all vars defined this way. |

## [Notes](win_environment_module.md#id3)

> **Note:**
>
> - This module is best-suited for setting the entire value of an environment variable. For safe element-based management of path-like environment vars, use the [ansible.windows.win_path](win_path_module.md#ansible-collections-ansible-windows-win-path-module) module.
> - This module does not broadcast change events. This means that the minority of windows applications which can have their environment changed without restarting will not be notified and therefore will need restarting to pick up new environment settings. User level environment variables will require the user to log out and in again before they become available.
> - In the return, `before_value` and `value` will be set to the last values when using *variables*. It’s best to use `values` in that case if you need to find a specific variable’s before and after values.

## [See Also](win_environment_module.md#id4)

> **See also:**
>
> [ansible.windows.win_path](win_path_module.md#ansible-collections-ansible-windows-win-path-module)
> :   Manage Windows path environment variables.

## [Examples](win_environment_module.md#id5)

```yaml+jinja
- name: Set an environment variable for all users
  ansible.windows.win_environment:
    state: present
    name: TestVariable
    value: Test value
    level: machine

- name: Remove an environment variable for the current user
  ansible.windows.win_environment:
    state: absent
    name: TestVariable
    level: user

- name: Set several variables at once
  ansible.windows.win_environment:
    level: machine
    variables:
      TestVariable: Test value
      CUSTOM_APP_VAR: 'Very important value'
      ANOTHER_VAR: '{{ my_ansible_var }}'

- name: Set and remove multiple variables at once
  ansible.windows.win_environment:
    level: user
    variables:
      TestVariable: Test value
      CUSTOM_APP_VAR: 'Very important value'
      ANOTHER_VAR: '{{ my_ansible_var }}'
      UNWANTED_VAR: ''  # < this will be removed
```

## [Return Values](win_environment_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **before_value**  string | the value of the environment key before a change, this is null if it didn’t exist  Returned: always  Sample: `"C:\\Windows\\System32"` |
| **value**  string | the value the environment key has been set to, this is null if removed  Returned: always  Sample: `"C:\\Program Files\\jdk1.8"` |
| **values**  dictionary  added in ansible.windows 1.3.0 | dictionary of before and after values; each key is a variable name, each value is another dict with `before`, `after`, and `changed` keys  Returned: always |

### Authors

- Jon Hawkesworth (@jhawkesworth)
- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
