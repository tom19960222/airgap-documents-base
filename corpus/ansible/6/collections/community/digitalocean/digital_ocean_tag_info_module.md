---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_tag_info module – Gather information about DigitalOcean tags"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_tag_info_module.html
fetched_at: 2026-07-27T17:06:58+00:00
---
# community.digitalocean.digital_ocean_tag_info module – Gather information about DigitalOcean tags

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
> see [Requirements](digital_ocean_tag_info_module.md#ansible-collections-community-digitalocean-digital-ocean-tag-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_tag_info`.

- [Synopsis](digital_ocean_tag_info_module.md#synopsis)
- [Requirements](digital_ocean_tag_info_module.md#requirements)
- [Parameters](digital_ocean_tag_info_module.md#parameters)
- [Examples](digital_ocean_tag_info_module.md#examples)
- [Return Values](digital_ocean_tag_info_module.md#return-values)

## [Synopsis](digital_ocean_tag_info_module.md#id1)

- This module can be used to gather information about DigitalOcean provided tags.
- This module was called `digital_ocean_tag_facts` before Ansible 2.9. The usage did not change.

## [Requirements](digital_ocean_tag_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_tag_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **tag_name**  string | Tag name that can be used to identify and reference a tag. |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_tag_info_module.md#id4)

```yaml+jinja
- name: Gather information about all tags
  community.digitalocean.digital_ocean_tag_info:
    oauth_token: "{{ oauth_token }}"

- name: Gather information about tag with given name
  community.digitalocean.digital_ocean_tag_info:
    oauth_token: "{{ oauth_token }}"
    tag_name: "extra_awesome_tag"

- name: Get resources from tag name
  community.digitalocean.digital_ocean_tag_info:
  register: resp_out
- set_fact:
    resources: "{{ item.resources }}"
  loop: "{{ resp_out.data | community.general.json_query(name) }}"
  vars:
    name: "[?name=='extra_awesome_tag']"
- debug:
    var: resources
```

## [Return Values](digital_ocean_tag_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | DigitalOcean tag information  Returned: success  Sample: `[{"name": "extra-awesome", "resources": {"droplets": {"...": null, "count": 1}}}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
