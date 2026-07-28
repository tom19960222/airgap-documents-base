---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_vpc module – Create and delete DigitalOcean VPCs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_vpc_module.html
fetched_at: 2026-07-27T17:06:59+00:00
---
# community.digitalocean.digital_ocean_vpc module – Create and delete DigitalOcean VPCs

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_vpc`.

New in community.digitalocean 1.7.0

- [Synopsis](digital_ocean_vpc_module.md#synopsis)
- [Parameters](digital_ocean_vpc_module.md#parameters)
- [Examples](digital_ocean_vpc_module.md#examples)
- [Return Values](digital_ocean_vpc_module.md#return-values)

## [Synopsis](digital_ocean_vpc_module.md#id1)

- This module can be used to create and delete DigitalOcean VPCs.

## [Parameters](digital_ocean_vpc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **default**  boolean | A boolean value indicating whether or not the VPC is the default network for the region.  All applicable resources are placed into the default VPC network unless otherwise specified during their creation.  The `default` field cannot be unset from `true`.  If you want to set a new default VPC network, update the `default` field of another VPC network in the same region.  The previous network’s `default` field will be set to `false` when a new default VPC has been defined.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A free-form text field for describing the VPC’s purpose.  It may be a maximum of 255 characters. |
| **ip_range**  string | The requested range of IP addresses for the VPC in CIDR notation.  Network ranges cannot overlap with other networks in the same account and must be in range of private addresses as defined in RFC1918.  It may not be smaller than /24 nor larger than /16.  If no IP range is specified, a /20 network range is generated that won’t conflict with other VPC networks in your account. |
| **name**  string / required | The name of the VPC.  Must be unique and contain alphanumeric characters, dashes, and periods only. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **region**  string | The slug identifier for the region where the VPC will be created. |
| **state**  string | Whether the VPC should be present (created) or absent (deleted).  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_vpc_module.md#id3)

```yaml+jinja
- name: Create a VPC
  community.digitalocean.digital_ocean_vpc:
    state: present
    name: myvpc1
    region: nyc1

- name: Create a VPC (choose IP range)
  community.digitalocean.digital_ocean_vpc:
    state: present
    name: myvpc1
    region: nyc1
    ip_range: 192.168.192.0/24

- name: Update a VPC (make it default)
  community.digitalocean.digital_ocean_vpc:
    state: present
    name: myvpc1
    region: nyc1
    default: true

- name: Update a VPC (change description)
  community.digitalocean.digital_ocean_vpc:
    state: present
    name: myvpc1
    region: nyc1
    description: myvpc

- name: Delete a VPC
  community.digitalocean.digital_ocean_vpc:
    state: absent
    name: myvpc1
```

## [Return Values](digital_ocean_vpc_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | A DigitalOcean VPC.  Returned: success  Sample: `{"msg": "Created VPC myvpc1 in nyc1", "vpc": {"created_at": "2021-06-17T11:43:12.12121565Z", "default": false, "description": "", "id": "a3b72d97-192f-4984-9d71-08a5faf2e0c7", "ip_range": "10.116.16.0/20", "name": "testvpc1", "region": "nyc1", "urn": "do:vpc:a3b72d97-192f-4984-9d71-08a5faf2e0c7"}}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
