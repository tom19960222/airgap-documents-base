---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_lag module – Manage FlashBlade Link Aggregation Groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_lag_module.html
fetched_at: 2026-07-28T02:52:04+00:00
---
# purestorage.flashblade.purefb_lag module – Manage FlashBlade Link Aggregation Groups

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_lag_module.md#ansible-collections-purestorage-flashblade-purefb-lag-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_lag`.

New in purestorage.flashblade 1.7.0

- [Synopsis](purefb_lag_module.md#synopsis)
- [Requirements](purefb_lag_module.md#requirements)
- [Parameters](purefb_lag_module.md#parameters)
- [Notes](purefb_lag_module.md#notes)
- [Examples](purefb_lag_module.md#examples)
- [Return Values](purefb_lag_module.md#return-values)

## [Synopsis](purefb_lag_module.md#id1)

- Maintain FlashBlade Link Aggregation Groups

## [Requirements](purefb_lag_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_lag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string | Name of the Link Aggregation Group  **Default:** `"uplink"` |
| **ports**  list / elements=string | Name of network ports assigned to the LAG  Format should be CHx.ETHy, where CHx is the chassis number and ETHy is the ethernet port number.  Matched port pairs from each Fabric Module in the Chassis will be used.  To modify required ports for a LAG specify only the ports required by the LAG. Any ports currently used by the LAG not specified will be disconnected from the LAG. |
| **state**  string | Define whether the LAG should be added or deleted  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_lag_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_lag_module.md#id5)

```yaml+jinja
- name: Add LAG
  purestorage.flashblade.purefb_lag:
    name: lag2
    ports:
    - ch1.eth2
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Upate LAG
  purestorage.flashblade.purefb_lag:
    name: lag2
    ports:
    - ch1.eth2
    - ch1.eth4
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Delete LAG
  purestorage.flashblade.purefb_lag:
    name: lag2
    state: absent
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

## [Return Values](purefb_lag_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lag**  dictionary | A dictionary describing the LAG.  **Returned:** success |
| **lag_speed**  string | Combined speed of all ports in the LAG in Gb/s  **Returned:** success |
| **mac_address**  string | Unique MAC address assigned to the LAG  **Returned:** success |
| **port_speed**  string | Configured speed of each port in the LAG in Gb/s  **Returned:** success |
| **status**  string | Health status of the LAG.  **Returned:** success |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
