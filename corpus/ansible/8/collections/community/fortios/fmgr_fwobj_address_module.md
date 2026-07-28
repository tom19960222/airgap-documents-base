---
collection: ansible
version: "8"
title: "community.fortios.fmgr_fwobj_address module – Allows the management of firewall objects in FortiManager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_fwobj_address_module.html
fetched_at: 2026-07-28T01:44:09+00:00
---
# community.fortios.fmgr_fwobj_address module – Allows the management of firewall objects in FortiManager

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_fwobj_address`.

- [Synopsis](fmgr_fwobj_address_module.md#synopsis)
- [Parameters](fmgr_fwobj_address_module.md#parameters)
- [Notes](fmgr_fwobj_address_module.md#notes)
- [Examples](fmgr_fwobj_address_module.md#examples)
- [Return Values](fmgr_fwobj_address_module.md#return-values)

## [Synopsis](fmgr_fwobj_address_module.md#id1)

- Allows for the management of IPv4, IPv6, and multicast address objects within FortiManager.

## [Parameters](fmgr_fwobj_address_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **allow_routing**  string | Enable/disable use of this address in the static route configuration.  **Choices:**   - `"enable"` - `"disable"` ← (default) |
| **associated_interface**  string | Associated interface name. |
| **cache_ttl**  string | Minimal TTL of individual IP addresses in FQDN cache. Only applies when type = wildcard-fqdn. |
| **color**  string | Color of the object in FortiManager GUI.  Takes integers 1-32  **Default:** `22` |
| **comment**  string | Comment for the object in FortiManager. |
| **country**  string | Country name. Required if type = geographic. |
| **end_ip**  string | End IP. Only used when ipv4 = iprange. |
| **fqdn**  string | Fully qualified domain name. |
| **group_members**  string | Address group member. If this is defined w/out group_name, the operation will fail. |
| **group_name**  string | Address group name. If this is defined in playbook task, all other options are ignored. |
| **ipv4**  string | Type of IPv4 Object.  Must not be specified with either multicast or IPv6 parameters.  **Choices:**   - `"ipmask"` - `"iprange"` - `"fqdn"` - `"wildcard"` - `"geography"` - `"wildcard-fqdn"` - `"group"` |
| **ipv4addr**  string | IP and network mask. If only defining one IP use this parameter. (i.e. 10.7.220.30/255.255.255.255)  Can also define subnets (i.e. 10.7.220.0/255.255.255.0)  Also accepts CIDR (i.e. 10.7.220.0/24)  If Netmask is omitted after IP address, /32 is assumed.  When multicast is set to Broadcast Subnet the ipv4addr parameter is used to specify the subnet. |
| **ipv6**  string | Puts module into IPv6 mode.  Must not be specified with either ipv4 or multicast parameters.  **Choices:**   - `"ip"` - `"iprange"` - `"group"` |
| **ipv6addr**  string | IPv6 address in full. (i.e. 2001:0db8:85a3:0000:0000:8a2e:0370:7334) |
| **mode**  string | Sets one of three modes for managing the object.  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` |
| **multicast**  string | Manages Multicast Address Objects.  Sets either a Multicast IP Range or a Broadcast Subnet.  Must not be specified with either ipv4 or ipv6 parameters.  When set to Broadcast Subnet the ipv4addr parameter is used to specify the subnet.  Can create IPv4 Multicast Objects (multicastrange and broadcastmask options – uses start/end-ip and ipv4addr).  **Choices:**   - `"multicastrange"` - `"broadcastmask"` - `"ip6"` |
| **name**  string | Friendly Name Address object name in FortiManager. |
| **obj_id**  string | Object ID for NSX. |
| **start_ip**  string | Start IP. Only used when ipv4 = iprange. |
| **visibility**  string | Enable/disable address visibility.  **Choices:**   - `"enable"` ← (default) - `"disable"` |
| **wildcard**  string | IP address and wildcard netmask. Required if ipv4 = wildcard. |
| **wildcard_fqdn**  string | Wildcard FQDN. Required if ipv4 = wildcard-fqdn. |

## [Notes](fmgr_fwobj_address_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_fwobj_address_module.md#id4)

```yaml+jinja
- name: ADD IPv4 IP ADDRESS OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "ipmask"
    ipv4addr: "10.7.220.30/32"
    name: "ansible_v4Obj"
    comment: "Created by Ansible"
    color: "6"

- name: ADD IPv4 IP ADDRESS OBJECT MORE OPTIONS
  community.fortios.fmgr_fwobj_address:
    ipv4: "ipmask"
    ipv4addr: "10.7.220.34/32"
    name: "ansible_v4Obj_MORE"
    comment: "Created by Ansible"
    color: "6"
    allow_routing: "enable"
    cache_ttl: "180"
    associated_interface: "port1"
    obj_id: "123"

- name: ADD IPv4 IP ADDRESS SUBNET OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "ipmask"
    ipv4addr: "10.7.220.0/255.255.255.128"
    name: "ansible_subnet"
    comment: "Created by Ansible"
    mode: "set"

- name: ADD IPv4 IP ADDRESS RANGE OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "iprange"
    start_ip: "10.7.220.1"
    end_ip: "10.7.220.125"
    name: "ansible_range"
    comment: "Created by Ansible"

- name: ADD IPv4 IP ADDRESS WILDCARD OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "wildcard"
    wildcard: "10.7.220.30/255.255.255.255"
    name: "ansible_wildcard"
    comment: "Created by Ansible"

- name: ADD IPv4 IP ADDRESS WILDCARD FQDN OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "wildcard-fqdn"
    wildcard_fqdn: "*.myds.com"
    name: "Synology myds DDNS service"
    comment: "Created by Ansible"

- name: ADD IPv4 IP ADDRESS FQDN OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "fqdn"
    fqdn: "ansible.com"
    name: "ansible_fqdn"
    comment: "Created by Ansible"

- name: ADD IPv4 IP ADDRESS GEO OBJECT
  community.fortios.fmgr_fwobj_address:
    ipv4: "geography"
    country: "usa"
    name: "ansible_geo"
    comment: "Created by Ansible"

- name: ADD IPv6 ADDRESS
  community.fortios.fmgr_fwobj_address:
    ipv6: "ip"
    ipv6addr: "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    name: "ansible_v6Obj"
    comment: "Created by Ansible"

- name: ADD IPv6 ADDRESS RANGE
  community.fortios.fmgr_fwobj_address:
    ipv6: "iprange"
    start_ip: "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    end_ip: "2001:0db8:85a3:0000:0000:8a2e:0370:7446"
    name: "ansible_v6range"
    comment: "Created by Ansible"

- name: ADD IPv4 IP ADDRESS GROUP
  community.fortios.fmgr_fwobj_address:
    ipv4: "group"
    group_name: "ansibleIPv4Group"
    group_members: "ansible_fqdn, ansible_wildcard, ansible_range"

- name: ADD IPv6 IP ADDRESS GROUP
  community.fortios.fmgr_fwobj_address:
    ipv6: "group"
    group_name: "ansibleIPv6Group"
    group_members: "ansible_v6Obj, ansible_v6range"

- name: ADD MULTICAST RANGE
  community.fortios.fmgr_fwobj_address:
    multicast: "multicastrange"
    start_ip: "224.0.0.251"
    end_ip: "224.0.0.251"
    name: "ansible_multicastrange"
    comment: "Created by Ansible"

- name: ADD BROADCAST SUBNET
  community.fortios.fmgr_fwobj_address:
    multicast: "broadcastmask"
    ipv4addr: "10.7.220.0/24"
    name: "ansible_broadcastSubnet"
    comment: "Created by Ansible"
```

## [Return Values](fmgr_fwobj_address_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
