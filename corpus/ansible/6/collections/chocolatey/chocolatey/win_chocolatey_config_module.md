---
collection: ansible
version: "6"
title: "chocolatey.chocolatey.win_chocolatey_config module – Manages Chocolatey config settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/chocolatey/chocolatey/win_chocolatey_config_module.html
fetched_at: 2026-07-27T16:48:59+00:00
---
# chocolatey.chocolatey.win_chocolatey_config module – Manages Chocolatey config settings

> **Note:**
>
> This module is part of the [chocolatey.chocolatey collection](https://galaxy.ansible.com/chocolatey/chocolatey) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install chocolatey.chocolatey`.
>
> To use it in a playbook, specify: `chocolatey.chocolatey.win_chocolatey_config`.

New in chocolatey.chocolatey 0.2.7

- [Synopsis](win_chocolatey_config_module.md#synopsis)
- [Parameters](win_chocolatey_config_module.md#parameters)
- [See Also](win_chocolatey_config_module.md#see-also)
- [Examples](win_chocolatey_config_module.md#examples)

## [Synopsis](win_chocolatey_config_module.md#id1)

- Used to manage Chocolatey config settings as well as unset the values.

## [Parameters](win_chocolatey_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | The name of the config setting to manage.  See <https://chocolatey.org/docs/chocolatey-configuration> for a list of valid configuration settings that can be changed.  Any config values that contain encrypted values like a password are not idempotent as the plaintext value cannot be read. |
| **state**  string | When `absent`, it will ensure the setting is unset or blank.  When `present`, it will ensure the setting is set to the value of *value*.  Choices:   - `"absent"` - `"present"` ← (default) |
| **value**  string | Used when `state=present` that contains the value to set for the config setting.  Cannot be null or an empty string, use `state=absent` to unset a config value instead. |

## [See Also](win_chocolatey_config_module.md#id3)

> **See also:**
>
> win_chocolatey
> :   The official documentation on the **win_chocolatey** module.
>
> win_chocolatey_facts
> :   The official documentation on the **win_chocolatey_facts** module.
>
> win_chocolatey_feature
> :   The official documentation on the **win_chocolatey_feature** module.
>
> win_chocolatey_source
> :   The official documentation on the **win_chocolatey_source** module.

## [Examples](win_chocolatey_config_module.md#id4)

```yaml+jinja
- name: Set the cache location
  win_chocolatey_config:
    name: cacheLocation
    state: present
    value: D:\chocolatey_temp

- name: Unset the cache location
  win_chocolatey_config:
    name: cacheLocation
    state: absent
```

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
[Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
