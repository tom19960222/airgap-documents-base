---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_affinitygroup module – Manages affinity groups on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_affinitygroup_module.html
fetched_at: 2026-07-28T02:45:41+00:00
---
# ngine_io.cloudstack.cs_affinitygroup module – Manages affinity groups on Apache CloudStack based clouds.

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
> see [Requirements](cs_affinitygroup_module.md#ansible-collections-ngine-io-cloudstack-cs-affinitygroup-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_affinitygroup`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_affinitygroup_module.md#synopsis)
- [Requirements](cs_affinitygroup_module.md#requirements)
- [Parameters](cs_affinitygroup_module.md#parameters)
- [Notes](cs_affinitygroup_module.md#notes)
- [Examples](cs_affinitygroup_module.md#examples)
- [Return Values](cs_affinitygroup_module.md#return-values)

## [Synopsis](cs_affinitygroup_module.md#id1)

- Create and remove affinity groups.

## [Requirements](cs_affinitygroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_affinitygroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the affinity group is related to. |
| **affinity_type**  string | Type of the affinity group. If not specified, first found affinity type is used. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **description**  string | Description of the affinity group. |
| **domain**  string | Domain the affinity group is related to. |
| **name**  string / required | Name of the affinity group. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the affinity group is related to. |
| **state**  string | State of the affinity group.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_affinitygroup_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_affinitygroup_module.md#id5)

```yaml+jinja
- name: Create a affinity group
  ngine_io.cloudstack.cs_affinitygroup:
    name: haproxy
    affinity_type: host anti-affinity

- name: Remove a affinity group
  ngine_io.cloudstack.cs_affinitygroup:
    name: haproxy
    state: absent
```

## [Return Values](cs_affinitygroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the affinity group is related to.  **Returned:** success  **Sample:** `"example account"` |
| **affinity_type**  string | Type of affinity group.  **Returned:** success  **Sample:** `"host anti-affinity"` |
| **description**  string | Description of affinity group.  **Returned:** success  **Sample:** `"application affinity group"` |
| **domain**  string | Domain the affinity group is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the affinity group.  **Returned:** success  **Sample:** `"87b1e0ce-4e01-11e4-bb66-0050569e64b8"` |
| **name**  string | Name of affinity group.  **Returned:** success  **Sample:** `"app"` |
| **project**  string | Name of project the affinity group is related to.  **Returned:** success  **Sample:** `"Production"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
