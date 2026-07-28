---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_tag module – Create and remove tag(s) to DigitalOcean resource."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_tag_module.html
fetched_at: 2026-07-27T17:06:57+00:00
---
# community.digitalocean.digital_ocean_tag module – Create and remove tag(s) to DigitalOcean resource.

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
> see [Requirements](digital_ocean_tag_module.md#ansible-collections-community-digitalocean-digital-ocean-tag-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_tag`.

- [Synopsis](digital_ocean_tag_module.md#synopsis)
- [Requirements](digital_ocean_tag_module.md#requirements)
- [Parameters](digital_ocean_tag_module.md#parameters)
- [Notes](digital_ocean_tag_module.md#notes)
- [Examples](digital_ocean_tag_module.md#examples)
- [Return Values](digital_ocean_tag_module.md#return-values)

## [Synopsis](digital_ocean_tag_module.md#id1)

- Create and remove tag(s) to DigitalOcean resource.

## [Requirements](digital_ocean_tag_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_tag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **name**  string / required | The name of the tag. The supported characters for names include alphanumeric characters, dashes, and underscores. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **resource_id**  aliases: droplet_id  string | The ID of the resource to operate on.  The data type of resource_id is changed from integer to string since Ansible 2.5. |
| **resource_type**  string | The type of resource to operate on. Currently, only tagging of droplets is supported.  Choices:   - `"droplet"` ← (default) |
| **state**  string | Whether the tag should be present or absent on the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](digital_ocean_tag_module.md#id4)

> **Note:**
>
> - Two environment variables can be used, DO_API_KEY and DO_API_TOKEN. They both refer to the v2 token.
> - As of Ansible 2.0, Version 2 of the DigitalOcean API is used.

## [Examples](digital_ocean_tag_module.md#id5)

```yaml+jinja
- name: Create a tag
  community.digitalocean.digital_ocean_tag:
    name: production
    state: present

- name: Tag a resource; creating the tag if it does not exist
  community.digitalocean.digital_ocean_tag:
    name: "{{ item }}"
    resource_id: "73333005"
    state: present
  loop:
    - staging
    - dbserver

- name: Untag a resource
  community.digitalocean.digital_ocean_tag:
    name: staging
    resource_id: "73333005"
    state: absent

# Deleting a tag also untags all the resources that have previously been
# tagged with it
- name: Remove a tag
  community.digitalocean.digital_ocean_tag:
    name: dbserver
    state: absent
```

## [Return Values](digital_ocean_tag_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | a DigitalOcean Tag resource  Returned: success and no resource constraint  Sample: `{"tag": {"name": "awesome", "resources": {"droplets": {"count": 0, "last_tagged": null}}}}` |

### Authors

- Victor Volle (@kontrafiktion)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
