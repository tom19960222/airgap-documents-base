---
collection: ansible
version: "6"
title: "community.general.hwc_vpc_private_ip module – Creates a resource of Vpc/PrivateIP in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_vpc_private_ip_module.html
fetched_at: 2026-07-27T17:09:29+00:00
---
# community.general.hwc_vpc_private_ip module – Creates a resource of Vpc/PrivateIP in Huawei Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](hwc_vpc_private_ip_module.md#ansible-collections-community-general-hwc-vpc-private-ip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_private_ip`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_private_ip_module.md#synopsis)
- [Requirements](hwc_vpc_private_ip_module.md#requirements)
- [Parameters](hwc_vpc_private_ip_module.md#parameters)
- [Notes](hwc_vpc_private_ip_module.md#notes)
- [Examples](hwc_vpc_private_ip_module.md#examples)
- [Return Values](hwc_vpc_private_ip_module.md#return-values)

## [Synopsis](hwc_vpc_private_ip_module.md#id1)

- vpc private ip management.

## [Requirements](hwc_vpc_private_ip_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_private_ip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **ip_address**  string | Specifies the target IP address. The value can be an available IP address in the subnet. If it is not specified, the system automatically assigns an IP address. Cannot be changed after creating the private ip. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string / required | Specifies the ID of the subnet from which IP addresses are assigned. Cannot be changed after creating the private ip. |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Notes](hwc_vpc_private_ip_module.md#id4)

> **Note:**
>
> - If *id* option is provided, it takes precedence over *subnet_id*, *ip_address* for private ip selection.
> - *subnet_id*, *ip_address* are used for private ip selection. If more than one private ip with this options exists, execution is aborted.
> - No parameter support updating. If one of option is changed, the module will create a new resource.
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_private_ip_module.md#id5)

```yaml+jinja
# create a private ip
- name: Create vpc
  hwc_network_vpc:
    cidr: "192.168.100.0/24"
    name: "ansible_network_vpc_test"
  register: vpc
- name: Create subnet
  hwc_vpc_subnet:
    gateway_ip: "192.168.100.32"
    name: "ansible_network_subnet_test"
    dhcp_enable: true
    vpc_id: "{{ vpc.id }}"
    cidr: "192.168.100.0/26"
  register: subnet
- name: Create a private ip
  community.general.hwc_vpc_private_ip:
    subnet_id: "{{ subnet.id }}"
    ip_address: "192.168.100.33"
```

## [Return Values](hwc_vpc_private_ip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ip_address**  string | Specifies the target IP address. The value can be an available IP address in the subnet. If it is not specified, the system automatically assigns an IP address.  Returned: success |
| **subnet_id**  string | Specifies the ID of the subnet from which IP addresses are assigned.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
