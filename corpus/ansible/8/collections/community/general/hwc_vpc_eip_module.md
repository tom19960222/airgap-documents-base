---
collection: ansible
version: "8"
title: "community.general.hwc_vpc_eip module – Creates a resource of Vpc/EIP in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hwc_vpc_eip_module.html
fetched_at: 2026-07-28T01:46:10+00:00
---
# community.general.hwc_vpc_eip module – Creates a resource of Vpc/EIP in Huawei Cloud

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
> see [Requirements](hwc_vpc_eip_module.md#ansible-collections-community-general-hwc-vpc-eip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_eip`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_eip_module.md#synopsis)
- [Requirements](hwc_vpc_eip_module.md#requirements)
- [Parameters](hwc_vpc_eip_module.md#parameters)
- [Attributes](hwc_vpc_eip_module.md#attributes)
- [Notes](hwc_vpc_eip_module.md#notes)
- [Examples](hwc_vpc_eip_module.md#examples)
- [Return Values](hwc_vpc_eip_module.md#return-values)

## [Synopsis](hwc_vpc_eip_module.md#id1)

- elastic ip management.

Aliases: cloud.huawei.hwc_vpc_eip

## [Requirements](hwc_vpc_eip_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_eip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dedicated_bandwidth**  dictionary | Specifies the dedicated bandwidth object. |
| **charge_mode**  string / required | Specifies whether the bandwidth is billed by traffic or by bandwidth size. The value can be bandwidth or traffic. If this parameter is left blank or is null character string, default value bandwidth is used. For IPv6 addresses, the default parameter value is bandwidth outside China and is traffic in China. |
| **name**  string / required | Specifies the bandwidth name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores (`_`), hyphens (`-`), and periods (`.`). |
| **size**  integer / required | Specifies the bandwidth size. The value ranges from 1 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.) The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows.  The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).  The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).  The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **enterprise_project_id**  string | Specifies the enterprise project ID. |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **ip_version**  integer | The value can be 4 (IPv4 address) or 6 (IPv6 address). If this parameter is left blank, an IPv4 address will be assigned. |
| **ipv4_address**  string | Specifies the obtained IPv4 EIP. The system automatically assigns an EIP if you do not specify it. |
| **password**  string / required | The password to login with. |
| **port_id**  string | Specifies the port ID. This parameter is returned only when a private IP address is bound with the EIP. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **shared_bandwidth_id**  string | Specifies the ID of shared bandwidth. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeouts**  dictionary | The timeouts for each operations.  **Default:** `{}` |
| **create**  string | The timeouts for create operation.  **Default:** `"5m"` |
| **update**  string | The timeouts for update operation.  **Default:** `"5m"` |
| **type**  string / required | Specifies the EIP type. |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Attributes](hwc_vpc_eip_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](hwc_vpc_eip_module.md#id5)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_eip_module.md#id6)

```yaml+jinja
# create an eip and bind it to a port
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
  hwc_vpc_port:
    subnet_id: "{{ subnet.id }}"
    ip_address: "192.168.100.33"
  register: port
- name: Create an eip and bind it to a port
  community.general.hwc_vpc_eip:
    type: "5_bgp"
    dedicated_bandwidth:
      charge_mode: "traffic"
      name: "ansible_test_dedicated_bandwidth"
      size: 1
    port_id: "{{ port.id }}"
```

## [Return Values](hwc_vpc_eip_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **create_time**  string | Specifies the time (UTC time) when the EIP was assigned.  **Returned:** success |
| **dedicated_bandwidth**  dictionary | Specifies the dedicated bandwidth object.  **Returned:** success |
| **charge_mode**  string | Specifies whether the bandwidth is billed by traffic or by bandwidth size. The value can be bandwidth or traffic. If this parameter is left blank or is null character string, default value bandwidth is used. For IPv6 addresses, the default parameter value is bandwidth outside China and is traffic in China.  **Returned:** success |
| **id**  string | Specifies the ID of dedicated bandwidth.  **Returned:** success |
| **name**  string | Specifies the bandwidth name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores (`_`), hyphens (`-`), and periods (`.`).  **Returned:** success |
| **size**  integer | Specifies the bandwidth size. The value ranges from 1 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.) The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:.  The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).  The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).  The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s.  **Returned:** success |
| **enterprise_project_id**  string | Specifies the enterprise project ID.  **Returned:** success |
| **ip_version**  integer | The value can be 4 (IPv4 address) or 6 (IPv6 address). If this parameter is left blank, an IPv4 address will be assigned.  **Returned:** success |
| **ipv4_address**  string | Specifies the obtained IPv4 EIP. The system automatically assigns an EIP if you do not specify it.  **Returned:** success |
| **ipv6_address**  string | Specifies the obtained IPv6 EIP.  **Returned:** success |
| **port_id**  string | Specifies the port ID. This parameter is returned only when a private IP address is bound with the EIP.  **Returned:** success |
| **private_ip_address**  string | Specifies the private IP address bound with the EIP. This parameter is returned only when a private IP address is bound with the EIP.  **Returned:** success |
| **shared_bandwidth_id**  string | Specifies the ID of shared bandwidth.  **Returned:** success |
| **type**  string | Specifies the EIP type.  **Returned:** success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
