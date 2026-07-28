---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_instancegroup module – Manages instance groups on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_instancegroup_module.html
fetched_at: 2026-07-28T02:45:54+00:00
---
# ngine_io.cloudstack.cs_instancegroup module – Manages instance groups on Apache CloudStack based clouds.

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
> see [Requirements](cs_instancegroup_module.md#ansible-collections-ngine-io-cloudstack-cs-instancegroup-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_instancegroup`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_instancegroup_module.md#synopsis)
- [Requirements](cs_instancegroup_module.md#requirements)
- [Parameters](cs_instancegroup_module.md#parameters)
- [Notes](cs_instancegroup_module.md#notes)
- [Examples](cs_instancegroup_module.md#examples)
- [Return Values](cs_instancegroup_module.md#return-values)

## [Synopsis](cs_instancegroup_module.md#id1)

- Create and remove instance groups.

## [Requirements](cs_instancegroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_instancegroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the instance group is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the instance group is related to. |
| **name**  string / required | Name of the instance group. |
| **project**  string | Project the instance group is related to. |
| **state**  string | State of the instance group.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_instancegroup_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_instancegroup_module.md#id5)

```yaml+jinja
- name: Create an instance group
  ngine_io.cloudstack.cs_instancegroup:
    name: loadbalancers

- name: Remove an instance group
  ngine_io.cloudstack.cs_instancegroup:
    name: loadbalancers
    state: absent
```

## [Return Values](cs_instancegroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the instance group is related to.  **Returned:** success  **Sample:** `"example account"` |
| **created**  string | Date when the instance group was created.  **Returned:** success  **Sample:** `"2015-05-03T15:05:51+0200"` |
| **domain**  string | Domain the instance group is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the instance group.  **Returned:** success  **Sample:** `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **name**  string | Name of the instance group.  **Returned:** success  **Sample:** `"webservers"` |
| **project**  string | Project the instance group is related to.  **Returned:** success  **Sample:** `"example project"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
