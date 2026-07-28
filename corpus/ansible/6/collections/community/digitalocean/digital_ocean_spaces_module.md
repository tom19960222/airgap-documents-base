---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_spaces module – Create and remove DigitalOcean Spaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_spaces_module.html
fetched_at: 2026-07-27T17:06:54+00:00
---
# community.digitalocean.digital_ocean_spaces module – Create and remove DigitalOcean Spaces.

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
> see [Requirements](digital_ocean_spaces_module.md#ansible-collections-community-digitalocean-digital-ocean-spaces-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_spaces`.

New in community.digitalocean 1.15.0

- [Synopsis](digital_ocean_spaces_module.md#synopsis)
- [Requirements](digital_ocean_spaces_module.md#requirements)
- [Parameters](digital_ocean_spaces_module.md#parameters)
- [Examples](digital_ocean_spaces_module.md#examples)
- [Return Values](digital_ocean_spaces_module.md#return-values)

## [Synopsis](digital_ocean_spaces_module.md#id1)

- Create and remove DigitalOcean Spaces.

## [Requirements](digital_ocean_spaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- boto3

## [Parameters](digital_ocean_spaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key_id**  aliases: AWS_ACCESS_KEY_ID  string / required | The AWS_ACCESS_KEY_ID to use. |
| **aws_secret_access_key**  aliases: AWS_SECRET_ACCESS_KEY  string / required | The AWS_SECRET_ACCESS_KEY to use. |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **name**  string / required | The name of the Spaces to create or delete. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **region**  aliases: region_id  string / required | The region to create or delete the Space in. |
| **state**  string | Whether the Space should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_spaces_module.md#id4)

```yaml+jinja
- name: Create a Space in nyc3
  community.digitalocean.digital_ocean_spaces:
    state: present
    name: my-space
    region: nyc3

- name: Delete a Space in nyc3
  community.digitalocean.digital_ocean_spaces:
    state: absent
    name: my-space
    region: nyc3
```

## [Return Values](digital_ocean_spaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | DigitalOcean Space  Returned: present  Sample: `{"space": {"endpoint_url": "https://nyc3.digitaloceanspaces.com", "name": "gh-ci-space-1", "region": "nyc3", "space_url": "https://gh-ci-space-1.nyc3.digitaloceanspaces.com"}}` |
| **msg**  string | Informational message  Returned: always  Sample: `"Created Space gh-ci-space-1 in nyc3"` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
