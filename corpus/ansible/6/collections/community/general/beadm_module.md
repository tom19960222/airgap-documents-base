---
collection: ansible
version: "6"
title: "community.general.beadm module – Manage ZFS boot environments on FreeBSD/Solaris/illumos systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/beadm_module.html
fetched_at: 2026-07-27T17:08:13+00:00
---
# community.general.beadm module – Manage ZFS boot environments on FreeBSD/Solaris/illumos systems

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.beadm`.

- [Synopsis](beadm_module.md#synopsis)
- [Parameters](beadm_module.md#parameters)
- [Examples](beadm_module.md#examples)
- [Return Values](beadm_module.md#return-values)

## [Synopsis](beadm_module.md#id1)

- Create, delete or activate ZFS boot environments.
- Mount and unmount ZFS boot environments.

## [Parameters](beadm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Associate a description with a new boot environment. This option is available only on Solarish platforms. |
| **force**  boolean | Specifies if the unmount should be forced.  Choices:   - `false` ← (default) - `true` |
| **mountpoint**  path | Path where to mount the ZFS boot environment. |
| **name**  aliases: be  string / required | ZFS boot environment name. |
| **options**  string | Create the datasets for new BE with specific ZFS properties.  Multiple options can be specified.  This option is available only on Solarish platforms. |
| **snapshot**  string | If specified, the new boot environment will be cloned from the given snapshot or inactive boot environment. |
| **state**  string | Create or delete ZFS boot environment.  Choices:   - `"absent"` - `"activated"` - `"mounted"` - `"present"` ← (default) - `"unmounted"` |

## [Examples](beadm_module.md#id3)

```yaml+jinja
- name: Create ZFS boot environment
  community.general.beadm:
    name: upgrade-be
    state: present

- name: Create ZFS boot environment from existing inactive boot environment
  community.general.beadm:
    name: upgrade-be
    snapshot: be@old
    state: present

- name: Create ZFS boot environment with compression enabled and description "upgrade"
  community.general.beadm:
    name: upgrade-be
    options: "compression=on"
    description: upgrade
    state: present

- name: Delete ZFS boot environment
  community.general.beadm:
    name: old-be
    state: absent

- name: Mount ZFS boot environment on /tmp/be
  community.general.beadm:
    name: BE
    mountpoint: /tmp/be
    state: mounted

- name: Unmount ZFS boot environment
  community.general.beadm:
    name: BE
    state: unmounted

- name: Activate ZFS boot environment
  community.general.beadm:
    name: upgrade-be
    state: activated
```

## [Return Values](beadm_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | BE description  Returned: always  Sample: `"Upgrade from 9.0 to 10.0"` |
| **force**  boolean | If forced action is wanted  Returned: always  Sample: `false` |
| **mountpoint**  string | BE mountpoint  Returned: always  Sample: `"/mnt/be"` |
| **name**  string | BE name  Returned: always  Sample: `"pre-upgrade"` |
| **options**  string | BE additional options  Returned: always  Sample: `"compression=on"` |
| **snapshot**  string | ZFS snapshot to create BE from  Returned: always  Sample: `"rpool/ROOT/oi-hipster@fresh"` |
| **state**  string | state of the target  Returned: always  Sample: `"present"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
