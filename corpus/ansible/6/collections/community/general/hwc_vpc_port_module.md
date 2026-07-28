---
collection: ansible
version: "6"
title: "community.general.hwc_vpc_port module – Creates a resource of Vpc/Port in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_vpc_port_module.html
fetched_at: 2026-07-27T17:09:28+00:00
---
# community.general.hwc_vpc_port module – Creates a resource of Vpc/Port in Huawei Cloud

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
> see [Requirements](hwc_vpc_port_module.md#ansible-collections-community-general-hwc-vpc-port-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_port`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_port_module.md#synopsis)
- [Requirements](hwc_vpc_port_module.md#requirements)
- [Parameters](hwc_vpc_port_module.md#parameters)
- [Notes](hwc_vpc_port_module.md#notes)
- [Examples](hwc_vpc_port_module.md#examples)
- [Return Values](hwc_vpc_port_module.md#return-values)

## [Synopsis](hwc_vpc_port_module.md#id1)

- vpc port management.

## [Requirements](hwc_vpc_port_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state_up**  boolean | Specifies the administrative state of the port.  Choices:   - `false` - `true` |
| **allowed_address_pairs**  list / elements=dictionary | Specifies a set of zero or more allowed address pairs. |
| **ip_address**  string | Specifies the IP address. It cannot set it to 0.0.0.0. Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter allowed_address_pairs. |
| **mac_address**  string | Specifies the MAC address. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **extra_dhcp_opts**  list / elements=dictionary | Specifies the extended option of DHCP. |
| **name**  string | Specifies the option name. |
| **value**  string | Specifies the option value. |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **ip_address**  string | Specifies the port IP address. |
| **name**  string | Specifies the port name. The value can contain no more than 255 characters. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **security_groups**  list / elements=string | Specifies the ID of the security group. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string / required | Specifies the ID of the subnet to which the port belongs. |
| **timeouts**  dictionary | The timeouts for each operations.  Default: `{}` |
| **create**  string | The timeouts for create operation.  Default: `"15m"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Notes](hwc_vpc_port_module.md#id4)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_port_module.md#id5)

```yaml+jinja
# create a port
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
- name: Create a port
  community.general.hwc_vpc_port:
    subnet_id: "{{ subnet.id }}"
    ip_address: "192.168.100.33"
```

## [Return Values](hwc_vpc_port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **admin_state_up**  boolean | Specifies the administrative state of the port.  Returned: success |
| **allowed_address_pairs**  list / elements=string | Specifies a set of zero or more allowed address pairs.  Returned: success |
| **ip_address**  string | Specifies the IP address. It cannot set it to 0.0.0.0. Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter allowed_address_pairs.  Returned: success |
| **mac_address**  string | Specifies the MAC address.  Returned: success |
| **extra_dhcp_opts**  list / elements=string | Specifies the extended option of DHCP.  Returned: success |
| **name**  string | Specifies the option name.  Returned: success |
| **value**  string | Specifies the option value.  Returned: success |
| **ip_address**  string | Specifies the port IP address.  Returned: success |
| **mac_address**  string | Specifies the port MAC address.  Returned: success |
| **name**  string | Specifies the port name. The value can contain no more than 255 characters.  Returned: success |
| **security_groups**  list / elements=string | Specifies the ID of the security group.  Returned: success |
| **subnet_id**  string | Specifies the ID of the subnet to which the port belongs.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
