---
collection: ansible
version: "6"
title: "community.fortios.fmgr_secprof_dns module – Manage DNS security profiles in FortiManager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_secprof_dns_module.html
fetched_at: 2026-07-27T17:07:49+00:00
---
# community.fortios.fmgr_secprof_dns module – Manage DNS security profiles in FortiManager

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_dns`.

- [Synopsis](fmgr_secprof_dns_module.md#synopsis)
- [Parameters](fmgr_secprof_dns_module.md#parameters)
- [Notes](fmgr_secprof_dns_module.md#notes)
- [Examples](fmgr_secprof_dns_module.md#examples)
- [Return Values](fmgr_secprof_dns_module.md#return-values)

## [Synopsis](fmgr_secprof_dns_module.md#id1)

- Manage DNS security profiles in FortiManager

## [Parameters](fmgr_secprof_dns_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **block_action**  string | Action to take for blocked domains.  choice | block | Return NXDOMAIN for blocked domains.  choice | redirect | Redirect blocked domains to SDNS portal.  Choices:   - `"block"` - `"redirect"` |
| **block_botnet**  string | Enable/disable blocking botnet C&C; DNS lookups.  choice | disable | Disable blocking botnet C&C; DNS lookups.  choice | enable | Enable blocking botnet C&C; DNS lookups.  Choices:   - `"disable"` - `"enable"` |
| **comment**  string | Comment for the security profile to show in the FortiManager GUI. |
| **domain_filter_domain_filter_table**  string | DNS domain filter table ID. |
| **external_ip_blocklist**  string | One or more external IP block lists. |
| **ftgd_dns_filters_action**  string | Action to take for DNS requests matching the category.  choice | monitor | Allow DNS requests matching the category and log the result.  choice | block | Block DNS requests matching the category.  Choices:   - `"monitor"` - `"block"` |
| **ftgd_dns_filters_category**  string | Category number. |
| **ftgd_dns_filters_log**  string | Enable/disable DNS filter logging for this DNS profile.  choice | disable | Disable DNS filter logging.  choice | enable | Enable DNS filter logging.  Choices:   - `"disable"` - `"enable"` |
| **ftgd_dns_options**  string | FortiGuard DNS filter options.  FLAG Based Options. Specify multiple in list form.  flag | error-allow | Allow all domains when FortiGuard DNS servers fail.  flag | ftgd-disable | Disable FortiGuard DNS domain rating.  Choices:   - `"error-allow"` - `"ftgd-disable"` |
| **log_all_domain**  string | Enable/disable logging of all domains visited (detailed DNS logging).  choice | disable | Disable logging of all domains visited.  choice | enable | Enable logging of all domains visited.  Choices:   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values.  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Profile name. |
| **redirect_portal**  string | IP address of the SDNS redirect portal. |
| **safe_search**  string | Enable/disable Google, Bing, and YouTube safe search.  choice | disable | Disable Google, Bing, and YouTube safe search.  choice | enable | Enable Google, Bing, and YouTube safe search.  Choices:   - `"disable"` - `"enable"` |
| **sdns_domain_log**  string | Enable/disable domain filtering and botnet domain logging.  choice | disable | Disable domain filtering and botnet domain logging.  choice | enable | Enable domain filtering and botnet domain logging.  Choices:   - `"disable"` - `"enable"` |
| **sdns_ftgd_err_log**  string | Enable/disable FortiGuard SDNS rating error logging.  choice | disable | Disable FortiGuard SDNS rating error logging.  choice | enable | Enable FortiGuard SDNS rating error logging.  Choices:   - `"disable"` - `"enable"` |
| **youtube_restrict**  string | Set safe search for YouTube restriction level.  choice | strict | Enable strict safe seach for YouTube.  choice | moderate | Enable moderate safe search for YouTube.  Choices:   - `"strict"` - `"moderate"` |

## [Notes](fmgr_secprof_dns_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_dns_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_dns:
    name: "Ansible_DNS_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_dns:
    name: "Ansible_DNS_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "set"
    block_action: "block"
```

## [Return Values](fmgr_secprof_dns_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
