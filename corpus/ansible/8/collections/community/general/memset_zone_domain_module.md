---
collection: ansible
version: "8"
title: "community.general.memset_zone_domain module – Create and delete domains in Memset DNS zones"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/memset_zone_domain_module.html
fetched_at: 2026-07-28T01:47:59+00:00
---
# community.general.memset_zone_domain module – Create and delete domains in Memset DNS zones

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.memset_zone_domain`.

- [Synopsis](memset_zone_domain_module.md#synopsis)
- [Parameters](memset_zone_domain_module.md#parameters)
- [Attributes](memset_zone_domain_module.md#attributes)
- [Notes](memset_zone_domain_module.md#notes)
- [Examples](memset_zone_domain_module.md#examples)
- [Return Values](memset_zone_domain_module.md#return-values)

## [Synopsis](memset_zone_domain_module.md#id1)

- Manage DNS zone domains in a Memset account.

Aliases: cloud.memset.memset_zone_domain

## [Parameters](memset_zone_domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The API key obtained from the Memset control panel. |
| **domain**  aliases: name  string / required | The zone domain name. Ensure this value has at most 250 characters. |
| **state**  string | Indicates desired state of resource.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **zone**  string / required | The zone to add the domain to (this must already exist). |

## [Attributes](memset_zone_domain_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](memset_zone_domain_module.md#id4)

> **Note:**
>
> - Zone domains can be thought of as a collection of domains, all of which share the same DNS records (i.e. they point to the same IP). An API key generated via the Memset customer control panel is needed with the following minimum scope - `dns.zone_domain_create`, `dns.zone_domain_delete`, `dns.zone_domain_list`.
> - Currently this module can only create one domain at a time. Multiple domains should be created using `loop`.

## [Examples](memset_zone_domain_module.md#id5)

```yaml+jinja
# Create the zone domain 'test.com'
- name: Create zone domain
  community.general.memset_zone_domain:
    domain: test.com
    zone: testzone
    state: present
    api_key: 5eb86c9196ab03919abcf03857163741
  delegate_to: localhost
```

## [Return Values](memset_zone_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **memset_api**  complex | Domain info from the Memset API  **Returned:** when changed or state == present |
| **domain**  string | Domain name  **Returned:** always  **Sample:** `"example.com"` |
| **id**  string | Domain ID  **Returned:** always  **Sample:** `"b0bb1ce851aeea6feeb2dc32fe83bf9c"` |

### Authors

- Simon Weald (@glitchcrab)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
