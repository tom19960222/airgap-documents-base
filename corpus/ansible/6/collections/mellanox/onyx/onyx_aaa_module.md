---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_aaa module – Configures AAA parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_aaa_module.html
fetched_at: 2026-07-27T17:55:21+00:00
---
# mellanox.onyx.onyx_aaa module – Configures AAA parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_aaa`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_aaa_module.md#synopsis)
- [Parameters](onyx_aaa_module.md#parameters)
- [Examples](onyx_aaa_module.md#examples)
- [Return Values](onyx_aaa_module.md#return-values)

## [Synopsis](onyx_aaa_module.md#id1)

- This module provides declarative management of AAA protocol params on Mellanox ONYX network devices.

## [Parameters](onyx_aaa_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_default_user**  string | Sets local user default mapping.  Choices:   - `"admin"` - `"monitor"` |
| **auth_fallback_enabled**  boolean | Enables/Disables fallback server-err option.  Choices:   - `false` - `true` |
| **auth_order**  string | Sets the order on how to handle remote to local user mappings.  Choices:   - `"local-only"` - `"remote-first"` - `"remote-only"` |
| **tacacs_accounting_enabled**  boolean | Configures accounting settings.  Choices:   - `false` - `true` |

## [Examples](onyx_aaa_module.md#id3)

```yaml+jinja
- name: Configures aaa
  onyx_aaa:
    tacacs_accounting_enabled: yes
    auth_default_user: monitor
    auth_order: local-only
    auth_fallback_enabled: false
```

## [Return Values](onyx_aaa_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["aaa accounting changes default stop-only tacacs+", "no aaa accounting changes default stop-only tacacs+", "aaa authorization map default-user <user>", "aaa authorization map order <order>", "aaa authorization map fallback server-err", "no aaa authorization map fallback server-err"]` |

### Authors

- Sara Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
