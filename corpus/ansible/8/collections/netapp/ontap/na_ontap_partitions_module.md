---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_partitions module – NetApp ONTAP Assign partitions and disks to nodes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_partitions_module.html
fetched_at: 2026-07-28T02:42:57+00:00
---
# netapp.ontap.na_ontap_partitions module – NetApp ONTAP Assign partitions and disks to nodes.

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_partitions_module.md#ansible-collections-netapp-ontap-na-ontap-partitions-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_partitions`.

New in netapp.ontap 21.8.0

- [Synopsis](na_ontap_partitions_module.md#synopsis)
- [Requirements](na_ontap_partitions_module.md#requirements)
- [Parameters](na_ontap_partitions_module.md#parameters)
- [Notes](na_ontap_partitions_module.md#notes)
- [Examples](na_ontap_partitions_module.md#examples)

## [Synopsis](na_ontap_partitions_module.md#id1)

- Assign the specified number of partitions or disks eligible for partitioning to a node.
- There is some overlap between this module and the na_ontap_disks module.
- If you don’t have ADP v1 or v2 then you should be using the na_ontap_disks module to assign whole disks.
- Partitions/disks are added in the following order
- 1. Any unassigned partitions are added.
- 2. Any unassigned disks of the correct type are added and will be partitioned when added to an aggregate if required.
- 3. Any spare partner partitions will be re-assigned.
- 4. Any partner spare disks will be re-assigned and be partitioned when added to an aggregate.
- If you specify a partition_count less than the current number of partitions, then spare partitions will be unassigned.
- If a previously partitioned disk has the partitions removed, and even if it is “slow zeroed” the system will consider it a shared partitioned disk rather than a spare.
- In a root-data-data configuration (ADPv2) if you specify data1 as the partition_type then only P1 partitions will be counted.
- Disk autoassign must be turned off before using this module to prevent the disks being reassigned automatically by the cluster.
- This can be done through na_ontap_disk_options or via the cli “disk option modify -node <node_name> -autoassign off”.

## [Requirements](na_ontap_partitions_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_partitions_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **disk_type**  string / required | The type of disk that the partitions that should use.  **Choices:**   - `"ATA"` - `"BSAS"` - `"FCAL"` - `"FSAS"` - `"LUN"` - `"MSATA"` - `"SAS"` - `"SSD"` - `"SSD_NVM"` - `"VMDISK"` - `"unknown"` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **min_spares**  integer | Minimum spares disks or partitions required per type for the node. |
| **node**  string / required | Specifies the node that the partitions and disks should be assigned to. |
| **ontapi**  integer | The ontap api version to use |
| **partition_count**  integer / required | Total number of partitions that should be assigned to the owner. |
| **partition_type**  string / required | The type of partiton being assigned either root, data, data1 or data2,  **Choices:**   - `"data"` - `"root"` - `"data1"` - `"data2"` |
| **partitioning_method**  string / required | The type of partiton method being used, either root_data or root_data1_data2.  **Choices:**   - `"root_data"` - `"root_data1_data2"` |
| **password**  aliases: pass  string | Password for the specified user. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_partitions_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_partitions_module.md#id5)

```yaml+jinja
- name: Assign specified total partitions to node cluster-01
  na_ontap_disk_partitions_custom:
    node: cluster-01
    partition_count: 56
    disk_type: FSAS
    partition_type: data
    hostname: "{{ hostname }}"
    username: "{{ admin username }}"
    password: "{{ admin password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
