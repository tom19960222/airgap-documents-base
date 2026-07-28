---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_file module – Manage FlashArray File Copies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_file_module.html
fetched_at: 2026-07-28T02:50:57+00:00
---
# purestorage.flasharray.purefa_file module – Manage FlashArray File Copies

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
> see [Requirements](purefa_file_module.md#ansible-collections-purestorage-flasharray-purefa-file-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_file`.

New in purestorage.flasharray 1.22.0

- [Synopsis](purefa_file_module.md#synopsis)
- [Requirements](purefa_file_module.md#requirements)
- [Parameters](purefa_file_module.md#parameters)
- [Notes](purefa_file_module.md#notes)
- [Examples](purefa_file_module.md#examples)

## [Synopsis](purefa_file_module.md#id1)

- Copy FlashArray File from one filesystem to another

## [Requirements](purefa_file_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_file_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **overwrite**  boolean | Define whether to overwrite an existing target file  **Choices:**   - `false` ← (default) - `true` |
| **source_dir**  string / required | Name of the source managed directory containing the source file to be copied |
| **source_file**  string / required | Name of the file to copy  Include full path from the perspective of the source managed directory |
| **target_dir**  string | Name of the target managed directory containing the source file to be copied  If not provided will use managed directory specified by *source_dir* |
| **target_file**  string | Name of the file to copy to  Include full path from the perspective of the target managed directory  If not provided the file will be copied to the relative path specified by *name* |

## [Notes](purefa_file_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_file_module.md#id5)

```yaml+jinja
- name: Copy a file from dir foo to dir bar
  purestorage.flasharray.purefa_file:
    source_file: "/directory1/file1"
    source_dir: "fs1:root"
    target_file: "/diff_dir/file1"
    target_dir: "fs1:root"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Copy a file in a direcotry to the same directory with a different name
  purestorage.flasharray.purefa_file:
    source_file: "/directory1/file1"
    source_dir: "fs1:root"
    target_file: "/directory_1/file2"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Copy a file in a direcotry to an existing file with overwrite
  purestorage.flasharray.purefa_file:
    source_file: "/directory1/file1"
    source_dir: "fs1:root"
    target_file: "/diff_dir/file1"
    target_dir: "fs2:root"
    overwrite: true
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
