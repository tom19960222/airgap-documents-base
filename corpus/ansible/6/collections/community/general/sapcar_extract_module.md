---
collection: ansible
version: "6"
title: "community.general.sapcar_extract module – Manages SAP SAPCAR archives"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sapcar_extract_module.html
fetched_at: 2026-07-27T17:12:52+00:00
---
# community.general.sapcar_extract module – Manages SAP SAPCAR archives

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
> To use it in a playbook, specify: `community.general.sapcar_extract`.

New in community.general 3.2.0

- [Synopsis](sapcar_extract_module.md#synopsis)
- [Parameters](sapcar_extract_module.md#parameters)
- [Notes](sapcar_extract_module.md#notes)
- [Examples](sapcar_extract_module.md#examples)

## [Synopsis](sapcar_extract_module.md#id1)

- Provides support for unpacking `sar`/`car` files with the SAPCAR binary from SAP and pulling information back into Ansible.

## [Parameters](sapcar_extract_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **binary_path**  path | The path to the SAPCAR binary, for example, `/home/dummy/sapcar` or `https://myserver/SAPCAR`. If this parameter is not provided the module will look in `PATH`. |
| **dest**  path | The destination where SAPCAR extracts the SAR file. Missing folders will be created. If this parameter is not provided it will unpack in the same folder as the SAR file. |
| **manifest**  string | The name of the manifest.  Default: `"SIGNATURE.SMF"` |
| **path**  path / required | The path to the SAR/CAR file. |
| **remove**  boolean | If `true` the SAR/CAR file will be removed. **This should be used with caution!**  Choices:   - `false` ← (default) - `true` |
| **security_library**  path | The path to the security library, for example, `/usr/sap/hostctrl/exe/libsapcrytp.so`, for signature operations. |
| **signature**  boolean | If `true` the signature will be extracted.  Choices:   - `false` ← (default) - `true` |

## [Notes](sapcar_extract_module.md#id3)

> **Note:**
>
> - Always returns `changed=true` in `check_mode`.

## [Examples](sapcar_extract_module.md#id4)

```yaml+jinja
- name: Extract SAR file
  community.general.sapcar_extract:
    path: "~/source/hana.sar"

- name: Extract SAR file with destination
  community.general.sapcar_extract:
    path: "~/source/hana.sar"
    dest: "~/test/"

- name: Extract SAR file with destination and download from webserver can be a fileshare as well
  community.general.sapcar_extract:
    path: "~/source/hana.sar"
    dest: "~/dest/"
    binary_path: "https://myserver/SAPCAR"

- name: Extract SAR file and delete SAR after extract
  community.general.sapcar_extract:
    path: "~/source/hana.sar"
    remove: true

- name: Extract SAR file with manifest
  community.general.sapcar_extract:
    path: "~/source/hana.sar"
    signature: true

- name: Extract SAR file with manifest and rename it
  community.general.sapcar_extract:
    path: "~/source/hana.sar"
    manifest: "MyNewSignature.SMF"
    signature: true
```

### Authors

- Rainer Leber (@RainerLeber)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
