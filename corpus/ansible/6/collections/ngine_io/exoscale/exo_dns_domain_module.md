---
collection: ansible
version: "6"
title: "ngine_io.exoscale.exo_dns_domain module – Manages domain records on Exoscale DNS API."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/exoscale/exo_dns_domain_module.html
fetched_at: 2026-07-28T00:15:59+00:00
---
# ngine_io.exoscale.exo_dns_domain module – Manages domain records on Exoscale DNS API.

> **Note:**
>
> This module is part of the [ngine_io.exoscale collection](https://galaxy.ansible.com/ngine_io/exoscale) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.exoscale`.
> You need further requirements to be able to use this module,
> see [Requirements](exo_dns_domain_module.md#ansible-collections-ngine-io-exoscale-exo-dns-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.exoscale.exo_dns_domain`.

New in ngine_io.exoscale 0.1.0

- [Synopsis](exo_dns_domain_module.md#synopsis)
- [Requirements](exo_dns_domain_module.md#requirements)
- [Parameters](exo_dns_domain_module.md#parameters)
- [Notes](exo_dns_domain_module.md#notes)
- [Examples](exo_dns_domain_module.md#examples)
- [Return Values](exo_dns_domain_module.md#return-values)

## [Synopsis](exo_dns_domain_module.md#id1)

- Create and remove domain records.

## [Requirements](exo_dns_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](exo_dns_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | API key of the Exoscale DNS API.  The ENV variable `CLOUDSTACK_KEY` is used as default, when defined. |
| **api_region**  string | Name of the ini section in the `cloustack.ini` file.  The ENV variable `CLOUDSTACK_REGION` is used as default, when defined.  Default: `"cloudstack"` |
| **api_secret**  string | Secret key of the Exoscale DNS API.  The ENV variable `CLOUDSTACK_SECRET` is used as default, when defined. |
| **api_timeout**  integer | HTTP timeout to Exoscale DNS API.  The ENV variable `CLOUDSTACK_TIMEOUT` is used as default, when defined.  Default: `10` |
| **name**  string / required | Name of the record. |
| **state**  string | State of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Exoscale DNS API.  Choices:   - `false` - `true` ← (default) |

## [Notes](exo_dns_domain_module.md#id4)

> **Note:**
>
> - As Exoscale DNS uses the same API key and secret for all services, we reuse the config used for Exscale Compute based on CloudStack. The config is read from several locations, in the following order. The `CLOUDSTACK_KEY`, `CLOUDSTACK_SECRET` environment variables. A `CLOUDSTACK_CONFIG` environment variable pointing to an `.ini` file, A `cloudstack.ini` file in the current working directory. A `.cloudstack.ini` file in the users home directory. Optionally multiple credentials and endpoints can be specified using ini sections in `cloudstack.ini`. Use the argument `api_region` to select the section name, default section is `cloudstack`.
> - This module does not support multiple A records and will complain properly if you try.
> - More information Exoscale DNS can be found on <https://community.exoscale.ch/documentation/dns/>.
> - This module supports check mode and diff.

## [Examples](exo_dns_domain_module.md#id5)

```yaml+jinja
- name: Create a domain
  exo_dns_domain:
    name: example.com

- name: Remove a domain
  exo_dns_domain:
    name: example.com
    state: absent
```

## [Return Values](exo_dns_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exo_dns_domain**  complex | API domain results  Returned: success |
| **account_id**  integer | Your account ID  Returned: success  Sample: `34569` |
| **auto_renew**  boolean | Whether domain is auto renewed or not  Returned: success  Sample: `false` |
| **created_at**  string | When the domain was created  Returned: success  Sample: `"2016-08-12T15:24:23.989Z"` |
| **expires_on**  string | When the domain expires  Returned: success  Sample: `"2016-08-12T15:24:23.989Z"` |
| **id**  integer | ID of the domain  Returned: success  Sample: `"2016-08-12T15:24:23.989Z"` |
| **lockable**  boolean | Whether the domain is lockable or not  Returned: success  Sample: `true` |
| **name**  string | Domain name  Returned: success  Sample: `"example.com"` |
| **record_count**  integer | Number of records related to this domain  Returned: success  Sample: `5` |
| **registrant_id**  integer | ID of the registrant  Returned: success |
| **service_count**  integer | Number of services  Returned: success  Sample: `0` |
| **state**  string | State of the domain  Returned: success  Sample: `"hosted"` |
| **token**  string | Token  Returned: success  Sample: `"r4NzTRp6opIeFKfaFYvOd6MlhGyD07jl"` |
| **unicode_name**  string | Domain name as unicode  Returned: success  Sample: `"example.com"` |
| **updated_at**  string | When the domain was updated last.  Returned: success  Sample: `"2016-08-12T15:24:23.989Z"` |
| **user_id**  integer | ID of the user  Returned: success |
| **whois_protected**  boolean | Whether the whois is protected or not  Returned: success  Sample: `false` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-exoscale/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-exoscale)
