---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_igmp module – Configures IGMP global parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_igmp_module.html
fetched_at: 2026-07-27T17:55:26+00:00
---
# mellanox.onyx.onyx_igmp module – Configures IGMP global parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_igmp`.

- [Synopsis](onyx_igmp_module.md#synopsis)
- [Parameters](onyx_igmp_module.md#parameters)
- [Notes](onyx_igmp_module.md#notes)
- [Examples](onyx_igmp_module.md#examples)
- [Return Values](onyx_igmp_module.md#return-values)

## [Synopsis](onyx_igmp_module.md#id1)

- This module provides declarative management of IGMP protocol params on Mellanox ONYX network devices.

## [Parameters](onyx_igmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **default_version**  string | Configure the default operating version of the IGMP snooping  Choices:   - `"V2"` - `"V3"` |
| **last_member_query_interval**  string | Configure the last member query interval, range 1-25 |
| **mrouter_timeout**  string | Configure the mrouter timeout, range 60-600 |
| **port_purge_timeout**  string | Configure the host port purge timeout, range 130-1225 |
| **proxy_reporting**  string | Configure ip igmp snooping proxy and enable reporting mode  Choices:   - `"enabled"` - `"disabled"` |
| **report_suppression_interval**  string | Configure the report suppression interval, range 1-25 |
| **state**  string / required | IGMP state.  Choices:   - `"enabled"` - `"disabled"` |
| **unregistered_multicast**  string | Configure the unregistered multicast mode Flood unregistered multicast Forward unregistered multicast to mrouter ports  Choices:   - `"flood"` - `"forward-to-mrouter-ports"` |

## [Notes](onyx_igmp_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.6107

## [Examples](onyx_igmp_module.md#id4)

```yaml+jinja
- name: Configure igmp
  onyx_igmp:
    state: enabled
    unregistered_multicast: flood
```

## [Return Values](onyx_igmp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["ip igmp snooping", "ip igmp snooping last-member-query-interval 10", "ip igmp snooping mrouter-timeout 150", "ip igmp snooping port-purge-timeout 150"]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
