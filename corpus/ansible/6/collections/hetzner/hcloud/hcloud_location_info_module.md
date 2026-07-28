---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_location_info module – Gather infos about your Hetzner Cloud locations."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_location_info_module.html
fetched_at: 2026-07-27T17:49:45+00:00
---
# hetzner.hcloud.hcloud_location_info module – Gather infos about your Hetzner Cloud locations.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_location_info_module.md#ansible-collections-hetzner-hcloud-hcloud-location-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_location_info`.

- [Synopsis](hcloud_location_info_module.md#synopsis)
- [Requirements](hcloud_location_info_module.md#requirements)
- [Parameters](hcloud_location_info_module.md#parameters)
- [See Also](hcloud_location_info_module.md#see-also)
- [Examples](hcloud_location_info_module.md#examples)
- [Return Values](hcloud_location_info_module.md#return-values)

## [Synopsis](hcloud_location_info_module.md#id1)

- Gather infos about your Hetzner Cloud locations.
- This module was called `hcloud_location_facts` before Ansible 2.9, returning `ansible_facts` and `hcloud_location_facts`. Note that the [hetzner.hcloud.hcloud_location_info](hcloud_location_info_module.md#ansible-collections-hetzner-hcloud-hcloud-location-info-module) module no longer returns `ansible_facts` and the value was renamed to `hcloud_location_info`!

## [Requirements](hcloud_location_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_location_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the location you want to get. |
| **name**  string | The name of the location you want to get. |

## [See Also](hcloud_location_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_location_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud location infos
  hcloud_location_info:
  register: output

- name: Print the gathered infos
  debug:
    var: output
```

## [Return Values](hcloud_location_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_location_info**  complex | The location infos as list  Returned: always |
| **city**  string | City of the location  Returned: always  Sample: `"Falkenstein"` |
| **country**  string | Country code of the location  Returned: always  Sample: `"DE"` |
| **description**  string | Detail description of the location  Returned: always  Sample: `"Falkenstein DC Park 1"` |
| **id**  integer | Numeric identifier of the location  Returned: always  Sample: `1937415` |
| **name**  string | Name of the location  Returned: always  Sample: `"fsn1"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
