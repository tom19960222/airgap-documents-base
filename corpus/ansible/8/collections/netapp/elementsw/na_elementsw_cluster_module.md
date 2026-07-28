---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_cluster module – NetApp Element Software Create Cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_cluster_module.html
fetched_at: 2026-07-28T02:41:18+00:00
---
# netapp.elementsw.na_elementsw_cluster module – NetApp Element Software Create Cluster

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
> see [Requirements](na_elementsw_cluster_module.md#ansible-collections-netapp-elementsw-na-elementsw-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_cluster`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_cluster_module.md#synopsis)
- [Requirements](na_elementsw_cluster_module.md#requirements)
- [Parameters](na_elementsw_cluster_module.md#parameters)
- [Notes](na_elementsw_cluster_module.md#notes)
- [Examples](na_elementsw_cluster_module.md#examples)
- [Return Values](na_elementsw_cluster_module.md#return-values)

## [Synopsis](na_elementsw_cluster_module.md#id1)

- Initialize Element Software node ownership to form a cluster.
- If the cluster does not exist, username/password are still required but ignored for initial creation.
- username/password are used as the node credentials to see if the cluster already exists.
- username/password can also be used to set the cluster credentials.
- If the cluster already exists, no error is returned, but changed is set to false.
- Cluster modifications are not supported and are ignored.

## [Requirements](na_elementsw_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_eula**  boolean | Required to indicate your acceptance of the End User License Agreement when creating this cluster.  To accept the EULA, set this parameter to true.  **Choices:**   - `false` - `true` |
| **attributes**  dictionary | List of name-value pairs in JSON object format. |
| **cluster_admin_password**  string | Initial password for the cluster admin account.  If not provided, default to password. |
| **cluster_admin_username**  string | Username for the cluster admin.  If not provided, default to username. |
| **encryption**  boolean  *added in netapp.elementsw 20.10.0* | to enable or disable encryption at rest  **Choices:**   - `false` - `true` |
| **fail_if_cluster_already_exists_with_larger_ensemble**  boolean  *added in netapp.elementsw 20.8.0* | If the cluster exists, the default is to verify that *nodes* is a superset of the existing ensemble.  A superset is accepted because some nodes may have a different role.  But the module reports an error if the existing ensemble contains a node not listed in *nodes*.  This checker is disabled when this option is set to false.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **management_virtual_ip**  string / required | Floating (virtual) IP address for the cluster on the management network. |
| **nodes**  list / elements=string / required | Storage IP (SIP) addresses of the initial set of nodes making up the cluster.  nodes IP must be in the list. |
| **order_number**  string  *added in netapp.elementsw 20.10.0* | (experimental) order number as provided by NetApp |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **replica_count**  integer | Number of replicas of each piece of data to store in the cluster.  **Default:** `2` |
| **serial_number**  string  *added in netapp.elementsw 20.10.0* | (experimental) serial number as provided by NetApp |
| **storage_virtual_ip**  string / required | Floating (virtual) IP address for the cluster on the storage (iSCSI) network. |
| **timeout**  integer  *added in netapp.elementsw 20.8.0* | Time to wait for cluster creation to complete.  **Default:** `100` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_cluster_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_cluster_module.md#id5)

```yaml+jinja
- name: Initialize new cluster
  tags:
  - elementsw_cluster
  na_elementsw_cluster:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    management_virtual_ip: 10.226.108.32
    storage_virtual_ip: 10.226.109.68
    replica_count: 2
    accept_eula: true
    nodes:
    - 10.226.109.72
    - 10.226.109.74
```

## [Return Values](na_elementsw_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
