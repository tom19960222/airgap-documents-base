---
collection: ansible
version: "8"
title: "community.network.ftd_file_download module – Downloads files from Cisco FTD devices over HTTP(S)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ftd_file_download_module.html
fetched_at: 2026-07-28T01:56:41+00:00
---
# community.network.ftd_file_download module – Downloads files from Cisco FTD devices over HTTP(S)

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ftd_file_download`.

- [Synopsis](ftd_file_download_module.md#synopsis)
- [Parameters](ftd_file_download_module.md#parameters)
- [Examples](ftd_file_download_module.md#examples)
- [Return Values](ftd_file_download_module.md#return-values)

## [Synopsis](ftd_file_download_module.md#id1)

- Downloads files from Cisco FTD devices including pending changes, disk files, certificates, troubleshoot reports, and backups.

Aliases: network.ftd.ftd_file_download

## [Parameters](ftd_file_download_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **destination**  path / required | Absolute path of where to download the file to.  If destination is a directory, the module uses a filename from ‘Content-Disposition’ header specified by the server. |
| **operation**  string / required | The name of the operation to execute.  Only operations that return a file can be used in this module. |
| **path_params**  dictionary | Key-value pairs that should be sent as path parameters in a REST API call. |

## [Examples](ftd_file_download_module.md#id3)

```yaml+jinja
- name: Download pending changes
  community.network.ftd_file_download:
    operation: 'getdownload'
    path_params:
      objId: 'default'
    destination: /tmp/
```

## [Return Values](ftd_file_download_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The error message describing why the module failed.  **Returned:** error |

### Authors

- Cisco Systems, Inc. (@annikulin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
