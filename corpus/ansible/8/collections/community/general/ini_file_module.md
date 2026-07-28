---
collection: ansible
version: "8"
title: "community.general.ini_file module – Tweak settings in INI files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ini_file_module.html
fetched_at: 2026-07-28T01:46:32+00:00
---
# community.general.ini_file module – Tweak settings in INI files

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
> To use it in a playbook, specify: `community.general.ini_file`.

- [Synopsis](ini_file_module.md#synopsis)
- [Parameters](ini_file_module.md#parameters)
- [Attributes](ini_file_module.md#attributes)
- [Notes](ini_file_module.md#notes)
- [Examples](ini_file_module.md#examples)

## [Synopsis](ini_file_module.md#id1)

- Manage (add, remove, change) individual settings in an INI-style file without having to manage the file as a whole with, say, [ansible.builtin.template](../../ansible/builtin/template_module.md#ansible-collections-ansible-builtin-template-module) or [ansible.builtin.assemble](../../ansible/builtin/assemble_module.md#ansible-collections-ansible-builtin-assemble-module).
- Adds missing sections if they don’t exist.
- Before Ansible 2.0, comments are discarded when the source file is read, and therefore will not show up in the destination file.
- Since Ansible 2.3, this module adds missing ending newlines to files to keep in line with the POSIX standard, even when no other modifications need to be applied.

Aliases: files.ini_file

## [Parameters](ini_file_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_no_value**  boolean | Allow option without value and without ‘=’ symbol.  **Choices:**   - `false` ← (default) - `true` |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **create**  boolean | If set to `false`, the module will fail if the file does not already exist.  By default it will create the file if it is missing.  **Choices:**   - `false` - `true` ← (default) |
| **exclusive**  boolean  *added in community.general 3.6.0* | If set to `true` (default), all matching `option` lines are removed when `state=absent`, or replaced when `state=present`.  If set to `false`, only the specified `value`/`values` are added when `state=present`, or removed when `state=absent`, and existing ones are not modified.  **Choices:**   - `false` - `true` ← (default) |
| **follow**  boolean  *added in community.general 7.1.0* | This flag indicates that filesystem links, if they exist, should be followed.  `follow=true` can modify `path` when combined with parameters such as `mode`.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **ignore_spaces**  boolean  *added in community.general 7.5.0* | Do not change a line if doing so would only add or remove spaces before or after the `=` symbol.  **Choices:**   - `false` ← (default) - `true` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **no_extra_spaces**  boolean | Do not insert spaces before and after ‘=’ symbol.  **Choices:**   - `false` ← (default) - `true` |
| **option**  string | If set (required for changing a `value`), this is the name of the option.  May be omitted if adding/removing a whole `section`. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  aliases: dest  path / required | Path to the INI-style file; this file is created if required.  Before Ansible 2.3 this option was only usable as `dest`. |
| **section**  string | Section name in INI file. This is added if `state=present` automatically when a single value is being set.  If being omitted, the `option` will be placed before the first `section`.  Omitting `section` is also required if the config format does not support sections. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | If set to `absent` and `exclusive` set to `true` all matching `option` lines are removed.  If set to `absent` and `exclusive` set to `false` the specified `option=value` lines are removed, but the other `option`s with the same name are not touched.  If set to `present` and `exclusive` set to `false` the specified `option=values` lines are added, but the other `option`s with the same name are not touched.  If set to `present` and `exclusive` set to `true` all given `option=values` lines will be added and the other `option`s with the same name are removed.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **value**  string | The string value to be associated with an `option`.  May be omitted when removing an `option`.  Mutually exclusive with `values`.  `value=v` is equivalent to `values=[v]`. |
| **values**  list / elements=string  *added in community.general 3.6.0* | The string value to be associated with an `option`.  May be omitted when removing an `option`.  Mutually exclusive with `value`.  `value=v` is equivalent to `values=[v]`. |

## [Attributes](ini_file_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ini_file_module.md#id4)

> **Note:**
>
> - While it is possible to add an `option` without specifying a `value`, this makes no sense.
> - As of Ansible 2.3, the `dest` option has been changed to `path` as default, but `dest` still works as well.
> - As of community.general 3.2.0, UTF-8 BOM markers are discarded when reading files.

## [Examples](ini_file_module.md#id5)

```yaml+jinja
# Before Ansible 2.3, option 'dest' was used instead of 'path'
- name: Ensure "fav=lemonade is in section "[drinks]" in specified file
  community.general.ini_file:
    path: /etc/conf
    section: drinks
    option: fav
    value: lemonade
    mode: '0600'
    backup: true

- name: Ensure "temperature=cold is in section "[drinks]" in specified file
  community.general.ini_file:
    path: /etc/anotherconf
    section: drinks
    option: temperature
    value: cold
    backup: true

- name: Add "beverage=lemon juice" is in section "[drinks]" in specified file
  community.general.ini_file:
    path: /etc/conf
    section: drinks
    option: beverage
    value: lemon juice
    mode: '0600'
    state: present
    exclusive: false

- name: Ensure multiple values "beverage=coke" and "beverage=pepsi" are in section "[drinks]" in specified file
  community.general.ini_file:
    path: /etc/conf
    section: drinks
    option: beverage
    values:
      - coke
      - pepsi
    mode: '0600'
    state: present

- name: Add "beverage=lemon juice" outside a section in specified file
  community.general.ini_file:
    path: /etc/conf
    option: beverage
    value: lemon juice
    state: present
```

### Authors

- Jan-Piet Mens (@jpmens)
- Ales Nosek (@noseka1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
