---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_bgp_communities module – Manage BGP community and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_bgp_communities_module.html
fetched_at: 2026-07-27T17:24:49+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_communities module – Manage BGP community and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp_communities`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_communities_module.md#synopsis)
- [Parameters](sonic_bgp_communities_module.md#parameters)
- [Notes](sonic_bgp_communities_module.md#notes)
- [Examples](sonic_bgp_communities_module.md#examples)
- [Return Values](sonic_bgp_communities_module.md#return-values)

## [Synopsis](sonic_bgp_communities_module.md#id1)

- This module provides configuration management of BGP bgp_communities for device running Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_communities_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of ‘bgp_communities’ configurations. |
| **aann**  string | Community number aa:nn format 0..65535:0..65535; applicable for standard BGP community type. |
| **local_as**  boolean | Do not send outside local AS (well-known community); applicable for standard BGP community type.  Choices:   - `false` - `true` |
| **match**  string | Matches any/all of the members.  Choices:   - `"ALL"` - `"ANY"` ← (default) |
| **members**  dictionary | Members of this BGP community list. |
| **regex**  list / elements=string | Members of this BGP community list. Regular expression string can be given here. Applicable for expanded BGP community type. |
| **name**  string / required | Name of the BGP communitylist. |
| **no_advertise**  boolean | Do not advertise to any peer (well-known community); applicable for standard BGP community type.  Choices:   - `false` - `true` |
| **no_export**  boolean | Do not export to next AS (well-known community); applicable for standard BGP community type.  Choices:   - `false` - `true` |
| **no_peer**  boolean | Do not export to next AS (well-known community); applicable for standard BGP community type.  Choices:   - `false` - `true` |
| **permit**  boolean | Permits or denies this community.  Choices:   - `false` - `true` |
| **type**  string | Whether it is a standard or expanded community-list entry.  Choices:   - `"standard"` ← (default) - `"expanded"` |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_bgp_communities_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_communities_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# show bgp community-list
# Standard community list test:  match: ANY
#     101
#     201
# Standard community list test1:  match: ANY
#     301

- name: Deletes BGP community member
  dellemc.enterprise_sonic.sonic_bgp_communities:
    config:
      - name: test
        members:
          regex:
          - 201
    state: deleted

# After state:
# ------------
#
# show bgp community-list
# Standard community list test:  match: ANY
#     101
# Standard community list test1:  match: ANY
#     301

# Using deleted

# Before state:
# -------------
#
# show bgp community-list
# Standard community list test:  match: ANY
#     101
# Expanded community list test1:   match: ANY
#     201

- name: Deletes a single BGP community
  dellemc.enterprise_sonic.sonic_bgp_communities:
    config:
      - name: test
        members:
    state: deleted

# After state:
# ------------
#
# show bgp community-list
# Expanded community list test1:   match: ANY
#     201

# Using deleted

# Before state:
# -------------
#
# show bgp community-list
# Standard community list test:  match: ANY
#     101
# Expanded community list test1:   match: ANY
#     201

- name: Delete All BGP communities
  dellemc.enterprise_sonic.sonic_bgp_communities:
    config:
    state: deleted

# After state:
# ------------
#
# show bgp community-list
#

# Using deleted

# Before state:
# -------------
#
# show bgp community-list
# Standard community list test:  match: ANY
#     101
# Expanded community list test1:   match: ANY
#     201

- name: Deletes all members in a single BGP community
  dellemc.enterprise_sonic.sonic_bgp_communities:
    config:
      - name: test
        members:
          regex:
    state: deleted

# After state:
# ------------
#
# show bgp community-list
# Expanded community list test:   match: ANY
# Expanded community list test1:   match: ANY
#     201

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

## [Return Values](sonic_bgp_communities_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration that is returned is always in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration that is returned is always in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands that are pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Kumaraguru Narayanan (@nkumaraguru)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
