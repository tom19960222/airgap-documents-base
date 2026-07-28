---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_vpc_offering module – Manages vpc offerings on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_vpc_offering_module.html
fetched_at: 2026-07-28T02:46:38+00:00
---
# ngine_io.cloudstack.cs_vpc_offering module – Manages vpc offerings on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_vpc_offering_module.md#ansible-collections-ngine-io-cloudstack-cs-vpc-offering-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_vpc_offering`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_vpc_offering_module.md#synopsis)
- [Requirements](cs_vpc_offering_module.md#requirements)
- [Parameters](cs_vpc_offering_module.md#parameters)
- [Notes](cs_vpc_offering_module.md#notes)
- [Examples](cs_vpc_offering_module.md#examples)
- [Return Values](cs_vpc_offering_module.md#return-values)

## [Synopsis](cs_vpc_offering_module.md#id1)

- Create, update, enable, disable and remove CloudStack VPC offerings.

## [Requirements](cs_vpc_offering_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_vpc_offering_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **display_text**  string | Display text of the vpc offerings |
| **name**  string / required | The name of the vpc offering |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **service_capabilities**  aliases: service_capability  list / elements=dictionary | Desired service capabilities as part of vpc offering. |
| **service_offering**  string | The name or ID of the service offering for the VPC router appliance. |
| **service_providers**  aliases: service_provider  list / elements=dictionary | provider to service mapping. If not specified, the provider for the service will be mapped to the default provider on the physical network |
| **state**  string | State of the vpc offering.  **Choices:**   - `"enabled"` - `"present"` ← (default) - `"disabled"` - `"absent"` |
| **supported_services**  aliases: supported_service  list / elements=string | Services supported by the vpc offering |

## [Notes](cs_vpc_offering_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_vpc_offering_module.md#id5)

```yaml+jinja
- name: Create a vpc offering and enable it
  ngine_io.cloudstack.cs_vpc_offering:
    name: my_vpc_offering
    display_text: vpc offering description
    state: enabled
    supported_services: [ Dns, Dhcp ]
    service_providers:
      - {service: 'dns', provider: 'VpcVirtualRouter'}
      - {service: 'dhcp', provider: 'VpcVirtualRouter'}

- name: Create a vpc offering with redundant router
  ngine_io.cloudstack.cs_vpc_offering:
    name: my_vpc_offering
    display_text: vpc offering description
    supported_services: [ Dns, Dhcp, SourceNat ]
    service_providers:
      - {service: 'dns', provider: 'VpcVirtualRouter'}
      - {service: 'dhcp', provider: 'VpcVirtualRouter'}
      - {service: 'SourceNat', provider: 'VpcVirtualRouter'}
    service_capabilities:
      - {service: 'SourceNat', capabilitytype: 'RedundantRouter', capabilityvalue: true}

- name: Create a region level vpc offering with distributed router
  ngine_io.cloudstack.cs_vpc_offering:
    name: my_vpc_offering
    display_text: vpc offering description
    state: present
    supported_services: [ Dns, Dhcp, SourceNat ]
    service_providers:
      - {service: 'dns', provider: 'VpcVirtualRouter'}
      - {service: 'dhcp', provider: 'VpcVirtualRouter'}
      - {service: 'SourceNat', provider: 'VpcVirtualRouter'}
    service_capabilities:
      - {service: 'Connectivity', capabilitytype: 'DistributedRouter', capabilityvalue: true}
      - {service: 'Connectivity', capabilitytype: 'RegionLevelVPC', capabilityvalue: true}

- name: Remove a vpc offering
  ngine_io.cloudstack.cs_vpc_offering:
    name: my_vpc_offering
    state: absent
```

## [Return Values](cs_vpc_offering_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **display_text**  string | The display text of the vpc offering  **Returned:** success  **Sample:** `"My vpc offering"` |
| **distributed**  boolean | Indicates if the vpc offering supports distributed router for one-hop forwarding.  **Returned:** success  **Sample:** `false` |
| **id**  string | UUID of the vpc offering.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **is_default**  boolean | Whether VPC offering is the default offering or not.  **Returned:** success  **Sample:** `false` |
| **name**  string | The name of the vpc offering  **Returned:** success  **Sample:** `"MyCustomVPCOffering"` |
| **region_level**  boolean | Indicated if the offering can support region level vpc.  **Returned:** success  **Sample:** `false` |
| **service_offering_id**  string | The service offering ID.  **Returned:** success  **Sample:** `"c5f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **state**  string | The state of the vpc offering  **Returned:** success  **Sample:** `"Enabled"` |

### Authors

- David Passante (@dpassante)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
