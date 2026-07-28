---
collection: ansible
version: "6"
title: "community.general.hwc_vpc_route module – Creates a resource of Vpc/Route in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_vpc_route_module.html
fetched_at: 2026-07-27T17:09:30+00:00
---
# community.general.hwc_vpc_route module – Creates a resource of Vpc/Route in Huawei Cloud

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
> see [Requirements](hwc_vpc_route_module.md#ansible-collections-community-general-hwc-vpc-route-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_vpc_route`.

New in community.general 0.2.0

- [Synopsis](hwc_vpc_route_module.md#synopsis)
- [Requirements](hwc_vpc_route_module.md#requirements)
- [Parameters](hwc_vpc_route_module.md#parameters)
- [Notes](hwc_vpc_route_module.md#notes)
- [Examples](hwc_vpc_route_module.md#examples)
- [Return Values](hwc_vpc_route_module.md#return-values)

## [Synopsis](hwc_vpc_route_module.md#id1)

- vpc route management.

## [Requirements](hwc_vpc_route_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_vpc_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **destination**  string / required | Specifies the destination IP address or CIDR block. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **next_hop**  string / required | Specifies the next hop. The value is VPC peering connection ID. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | Specifies the type of route.  Default: `"peering"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |
| **vpc_id**  string / required | Specifies the VPC ID to which route is added. |

## [Notes](hwc_vpc_route_module.md#id4)

> **Note:**
>
> - If *id* option is provided, it takes precedence over *destination*, *vpc_id*, *type* and *next_hop* for route selection.
> - *destination*, *vpc_id*, *type* and *next_hop* are used for route selection. If more than one route with this options exists, execution is aborted.
> - No parameter support updating. If one of option is changed, the module will create a new resource.
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_vpc_route_module.md#id5)

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
  hwc_vpc_peering_connect:
    local_vpc_id: "{{ vpc1.id }}"
    name: "ansible_network_peering_test"
    filters:
      - "name"
    peering_vpc:
      vpc_id: "{{ vpc2.id }}"
  register: connect
- name: Create a route
  community.general.hwc_vpc_route:
    vpc_id: "{{ vpc1.id }}"
    destination: "192.168.0.0/16"
    next_hop: "{{ connect.id }}"
```

## [Return Values](hwc_vpc_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **destination**  string | Specifies the destination IP address or CIDR block.  Returned: success |
| **id**  string | UUID of the route.  Returned: success |
| **next_hop**  string | Specifies the next hop. The value is VPC peering connection ID.  Returned: success |
| **type**  string | Specifies the type of route.  Returned: success |
| **vpc_id**  string | Specifies the VPC ID to which route is added.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
