---
collection: ansible
version: "8"
title: "community.general.hwc_vpc_security_group module – Creates a resource of Vpc/SecurityGroup in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hwc_vpc_security_group_module.html
fetched_at: 2026-07-28T01:46:14+00:00
---
# community.general.hwc_vpc_security_group module – Creates a resource of Vpc/SecurityGroup in Huawei Cloud

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
> see [Requirements](hwc_vpc_security_group_module.md#ansible-collections-community-general-hwc-vpc-security-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_security_group`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_security_group_module.md#synopsis)
- [Requirements](hwc_vpc_security_group_module.md#requirements)
- [Parameters](hwc_vpc_security_group_module.md#parameters)
- [Attributes](hwc_vpc_security_group_module.md#attributes)
- [Notes](hwc_vpc_security_group_module.md#notes)
- [Examples](hwc_vpc_security_group_module.md#examples)
- [Return Values](hwc_vpc_security_group_module.md#return-values)

## [Synopsis](hwc_vpc_security_group_module.md#id1)

- vpc security group management.

Aliases: cloud.huawei.hwc_vpc_security_group

## [Requirements](hwc_vpc_security_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_security_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **enterprise_project_id**  string | Specifies the enterprise project ID. When creating a security group, associate the enterprise project ID with the security group.s |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **name**  string / required | Specifies the security group name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores (`_`), hyphens (`-`), and periods (`.`). |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |
| **vpc_id**  string | Specifies the resource ID of the VPC to which the security group belongs. |

## [Attributes](hwc_vpc_security_group_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](hwc_vpc_security_group_module.md#id5)

> **Note:**
>
> - If `id` option is provided, it takes precedence over `name`, `enterprise_project_id`, and `vpc_id` for security group selection.
> - `name`, `enterprise_project_id` and `vpc_id` are used for security group selection. If more than one security group with this options exists, execution is aborted.
> - No parameter support updating. If one of option is changed, the module will create a new resource.
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_security_group_module.md#id6)

```yaml+jinja
# create a security group
- name: Create a security group
  community.general.hwc_vpc_security_group:
    name: "ansible_network_security_group_test"
```

## [Return Values](hwc_vpc_security_group_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enterprise_project_id**  string | Specifies the enterprise project ID. When creating a security group, associate the enterprise project ID with the security group.  **Returned:** success |
| **name**  string | Specifies the security group name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores (`_`), hyphens (`-`), and periods (`.`).  **Returned:** success |
| **rules**  complex | Specifies the security group rule, which ensures that resources in the security group can communicate with one another.  **Returned:** success |
| **description**  string | Provides supplementary information about the security group rule.  **Returned:** success |
| **direction**  string | Specifies the direction of access control. The value can be egress or ingress.  **Returned:** success |
| **ethertype**  string | Specifies the IP protocol version. The value can be IPv4 or IPv6.  **Returned:** success |
| **id**  string | Specifies the security group rule ID.  **Returned:** success |
| **port_range_max**  integer | Specifies the end port number. The value ranges from 1 to 65535. If the protocol is not icmp, the value cannot be smaller than the port_range_min value. An empty value indicates all ports.  **Returned:** success |
| **port_range_min**  integer | Specifies the start port number. The value ranges from 1 to 65535. The value cannot be greater than the port_range_max value. An empty value indicates all ports.  **Returned:** success |
| **protocol**  string | Specifies the protocol type. The value can be icmp, tcp, udp, or others. If the parameter is left blank, the security group supports all protocols.  **Returned:** success |
| **remote_address_group_id**  string | Specifies the ID of remote IP address group.  **Returned:** success |
| **remote_group_id**  string | Specifies the ID of the peer security group.  **Returned:** success |
| **remote_ip_prefix**  string | Specifies the remote IP address. If the access control direction is set to egress, the parameter specifies the source IP address. If the access control direction is set to ingress, the parameter specifies the destination IP address.  **Returned:** success |
| **vpc_id**  string | Specifies the resource ID of the VPC to which the security group belongs.  **Returned:** success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
