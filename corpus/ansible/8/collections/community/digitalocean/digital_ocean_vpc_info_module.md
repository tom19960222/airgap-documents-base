---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_vpc_info module – Gather information about DigitalOcean VPCs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_vpc_info_module.html
fetched_at: 2026-07-28T01:43:19+00:00
---
# community.digitalocean.digital_ocean_vpc_info module – Gather information about DigitalOcean VPCs

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_vpc_info`.

New in community.digitalocean 1.7.0

- [Synopsis](digital_ocean_vpc_info_module.md#synopsis)
- [Parameters](digital_ocean_vpc_info_module.md#parameters)
- [Examples](digital_ocean_vpc_info_module.md#examples)
- [Return Values](digital_ocean_vpc_info_module.md#return-values)

## [Synopsis](digital_ocean_vpc_info_module.md#id1)

- This module can be used to gather information about DigitalOcean VPCs.

## [Parameters](digital_ocean_vpc_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **members**  boolean | Return VPC members (instead of all VPCs).  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of the VPC. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_vpc_info_module.md#id3)

```yaml+jinja
- name: Fetch all VPCs
  community.digitalocean.digital_ocean_vpc_info:
  register: my_vpcs

- name: Fetch members of a VPC
  community.digitalocean.digital_ocean_vpc_info:
    members: true
    name: myvpc1
  register: my_vpc_members
```

## [Return Values](digital_ocean_vpc_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | All DigitalOcean VPCs, or, members of a VPC (with `members=True`).  **Returned:** success  **Sample:** `[{"created_at": "2021-02-06T17:57:22Z", "default": true, "description": "", "id": "0db3519b-9efc-414a-8868-8f2e6934688c", "ip_range": "10.116.0.0/20", "name": "default-nyc1", "region": "nyc1", "urn": "do:vpc:0db3519b-9efc-414a-8868-8f2e6934688c"}, {"links": {}, "members": [], "meta": {"total": 0}}]` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
