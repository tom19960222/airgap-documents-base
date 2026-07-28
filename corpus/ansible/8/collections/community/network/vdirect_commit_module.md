---
collection: ansible
version: "8"
title: "community.network.vdirect_commit module – Commits pending configuration changes on Radware devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/vdirect_commit_module.html
fetched_at: 2026-07-28T01:57:55+00:00
---
# community.network.vdirect_commit module – Commits pending configuration changes on Radware devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](vdirect_commit_module.md#ansible-collections-community-network-vdirect-commit-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.vdirect_commit`.

- [Synopsis](vdirect_commit_module.md#synopsis)
- [Requirements](vdirect_commit_module.md#requirements)
- [Parameters](vdirect_commit_module.md#parameters)
- [Notes](vdirect_commit_module.md#notes)
- [Examples](vdirect_commit_module.md#examples)
- [Return Values](vdirect_commit_module.md#return-values)

## [Synopsis](vdirect_commit_module.md#id1)

- Commits pending configuration changes on one or more Radware devices via vDirect server.
- For Alteon ADC device, apply, sync and save actions will be performed by default. Skipping of an action is possible by explicit parameter specifying.
- For Alteon VX Container device, no sync operation will be performed since sync action is only relevant for Alteon ADC devices.
- For DefensePro and AppWall devices, a bulk commit action will be performed. Explicit apply, sync and save actions specifying is not relevant.

Aliases: network.radware.vdirect_commit

## [Requirements](vdirect_commit_module.md#id2)

The below requirements are needed on the host that executes this module.

- vdirect-client >= 4.9.0-post4

## [Parameters](vdirect_commit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply**  boolean | If `no`, apply action will not be performed. Relevant for ADC devices only.  **Choices:**   - `false` - `true` ← (default) |
| **devices**  string / required | List of Radware Alteon device names for commit operations. |
| **save**  boolean | If `no`, save action will not be performed. Relevant for ADC devices only.  **Choices:**   - `false` - `true` ← (default) |
| **sync**  boolean | If `no`, sync action will not be performed. Relevant for ADC devices only.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  aliases: vdirect_validate_certs  boolean | If `no`, SSL certificates will not be validated,  may be set as `VDIRECT_VALIDATE_CERTS` or `VDIRECT_VERIFY` environment variable.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vdirect_http_port**  string | vDirect server HTTP port number, may be set as `VDIRECT_HTTP_PORT` environment variable.  **Default:** `2188` |
| **vdirect_https_port**  string | vDirect server HTTPS port number, may be set as `VDIRECT_HTTPS_PORT` environment variable.  **Default:** `2189` |
| **vdirect_ip**  string / required | Primary vDirect server IP address, may be set as `VDIRECT_IP` environment variable. |
| **vdirect_password**  string / required | vDirect server password, may be set as `VDIRECT_PASSWORD` environment variable. |
| **vdirect_secondary_ip**  string | Secondary vDirect server IP address, may be set as `VDIRECT_SECONDARY_IP` environment variable. |
| **vdirect_timeout**  string | Amount of time to wait for async operation completion [seconds],  may be set as `VDIRECT_TIMEOUT` environment variable.  **Default:** `60` |
| **vdirect_use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection,  may be set as `VDIRECT_HTTPS` or `VDIRECT_USE_SSL` environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **vdirect_user**  string / required | vDirect server username, may be set as `VDIRECT_USER` environment variable. |
| **vdirect_wait**  boolean | Wait for async operation to complete, may be set as `VDIRECT_WAIT` environment variable.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vdirect_commit_module.md#id4)

> **Note:**
>
> - Requires the Radware vdirect-client Python package on the host. This is as easy as `pip install vdirect-client`

## [Examples](vdirect_commit_module.md#id5)

```yaml+jinja
- name: Commit
  community.network.vdirect_commit:
      vdirect_ip: 10.10.10.10
      vdirect_user: vDirect
      vdirect_password: radware
      devices: ['dev1', 'dev2']
      sync: false
```

## [Return Values](vdirect_commit_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | Message detailing actions result  **Returned:** success  **Sample:** `"Requested actions were successfully performed on all devices."` |

### Authors

- Evgeny Fedoruk @ Radware LTD (@evgenyfedoruk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
