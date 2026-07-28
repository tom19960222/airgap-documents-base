---
collection: ansible
version: "8"
title: "community.general.hwc_vpc_peering_connect module – Creates a resource of Vpc/PeeringConnect in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hwc_vpc_peering_connect_module.html
fetched_at: 2026-07-28T01:46:11+00:00
---
# community.general.hwc_vpc_peering_connect module – Creates a resource of Vpc/PeeringConnect in Huawei Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](hwc_vpc_peering_connect_module.md#ansible-collections-community-general-hwc-vpc-peering-connect-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_peering_connect`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_peering_connect_module.md#synopsis)
- [Requirements](hwc_vpc_peering_connect_module.md#requirements)
- [Parameters](hwc_vpc_peering_connect_module.md#parameters)
- [Attributes](hwc_vpc_peering_connect_module.md#attributes)
- [Notes](hwc_vpc_peering_connect_module.md#notes)
- [Examples](hwc_vpc_peering_connect_module.md#examples)
- [Return Values](hwc_vpc_peering_connect_module.md#return-values)

## [Synopsis](hwc_vpc_peering_connect_module.md#id1)

- vpc peering management.

Aliases: cloud.huawei.hwc_vpc_peering_connect

## [Requirements](hwc_vpc_peering_connect_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_peering_connect_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description of vpc peering connection. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **local_vpc_id**  string / required | Specifies the ID of local VPC. |
| **name**  string / required | Specifies the name of the VPC peering connection. The value can contain 1 to 64 characters. |
| **password**  string / required | The password to login with. |
| **peering_vpc**  dictionary / required | Specifies information about the peering VPC. |
| **project_id**  string | Specifies the ID of the project which the peering vpc belongs to. |
| **vpc_id**  string / required | Specifies the ID of peering VPC. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeouts**  dictionary | The timeouts for each operations.  **Default:** `{}` |
| **create**  string | The timeouts for create operation.  **Default:** `"15m"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Attributes](hwc_vpc_peering_connect_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](hwc_vpc_peering_connect_module.md#id5)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_peering_connect_module.md#id6)

```yaml+jinja
# create a peering connect
- name: Create a local vpc
  hwc_network_vpc:
    cidr: "192.168.0.0/16"
    name: "ansible_network_vpc_test_local"
  register: vpc1
- name: Create a peering vpc
  hwc_network_vpc:
    cidr: "192.168.0.0/16"
    name: "ansible_network_vpc_test_peering"
  register: vpc2
- name: Create a peering connect
  community.general.hwc_vpc_peering_connect:
    local_vpc_id: "{{ vpc1.id }}"
    name: "ansible_network_peering_test"
    peering_vpc:
      vpc_id: "{{ vpc2.id }}"
```

## [Return Values](hwc_vpc_peering_connect_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description of vpc peering connection.  **Returned:** success |
| **local_vpc_id**  string | Specifies the ID of local VPC.  **Returned:** success |
| **name**  string | Specifies the name of the VPC peering connection. The value can contain 1 to 64 characters.  **Returned:** success |
| **peering_vpc**  dictionary | Specifies information about the peering VPC.  **Returned:** success |
| **project_id**  string | Specifies the ID of the project which the peering vpc belongs to.  **Returned:** success |
| **vpc_id**  string | Specifies the ID of peering VPC.  **Returned:** success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
