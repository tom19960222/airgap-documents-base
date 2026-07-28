---
collection: ansible
version: "6"
title: "community.general.hwc_vpc_subnet module – Creates a resource of Vpc/Subnet in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_vpc_subnet_module.html
fetched_at: 2026-07-27T17:09:33+00:00
---
# community.general.hwc_vpc_subnet module – Creates a resource of Vpc/Subnet in Huawei Cloud

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
> see [Requirements](hwc_vpc_subnet_module.md#ansible-collections-community-general-hwc-vpc-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_subnet`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_subnet_module.md#synopsis)
- [Requirements](hwc_vpc_subnet_module.md#requirements)
- [Parameters](hwc_vpc_subnet_module.md#parameters)
- [Notes](hwc_vpc_subnet_module.md#notes)
- [Examples](hwc_vpc_subnet_module.md#examples)
- [Return Values](hwc_vpc_subnet_module.md#return-values)

## [Synopsis](hwc_vpc_subnet_module.md#id1)

- subnet management.

## [Requirements](hwc_vpc_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **availability_zone**  string | Specifies the AZ to which the subnet belongs. Cannot be changed after creating the subnet. |
| **cidr**  string / required | Specifies the subnet CIDR block. The value must be within the VPC CIDR block and be in CIDR format. The subnet mask cannot be greater than 28. Cannot be changed after creating the subnet. |
| **dhcp_enable**  boolean | Specifies whether DHCP is enabled for the subnet. The value can be true (enabled) or false(disabled), and default value is true. If this parameter is set to false, newly created ECSs cannot obtain IP addresses, and usernames and passwords cannot be injected using Cloud-init.  Choices:   - `false` - `true` |
| **dns_address**  list / elements=string | Specifies the DNS server addresses for subnet. The address in the head will be used first. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **gateway_ip**  string / required | Specifies the gateway of the subnet. The value must be an IP address in the subnet. Cannot be changed after creating the subnet. |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **name**  string / required | Specifies the subnet name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores `_`, hyphens (-), and periods (.). |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeouts**  dictionary | The timeouts for each operations.  Default: `{}` |
| **create**  string | The timeouts for create operation.  Default: `"15m"` |
| **update**  string | The timeouts for update operation.  Default: `"15m"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |
| **vpc_id**  string / required | Specifies the ID of the VPC to which the subnet belongs. Cannot be changed after creating the subnet. |

## [Notes](hwc_vpc_subnet_module.md#id4)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_subnet_module.md#id5)

```yaml+jinja
# create subnet
- name: Create vpc
  hwc_network_vpc:
    cidr: "192.168.100.0/24"
    name: "ansible_network_vpc_test"
  register: vpc
- name: Create subnet
  community.general.hwc_vpc_subnet:
    vpc_id: "{{ vpc.id }}"
    cidr: "192.168.100.0/26"
    gateway_ip: "192.168.100.32"
    name: "ansible_network_subnet_test"
    dhcp_enable: true
```

## [Return Values](hwc_vpc_subnet_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **availability_zone**  string | Specifies the AZ to which the subnet belongs.  Returned: success |
| **cidr**  string | Specifies the subnet CIDR block. The value must be within the VPC CIDR block and be in CIDR format. The subnet mask cannot be greater than 28.  Returned: success |
| **dhcp_enable**  boolean | Specifies whether DHCP is enabled for the subnet. The value can be true (enabled) or false(disabled), and default value is true. If this parameter is set to false, newly created ECSs cannot obtain IP addresses, and usernames and passwords cannot be injected using Cloud-init.  Returned: success |
| **dns_address**  list / elements=string | Specifies the DNS server addresses for subnet. The address in the head will be used first.  Returned: success |
| **gateway_ip**  string | Specifies the gateway of the subnet. The value must be an IP address in the subnet.  Returned: success |
| **name**  string | Specifies the subnet name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores `_`, hyphens (-), and periods (.).  Returned: success |
| **vpc_id**  string | Specifies the ID of the VPC to which the subnet belongs.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
