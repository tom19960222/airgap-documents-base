---
collection: ansible
version: "8"
title: "community.general.hwc_network_vpc module – Creates a Huawei Cloud VPC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hwc_network_vpc_module.html
fetched_at: 2026-07-28T01:46:09+00:00
---
# community.general.hwc_network_vpc module – Creates a Huawei Cloud VPC

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
> see [Requirements](hwc_network_vpc_module.md#ansible-collections-community-general-hwc-network-vpc-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_network_vpc`.

- [Synopsis](hwc_network_vpc_module.md#synopsis)
- [Requirements](hwc_network_vpc_module.md#requirements)
- [Parameters](hwc_network_vpc_module.md#parameters)
- [Attributes](hwc_network_vpc_module.md#attributes)
- [Notes](hwc_network_vpc_module.md#notes)
- [Examples](hwc_network_vpc_module.md#examples)
- [Return Values](hwc_network_vpc_module.md#return-values)

## [Synopsis](hwc_network_vpc_module.md#id1)

- Represents an vpc resource.

Aliases: cloud.huawei.hwc_network_vpc

## [Requirements](hwc_network_vpc_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.18.4
- keystoneauth1 >= 3.6.0

## [Parameters](hwc_network_vpc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cidr**  string / required | The range of available subnets in the vpc. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **name**  string / required | The name of vpc. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in vpc.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeouts**  dictionary | The timeouts for each operations.  **Default:** `{}` |
| **create**  string | The timeout for create operation.  **Default:** `"15m"` |
| **delete**  string | The timeout for delete operation.  **Default:** `"15m"` |
| **update**  string | The timeout for update operation.  **Default:** `"15m"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Attributes](hwc_network_vpc_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](hwc_network_vpc_module.md#id5)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_network_vpc_module.md#id6)

```yaml+jinja
- name: Create a vpc
  community.general.hwc_network_vpc:
      identity_endpoint: "{{ identity_endpoint }}"
      user: "{{ user }}"
      password: "{{ password }}"
      domain: "{{ domain }}"
      project: "{{ project }}"
      region: "{{ region }}"
      name: "vpc_1"
      cidr: "192.168.100.0/24"
      state: present
```

## [Return Values](hwc_network_vpc_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cidr**  string | the range of available subnets in the vpc.  **Returned:** success |
| **enable_shared_snat**  boolean | show whether the shared snat is enabled.  **Returned:** success |
| **id**  string | the id of vpc.  **Returned:** success |
| **name**  string | the name of vpc.  **Returned:** success |
| **routes**  complex | the route information.  **Returned:** success |
| **destination**  string | the destination network segment of a route.  **Returned:** success |
| **next_hop**  string | the next hop of a route. If the route type is peering, it will provide VPC peering connection ID.  **Returned:** success |
| **status**  string | the status of vpc.  **Returned:** success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
