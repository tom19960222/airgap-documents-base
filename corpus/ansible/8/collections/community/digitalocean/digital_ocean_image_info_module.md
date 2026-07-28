---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_image_info module – Gather information about DigitalOcean images"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_image_info_module.html
fetched_at: 2026-07-28T01:43:04+00:00
---
# community.digitalocean.digital_ocean_image_info module – Gather information about DigitalOcean images

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
> You need further requirements to be able to use this module,
> see [Requirements](digital_ocean_image_info_module.md#ansible-collections-community-digitalocean-digital-ocean-image-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_image_info`.

- [Synopsis](digital_ocean_image_info_module.md#synopsis)
- [Requirements](digital_ocean_image_info_module.md#requirements)
- [Parameters](digital_ocean_image_info_module.md#parameters)
- [Examples](digital_ocean_image_info_module.md#examples)
- [Return Values](digital_ocean_image_info_module.md#return-values)

## [Synopsis](digital_ocean_image_info_module.md#id1)

- This module can be used to gather information about DigitalOcean provided images.
- These images can be either of type `distribution`, `application` and `private`.
- This module was called `digital_ocean_image_facts` before Ansible 2.9. The usage did not change.

Aliases: digital_ocean_image_facts

## [Requirements](digital_ocean_image_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_image_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **image_type**  string | Specifies the type of image information to be retrieved.  If set to `application`, then information are gathered related to all application images.  If set to `distribution`, then information are gathered related to all distribution images.  If set to `private`, then information are gathered related to all private images.  If not set to any of above, then information are gathered related to all images.  **Choices:**   - `"all"` ← (default) - `"application"` - `"distribution"` - `"private"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_image_info_module.md#id4)

```yaml+jinja
- name: Gather information about all images
  community.digitalocean.digital_ocean_image_info:
    image_type: all
    oauth_token: "{{ oauth_token }}"

- name: Gather information about application images
  community.digitalocean.digital_ocean_image_info:
    image_type: application
    oauth_token: "{{ oauth_token }}"

- name: Gather information about distribution images
  community.digitalocean.digital_ocean_image_info:
    image_type: distribution
    oauth_token: "{{ oauth_token }}"

- name: Get distribution about image with slug coreos-beta
  community.digitalocean.digital_ocean_image_info:
  register: resp_out
- set_fact:
    distribution_name: "{{ item.distribution }}"
  loop: "{{ resp_out.data | community.general.json_query(name) }}"
  vars:
    name: "[?slug=='coreos-beta']"
- debug:
    var: distribution_name
```

## [Return Values](digital_ocean_image_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=string | DigitalOcean image information  **Returned:** success  **Sample:** `[{"created_at": "2018-02-02T07:11:43Z", "distribution": "CoreOS", "id": 31434061, "min_disk_size": 20, "name": "1662.1.0 (beta)", "public": true, "regions": ["nyc1", "sfo1", "nyc2", "ams2", "sgp1", "lon1", "nyc3", "ams3", "fra1", "tor1", "sfo2", "blr1"], "size_gigabytes": 0.42, "slug": "coreos-beta", "type": "snapshot"}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
