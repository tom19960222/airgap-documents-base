---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_buffer_pool module – Configures Buffer Pool"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_buffer_pool_module.html
fetched_at: 2026-07-27T17:55:23+00:00
---
# mellanox.onyx.onyx_buffer_pool module – Configures Buffer Pool

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_buffer_pool`.

- [Synopsis](onyx_buffer_pool_module.md#synopsis)
- [Parameters](onyx_buffer_pool_module.md#parameters)
- [Notes](onyx_buffer_pool_module.md#notes)
- [Examples](onyx_buffer_pool_module.md#examples)
- [Return Values](onyx_buffer_pool_module.md#return-values)

## [Synopsis](onyx_buffer_pool_module.md#id1)

- This module provides declarative management of Onyx Buffer Pool configuration on Mellanox ONYX network devices.

## [Parameters](onyx_buffer_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **memory_percent**  string | memory percent. |
| **name**  string / required | pool name. |
| **pool_type**  string | pool type.  Choices:   - `"lossless"` - `"lossy"` ← (default) |
| **switch_priority**  string | switch priority, range 1-7. |

## [Notes](onyx_buffer_pool_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.8130

## [Examples](onyx_buffer_pool_module.md#id4)

```yaml+jinja
- name: Configure buffer pool
  onyx_buffer_pool:
    name: roce
    pool_type: lossless
    memory_percent: 50.00
    switch_priority: 3
```

## [Return Values](onyx_buffer_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["traffic pool roce type lossless", "traffic pool roce memory percent 50.00", "traffic pool roce map switch-priority 3"]` |

### Authors

- Anas Badaha (@anasb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
