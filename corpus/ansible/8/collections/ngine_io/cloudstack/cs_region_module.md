---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_region module – Manages regions on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_region_module.html
fetched_at: 2026-07-28T02:46:14+00:00
---
# ngine_io.cloudstack.cs_region module – Manages regions on Apache CloudStack based clouds.

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
> see [Requirements](cs_region_module.md#ansible-collections-ngine-io-cloudstack-cs-region-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_region`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_region_module.md#synopsis)
- [Requirements](cs_region_module.md#requirements)
- [Parameters](cs_region_module.md#parameters)
- [Notes](cs_region_module.md#notes)
- [Examples](cs_region_module.md#examples)
- [Return Values](cs_region_module.md#return-values)

## [Synopsis](cs_region_module.md#id1)

- Add, update and remove regions.

## [Requirements](cs_region_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_region_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **endpoint**  string | Endpoint URL of the region.  Required if *state=present* |
| **id**  integer / required | ID of the region.  Must be an number (int). |
| **name**  string | Name of the region.  Required if *state=present* |
| **state**  string | State of the region.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_region_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_region_module.md#id5)

```yaml+jinja
- name: create a region
  ngine_io.cloudstack.cs_region:
    id: 2
    name: geneva
    endpoint: https://cloud.gva.example.com

- name: remove a region with ID 2
  ngine_io.cloudstack.cs_region:
    id: 2
    state: absent
```

## [Return Values](cs_region_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **endpoint**  string | Endpoint of the region.  **Returned:** success  **Sample:** `"http://cloud.example.com"` |
| **gslb_service_enabled**  boolean | Whether the GSLB service is enabled or not.  **Returned:** success  **Sample:** `true` |
| **id**  integer | ID of the region.  **Returned:** success  **Sample:** `1` |
| **name**  string | Name of the region.  **Returned:** success  **Sample:** `"local"` |
| **portable_ip_service_enabled**  boolean | Whether the portable IP service is enabled or not.  **Returned:** success  **Sample:** `true` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
