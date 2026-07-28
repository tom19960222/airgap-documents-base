---
collection: ansible
version: "6"
title: "community.general.selogin module – Manages linux user to SELinux user mapping"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/selogin_module.html
fetched_at: 2026-07-27T17:13:08+00:00
---
# community.general.selogin module – Manages linux user to SELinux user mapping

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](selogin_module.md#ansible-collections-community-general-selogin-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.selogin`.

- [Synopsis](selogin_module.md#synopsis)
- [Requirements](selogin_module.md#requirements)
- [Parameters](selogin_module.md#parameters)
- [Notes](selogin_module.md#notes)
- [Examples](selogin_module.md#examples)

## [Synopsis](selogin_module.md#id1)

- Manages linux user to SELinux user mapping

## [Requirements](selogin_module.md#id2)

The below requirements are needed on the host that executes this module.

- libselinux
- policycoreutils

## [Parameters](selogin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ignore_selinux_state**  boolean | Run independent of selinux runtime state  Choices:   - `false` ← (default) - `true` |
| **login**  string / required | a Linux user |
| **reload**  boolean | Reload SELinux policy after commit.  Choices:   - `false` - `true` ← (default) |
| **selevel**  aliases: serange  string | MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range for SELinux login mapping defaults to the SELinux user record range.  Default: `"s0"` |
| **seuser**  string | SELinux user name |
| **state**  string | Desired mapping value.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](selogin_module.md#id4)

> **Note:**
>
> - The changes are persistent across reboots
> - Not tested on any debian based system

## [Examples](selogin_module.md#id5)

```yaml+jinja
- name: Modify the default user on the system to the guest_u user
  community.general.selogin:
    login: __default__
    seuser: guest_u
    state: present

- name: Assign gijoe user on an MLS machine a range and to the staff_u user
  community.general.selogin:
    login: gijoe
    seuser: staff_u
    serange: SystemLow-Secret
    state: present

- name: Assign all users in the engineering group to the staff_u user
  community.general.selogin:
    login: '%engineering'
    seuser: staff_u
    state: present
```

### Authors

- Dan Keder (@dankeder)
- Petr Lautrbach (@bachradsusi)
- James Cassell (@jamescassell)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
