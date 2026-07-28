---
collection: ansible
version: "8"
title: "ansible.windows.win_regedit module – Add, change, or remove registry keys and values"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_regedit_module.html
fetched_at: 2026-07-28T01:10:46+00:00
---
# ansible.windows.win_regedit module – Add, change, or remove registry keys and values

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_regedit`.

- [Synopsis](win_regedit_module.md#synopsis)
- [Parameters](win_regedit_module.md#parameters)
- [Notes](win_regedit_module.md#notes)
- [See Also](win_regedit_module.md#see-also)
- [Examples](win_regedit_module.md#examples)
- [Return Values](win_regedit_module.md#return-values)

## [Synopsis](win_regedit_module.md#id1)

- Add, modify or remove registry keys and values.
- More information about the windows registry from Wikipedia <https://en.wikipedia.org/wiki/Windows_Registry>.

## [Parameters](win_regedit_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **data**  any | Value of the registry entry `name` in `path`.  If not specified then the value for the property will be null for the corresponding `type`.  Binary and None data should be expressed in a yaml byte array or as comma separated hex values.  An easy way to generate this is to run `regedit.exe` and use the *export* option to save the registry values to a file.  In the exported file, binary value will look like `hex:be,ef,be,ef`, the `hex:` prefix is optional.  DWORD and QWORD values should either be represented as a decimal number or a hex value.  Multistring values should be passed in as a list.  See the examples for more details on how to format this data. |
| **delete_key**  boolean | When `state` is ‘absent’ then this will delete the entire key.  If `false` then it will only clear out the ‘(Default)’ property for that key.  **Choices:**   - `false` - `true` ← (default) |
| **hive**  path | A path to a hive key like C:\Users\Default\NTUSER.DAT to load in the registry.  This hive is loaded under the HKLM:\ANSIBLE key which can then be used in *name* like any other path.  This can be used to load the default user profile registry hive or any other hive saved as a file.  Using this function requires the user to have the `SeRestorePrivilege` and `SeBackupPrivilege` privileges enabled. |
| **name**  aliases: entry, value  string | Name of the registry entry in the above `path` parameters.  If not provided, or empty then the ‘(Default)’ property for the key will be used. |
| **path**  aliases: key  string / required | Name of the registry path.  Should be in one of the following registry hives: HKCC, HKCR, HKCU, HKLM, HKU. |
| **state**  string | The state of the registry entry.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  aliases: datatype  string | The registry value data type.  **Choices:**   - `"none"` - `"binary"` - `"dword"` - `"expandstring"` - `"multistring"` - `"string"` ← (default) - `"qword"` |

## [Notes](win_regedit_module.md#id3)

> **Note:**
>
> - Check-mode `-C/--check` and diff output `-D/--diff` are supported, so that you can test every change against the active configuration before applying changes.
> - Beware that some registry hives (`HKEY_USERS` in particular) do not allow to create new registry paths in the root folder.

## [See Also](win_regedit_module.md#id4)

> **See also:**
>
> [ansible.windows.win_reg_stat](win_reg_stat_module.md#ansible-collections-ansible-windows-win-reg-stat-module)
> :   Get information about Windows registry keys.
>
> [community.windows.win_regmerge](../../community/windows/win_regmerge_module.md#ansible-collections-community-windows-win-regmerge-module)
> :   Merges the contents of a registry file into the Windows registry.

## [Examples](win_regedit_module.md#id5)

```yaml+jinja
- name: Create registry path MyCompany
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany

- name: Add or update registry path MyCompany, with entry 'hello', and containing 'world'
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: world

- name: Add or update registry path MyCompany, with dword entry 'hello', and containing 1337 as the decimal value
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: 1337
    type: dword

- name: Add or update registry path MyCompany, with dword entry 'hello', and containing 0xff2500ae as the hex value
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: 0xff2500ae
    type: dword

- name: Add or update registry path MyCompany, with binary entry 'hello', and containing binary data in hex-string format
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: hex:be,ef,be,ef,be,ef,be,ef,be,ef
    type: binary

- name: Add or update registry path MyCompany, with binary entry 'hello', and containing binary data in yaml format
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: [0xbe,0xef,0xbe,0xef,0xbe,0xef,0xbe,0xef,0xbe,0xef]
    type: binary

- name: Add or update registry path MyCompany, with expand string entry 'hello'
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: '%appdata%\local'
    type: expandstring

- name: Add or update registry path MyCompany, with multi string entry 'hello'
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    data: ['hello', 'world']
    type: multistring

- name: Disable keyboard layout hotkey for all users (changes existing)
  ansible.windows.win_regedit:
    path: HKU:\.DEFAULT\Keyboard Layout\Toggle
    name: Layout Hotkey
    data: 3
    type: dword

- name: Disable language hotkey for current users (adds new)
  ansible.windows.win_regedit:
    path: HKCU:\Keyboard Layout\Toggle
    name: Language Hotkey
    data: 3
    type: dword

- name: Remove registry path MyCompany (including all entries it contains)
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    state: absent
    delete_key: true

- name: Clear the existing (Default) entry at path MyCompany
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    state: absent
    delete_key: false

- name: Remove entry 'hello' from registry path MyCompany
  ansible.windows.win_regedit:
    path: HKCU:\Software\MyCompany
    name: hello
    state: absent

- name: Change default mouse trailing settings for new users
  ansible.windows.win_regedit:
    path: HKLM:\ANSIBLE\Control Panel\Mouse
    name: MouseTrails
    data: 10
    type: string
    state: present
    hive: C:\Users\Default\NTUSER.dat
```

## [Return Values](win_regedit_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data_changed**  boolean | Whether this invocation changed the data in the registry value.  **Returned:** success  **Sample:** `false` |
| **data_type_changed**  boolean | Whether this invocation changed the datatype of the registry value.  **Returned:** success  **Sample:** `true` |

### Authors

- Adam Keech (@smadam813)
- Josh Ludwig (@joshludwig)
- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
