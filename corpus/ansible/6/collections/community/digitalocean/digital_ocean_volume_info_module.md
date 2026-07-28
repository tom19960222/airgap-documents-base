---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_volume_info module – Gather information about DigitalOcean volumes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_volume_info_module.html
fetched_at: 2026-07-27T17:06:58+00:00
---
# community.digitalocean.digital_ocean_volume_info module – Gather information about DigitalOcean volumes

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
> see [Requirements](digital_ocean_volume_info_module.md#ansible-collections-community-digitalocean-digital-ocean-volume-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_volume_info`.

- [Synopsis](digital_ocean_volume_info_module.md#synopsis)
- [Requirements](digital_ocean_volume_info_module.md#requirements)
- [Parameters](digital_ocean_volume_info_module.md#parameters)
- [Examples](digital_ocean_volume_info_module.md#examples)
- [Return Values](digital_ocean_volume_info_module.md#return-values)

## [Synopsis](digital_ocean_volume_info_module.md#id1)

- This module can be used to gather information about DigitalOcean provided volumes.
- This module was called `digital_ocean_volume_facts` before Ansible 2.9. The usage did not change.

## [Requirements](digital_ocean_volume_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_volume_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **region_name**  string | Name of region to restrict results to volumes available in a specific region.  Please use [community.digitalocean.digital_ocean_region_info](digital_ocean_region_info_module.md#ansible-collections-community-digitalocean-digital-ocean-region-info-module) for getting valid values related regions. |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_volume_info_module.md#id4)

```yaml+jinja
- name: Gather information about all volume
  community.digitalocean.digital_ocean_volume_info:
    oauth_token: "{{ oauth_token }}"

- name: Gather information about volume in given region
  community.digitalocean.digital_ocean_volume_info:
    region_name: nyc1
    oauth_token: "{{ oauth_token }}"

- name: Get information about volume named nyc3-test-volume
  community.digitalocean.digital_ocean_volume_info:
  register: resp_out
- set_fact:
    volume_id: "{{ item.id }}"
  loop: "{{ resp_out.data | community.general.json_query(name) }}"
  vars:
    name: "[?name=='nyc3-test-volume']"
- debug: var=volume_id
```

## [Return Values](digital_ocean_volume_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=string | DigitalOcean volume information  Returned: success  Sample: `[{"created_at": "2016-03-02T17:00:49Z", "description": "Block store for examples", "droplet_ids": [], "id": "506f78a4-e098-11e5-ad9f-000f53306ae1", "name": "example", "region": {"available": true, "features": ["private_networking", "backups", "ipv6", "metadata"], "name": "New York 1", "sizes": ["s-1vcpu-1gb", "s-1vcpu-2gb", "s-1vcpu-3gb", "s-2vcpu-2gb", "s-3vcpu-1gb", "s-2vcpu-4gb", "s-4vcpu-8gb", "s-6vcpu-16gb", "s-8vcpu-32gb", "s-12vcpu-48gb", "s-16vcpu-64gb", "s-20vcpu-96gb", "s-24vcpu-128gb", "s-32vcpu-192gb"], "slug": "nyc1"}, "size_gigabytes": 10}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
