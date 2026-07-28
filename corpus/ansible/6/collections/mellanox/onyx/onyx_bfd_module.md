---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_bfd module – Configures BFD parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_bfd_module.html
fetched_at: 2026-07-27T17:55:22+00:00
---
# mellanox.onyx.onyx_bfd module – Configures BFD parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_bfd`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_bfd_module.md#synopsis)
- [Parameters](onyx_bfd_module.md#parameters)
- [Examples](onyx_bfd_module.md#examples)
- [Return Values](onyx_bfd_module.md#return-values)

## [Synopsis](onyx_bfd_module.md#id1)

- This module provides declarative management of BFD protocol params on Mellanox ONYX network devices.

## [Parameters](onyx_bfd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interval_min_rx**  integer | Minimum desired receive rate, should be between 50 and 6000. |
| **interval_multiplier**  integer | Desired detection multiplier, should be between 3 and 50. |
| **interval_transmit_rate**  integer | Minimum desired transmit rate, should be between 50 and 60000. |
| **iproute_mask_length**  integer | Configures the mask length of the ip route network prefix, e.g 24. |
| **iproute_network_prefix**  string | Configures the ip route network prefix, e.g 1.1.1.1. |
| **iproute_next_hop**  string | Configures the ip route next hop, e.g 2.2.2.2. |
| **shutdown**  boolean | Administratively shut down BFD protection.  Choices:   - `false` - `true` |
| **vrf**  string | Specifys the vrf name. |

## [Examples](onyx_bfd_module.md#id3)

```yaml+jinja
- name: Configures bfd
  onyx_bfd:
    shutdown: yes
    vrf: 5
    interval_min_rx: 55
    interval_multiplier: 8
    interval_transmit_rate: 88
    iproute_network_prefix: 1.1.1.0
    iproute_mask_length: 24
    iproute_next_hop: 3.2.2.2
```

## [Return Values](onyx_bfd_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["ip bfd shutdown", "no ip bfd shutdown", "ip bfd shutdown vrf <vrf_name>", "no ip bfd shutdown vrf <vrf_name>", "ip bfd vrf <vrf_name> interval min-rx <min_rx> multiplier <multiplier> transmit-rate <transmit_rate> force", "ip bfd interval min-rx <min_rx> multiplier <multiplier> transmit-rate <transmit_rate> force", "ip route vrf <vrf_name> <network_prefix>/<mask_length> <next_hop> bfd", "ip route <network_prefix>/<mask_length> <next_hop> bfd"]` |

### Authors

- Sara Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
