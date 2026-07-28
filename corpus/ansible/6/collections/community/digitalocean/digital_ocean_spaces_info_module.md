---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_spaces_info module – List DigitalOcean Spaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_spaces_info_module.html
fetched_at: 2026-07-27T17:06:55+00:00
---
# community.digitalocean.digital_ocean_spaces_info module – List DigitalOcean Spaces.

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
> You need further requirements to be able to use this module,
> see [Requirements](digital_ocean_spaces_info_module.md#ansible-collections-community-digitalocean-digital-ocean-spaces-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_spaces_info`.

New in community.digitalocean 1.15.0

- [Synopsis](digital_ocean_spaces_info_module.md#synopsis)
- [Requirements](digital_ocean_spaces_info_module.md#requirements)
- [Parameters](digital_ocean_spaces_info_module.md#parameters)
- [Examples](digital_ocean_spaces_info_module.md#examples)
- [Return Values](digital_ocean_spaces_info_module.md#return-values)

## [Synopsis](digital_ocean_spaces_info_module.md#id1)

- List DigitalOcean Spaces.

## [Requirements](digital_ocean_spaces_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- boto3

## [Parameters](digital_ocean_spaces_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key_id**  aliases: AWS_ACCESS_KEY_ID  string / required | The AWS_ACCESS_KEY_ID to use. |
| **aws_secret_access_key**  aliases: AWS_SECRET_ACCESS_KEY  string / required | The AWS_SECRET_ACCESS_KEY to use. |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **region**  aliases: region_id  string / required | The region from which to list Spaces. |
| **state**  string | Only present is supported.  Choices:   - `"present"` ← (default) |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_spaces_info_module.md#id4)

```yaml+jinja
- name: List all Spaces in nyc3
  community.digitalocean.digital_ocean_spaces_info:
    state: present
    region: nyc3
```

## [Return Values](digital_ocean_spaces_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | List of DigitalOcean Spaces  Returned: always  Sample: `{"spaces": [{"endpoint_url": "https://nyc3.digitaloceanspaces.com", "name": "gh-ci-space", "region": "nyc3", "space_url": "https://gh-ci-space.nyc3.digitaloceanspaces.com"}]}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
