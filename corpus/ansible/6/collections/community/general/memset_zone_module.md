---
collection: ansible
version: "6"
title: "community.general.memset_zone module – Creates and deletes Memset DNS zones"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/memset_zone_module.html
fetched_at: 2026-07-27T17:10:56+00:00
---
# community.general.memset_zone module – Creates and deletes Memset DNS zones

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.memset_zone`.

- [Synopsis](memset_zone_module.md#synopsis)
- [Parameters](memset_zone_module.md#parameters)
- [Notes](memset_zone_module.md#notes)
- [Examples](memset_zone_module.md#examples)
- [Return Values](memset_zone_module.md#return-values)

## [Synopsis](memset_zone_module.md#id1)

- Manage DNS zones in a Memset account.

## [Parameters](memset_zone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The API key obtained from the Memset control panel. |
| **force**  boolean | Forces deletion of a zone and all zone domains/zone records it contains.  Choices:   - `false` ← (default) - `true` |
| **name**  aliases: nickname  string / required | The zone nickname; usually the same as the main domain. Ensure this value has at most 250 characters. |
| **state**  string / required | Indicates desired state of resource.  Choices:   - `"absent"` - `"present"` |
| **ttl**  integer | The default TTL for all records created in the zone. This must be a valid int from <https://www.memset.com/apidocs/methods_dns.html#dns.zone_create>.  Choices:   - `0` ← (default) - `300` - `600` - `900` - `1800` - `3600` - `7200` - `10800` - `21600` - `43200` - `86400` |

## [Notes](memset_zone_module.md#id3)

> **Note:**
>
> - Zones can be thought of as a logical group of domains, all of which share the same DNS records (i.e. they point to the same IP). An API key generated via the Memset customer control panel is needed with the following minimum scope - *dns.zone_create*, *dns.zone_delete*, *dns.zone_list*.

## [Examples](memset_zone_module.md#id4)

```yaml+jinja
# Create the zone 'test'
- name: Create zone
  community.general.memset_zone:
    name: test
    state: present
    api_key: 5eb86c9196ab03919abcf03857163741
    ttl: 300
  delegate_to: localhost

# Force zone deletion
- name: Force delete zone
  community.general.memset_zone:
    name: test
    state: absent
    api_key: 5eb86c9196ab03919abcf03857163741
    force: true
  delegate_to: localhost
```

## [Return Values](memset_zone_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **memset_api**  complex | Zone info from the Memset API  Returned: when state == present |
| **domains**  list / elements=string | List of domains in this zone  Returned: always  Sample: `[]` |
| **id**  string | Zone id  Returned: always  Sample: `"b0bb1ce851aeea6feeb2dc32fe83bf9c"` |
| **nickname**  string | Zone name  Returned: always  Sample: `"example.com"` |
| **records**  list / elements=string | List of DNS records for domains in this zone  Returned: always  Sample: `[]` |
| **ttl**  integer | Default TTL for domains in this zone  Returned: always  Sample: `300` |

### Authors

- Simon Weald (@glitchcrab)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
