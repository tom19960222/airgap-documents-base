---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_inventory module – Collect information from Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_inventory_module.html
fetched_at: 2026-07-28T00:18:15+00:00
---
# purestorage.flasharray.purefa_inventory module – Collect information from Pure Storage FlashArray

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/purestorage/flasharray) (version 1.15.0).
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
| **purefa_inventory**  complex | Returns the inventory information for the FlashArray  Returned: always  Sample: `{"chassis": {"CH0": {"model": null, "serial": "ABC123", "status": "ok"}}, "controllers": {"CT0": {"model": null, "serial": null, "status": "ok"}, "CT1": {"model": "FA-405", "serial": "FHVBT52", "status": "ok"}}, "drives": {"SH0.BAY0": {"capacity": 2147483648, "protocol": "SAS", "serial": "S18NNEAFA01416", "status": "healthy", "type": "NVRAM"}, "SH0.BAY1": {"capacity": 511587647488, "protocol": "SAS", "serial": "S0WZNEACC00517", "status": "healthy", "type": "SSD"}, "SH0.BAY10": {"capacity": 511587647488, "protocol": "SAS", "serial": "S0WZNEACB00266", "status": "healthy", "type": "SSD"}}, "fans": {"CT0.FAN0": {"status": "ok"}, "CT0.FAN1": {"status": "ok"}, "CT0.FAN10": {"status": "ok"}}, "interfaces": {"CT0.ETH0": {"speed": 1000000000, "status": "ok"}, "CT0.ETH1": {"speed": 0, "status": "ok"}, "CT0.FC0": {"speed": 8000000000, "status": "ok"}, "CT1.IB1": {"speed": 56000000000, "status": "ok"}, "CT1.SAS0": {"speed": 24000000000, "status": "ok"}}, "power": {"CT0.PWR0": {"model": null, "serial": null, "status": "ok", "voltage": null}, "CT0.PWR1": {"model": null, "serial": null, "status": "ok", "voltage": null}}, "temps": {"CT0.TMP0": {"status": "ok", "temperature": 18}, "CT0.TMP1": {"status": "ok", "temperature": 32}}}` |

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
