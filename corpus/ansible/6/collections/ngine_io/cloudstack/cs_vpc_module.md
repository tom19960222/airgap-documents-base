---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_vpc module – Manages VPCs on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_vpc_module.html
fetched_at: 2026-07-28T00:15:54+00:00
---
# ngine_io.cloudstack.cs_vpc module – Manages VPCs on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_vpc_module.md#ansible-collections-ngine-io-cloudstack-cs-vpc-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_vpc`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_vpc_module.md#synopsis)
- [Requirements](cs_vpc_module.md#requirements)
- [Parameters](cs_vpc_module.md#parameters)
- [Notes](cs_vpc_module.md#notes)
- [Examples](cs_vpc_module.md#examples)
- [Return Values](cs_vpc_module.md#return-values)

## [Synopsis](cs_vpc_module.md#id1)

- Create, update and delete VPCs.

## [Requirements](cs_vpc_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_vpc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the VPC is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cidr**  string | CIDR of the VPC, e.g. 10.1.0.0/16  All VPC guest networks’ CIDRs must be within this CIDR.  Required on *state=present*. |
| **clean_up**  boolean | Whether to redeploy a VPC router or not when *state=restarted*  Choices:   - `false` - `true` |
| **display_text**  string | Display text of the VPC.  If not set, *name* will be used for creating. |
| **domain**  string | Domain the VPC is related to. |
| **name**  string / required | Name of the VPC. |
| **network_domain**  string | Network domain for the VPC.  All networks inside the VPC will belong to this domain.  Only considered while creating the VPC, can not be changed. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the VPC is related to. |
| **state**  string | State of the VPC.  The state `present` creates a started VPC.  The state `stopped` is only considered while creating the VPC, added in version 2.6.  Choices:   - `"present"` ← (default) - `"absent"` - `"stopped"` - `"restarted"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  For deleting all tags, set an empty list e.g. *tags: []*. |
| **vpc_offering**  string | Name of the VPC offering.  If not set, default VPC offering is used. |
| **zone**  string / required | Name of the zone. |

## [Notes](cs_vpc_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_vpc_module.md#id5)

```yaml+jinja
- name: Ensure a VPC is present but not started after creating
  ngine_io.cloudstack.cs_vpc:
    name: my_vpc
    zone: zone01
    display_text: My example VPC
    cidr: 10.10.0.0/16
    state: stopped

- name: Ensure a VPC is present and started after creating
  ngine_io.cloudstack.cs_vpc:
    name: my_vpc
    zone: zone01
    display_text: My example VPC
    cidr: 10.10.0.0/16

- name: Ensure a VPC is absent
  ngine_io.cloudstack.cs_vpc:
    name: my_vpc
    zone: zone01
    state: absent

- name: Ensure a VPC is restarted with clean up
  ngine_io.cloudstack.cs_vpc:
    name: my_vpc
    zone: zone01
    clean_up: yes
    state: restarted
```

## [Return Values](cs_vpc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the VPC is related to.  Returned: success  Sample: `"example account"` |
| **cidr**  string | CIDR of the VPC.  Returned: success  Sample: `"10.10.0.0/16"` |
| **display_text**  string | Display text of the VPC.  Returned: success  Sample: `"My example VPC"` |
| **distributed_vpc_router**  boolean | Whether the VPC uses distributed router or not.  Returned: success  Sample: `true` |
| **domain**  string | Domain the VPC is related to.  Returned: success  Sample: `"example domain"` |
| **id**  string | UUID of the VPC.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **name**  string | Name of the VPC.  Returned: success  Sample: `"my_vpc"` |
| **network_domain**  string | Network domain of the VPC.  Returned: success  Sample: `"example.com"` |
| **project**  string | Name of project the VPC is related to.  Returned: success  Sample: `"Production"` |
| **redundant_vpc_router**  boolean | Whether the VPC has redundant routers or not.  Returned: success  Sample: `true` |
| **region_level_vpc**  boolean | Whether the VPC is region level or not.  Returned: success  Sample: `true` |
| **restart_required**  boolean | Whether the VPC router needs a restart or not.  Returned: success  Sample: `true` |
| **state**  string | State of the VPC.  Returned: success  Sample: `"Enabled"` |
| **tags**  list / elements=string | List of resource tags associated with the VPC.  Returned: success  Sample: `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **zone**  string | Name of zone the VPC is in.  Returned: success  Sample: `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
