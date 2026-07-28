---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_network module – Manage network interfaces in a Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_network_module.html
fetched_at: 2026-07-28T00:18:18+00:00
---
# purestorage.flasharray.purefa_network module – Manage network interfaces in a Pure Storage FlashArray

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
> see [Requirements](purefa_network_module.md#ansible-collections-purestorage-flasharray-purefa-network-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_network`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_network_module.md#synopsis)
- [Requirements](purefa_network_module.md#requirements)
- [Parameters](purefa_network_module.md#parameters)
- [Notes](purefa_network_module.md#notes)
- [Examples](purefa_network_module.md#examples)

## [Synopsis](purefa_network_module.md#id1)

- This module manages the physical and virtual network interfaces on a Pure Storage FlashArray.
- To manage VLAN interfaces use the *purestorage.flasharray.purefa_vlan* module.
- To manage network subnets use the *purestorage.flasharray.purefa_subnet* module.
- To remove an IP address from a non-management port use 0.0.0.0/0

## [Requirements](purefa_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | IPv4 or IPv6 address of interface in CIDR notation.  To remove an IP address from a non-management port use 0.0.0.0/0 |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **gateway**  string | IPv4 or IPv6 address of interface gateway. |
| **mtu**  integer | MTU size of the interface. Range is 1280 to 9216.  Default: `1500` |
| **name**  string / required | Interface name (physical or virtual). |
| **servicelist**  list / elements=string  added in purestorage.flasharray 1.15.0 | Assigns the specified (comma-separated) service list to one or more specified interfaces.  Replaces the previous service list.  Supported service lists depend on whether the network interface is Ethernet or Fibre Channel.  Note that *system* is only valid for Cloud Block Store.  Choices:   - `"replication"` - `"management"` - `"ds"` - `"file"` - `"iscsi"` - `"scsi-fc"` - `"nvme-fc"` - `"system"` |
| **state**  string | State of existing interface (on/off).  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](purefa_network_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_network_module.md#id5)

```yaml+jinja
- name: Configure and enable network interface ct0.eth8
  purestorage.flasharray.purefa_network:
    name: ct0.eth8
    gateway: 10.21.200.1
    address: "10.21.200.18/24"
    mtu: 9000
    state: present
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Disable physical interface ct1.eth2
  purestorage.flasharray.purefa_network:
    name: ct1.eth2
    state: absent
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Enable virtual network interface vir0
  purestorage.flasharray.purefa_network:
    name: vir0
    state: present
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Remove an IP address from iSCSI interface ct0.eth4
  purestorage.flasharray.purefa_network:
    name: ct0.eth4
    address: 0.0.0.0/0
    gateway: 0.0.0.0
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Change service list for FC interface ct0.fc1
  purestorage.flasharray.purefa_network:
    name: ct0.fc1
    servicelist:
      - replication
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
