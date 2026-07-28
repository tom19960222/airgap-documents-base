---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_grid_ntp module – NetApp StorageGRID manage external NTP servers for the grid."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_grid_ntp_module.html
fetched_at: 2026-07-28T02:43:53+00:00
---
# netapp.storagegrid.na_sg_grid_ntp module – NetApp StorageGRID manage external NTP servers for the grid.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/ui/repo/published/netapp/storagegrid/) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_ntp`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_grid_ntp_module.md#synopsis)
- [Parameters](na_sg_grid_ntp_module.md#parameters)
- [Notes](na_sg_grid_ntp_module.md#notes)
- [Examples](na_sg_grid_ntp_module.md#examples)
- [Return Values](na_sg_grid_ntp_module.md#return-values)

## [Synopsis](na_sg_grid_ntp_module.md#id1)

- Update NTP server on NetApp StorageGRID.

## [Parameters](na_sg_grid_ntp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **ntp_servers**  list / elements=string / required | List of comma separated NTP server address. |
| **passphrase**  string / required | passphrase for GRID. |
| **state**  string | Whether the specified user should exist or not.  **Choices:**   - `"present"` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_ntp_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_ntp_module.md#id4)

```yaml+jinja
- name: update NTP servers
  netapp.storagegrid.na_sg_grid_ntp:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    passphrase: "{{ grid_pass }}"
    ntp_servers: "x.x.x.x,xx.x.xx.x"
```

## [Return Values](na_sg_grid_ntp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  list / elements=string | Returns information about the configured NTP servers.  **Returned:** success  **Sample:** `["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]` |

### Authors

- NetApp Ansible Team (@jkandati)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
