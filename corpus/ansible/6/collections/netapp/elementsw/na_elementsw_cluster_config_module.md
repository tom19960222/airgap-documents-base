---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_cluster_config module – Configure Element SW Cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_cluster_config_module.html
fetched_at: 2026-07-28T00:11:46+00:00
---
# netapp.elementsw.na_elementsw_cluster_config module – Configure Element SW Cluster

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/netapp/elementsw) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_cluster_config_module.md#ansible-collections-netapp-elementsw-na-elementsw-cluster-config-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_cluster_config`.

New in netapp.elementsw 2.8.0

- [Synopsis](na_elementsw_cluster_config_module.md#synopsis)
- [Requirements](na_elementsw_cluster_config_module.md#requirements)
- [Parameters](na_elementsw_cluster_config_module.md#parameters)
- [Notes](na_elementsw_cluster_config_module.md#notes)
- [Examples](na_elementsw_cluster_config_module.md#examples)
- [Return Values](na_elementsw_cluster_config_module.md#return-values)

## [Synopsis](na_elementsw_cluster_config_module.md#id1)

- Configure Element Software cluster.

## [Requirements](na_elementsw_cluster_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_cluster_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enable_virtual_volumes**  boolean | Enable the NetApp SolidFire VVols cluster feature  Choices:   - `false` - `true` ← (default) |
| **encryption_at_rest**  string | enable or disable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster  Choices:   - `"present"` - `"absent"` |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **modify_cluster_full_threshold**  dictionary | The capacity level at which the cluster generates an event  Requires a stage3_block_threshold_percent or  max_metadata_over_provision_factor or  stage2_aware_threshold |
| **max_metadata_over_provision_factor**  integer | The number of times metadata space can be overprovisioned relative to the amount of space available |
| **stage2_aware_threshold**  integer | The number of nodes of capacity remaining in the cluster before the system triggers a notification |
| **stage3_block_threshold_percent**  integer | The percentage below the “Error” threshold that triggers a cluster “Warning” alert |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **set_ntp_info**  dictionary | configure NTP on cluster node  Requires a list of one or more ntp_servers |
| **broadcastclient**  boolean | Enables every node in the cluster as a broadcast client  Choices:   - `false` ← (default) - `true` |
| **ntp_servers**  list / elements=string | list of NTP servers to add to each nodes NTP configuration |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_cluster_config_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_cluster_config_module.md#id5)

```yaml+jinja
- name: Configure cluster
  tags:
  - elementsw_cluster_config
  na_elementsw_cluster_config:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    modify_cluster_full_threshold:
      stage2_aware_threshold: 2
      stage3_block_threshold_percent: 10
      max_metadata_over_provision_factor: 2
    encryption_at_rest: absent
    set_ntp_info:
      broadcastclient: False
      ntp_servers:
      - 1.1.1.1
      - 2.2.2.2
    enable_virtual_volumes: True
```

## [Return Values](na_elementsw_cluster_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
