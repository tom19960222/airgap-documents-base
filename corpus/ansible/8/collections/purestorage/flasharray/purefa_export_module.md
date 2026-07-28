---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_export module – Manage FlashArray File System Exports"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_export_module.html
fetched_at: 2026-07-28T02:50:56+00:00
---
# purestorage.flasharray.purefa_export module – Manage FlashArray File System Exports

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
> see [Requirements](purefa_export_module.md#ansible-collections-purestorage-flasharray-purefa-export-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_export`.

New in purestorage.flasharray 1.5.0

- [Synopsis](purefa_export_module.md#synopsis)
- [Requirements](purefa_export_module.md#requirements)
- [Parameters](purefa_export_module.md#parameters)
- [Notes](purefa_export_module.md#notes)
- [Examples](purefa_export_module.md#examples)

## [Synopsis](purefa_export_module.md#id1)

- Create/Delete FlashArray File Systems Exports

## [Requirements](purefa_export_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_export_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **directory**  string / required | Name of the managed directory in the file system the export applies to |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **filesystem**  string / required | Name of the filesystem the export applies to |
| **name**  string / required | Name of the export |
| **nfs_policy**  string | Name of NFS Policy to apply to the export |
| **smb_policy**  string | Name of SMB Policy to apply to the export |
| **state**  string | Define whether the export should exist or not.  You must specify an NFS or SMB policy, or both on creation and deletion.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_export_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_export_module.md#id5)

```yaml+jinja
- name: Create NFS and SMB exports for directory foo in filesysten bar
  purestorage.flasharray.purefa_export:
    name: export1
    filesystem: bar
    directory: foo
    nfs_policy: nfs-example
    smb_polict: smb-example
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete NFS export for directory foo in filesystem bar
  purestorage.flasharray.purefa_export:
    name: export1
    filesystem: bar
    directory: foo
    nfs_policy: nfs-example
    state: absent
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
