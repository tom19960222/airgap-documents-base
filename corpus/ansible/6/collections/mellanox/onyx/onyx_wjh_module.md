---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_wjh module – Configure what-just-happend module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_wjh_module.html
fetched_at: 2026-07-27T17:55:46+00:00
---
# mellanox.onyx.onyx_wjh module – Configure what-just-happend module

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_wjh`.

- [Synopsis](onyx_wjh_module.md#synopsis)
- [Parameters](onyx_wjh_module.md#parameters)
- [Examples](onyx_wjh_module.md#examples)
- [Return Values](onyx_wjh_module.md#return-values)

## [Synopsis](onyx_wjh_module.md#id1)

- This module provides declarative management of wjh on Mellanox ONYX network devices.

## [Parameters](onyx_wjh_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_export**  boolean | wjh group auto export pcap file status  Choices:   - `false` - `true` |
| **clear_group**  string | clear pcap file by group  Choices:   - `"all"` - `"user"` - `"auto-export"` |
| **enabled**  boolean | wjh group status  Choices:   - `false` - `true` |
| **export_group**  string | wjh group auto export group  Choices:   - `"all"` - `"forwarding"` - `"acl"` |
| **group**  string | Name of wjh group.  Choices:   - `"all"` - `"forwarding"` - `"acl"` |

## [Examples](onyx_wjh_module.md#id3)

```yaml+jinja
- name: Enable wjh
  onyx_wjh:
      group: forwarding
      enabled: True

- name: Disable wjh
  onyx_wjh:
      group: forwarding
      enabled: False

- name: Enable auto-export
  onyx_wjh:
        auto_export: True
        export_group: forwarding
- name: Disable auto-export
  onyx_wjh:
        auto_export: False
        export_group: forwarding
- name: Clear pcap file
  onyx_wjh:
        clear_group: auto-export
```

## [Return Values](onyx_wjh_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["what-just-happend forwarding enable", "what-just-happend auto-export forwarding enable", "clear what-just-happend pcap-file user"]` |

### Authors

- Anas Shami (@anass)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
