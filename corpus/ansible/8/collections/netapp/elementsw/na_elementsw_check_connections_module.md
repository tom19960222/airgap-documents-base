---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_check_connections module – NetApp Element Software Check connectivity to MVIP and SVIP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_check_connections_module.html
fetched_at: 2026-07-28T02:41:18+00:00
---
# netapp.elementsw.na_elementsw_check_connections module – NetApp Element Software Check connectivity to MVIP and SVIP.

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/ui/repo/published/netapp/elementsw/) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_check_connections_module.md#ansible-collections-netapp-elementsw-na-elementsw-check-connections-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_check_connections`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_check_connections_module.md#synopsis)
- [Requirements](na_elementsw_check_connections_module.md#requirements)
- [Parameters](na_elementsw_check_connections_module.md#parameters)
- [Notes](na_elementsw_check_connections_module.md#notes)
- [Examples](na_elementsw_check_connections_module.md#examples)

## [Synopsis](na_elementsw_check_connections_module.md#id1)

- Used to test the management connection to the cluster.
- The test pings the MVIP and SVIP, and executes a simple API method to verify connectivity.

## [Requirements](na_elementsw_check_connections_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_check_connections_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **mvip**  string | Optionally, use to test connection of a different MVIP.  This is not needed to test the connection to the target cluster. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **skip**  string | Skip checking connection to SVIP or MVIP.  **Choices:**   - `"svip"` - `"mvip"` |
| **svip**  string | Optionally, use to test connection of a different SVIP.  This is not needed to test the connection to the target cluster. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_check_connections_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_check_connections_module.md#id5)

```yaml+jinja
- name: Check connections to MVIP and SVIP
  na_elementsw_check_connections:
    hostname: "{{ solidfire_hostname }}"
    username: "{{ solidfire_username }}"
    password: "{{ solidfire_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
