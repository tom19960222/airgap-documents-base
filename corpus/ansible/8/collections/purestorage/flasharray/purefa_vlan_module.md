---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_vlan module – Manage network VLAN interfaces in a Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_vlan_module.html
fetched_at: 2026-07-28T02:51:35+00:00
---
# purestorage.flasharray.purefa_vlan module – Manage network VLAN interfaces in a Pure Storage FlashArray

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
> see [Requirements](purefa_vlan_module.md#ansible-collections-purestorage-flasharray-purefa-vlan-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_vlan`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_vlan_module.md#synopsis)
- [Requirements](purefa_vlan_module.md#requirements)
- [Parameters](purefa_vlan_module.md#parameters)
- [Notes](purefa_vlan_module.md#notes)
- [Examples](purefa_vlan_module.md#examples)

## [Synopsis](purefa_vlan_module.md#id1)

- This module manages the VLAN network interfaces on a Pure Storage FlashArray.

## [Requirements](purefa_vlan_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | IPv4 or IPv6 address of interface. |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **enabled**  boolean | Define if VLAN interface is enabled or not.  **Choices:**   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | Interface name, including controller indentifier.  VLANs are only supported on iSCSI, NVMe-RoCE and file physical interfaces |
| **state**  string | State of existing interface (on/off).  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet**  string / required | Name of subnet interface associated with. |

## [Notes](purefa_vlan_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_vlan_module.md#id5)

```yaml+jinja
- name: Configure and enable VLAN interface ct0.eth8 for subnet test
  purestorage.flasharray.purefa_vlan:
    name: ct0.eth8
    subnet: test
    address: 10.21.200.18
    state: present
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Disable VLAN interface for subnet test on ct1.eth2
  purestorage.flasharray.purefa_vlan:
    name: ct1.eth2
    subnet: test
    enabled: false
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Delete VLAN inteface for subnet test on ct0.eth4
  purestorage.flasharray.purefa_vlan:
    name: ct0.eth4
    subnet: test
    state: absent
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
