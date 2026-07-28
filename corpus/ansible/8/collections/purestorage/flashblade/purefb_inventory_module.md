---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_inventory module – Collect information from Pure Storage FlashBlade"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_inventory_module.html
fetched_at: 2026-07-28T02:52:02+00:00
---
# purestorage.flashblade.purefb_inventory module – Collect information from Pure Storage FlashBlade

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
> see [Requirements](purefb_inventory_module.md#ansible-collections-purestorage-flashblade-purefb-inventory-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_inventory`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_inventory_module.md#synopsis)
- [Requirements](purefb_inventory_module.md#requirements)
- [Parameters](purefb_inventory_module.md#parameters)
- [Notes](purefb_inventory_module.md#notes)
- [Examples](purefb_inventory_module.md#examples)
- [Return Values](purefb_inventory_module.md#return-values)

## [Synopsis](purefb_inventory_module.md#id1)

- Collect information from a Pure Storage FlashBlade running the Purity//FB operating system. By default, the module will collect basic information including hosts, host groups, protection groups and volume counts. Additional information can be collected based on the configured set of arguements.

## [Requirements](purefb_inventory_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_inventory_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |

## [Notes](purefb_inventory_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_inventory_module.md#id5)

```yaml+jinja
- name: collect FlashBlade inventory
  purestorage.flashblade.purefb_inventory:
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: blade_info
- name: show default information
  debug:
    msg: "{{ blade_info['purefb_info'] }}"
```

## [Return Values](purefb_inventory_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **purefb_inventory**  dictionary | Returns the inventory information for the FlashBlade  **Returned:** always |

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
