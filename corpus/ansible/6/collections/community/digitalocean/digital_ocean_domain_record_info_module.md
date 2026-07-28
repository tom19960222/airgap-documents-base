---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_domain_record_info module – Gather information about DigitalOcean domain records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_domain_record_info_module.html
fetched_at: 2026-07-27T17:06:41+00:00
---
# community.digitalocean.digital_ocean_domain_record_info module – Gather information about DigitalOcean domain records

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_domain_record_info`.

New in community.digitalocean 1.16.0

- [Synopsis](digital_ocean_domain_record_info_module.md#synopsis)
- [Parameters](digital_ocean_domain_record_info_module.md#parameters)
- [Notes](digital_ocean_domain_record_info_module.md#notes)
- [Examples](digital_ocean_domain_record_info_module.md#examples)
- [Return Values](digital_ocean_domain_record_info_module.md#return-values)

## [Synopsis](digital_ocean_domain_record_info_module.md#id1)

- Gather information about DigitalOcean domain records.

## [Parameters](digital_ocean_domain_record_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **name**  aliases: domain, domain_name  string / required | Name of the domain. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **record_id**  integer | Used to retrieve a specific record. |
| **state**  string | Indicate desired state of the target.  Choices:   - `"present"` ← (default) |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **type**  string | The type of record you would like to retrieve.  Choices:   - `"A"` - `"AAAA"` - `"CNAME"` - `"MX"` - `"TXT"` - `"SRV"` - `"NS"` - `"CAA"` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](digital_ocean_domain_record_info_module.md#id3)

> **Note:**
>
> - Version 2 of DigitalOcean API is used.
> - The number of requests that can be made through the API is currently limited to 5,000 per hour per OAuth token.

## [Examples](digital_ocean_domain_record_info_module.md#id4)

```yaml+jinja
- name: Retrieve all domain records for example.com
  community.digitalocean.digital_ocean_domain_record_info:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com

- name: Get specific domain record by ID
  community.digitalocean.digital_ocean_domain_record_info:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    record_id: 12345789
  register: result

- name: Retrieve all A domain records for example.com
  community.digitalocean.digital_ocean_domain_record_info:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    type: A
```

## [Return Values](digital_ocean_domain_record_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | list of DigitalOcean domain records  Returned: success  Sample: `[{"data": "ns1.digitalocean.com", "flags": null, "id": 296972269, "name": "@", "port": null, "priority": null, "tag": null, "ttl": 1800, "type": "NS", "weight": null}]` |

### Authors

- Adam Papai (@woohgit)
- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
