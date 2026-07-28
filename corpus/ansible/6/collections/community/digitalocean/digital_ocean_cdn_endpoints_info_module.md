---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_cdn_endpoints_info module – Display DigitalOcean CDN Endpoints"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_cdn_endpoints_info_module.html
fetched_at: 2026-07-27T17:06:36+00:00
---
# community.digitalocean.digital_ocean_cdn_endpoints_info module – Display DigitalOcean CDN Endpoints

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_cdn_endpoints_info`.

New in community.digitalocean 1.10.0

- [Synopsis](digital_ocean_cdn_endpoints_info_module.md#synopsis)
- [Parameters](digital_ocean_cdn_endpoints_info_module.md#parameters)
- [Examples](digital_ocean_cdn_endpoints_info_module.md#examples)
- [Return Values](digital_ocean_cdn_endpoints_info_module.md#return-values)

## [Synopsis](digital_ocean_cdn_endpoints_info_module.md#id1)

- Display DigitalOcean CDN Endpoints

## [Parameters](digital_ocean_cdn_endpoints_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **state**  string | The usual, `present` to create, `absent` to destroy  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_cdn_endpoints_info_module.md#id3)

```yaml+jinja
- name: Display DigitalOcean CDN Endpoints
  community.digitalocean.digital_ocean_cdn_endpoints_info:
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
```

## [Return Values](digital_ocean_cdn_endpoints_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | DigitalOcean CDN Endpoints  Returned: success  Sample: `{"data": {"endpoints": [{"created_at": "2021-09-05T13:47:23Z", "endpoint": "mamercad.nyc3.cdn.digitaloceanspaces.com", "id": "01739563-3f50-4da4-a451-27f6d59d7573", "origin": "mamercad.nyc3.digitaloceanspaces.com", "ttl": 3600}], "meta": {"total": 1}}}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
