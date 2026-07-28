---
collection: ansible
version: "6"
title: "community.general.scaleway_organization_info module – Gather information about the Scaleway organizations available"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_organization_info_module.html
fetched_at: 2026-07-27T17:12:59+00:00
---
# community.general.scaleway_organization_info module – Gather information about the Scaleway organizations available

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_organization_info`.

- [Synopsis](scaleway_organization_info_module.md#synopsis)
- [Parameters](scaleway_organization_info_module.md#parameters)
- [Notes](scaleway_organization_info_module.md#notes)
- [Examples](scaleway_organization_info_module.md#examples)
- [Return Values](scaleway_organization_info_module.md#return-values)

## [Synopsis](scaleway_organization_info_module.md#id1)

- Gather information about the Scaleway organizations available.

## [Parameters](scaleway_organization_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL  Default: `"https://account.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_organization_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_organization_info_module.md#id4)

```yaml+jinja
- name: Gather Scaleway organizations information
  community.general.scaleway_organization_info:
  register: result

- ansible.builtin.debug:
    msg: "{{ result.scaleway_organization_info }}"
```

## [Return Values](scaleway_organization_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scaleway_organization_info**  complex | Response from Scaleway API  Returned: success  Sample: `{"scaleway_organization_info": [{"address_city_name": "Paris", "address_country_code": "FR", "address_line1": "42 Rue de l'univers", "address_line2": null, "address_postal_code": "75042", "address_subdivision_code": "FR-75", "creation_date": "2018-08-06T13:43:28.508575+00:00", "currency": "EUR", "customer_class": "individual", "id": "3f709602-5e6c-4619-b80c-e8432ferewtr", "locale": "fr_FR", "modification_date": "2018-08-06T14:56:41.401685+00:00", "name": "James Bond", "support_id": "694324", "support_level": "basic", "support_pin": "9324", "users": [], "vat_number": null, "warnings": []}]}` |

### Authors

- Yanis Guenane (@Spredzy)
- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
