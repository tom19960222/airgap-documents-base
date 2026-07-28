---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_node module – NetApp Element Software Node Operation"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_node_module.html
fetched_at: 2026-07-28T00:11:52+00:00
---
# netapp.elementsw.na_elementsw_node module – NetApp Element Software Node Operation

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
> see [Requirements](na_elementsw_node_module.md#ansible-collections-netapp-elementsw-na-elementsw-node-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_node`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_node_module.md#synopsis)
- [Requirements](na_elementsw_node_module.md#requirements)
- [Parameters](na_elementsw_node_module.md#parameters)
- [Notes](na_elementsw_node_module.md#notes)
- [Examples](na_elementsw_node_module.md#examples)
- [Return Values](na_elementsw_node_module.md#return-values)

## [Synopsis](na_elementsw_node_module.md#id1)

- Add, remove cluster node on Element Software Cluster.
- Set cluster name on node.
- When using the preset_only option, hostname/username/password are required but not used.

## [Requirements](na_elementsw_node_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_node_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string  added in netapp.elementsw 20.9.0 | If set, the current node configuration is updated with this name before adding the node to the cluster.  This requires the node_ids to be specified as MIPs (Management IP Adresses) |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **node_ids**  aliases: node_id  list / elements=string / required | List of IDs or Names or IP Addresses of nodes to add or remove.  If cluster_name is set, node MIPs are required. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **preset_only**  boolean  added in netapp.elementsw 20.9.0 | If true and state is ‘present’, set the cluster name for each node in node_ids, but do not add the nodes.  They can be added using na_elementsw_cluster for initial cluster creation.  If false, proceed with addition/removal.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Element Software Storage Node operation state.  present - To add pending node to participate in cluster data storage.  absent - To remove node from active cluster. A node cannot be removed if active drives are present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_node_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_node_module.md#id5)

```yaml+jinja
- name: Add node from pending to active cluster
  tags:
  - elementsw_add_node
  na_elementsw_node:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    node_id: sf4805-meg-03

- name: Remove active node from cluster
  tags:
  - elementsw_remove_node
  na_elementsw_node:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    node_id: 13

- name: Add node from pending to active cluster using node IP
  tags:
  - elementsw_add_node_ip
  na_elementsw_node:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    node_id: 10.109.48.65
    cluster_name: sfcluster01

- name: Only set cluster name
  tags:
  - elementsw_add_node_ip
  na_elementsw_node:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    node_ids: 10.109.48.65,10.109.48.66
    cluster_name: sfcluster01
    preset_only: true
```

## [Return Values](na_elementsw_node_module.md#id6)

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
