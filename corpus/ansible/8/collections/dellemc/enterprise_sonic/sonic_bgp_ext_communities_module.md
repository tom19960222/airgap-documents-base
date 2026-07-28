---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_bgp_ext_communities module – Manage BGP extended community-list and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_bgp_ext_communities_module.html
fetched_at: 2026-07-28T02:03:30+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_ext_communities module – Manage BGP extended community-list and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp_ext_communities`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_ext_communities_module.md#synopsis)
- [Parameters](sonic_bgp_ext_communities_module.md#parameters)
- [Notes](sonic_bgp_ext_communities_module.md#notes)
- [Examples](sonic_bgp_ext_communities_module.md#examples)
- [Return Values](sonic_bgp_ext_communities_module.md#return-values)

## [Synopsis](sonic_bgp_ext_communities_module.md#id1)

- This module provides configuration management of BGP extcommunity-list for devices running Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_ext_communities_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of ‘bgp_extcommunity_list’ configurations. |
| **match**  string | Matches any/all of the the members.  **Choices:**   - `"all"` - `"any"` ← (default) |
| **members**  dictionary | Members of this BGP ext community list. |
| **regex**  list / elements=string | Members of this BGP ext community list. Regular expression string can be given here. Applicable for expanded ext BGP community type. |
| **route_origin**  list / elements=string | Members of this BGP ext community list. The format of route_origin is in either 0..65535:0..65535 or A.B.C.D:[1..65535] format. |
| **route_target**  list / elements=string | Members of this BGP ext community list. The format of route_target is in either 0..65535:0..65535 or A.B.C.D:[1..65535] format. |
| **name**  string / required | Name of the BGP ext communitylist. |
| **permit**  boolean | Permits or denies this community.  **Choices:**   - `false` - `true` |
| **type**  string | Whether it is a standard or expanded ext community_list entry.  **Choices:**   - `"standard"` ← (default) - `"expanded"` |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_bgp_ext_communities_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_ext_communities_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     rt:101:101
#     rt:201:201

- name: Deletes a BGP ext community member
  dellemc.enterprise_sonic.sonic_bgp_ext_communities:
    config:
      - name: test
        members:
          regex:
          - 201:201
    state: deleted

# After state:
# ------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     rt:101:101
#

# Using deleted

# Before state:
# -------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     101
# Expanded extended community list test1:   match: ANY
#     201

- name: Deletes a single BGP extended community
  dellemc.enterprise_sonic.sonic_bgp_ext_communities:
    config:
      - name: test1
        members:
    state: deleted

# After state:
# ------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     101
#

# Using deleted

# Before state:
# -------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     101
# Expanded extended community list test1:   match: ANY
#     201

- name: Deletes all BGP extended communities
  dellemc.enterprise_sonic.sonic_bgp_ext_communities:
    config:
    state: deleted

# After state:
# ------------
#
# show bgp ext-community-list
#

# Using deleted

# Before state:
# -------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     101
# Expanded extended community list test1:   match: ANY
#     201

- name: Deletes all members in a single BGP extended community
  dellemc.enterprise_sonic.sonic_bgp_ext_communities:
    config:
      - name: test1
        members:
          regex:
    state: deleted

# After state:
# ------------
#
# show bgp ext-community-list
# Standard extended community list test:  match: ANY
#     101
# Expanded extended community list test1:   match: ANY
#

# Using merged

# Before state:
# -------------
#
# show bgp as-path-access-list
# AS path list test:

- name: Adds 909.* to test as-path list
  dellemc.enterprise_sonic.sonic_bgp_as_paths:
    config:
      - name: test
        members:
        - 909.*
    state: merged

# After state:
# ------------
#
# show bgp as-path-access-list
# AS path list test:
#   members: 909.*
```

## [Return Values](sonic_bgp_ext_communities_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Kumaraguru Narayanan (@nkumaraguru)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
