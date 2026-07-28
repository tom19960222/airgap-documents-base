---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_inventory module – Collect information from Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_inventory_module.html
fetched_at: 2026-07-28T02:51:02+00:00
---
# purestorage.flasharray.purefa_inventory module – Collect information from Pure Storage FlashArray

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_inventory_module.md#ansible-collections-purestorage-flasharray-purefa-inventory-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_inventory`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_inventory_module.md#synopsis)
- [Requirements](purefa_inventory_module.md#requirements)
- [Parameters](purefa_inventory_module.md#parameters)
- [Notes](purefa_inventory_module.md#notes)
- [Examples](purefa_inventory_module.md#examples)
- [Return Values](purefa_inventory_module.md#return-values)

## [Synopsis](purefa_inventory_module.md#id1)

- Collect hardware inventory information from a Pure Storage Flasharray

## [Requirements](purefa_inventory_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_inventory_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |

## [Notes](purefa_inventory_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_inventory_module.md#id5)

```yaml+jinja
- name: collect FlashArray invenroty
  purestorage.flasharray.purefa_inventory:
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: show inventory information
  debug:
    msg: "{{ array_info['purefa_inv'] }}"
```

## [Return Values](purefa_inventory_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **purefa_inventory**  dictionary | Returns the inventory information for the FlashArray  **Returned:** always |

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
