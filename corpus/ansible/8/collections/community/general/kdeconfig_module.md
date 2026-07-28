---
collection: ansible
version: "8"
title: "community.general.kdeconfig module – Manage KDE configuration files"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/kdeconfig_module.html
fetched_at: 2026-07-28T01:47:04+00:00
---
# community.general.kdeconfig module – Manage KDE configuration files

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](kdeconfig_module.md#ansible-collections-community-general-kdeconfig-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.kdeconfig`.

New in community.general 6.5.0

- [Synopsis](kdeconfig_module.md#synopsis)
- [Requirements](kdeconfig_module.md#requirements)
- [Parameters](kdeconfig_module.md#parameters)
- [Attributes](kdeconfig_module.md#attributes)
- [Examples](kdeconfig_module.md#examples)

## [Synopsis](kdeconfig_module.md#id1)

- Add or change individual settings in KDE configuration files.
- It uses **kwriteconfig** under the hood.

## [Requirements](kdeconfig_module.md#id2)

The below requirements are needed on the host that executes this module.

- kwriteconfig

## [Parameters](kdeconfig_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **kwriteconfig_path**  path | Path to the kwriteconfig executable. If not specified, Ansible will try to discover it. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **path**  path / required | Path to the config file. If the file does not exist it will be created. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **values**  list / elements=dictionary / required | List of values to set. |
| **bool_value**  boolean | Boolean value.  One between this and `values[].value` is required.  **Choices:**   - `false` - `true` |
| **group**  string | The option’s group. One between this and `values[].groups` is required. |
| **groups**  list / elements=string | List of the option’s groups. One between this and `values[].group` is required. |
| **key**  string / required | The option’s name. |
| **value**  string | The option’s value. One between this and `values[].bool_value` is required. |

## [Attributes](kdeconfig_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](kdeconfig_module.md#id5)

```yaml+jinja
- name: Ensure "Homepage=https://www.ansible.com/" in group "Branding"
  community.general.kdeconfig:
    path: /etc/xdg/kickoffrc
    values:
      - group: Branding
        key: Homepage
        value: https://www.ansible.com/
    mode: '0644'

- name: Ensure "KEY=true" in groups "Group" and "Subgroup", and "KEY=VALUE" in Group2
  community.general.kdeconfig:
    path: /etc/xdg/someconfigrc
    values:
      - groups: [Group, Subgroup]
        key: KEY
        bool_value: true
      - group: Group2
        key: KEY
        value: VALUE
    backup: true
```

### Authors

- Salvatore Mesoraca (@smeso)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
