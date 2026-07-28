---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_router module – Manages routers on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_router_module.html
fetched_at: 2026-07-28T02:46:18+00:00
---
# ngine_io.cloudstack.cs_router module – Manages routers on Apache CloudStack based clouds.

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
> see [Requirements](cs_router_module.md#ansible-collections-ngine-io-cloudstack-cs-router-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_router`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_router_module.md#synopsis)
- [Requirements](cs_router_module.md#requirements)
- [Parameters](cs_router_module.md#parameters)
- [Notes](cs_router_module.md#notes)
- [Examples](cs_router_module.md#examples)
- [Return Values](cs_router_module.md#return-values)

## [Synopsis](cs_router_module.md#id1)

- Start, restart, stop and destroy routers.
- *state=present* is not able to create routers, use [ngine_io.cloudstack.cs_network](cs_network_module.md#ansible-collections-ngine-io-cloudstack-cs-network-module) instead.

## [Requirements](cs_router_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_router_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the router is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the router is related to. |
| **name**  string / required | Name of the router. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the router is related to. |
| **service_offering**  string | Name or id of the service offering of the router. |
| **state**  string | State of the router.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"started"` - `"stopped"` - `"restarted"` |
| **zone**  string | Name of the zone the router is deployed in.  If not set, all zones are used. |

## [Notes](cs_router_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_router_module.md#id5)

```yaml+jinja
# Ensure the router has the desired service offering, no matter if
# the router is running or not.
- name: Present router
  ngine_io.cloudstack.cs_router:
    name: r-40-VM
    service_offering: System Offering for Software Router

- name: Ensure started
  ngine_io.cloudstack.cs_router:
    name: r-40-VM
    state: started

# Ensure started with desired service offering.
# If the service offerings changes, router will be rebooted.
- name: Ensure started with desired service offering
  ngine_io.cloudstack.cs_router:
    name: r-40-VM
    service_offering: System Offering for Software Router
    state: started

- name: Ensure stopped
  ngine_io.cloudstack.cs_router:
    name: r-40-VM
    state: stopped

- name: Remove a router
  ngine_io.cloudstack.cs_router:
    name: r-40-VM
    state: absent
```

## [Return Values](cs_router_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the router is related to.  **Returned:** success  **Sample:** `"admin"` |
| **created**  string | Date of the router was created.  **Returned:** success  **Sample:** `"2014-12-01T14:57:57+0100"` |
| **domain**  string | Domain the router is related to.  **Returned:** success  **Sample:** `"ROOT"` |
| **id**  string | UUID of the router.  **Returned:** success  **Sample:** `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **name**  string | Name of the router.  **Returned:** success  **Sample:** `"r-40-VM"` |
| **redundant_state**  string | Redundant state of the router.  **Returned:** success  **Sample:** `"UNKNOWN"` |
| **requires_upgrade**  boolean | Whether the router needs to be upgraded to the new template.  **Returned:** success  **Sample:** `false` |
| **role**  string | Role of the router.  **Returned:** success  **Sample:** `"VIRTUAL_ROUTER"` |
| **service_offering**  string | Name of the service offering the router has.  **Returned:** success  **Sample:** `"System Offering For Software Router"` |
| **state**  string | State of the router.  **Returned:** success  **Sample:** `"Active"` |
| **template_version**  string | Version of the system VM template.  **Returned:** success  **Sample:** `"4.5.1"` |
| **zone**  string | Name of zone the router is in.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
