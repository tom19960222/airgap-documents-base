---
collection: ansible
version: "8"
title: "community.general.sysrc module – Manage FreeBSD using sysrc"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/sysrc_module.html
fetched_at: 2026-07-28T01:50:55+00:00
---
# community.general.sysrc module – Manage FreeBSD using sysrc

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
> To use it in a playbook, specify: `community.general.sysrc`.

New in community.general 2.0.0

- [Synopsis](sysrc_module.md#synopsis)
- [Parameters](sysrc_module.md#parameters)
- [Attributes](sysrc_module.md#attributes)
- [Notes](sysrc_module.md#notes)
- [Examples](sysrc_module.md#examples)
- [Return Values](sysrc_module.md#return-values)

## [Synopsis](sysrc_module.md#id1)

- Manages `/etc/rc.conf` for FreeBSD.

Aliases: system.sysrc

## [Parameters](sysrc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delim**  string | Delimiter to be used instead of `" "` (space).  Only used when `state=value_present` or `state=value_absent`.  **Default:** `" "` |
| **jail**  string | Name or ID of the jail to operate on. |
| **name**  string / required | Name of variable in `/etc/rc.conf` to manage. |
| **path**  string | Path to file to use instead of `/etc/rc.conf`.  **Default:** `"/etc/rc.conf"` |
| **state**  string | Use `present` to add the variable.  Use `absent` to remove the variable.  Use `value_present` to add the value to the existing variable.  Use `value_absent` to remove the value from the existing variable.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"value_present"` - `"value_absent"` |
| **value**  string | The value to set when `state=present`.  The value to add when `state=value_present`.  The value to remove when `state=value_absent`. |

## [Attributes](sysrc_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](sysrc_module.md#id4)

> **Note:**
>
> - The `name` cannot contain periods as sysrc does not support OID style names.

## [Examples](sysrc_module.md#id5)

```yaml+jinja
---
# enable mysql in the /etc/rc.conf
- name: Configure mysql pid file
  community.general.sysrc:
    name: mysql_pidfile
    value: "/var/run/mysqld/mysqld.pid"

# enable accf_http kld in the boot loader
- name: Enable accf_http kld
  community.general.sysrc:
    name: accf_http_load
    state: present
    value: "YES"
    path: /boot/loader.conf

# add gif0 to cloned_interfaces
- name: Add gif0 interface
  community.general.sysrc:
    name: cloned_interfaces
    state: value_present
    value: "gif0"

# enable nginx on a jail
- name: Enable nginx in test jail
  community.general.sysrc:
    name: nginx_enable
    value: "YES"
    jail: testjail
```

## [Return Values](sysrc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Return changed for sysrc actions.  **Returned:** always  **Sample:** `true` |

### Authors

- David Lundgren (@dlundgren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
