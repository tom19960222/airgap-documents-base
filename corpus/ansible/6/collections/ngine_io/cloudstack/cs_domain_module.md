---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_domain module – Manages domains on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_domain_module.html
fetched_at: 2026-07-28T00:15:25+00:00
---
# ngine_io.cloudstack.cs_domain module – Manages domains on Apache CloudStack based clouds.

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
> see [Requirements](cs_domain_module.md#ansible-collections-ngine-io-cloudstack-cs-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_domain`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_domain_module.md#synopsis)
- [Requirements](cs_domain_module.md#requirements)
- [Parameters](cs_domain_module.md#parameters)
- [Notes](cs_domain_module.md#notes)
- [Examples](cs_domain_module.md#examples)
- [Return Values](cs_domain_module.md#return-values)

## [Synopsis](cs_domain_module.md#id1)

- Create, update and remove domains.

## [Requirements](cs_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **clean_up**  boolean | Clean up all domain resources like child domains and accounts.  Considered on *state=absent*.  Choices:   - `false` ← (default) - `true` |
| **network_domain**  string | Network domain for networks in the domain. |
| **path**  string / required | Path of the domain.  Prefix `ROOT/` or `/ROOT/` in path is optional. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **state**  string | State of the domain.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_domain_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_domain_module.md#id5)

```yaml+jinja
- name: Create a domain
  ngine_io.cloudstack.cs_domain:
    path: ROOT/customers
    network_domain: customers.example.com

- name: Create another subdomain
  ngine_io.cloudstack.cs_domain:
    path: ROOT/customers/xy
    network_domain: xy.customers.example.com

- name: Remove a domain
  ngine_io.cloudstack.cs_domain:
    path: ROOT/customers/xy
    state: absent
```

## [Return Values](cs_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | UUID of the domain.  Returned: success  Sample: `"87b1e0ce-4e01-11e4-bb66-0050569e64b8"` |
| **name**  string | Name of the domain.  Returned: success  Sample: `"customers"` |
| **network_domain**  string | Network domain of the domain.  Returned: success  Sample: `"example.local"` |
| **parent_domain**  string | Parent domain of the domain.  Returned: success  Sample: `"ROOT"` |
| **path**  string | Domain path.  Returned: success  Sample: `"/ROOT/customers"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
