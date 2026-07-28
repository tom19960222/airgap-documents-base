---
collection: ansible
version: "6"
title: "community.general.hwc_vpc_security_group_rule module – Creates a resource of Vpc/SecurityGroupRule in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_vpc_security_group_rule_module.html
fetched_at: 2026-07-27T17:09:32+00:00
---
# community.general.hwc_vpc_security_group_rule module – Creates a resource of Vpc/SecurityGroupRule in Huawei Cloud

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
> see [Requirements](hwc_vpc_security_group_rule_module.md#ansible-collections-community-general-hwc-vpc-security-group-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_security_group_rule`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_security_group_rule_module.md#synopsis)
- [Requirements](hwc_vpc_security_group_rule_module.md#requirements)
- [Parameters](hwc_vpc_security_group_rule_module.md#parameters)
- [Notes](hwc_vpc_security_group_rule_module.md#notes)
- [Examples](hwc_vpc_security_group_rule_module.md#examples)
- [Return Values](hwc_vpc_security_group_rule_module.md#return-values)

## [Synopsis](hwc_vpc_security_group_rule_module.md#id1)

- vpc security group management.

## [Requirements](hwc_vpc_security_group_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_security_group_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Provides supplementary information about the security group rule. The value is a string of no more than 255 characters that can contain letters and digits. |
| **direction**  string / required | Specifies the direction of access control. The value can be egress or ingress. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **ethertype**  string | Specifies the IP protocol version. The value can be IPv4 or IPv6. If you do not set this parameter, IPv4 is used by default. |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **password**  string / required | The password to login with. |
| **port_range_max**  integer | Specifies the end port number. The value ranges from 1 to 65535. If the protocol is not icmp, the value cannot be smaller than the port_range_min value. An empty value indicates all ports. |
| **port_range_min**  integer | Specifies the start port number. The value ranges from 1 to 65535. The value cannot be greater than the port_range_max value. An empty value indicates all ports. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **protocol**  string | Specifies the protocol type. The value can be icmp, tcp, or udp. If the parameter is left blank, the security group supports all protocols. |
| **region**  string | The region to which the project belongs. |
| **remote_group_id**  string | Specifies the ID of the peer security group. The value is exclusive with parameter remote_ip_prefix. |
| **remote_ip_prefix**  string | Specifies the remote IP address. If the access control direction is set to egress, the parameter specifies the source IP address. If the access control direction is set to ingress, the parameter specifies the destination IP address. The value can be in the CIDR format or IP addresses. The parameter is exclusive with parameter remote_group_id. |
| **security_group_id**  string / required | Specifies the security group rule ID, which uniquely identifies the security group rule. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |

## [Notes](hwc_vpc_security_group_rule_module.md#id4)

> **Note:**
>
> - If *id* option is provided, it takes precedence over *enterprise_project_id* for security group rule selection.
> - *security_group_id* is used for security group rule selection. If more than one security group rule with this options exists, execution is aborted.
> - No parameter support updating. If one of option is changed, the module will create a new resource.
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_security_group_rule_module.md#id5)

```yaml+jinja
# create a security group rule
- name: Create a security group
  hwc_vpc_security_group:
    name: "ansible_network_security_group_test"
  register: sg
- name: Create a security group rule
  community.general.hwc_vpc_security_group_rule:
    direction: "ingress"
    protocol: "tcp"
    ethertype: "IPv4"
    port_range_max: 22
    security_group_id: "{{ sg.id }}"
    port_range_min: 22
    remote_ip_prefix: "0.0.0.0/0"
```

## [Return Values](hwc_vpc_security_group_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Provides supplementary information about the security group rule. The value is a string of no more than 255 characters that can contain letters and digits.  Returned: success |
| **direction**  string | Specifies the direction of access control. The value can be egress or ingress.  Returned: success |
| **ethertype**  string | Specifies the IP protocol version. The value can be IPv4 or IPv6. If you do not set this parameter, IPv4 is used by default.  Returned: success |
| **port_range_max**  integer | Specifies the end port number. The value ranges from 1 to 65535. If the protocol is not icmp, the value cannot be smaller than the port_range_min value. An empty value indicates all ports.  Returned: success |
| **port_range_min**  integer | Specifies the start port number. The value ranges from 1 to 65535. The value cannot be greater than the port_range_max value. An empty value indicates all ports.  Returned: success |
| **protocol**  string | Specifies the protocol type. The value can be icmp, tcp, or udp. If the parameter is left blank, the security group supports all protocols.  Returned: success |
| **remote_group_id**  string | Specifies the ID of the peer security group. The value is exclusive with parameter remote_ip_prefix.  Returned: success |
| **remote_ip_prefix**  string | Specifies the remote IP address. If the access control direction is set to egress, the parameter specifies the source IP address. If the access control direction is set to ingress, the parameter specifies the destination IP address. The value can be in the CIDR format or IP addresses. The parameter is exclusive with parameter remote_group_id.  Returned: success |
| **security_group_id**  string | Specifies the security group rule ID, which uniquely identifies the security group rule.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
