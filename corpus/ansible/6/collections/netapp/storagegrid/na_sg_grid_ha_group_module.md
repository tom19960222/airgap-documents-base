---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_grid_ha_group module – Manage high availability (HA) group configuration on StorageGRID."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_grid_ha_group_module.html
fetched_at: 2026-07-28T00:13:39+00:00
---
# netapp.storagegrid.na_sg_grid_ha_group module – Manage high availability (HA) group configuration on StorageGRID.

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
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_ha_group`.

New in netapp.storagegrid 21.10.0

- [Synopsis](na_sg_grid_ha_group_module.md#synopsis)
- [Parameters](na_sg_grid_ha_group_module.md#parameters)
- [Notes](na_sg_grid_ha_group_module.md#notes)
- [Examples](na_sg_grid_ha_group_module.md#examples)
- [Return Values](na_sg_grid_ha_group_module.md#return-values)

## [Synopsis](na_sg_grid_ha_group_module.md#id1)

- Create, Update, Delete HA Groups on NetApp StorageGRID.

## [Parameters](na_sg_grid_ha_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **description**  string | Description of the HA Group. |
| **gateway_cidr**  string | CIDR for the gateway IP and VIP subnet. |
| **ha_group_id**  string | HA Group ID.  May be used for modify or delete operation. |
| **interfaces**  list / elements=dictionary | A set of StorageGRID node interface pairs.  The primary interface is specified first, followed by the other interface pairs in failover order. |
| **interface**  string | The interface to bind to. eth0 corresponds to the Grid Network, eth1 to the Admin Network, and eth2 to the Client Network. |
| **node**  string | Name of the StorageGRID node. |
| **name**  string | Name of the HA Group. |
| **state**  string | Whether the specified HA Group should exist.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **virtual_ips**  list / elements=string | A list of virtual IP addresses. |

## [Notes](na_sg_grid_ha_group_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_ha_group_module.md#id4)

```yaml+jinja
- name: create HA Group
  netapp.storagegrid.na_sg_grid_ha_group:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: Site1-HA-Group
    description: "Site 1 HA Group"
    gateway_cidr: 192.168.50.1/24
    virtual_ips: 192.168.50.5
    interfaces:
      - node: SITE1-ADM1
        interface: eth2
      - node: SITE1-G1
        interface: eth2

- name: add VIP to HA Group
  netapp.storagegrid.na_sg_grid_ha_group:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: Site1-HA-Group
    description: "Site 1 HA Group"
    gateway_cidr: 192.168.50.1/24
    virtual_ips: 192.168.50.5,192.168.50.6
    interfaces:
      - node: SITE1-ADM1
        interface: eth2
      - node: SITE1-G1
        interface: eth2

- name: rename HA Group
  netapp.storagegrid.na_sg_grid_ha_group:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    ha_group_id: 00000000-0000-0000-0000-000000000000
    name: Site1-HA-Group-New-Name
    description: "Site 1 HA Group"
    gateway_cidr: 192.168.50.1/24
    virtual_ips: 192.168.50.5
    interfaces:
      - node: SITE1-ADM1
        interface: eth2
      - node: SITE1-G1
        interface: eth2

- name: delete HA Group
  netapp.storagegrid.na_sg_grid_ha_group:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: absent
    name: Site1-HA-Group
```

## [Return Values](na_sg_grid_ha_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID HA Group.  Returned: success  Sample: `{"description": "Site 1 HA Group", "gatewayCidr": "192.168.50.1/24", "id": "bb386f30-805d-4fec-a2c5-85790b460db0", "interfaces": [{"interface": "eth2", "nodeId": "0b1866ed-d6e7-41b4-815f-bf867348b76b"}, {"interface": "eth2", "nodeId": "7bb5bf05-a04c-4344-8abd-08c5c4048666"}], "name": "Site1-HA-Group", "virtualIps": ["192.168.50.5", "192.168.50.6"]}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
