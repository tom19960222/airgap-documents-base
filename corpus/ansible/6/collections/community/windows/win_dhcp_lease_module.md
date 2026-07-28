---
collection: ansible
version: "6"
title: "community.windows.win_dhcp_lease module – Manage Windows Server DHCP Leases"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_dhcp_lease_module.html
fetched_at: 2026-07-27T17:23:15+00:00
---
# community.windows.win_dhcp_lease module – Manage Windows Server DHCP Leases

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_dhcp_lease_module.md#ansible-collections-community-windows-win-dhcp-lease-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_dhcp_lease`.

- [Synopsis](win_dhcp_lease_module.md#synopsis)
- [Requirements](win_dhcp_lease_module.md#requirements)
- [Parameters](win_dhcp_lease_module.md#parameters)
- [Examples](win_dhcp_lease_module.md#examples)
- [Return Values](win_dhcp_lease_module.md#return-values)

## [Synopsis](win_dhcp_lease_module.md#id1)

- Manage Windows Server DHCP Leases (IPv4 Only)
- Adds, Removes and Modifies DHCP Leases and Reservations
- Task should be delegated to a Windows DHCP Server

## [Requirements](win_dhcp_lease_module.md#id2)

The below requirements are needed on the host that executes this module.

- This module requires Windows Server 2012 or Newer

## [Parameters](win_dhcp_lease_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Specifies the description for reservation being created.  Only applicable to l(type=reservation). |
| **dns_hostname**  string | Specifies the DNS hostname of the client for which the IP address lease is to be added. |
| **dns_regtype**  string | Indicates the type of DNS record to be registered by the DHCP. server service for this lease.  l(a) results in an A record being registered.  l(aptr) results in both A and PTR records to be registered.  l(noreg) results in no DNS records being registered.  Choices:   - `"aptr"` ← (default) - `"a"` - `"noreg"` |
| **duration**  integer | Specifies the duration of the DHCP lease in days.  The duration value only applies to l(type=lease).  Defaults to the duration specified by the DHCP server configuration.  Only applicable to l(type=lease). |
| **ip**  string | The IPv4 address of the client server/computer.  This is a required parameter, if l(mac) is not set.  Can be used to identify an existing lease/reservation, instead of l(mac). |
| **mac**  string | Specifies the client identifier to be set on the IPv4 address.  This is a required parameter, if l(ip) is not set.  Windows clients use the MAC address as the client ID.  Linux and other operating systems can use other types of identifiers.  Can be used to identify an existing lease/reservation, instead of l(ip). |
| **reservation_name**  string | Specifies the name of the reservation being created.  Only applicable to l(type=reservation). |
| **scope_id**  string | Specifies the scope identifier as defined by the DHCP server.  This is a required parameter, if l(state=present) and the reservation or lease doesn’t already exist. Not required if updating an existing lease or reservation. |
| **state**  string | Specifies the desired state of the DHCP lease or reservation.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | The type of DHCP address.  Leases expire as defined by l(duration).  When l(duration) is not specified, the server default is used.  Reservations are permanent.  Choices:   - `"reservation"` ← (default) - `"lease"` |

## [Examples](win_dhcp_lease_module.md#id4)

```yaml+jinja
- name: Ensure DHCP reservation exists
  community.windows.win_dhcp_lease:
    type: reservation
    ip: 192.168.100.205
    scope_id: 192.168.100.0
    mac: 00:B1:8A:D1:5A:1F
    dns_hostname: "{{ ansible_inventory }}"
    description: Testing Server

- name: Ensure DHCP lease or reservation does not exist
  community.windows.win_dhcp_lease:
    mac: 00:B1:8A:D1:5A:1F
    state: absent

- name: Ensure DHCP lease or reservation does not exist
  community.windows.win_dhcp_lease:
    ip: 192.168.100.205
    state: absent

- name: Convert DHCP lease to reservation & update description
  community.windows.win_dhcp_lease:
    type: reservation
    ip: 192.168.100.205
    description: Testing Server

- name: Convert DHCP reservation to lease
  community.windows.win_dhcp_lease:
    type: lease
    ip: 192.168.100.205
```

## [Return Values](win_dhcp_lease_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lease**  dictionary | New/Updated DHCP object parameters  Returned: When l(state=present)  Sample: `{"address_state": "InactiveReservation", "client_id": "0a-0b-0c-04-05-aa", "description": "Really Fancy", "ip_address": "172.16.98.230", "name": null, "scope_id": "172.16.98.0"}` |

### Authors

- Joe Zollo (@joezollo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
