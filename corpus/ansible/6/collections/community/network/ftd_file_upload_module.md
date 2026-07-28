---
collection: ansible
version: "6"
title: "community.network.ftd_file_upload module – Uploads files to Cisco FTD devices over HTTP(S)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ftd_file_upload_module.html
fetched_at: 2026-07-27T17:18:37+00:00
---
# community.network.ftd_file_upload module – Uploads files to Cisco FTD devices over HTTP(S)

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ftd_file_upload`.

- [Synopsis](ftd_file_upload_module.md#synopsis)
- [Parameters](ftd_file_upload_module.md#parameters)
- [Examples](ftd_file_upload_module.md#examples)
- [Return Values](ftd_file_upload_module.md#return-values)

## [Synopsis](ftd_file_upload_module.md#id1)

- Uploads files to Cisco FTD devices including disk files, backups, and upgrades.

## [Parameters](ftd_file_upload_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **file_to_upload**  path / required | Absolute path to the file that should be uploaded. |
| **operation**  string / required | The name of the operation to execute.  Only operations that upload file can be used in this module. |
| **register_as**  string | Specifies Ansible fact name that is used to register received response from the FTD device. |

## [Examples](ftd_file_upload_module.md#id3)

```yaml+jinja
- name: Upload disk file
  community.network.ftd_file_upload:
    operation: 'postuploaddiskfile'
    file_to_upload: /tmp/test1.txt
```

## [Return Values](ftd_file_upload_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The error message describing why the module failed.  Returned: error |

### Authors

- Cisco Systems, Inc. (@annikulin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
