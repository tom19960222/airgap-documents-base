---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_fs module – Manage FlashArray File Systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_fs_module.html
fetched_at: 2026-07-28T02:50:58+00:00
---
# purestorage.flasharray.purefa_fs module – Manage FlashArray File Systems

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_fs_module.md#ansible-collections-purestorage-flasharray-purefa-fs-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_fs`.

New in purestorage.flasharray 1.5.0

- [Synopsis](purefa_fs_module.md#synopsis)
- [Requirements](purefa_fs_module.md#requirements)
- [Parameters](purefa_fs_module.md#parameters)
- [Notes](purefa_fs_module.md#notes)
- [Examples](purefa_fs_module.md#examples)

## [Synopsis](purefa_fs_module.md#id1)

- Create/Delete FlashArray File Systems

## [Requirements](purefa_fs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_fs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **eradicate**  boolean | Define whether to eradicate the file system on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **move**  string  *added in purestorage.flasharray 1.13.0* | Move a filesystem in and out of a pod  Provide the name of pod to move the filesystem to  Pod names must be unique in the array  To move to the local array, specify `local`  This is not idempotent - use `ignore_errors` in the play |
| **name**  string / required | Name of the file system |
| **rename**  string | Value to rename the specified file system to  Rename only applies to the container the current filesystem is in.  There is no requirement to specify the pod name as this is implied. |
| **state**  string | Define whether the file system should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_fs_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_fs_module.md#id5)

```yaml+jinja
- name: Create file system foo
  purestorage.flasharray.purefa_fs:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete and eradicate file system foo
  purestorage.flasharray.purefa_fs:
    name: foo
    eradicate: true
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Rename file system foo to bar
  purestorage.flasharray.purefa_fs:
    name: foo
    rename: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
