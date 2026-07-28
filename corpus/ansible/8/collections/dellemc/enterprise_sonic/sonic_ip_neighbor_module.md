---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_ip_neighbor module – Manage IP neighbor global configuration on SONiC."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_ip_neighbor_module.html
fetched_at: 2026-07-28T02:03:37+00:00
---
# dellemc.enterprise_sonic.sonic_ip_neighbor module – Manage IP neighbor global configuration on SONiC.

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_ip_neighbor`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_ip_neighbor_module.md#synopsis)
- [Parameters](sonic_ip_neighbor_module.md#parameters)
- [Examples](sonic_ip_neighbor_module.md#examples)
- [Return Values](sonic_ip_neighbor_module.md#return-values)

## [Synopsis](sonic_ip_neighbor_module.md#id1)

- This module provides configuration management of IP neighbor global for devices running SONiC.

## [Parameters](sonic_ip_neighbor_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies IP neighbor global configurations. |
| **ipv4_arp_timeout**  integer | IPv4 ARP timeout.  The range is from 60 to 14400. |
| **ipv4_drop_neighbor_aging_time**  integer | IPv4 drop neighbor aging time.  The range is from 60 to 14400. |
| **ipv6_drop_neighbor_aging_time**  integer | IPv6 drop neighbor aging time.  The range is from 60 to 14400. |
| **ipv6_nd_cache_expiry**  integer | IPv6 ND cache expiry.  The range is from 60 to 14400. |
| **num_local_neigh**  integer | The number of reserved local neighbors.  The range is from 0 to 32000. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_ip_neighbor_module.md#id3)

```yaml+jinja
#
# Using merged
#
# Before state:
# -------------
#
#sonic# show running-configuration
#!
#ip arp timeout 180
#ip drop-neighbor aging-time 300
#ipv6 drop-neighbor aging-time 300
#ip reserve local-neigh 0
#ipv6 nd cache expire 180
#!
- name: Configure IP neighbor global
  sonic_ip_neighbor:
    config:
      ipv4_arp_timeout: 1200
      ipv4_drop_neighbor_aging_time: 600
      ipv6_drop_neighbor_aging_time: 600
      ipv6_nd_cache_expiry: 1200
      num_local_neigh: 1000
    state: merged

# After state:
# ------------
#
#sonic# show running-configuration
#!
#ip arp timeout 1200
#ip drop-neighbor aging-time 600
#ipv6 drop-neighbor aging-time 600
#ip reserve local-neigh 1000
#ipv6 nd cache expire 1200
#!
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show running-configuration
#!
#ip arp timeout 1200
#ip drop-neighbor aging-time 600
#ipv6 drop-neighbor aging-time 600
#ip reserve local-neigh 1000
#ipv6 nd cache expire 1200
#!
- name: Delete some IP neighbor configuration
  sonic_ip_neighbor:
    config:
      ipv4_arp_timeout: 0
      ipv4_drop_neighbor_aging_time: 0
    state: deleted

# After state:
# ------------
#
#sonic# show running-configuration
#!
#ip arp timeout 180
#ip drop-neighbor aging-time 300
#ipv6 drop-neighbor aging-time 600
#ip reserve local-neigh 1000
#ipv6 nd cache expire 1200
#!
#
# Using deleted
#
# Before state:
# -------------
#
#sonic# show running-configuration
#!
#ip arp timeout 1200
#ip drop-neighbor aging-time 600
#ipv6 drop-neighbor aging-time 600
#ip reserve local-neigh 1000
#ipv6 nd cache expire 1200
#!
- name: Delete all IP neighbor configuration
  sonic_ip_neighbor:
    config: {}
    state: deleted

# After state:
# ------------
#
#sonic# show running-configuration
#!
#ip arp timeout 180
#ip drop-neighbor aging-time 300
#ipv6 drop-neighbor aging-time 300
#ip reserve local-neigh 0
#ipv6 nd cache expire 180
#!
#
# Using replaced
#
# Before state:
# -------------
#
#sonic# show running-configuration
#!
#ip arp timeout 1200
#ip drop-neighbor aging-time 600
#ipv6 drop-neighbor aging-time 300
#ip reserve local-neigh 0
#ipv6 nd cache expire 180
#!
- name: Change some IP neighbor configuration
  sonic_ip_neighbor:
    config:
      ipv6_drop_neighbor_aging_time: 600
      ipv6_nd_cache_expiry: 1200
      num_local_neigh: 1000
    state: replaced

# After state:
# ------------
#
#sonic# show running-configuration
#!
#ip arp timeout 1200
#ip drop-neighbor aging-time 600
#ipv6 drop-neighbor aging-time 600
#ip reserve local-neigh 1000
#ipv6 nd cache expire 1200
#!
#
# Using overridden
#
# Before state:
# -------------
#
#sonic# show running-configuration
#!
#ip arp timeout 1200
#ip drop-neighbor aging-time 600
#ipv6 drop-neighbor aging-time 300
#ip reserve local-neigh 0
#ipv6 nd cache expire 180
#!
- name: Reset IP neighbor configuration, then configure some
  sonic_ip_neighbor:
    config:
      ipv6_drop_neighbor_aging_time: 600
      ipv6_nd_cache_expiry: 1200
      num_local_neigh: 1000
    state: overridden

# After state:
# ------------
#
#sonic# show running-configuration
#!
#ip arp timeout 180
#ip drop-neighbor aging-time 300
#ipv6 drop-neighbor aging-time 600
#ip reserve local-neigh 1000
#ipv6 nd cache expire 1200
#!
#
```

## [Return Values](sonic_ip_neighbor_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- 13. Zhang (@mingjunzhang2019)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
