---
collection: ansible
version: "6"
title: "ansible.windows.win_reg_stat module – Get information about Windows registry keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_reg_stat_module.html
fetched_at: 2026-07-27T16:45:01+00:00
---
# ansible.windows.win_reg_stat module – Get information about Windows registry keys

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
> To use it in a playbook, specify: `ansible.windows.win_reg_stat`.

- [Synopsis](win_reg_stat_module.md#synopsis)
- [Parameters](win_reg_stat_module.md#parameters)
- [Notes](win_reg_stat_module.md#notes)
- [See Also](win_reg_stat_module.md#see-also)
- [Examples](win_reg_stat_module.md#examples)
- [Return Values](win_reg_stat_module.md#return-values)

## [Synopsis](win_reg_stat_module.md#id1)

- Like [ansible.windows.win_file](win_file_module.md#ansible-collections-ansible-windows-win-file-module), [ansible.windows.win_reg_stat](win_reg_stat_module.md#ansible-collections-ansible-windows-win-reg-stat-module) will return whether the key/property exists.
- It also returns the sub keys and properties of the key specified.
- If specifying a property name through *property*, it will return the information specific for that property.

## [Parameters](win_reg_stat_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: entry, value, property  string | The registry property name to get information for, the return json will not include the sub_keys and properties entries for the *key* specified.  Set to an empty string to target the registry key’s `(Default`) property value. |
| **path**  aliases: key  string / required | The full registry key path including the hive to search for. |

## [Notes](win_reg_stat_module.md#id3)

> **Note:**
>
> - The `properties` return value will contain an empty string key `""` that refers to the key’s `Default` value. If the value has not been set then this key is not returned.

## [See Also](win_reg_stat_module.md#id4)

> **See also:**
>
> [ansible.windows.win_regedit](win_regedit_module.md#ansible-collections-ansible-windows-win-regedit-module)
> :   Add, change, or remove registry keys and values.
>
> [community.windows.win_regmerge](../../community/windows/win_regmerge_module.md#ansible-collections-community-windows-win-regmerge-module)
> :   Merges the contents of a registry file into the Windows registry.

## [Examples](win_reg_stat_module.md#id5)

```yaml+jinja
- name: Obtain information about a registry key using short form
  ansible.windows.win_reg_stat:
    path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
  register: current_version

- name: Obtain information about a registry key property
  ansible.windows.win_reg_stat:
    path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
    name: CommonFilesDir
  register: common_files_dir

- name: Obtain the registry key's (Default) property
  ansible.windows.win_reg_stat:
    path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion
    name: ''
  register: current_version_default
```

## [Return Values](win_reg_stat_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether anything was changed.  Returned: always  Sample: `true` |
| **exists**  boolean | States whether the registry key/property exists.  Returned: success and path/property exists  Sample: `true` |
| **properties**  dictionary | A dictionary containing all the properties and their values in the registry key.  Returned: success, path exists and property not specified  Sample: `{"": {"raw_value": "", "type": "REG_SZ", "value": ""}, "binary_property": {"raw_value": ["0x01", "0x16"], "type": "REG_BINARY", "value": [1, 22]}, "multi_string_property": {"raw_value": ["a", "b"], "type": "REG_MULTI_SZ", "value": ["a", "b"]}}` |
| **raw_value**  string | Returns the raw value of the registry property, REG_EXPAND_SZ has no string expansion, REG_BINARY or REG_NONE is in hex 0x format. REG_NONE, this value is a hex string in the 0x format.  Returned: success, path/property exists and property specified  Sample: `"%ProgramDir%\\\\Common Files"` |
| **sub_keys**  list / elements=string | A list of all the sub keys of the key specified.  Returned: success, path exists and property not specified  Sample: `["AppHost", "Casting", "DateTime"]` |
| **type**  string | The property type.  Returned: success, path/property exists and property specified  Sample: `"REG_EXPAND_SZ"` |
| **value**  string | The value of the property.  Returned: success, path/property exists and property specified  Sample: `"C:\\\\Program Files\\\\Common Files"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
