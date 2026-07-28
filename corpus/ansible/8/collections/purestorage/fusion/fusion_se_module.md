---
collection: ansible
version: "8"
title: "purestorage.fusion.fusion_se module – Manage storage endpoints in Pure Storage Fusion"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/fusion/fusion_se_module.html
fetched_at: 2026-07-28T02:52:45+00:00
---
# purestorage.fusion.fusion_se module – Manage storage endpoints in Pure Storage Fusion

> **Note:**
>
> This module is part of the [purestorage.fusion collection](https://galaxy.ansible.com/ui/repo/published/purestorage/fusion/) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.fusion`.
> You need further requirements to be able to use this module,
> see [Requirements](fusion_se_module.md#ansible-collections-purestorage-fusion-fusion-se-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.fusion.fusion_se`.

New in purestorage.fusion 1.0.0

- [Synopsis](fusion_se_module.md#synopsis)
- [Requirements](fusion_se_module.md#requirements)
- [Parameters](fusion_se_module.md#parameters)
- [Notes](fusion_se_module.md#notes)
- [Examples](fusion_se_module.md#examples)

## [Synopsis](fusion_se_module.md#id1)

- Create or delete storage endpoints in Pure Storage Fusion.

## [Requirements](fusion_se_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8
- purefusion

## [Parameters](fusion_se_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Access token for Fusion Service  Defaults to the set environment variable under FUSION_ACCESS_TOKEN |
| **addresses**  list / elements=string | DEPRECATED: Will be removed in version 2.0.0  List of IP addresses to be used in the subnet of the storage endpoint.  IP addresses must include a CIDR notation.  Only IPv4 is supported at the moment. |
| **availability_zone**  aliases: az  string / required | The name of the availability zone for the storage endpoint. |
| **cbs_azure_iscsi**  dictionary | CBS Azure iSCSI |
| **load_balancer**  string | The Load Balancer id which gives permissions to CBS array applications to modify the Load Balancer. |
| **load_balancer_addresses**  list / elements=string | The IPv4 addresses of the Load Balancer. |
| **storage_endpoint_collection_identity**  string | The Storage Endpoint Collection Identity which belongs to the Azure entities. |
| **display_name**  string | The human name of the storage endpoint.  If not provided, defaults to *name*. |
| **endpoint_type**  string | DEPRECATED: Will be removed in version 2.0.0  Type of the storage endpoint. Only iSCSI is available at the moment. |
| **gateway**  string | DEPRECATED: Will be removed in version 2.0.0  Address of the subnet gateway.  Currently this must be provided. |
| **iscsi**  list / elements=dictionary | List of discovery interfaces. |
| **address**  string | IP address to be used in the subnet of the storage endpoint.  IP address must include a CIDR notation.  Only IPv4 is supported at the moment. |
| **gateway**  string | Address of the subnet gateway. |
| **network_interface_groups**  list / elements=string | List of network interface groups to assign to the address. |
| **issuer_id**  aliases: app_id  string | Application ID from Pure1 Registration page  eg. pure1:apikey:dssf2331sd  Defaults to the set environment variable under FUSION_ISSUER_ID |
| **name**  string / required | The name of the storage endpoint. |
| **network_interface_groups**  list / elements=string | DEPRECATED: Will be removed in version 2.0.0  List of network interface groups to assign to the storage endpoints. |
| **private_key_file**  aliases: key_file  string | Path to the private key file  Defaults to the set environment variable under FUSION_PRIVATE_KEY_FILE. |
| **private_key_password**  string | Password of the encrypted private key file |
| **region**  string / required | The name of the region the availability zone is in |
| **state**  string | Define whether the storage endpoint should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](fusion_se_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.
> - This module requires the *purefusion* Python library
> - You must set `FUSION_ISSUER_ID` and `FUSION_PRIVATE_KEY_FILE` environment variables if *issuer_id* and *private_key_file* arguments are not passed to the module directly
> - If you want to use access token for authentication, you must use `FUSION_ACCESS_TOKEN` environment variable if *access_token* argument is not passed to the module directly

## [Examples](fusion_se_module.md#id5)

```yaml+jinja
- name: Create new storage endpoint foo in AZ bar
  purestorage.fusion.fusion_se:
    name: foo
    availability_zone: bar
    region: us-west
    iscsi:
      - address: 10.21.200.124/24
        gateway: 10.21.200.1
        network_interface_groups:
          - subnet-0
      - address: 10.21.200.36/24
        gateway: 10.21.200.2
        network_interface_groups:
          - subnet-0
          - subnet-1
    state: present
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: Create new CBS storage endpoint foo in AZ bar
  purestorage.fusion.fusion_se:
    name: foo
    availability_zone: bar
    region: us-west
    cbs_azure_iscsi:
      storage_endpoint_collection_identity: "/subscriptions/sub/resourcegroups/sec/providers/ms/userAssignedIdentities/secId"
      load_balancer: "/subscriptions/sub/resourcegroups/sec/providers/ms/loadBalancers/sec-lb"
      load_balancer_addresses:
        - 10.21.200.1
        - 10.21.200.2
    state: present
    app_id: key_name
    key_file: "az-admin-private-key.pem"

- name: Delete storage endpoint foo in AZ bar
  purestorage.fusion.fusion_se:
    name: foo
    availability_zone: bar
    region: us-west
    state: absent
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"

- name: (DEPRECATED) Create new storage endpoint foo in AZ bar
  purestorage.fusion.fusion_se:
    name: foo
    availability_zone: bar
    gateway: 10.21.200.1
    region: us-west
    addresses:
      - 10.21.200.124/24
      - 10.21.200.36/24
    network_interface_groups:
      - subnet-0
    state: present
    issuer_id: key_name
    private_key_file: "az-admin-private-key.pem"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/Fusion-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/Fusion-Collection)
