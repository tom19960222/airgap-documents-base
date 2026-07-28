---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_zone module – Manages zones on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_zone_module.html
fetched_at: 2026-07-28T00:15:57+00:00
---
# ngine_io.cloudstack.cs_zone module – Manages zones on Apache CloudStack based clouds.

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
> see [Requirements](cs_zone_module.md#ansible-collections-ngine-io-cloudstack-cs-zone-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_zone`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_zone_module.md#synopsis)
- [Requirements](cs_zone_module.md#requirements)
- [Parameters](cs_zone_module.md#parameters)
- [Notes](cs_zone_module.md#notes)
- [Examples](cs_zone_module.md#examples)
- [Return Values](cs_zone_module.md#return-values)

## [Synopsis](cs_zone_module.md#id1)

- Create, update and remove zones.

## [Requirements](cs_zone_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_zone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **dhcp_provider**  string | DHCP provider for the Zone. |
| **dns1**  string | First DNS for the zone.  Required if *state=present* |
| **dns1_ipv6**  string | First DNS for IPv6 for the zone. |
| **dns2**  string | Second DNS for the zone. |
| **dns2_ipv6**  string | Second DNS for IPv6 for the zone. |
| **domain**  string | Domain the zone is related to.  Zone is a public zone if not set. |
| **guest_cidr_address**  string | Guest CIDR address for the zone. |
| **id**  string | uuid of the existing zone. |
| **internal_dns1**  string | First internal DNS for the zone.  If not set *dns1* will be used on *state=present*. |
| **internal_dns2**  string | Second internal DNS for the zone. |
| **local_storage_enabled**  boolean | Whether to enable local storage for the zone or not..  Choices:   - `false` - `true` |
| **name**  string / required | Name of the zone. |
| **network_domain**  string | Network domain for the zone. |
| **network_type**  string | Network type of the zone.  Choices:   - `"Basic"` ← (default) - `"Advanced"` |
| **securitygroups_enabled**  boolean | Whether the zone is security group enabled or not.  Choices:   - `false` - `true` |
| **state**  string | State of the zone.  Choices:   - `"present"` ← (default) - `"enabled"` - `"disabled"` - `"absent"` |

## [Notes](cs_zone_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_zone_module.md#id5)

```yaml+jinja
- name: Ensure a zone is present
  ngine_io.cloudstack.cs_zone:
    name: ch-zrh-ix-01
    dns1: 8.8.8.8
    dns2: 8.8.4.4
    network_type: basic

- name: Ensure a zone is disabled
  ngine_io.cloudstack.cs_zone:
    name: ch-zrh-ix-01
    state: disabled

- name: Ensure a zone is enabled
  ngine_io.cloudstack.cs_zone:
    name: ch-zrh-ix-01
    state: enabled

- name: Ensure a zone is absent
  ngine_io.cloudstack.cs_zone:
    name: ch-zrh-ix-01
    state: absent
```

## [Return Values](cs_zone_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocation_state**  string | State of the zone.  Returned: success  Sample: `"Enabled"` |
| **dhcp_provider**  string | DHCP provider for the zone  Returned: success  Sample: `"VirtualRouter"` |
| **dns1**  string | First DNS for the zone.  Returned: success  Sample: `"8.8.8.8"` |
| **dns1_ipv6**  string | First IPv6 DNS for the zone.  Returned: success  Sample: `"2001:4860:4860::8888"` |
| **dns2**  string | Second DNS for the zone.  Returned: success  Sample: `"8.8.4.4"` |
| **dns2_ipv6**  string | Second IPv6 DNS for the zone.  Returned: success  Sample: `"2001:4860:4860::8844"` |
| **domain**  string | Domain the zone is related to.  Returned: success  Sample: `"ROOT"` |
| **guest_cidr_address**  string | Guest CIDR address for the zone  Returned: success  Sample: `"10.1.1.0/24"` |
| **id**  string | UUID of the zone.  Returned: success  Sample: `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **internal_dns1**  string | First internal DNS for the zone.  Returned: success  Sample: `"8.8.8.8"` |
| **internal_dns2**  string | Second internal DNS for the zone.  Returned: success  Sample: `"8.8.4.4"` |
| **local_storage_enabled**  boolean | Local storage offering enabled.  Returned: success  Sample: `false` |
| **name**  string | Name of the zone.  Returned: success  Sample: `"zone01"` |
| **network_domain**  string | Network domain for the zone.  Returned: success  Sample: `"example.com"` |
| **network_type**  string | Network type for the zone.  Returned: success  Sample: `"basic"` |
| **securitygroups_enabled**  boolean | Security groups support is enabled.  Returned: success  Sample: `false` |
| **tags**  list / elements=string | List of resource tags associated with the zone.  Returned: success  Sample: `[{"key": "foo", "value": "bar"}]` |
| **zone_token**  string | Zone token  Returned: success  Sample: `"ccb0a60c-79c8-3230-ab8b-8bdbe8c45bb7"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
