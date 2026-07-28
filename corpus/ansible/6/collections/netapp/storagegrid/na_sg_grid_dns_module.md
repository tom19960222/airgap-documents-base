---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_grid_dns module – NetApp StorageGRID manage external DNS servers for the grid."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_grid_dns_module.html
fetched_at: 2026-07-28T00:13:37+00:00
---
# netapp.storagegrid.na_sg_grid_dns module – NetApp StorageGRID manage external DNS servers for the grid.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/netapp/storagegrid) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_dns`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_grid_dns_module.md#synopsis)
- [Parameters](na_sg_grid_dns_module.md#parameters)
- [Notes](na_sg_grid_dns_module.md#notes)
- [Examples](na_sg_grid_dns_module.md#examples)
- [Return Values](na_sg_grid_dns_module.md#return-values)

## [Synopsis](na_sg_grid_dns_module.md#id1)

- Update NetApp StorageGRID DNS addresses.

## [Parameters](na_sg_grid_dns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **dns_servers**  list / elements=string / required | List of comma separated DNS Addresses to be updated or delete. |
| **state**  string | Whether the specified DNS address should exist or not.  Required for all operations.  Choices:   - `"present"` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_dns_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_dns_module.md#id4)

```yaml+jinja
- name: update DNS servers on StorageGRID
  netapp.storagegrid.na_sg_grid_dns:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    dns_servers: "x.x.x.x,xxx.xxx.xxx.xxx"
```

## [Return Values](na_sg_grid_dns_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  list / elements=string | Returns information about the configured DNS servers.  Returned: success  Sample: `["8.8.8.8", "8.8.4.4"]` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
