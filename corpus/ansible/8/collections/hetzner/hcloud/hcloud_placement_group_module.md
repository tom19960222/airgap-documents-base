---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_placement_group module – Create and manage placement groups on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_placement_group_module.html
fetched_at: 2026-07-28T02:34:06+00:00
---
# hetzner.hcloud.hcloud_placement_group module – Create and manage placement groups on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_placement_group_module.md#ansible-collections-hetzner-hcloud-hcloud-placement-group-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_placement_group`.

- [Synopsis](hcloud_placement_group_module.md#synopsis)
- [Requirements](hcloud_placement_group_module.md#requirements)
- [Parameters](hcloud_placement_group_module.md#parameters)
- [See Also](hcloud_placement_group_module.md#see-also)
- [Examples](hcloud_placement_group_module.md#examples)
- [Return Values](hcloud_placement_group_module.md#return-values)

## [Synopsis](hcloud_placement_group_module.md#id1)

- Create, update and manage placement groups on the Hetzner Cloud.

## [Requirements](hcloud_placement_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.15.0
- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_placement_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Hetzner Cloud placement group to manage.  Only required if no placement group *name* is given |
| **labels**  dictionary | User-defined labels (key-value pairs) |
| **name**  string | The Name of the Hetzner Cloud placement group to manage.  Only required if no placement group *id* is given, or a placement group does not exist. |
| **state**  string | State of the placement group.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string | The Type of the Hetzner Cloud placement group. |

## [See Also](hcloud_placement_group_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_placement_group_module.md#id5)

```yaml+jinja
- name: Create a basic placement group
  hcloud_placement_group:
    name: my-placement-group
    state: present
    type: spread

- name: Create a placement group with labels
  hcloud_placement_group:
    name: my-placement-group
    type: spread
    labels:
        key: value
        mylabel: 123
    state: present

- name: Ensure the placement group is absent (remove if needed)
  hcloud_placement_group:
    name: my-placement-group
    state: absent
```

## [Return Values](hcloud_placement_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_placement_group**  complex | The placement group instance  **Returned:** Always |
| **id**  integer | Numeric identifier of the placement group  **Returned:** always  **Sample:** `1937415` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **name**  string | Name of the placement group  **Returned:** always  **Sample:** `"my placement group"` |
| **servers**  list / elements=integer | Server IDs of the placement group  **Returned:** always  **Sample:** `[4711, 4712]` |
| **type**  string | Type of the placement group  **Returned:** always  **Sample:** `"spread"` |

### Authors

- Adrian Huber (@Adi146)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
