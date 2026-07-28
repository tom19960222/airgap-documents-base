---
collection: ansible
version: "8"
title: "chocolatey.chocolatey.win_chocolatey_config module – Manages Chocolatey config settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/chocolatey/chocolatey/win_chocolatey_config_module.html
fetched_at: 2026-07-28T01:18:36+00:00
---
# chocolatey.chocolatey.win_chocolatey_config module – Manages Chocolatey config settings

> **Note:**
>
> This module is part of the [chocolatey.chocolatey collection](https://galaxy.ansible.com/ui/repo/published/chocolatey/chocolatey/) (version 1.5.1).
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
| **state**  string | When `absent`, it will ensure the setting is unset or blank.  When `present`, it will ensure the setting is set to the value of *value*.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **value**  string | Used when `state=present` that contains the value to set for the config setting.  Cannot be null or an empty string, use `state=absent` to unset a config value instead. |

## [See Also](win_chocolatey_config_module.md#id3)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [chocolatey.chocolatey.win_chocolatey_facts](win_chocolatey_facts_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-facts-module)
> :   Create a facts collection for Chocolatey.
>
> [chocolatey.chocolatey.win_chocolatey_feature](win_chocolatey_feature_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-feature-module)
> :   Manages Chocolatey features.
>
> [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module)
> :   Manages Chocolatey sources.

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
- Rain Sallow (@vexx32)
- Josh King (@windos)

### Collection links

- [Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
- [Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
