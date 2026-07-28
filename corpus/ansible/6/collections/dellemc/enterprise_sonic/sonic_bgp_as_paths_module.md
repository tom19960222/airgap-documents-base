---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_bgp_as_paths module – Manage BGP autonomous system path (or as-path-list) and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_bgp_as_paths_module.html
fetched_at: 2026-07-27T17:24:48+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_as_paths module – Manage BGP autonomous system path (or as-path-list) and its parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp_as_paths`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_as_paths_module.md#synopsis)
- [Parameters](sonic_bgp_as_paths_module.md#parameters)
- [Notes](sonic_bgp_as_paths_module.md#notes)
- [Examples](sonic_bgp_as_paths_module.md#examples)
- [Return Values](sonic_bgp_as_paths_module.md#return-values)

## [Synopsis](sonic_bgp_as_paths_module.md#id1)

- This module provides configuration management of BGP bgp_as_paths for devices running Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_as_paths_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of ‘bgp_as_paths’ configurations. |
| **members**  list / elements=string | Members of this BGP as-path; regular expression string can be provided. |
| **name**  string / required | Name of as-path-list. |
| **permit**  boolean | Permits or denies this as path.  Choices:   - `false` - `true` |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_bgp_as_paths_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_as_paths_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# show bgp as-path-access-list
# AS path list test:
#   members: 808.*,909.*

- name: Delete BGP as path list
  dellemc.enterprise_sonic.sonic_bgp_as_paths:
    config:
      - name: test
        members:
        - 909.*
    state: deleted

# After state:
# ------------
#
# show bgp as-path-access-list
# AS path list test:
#   members: 808.*

# Using deleted

# Before state:
# -------------
#
# show bgp as-path-access-list
# AS path list test:
#   members: 808.*,909.*
# AS path list test1:
#   members: 608.*,709.*

- name: Deletes BGP as-path list
  dellemc.enterprise_sonic.sonic_bgp_as_paths:
    config:
      - name: test
        members:
    state: deleted

# After state:
# ------------
#
# show bgp as-path-access-list
# AS path list test1:
#   members: 608.*,709.*

# Using deleted

# Before state:
# -------------
#
# show bgp as-path-access-list
# AS path list test:
#   members: 808.*,909.*

- name: Deletes BGP as-path list
  dellemc.enterprise_sonic.sonic_bgp_as_paths:
    config:
    state: deleted

# After state:
# ------------
#
# show bgp as-path-access-list
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

## [Return Values](sonic_bgp_as_paths_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Kumaraguru Narayanan (@nkumaraguru)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
