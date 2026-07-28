---
collection: ansible
version: "6"
title: "community.windows.win_dns_zone module – Manage Windows Server DNS Zones"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_dns_zone_module.html
fetched_at: 2026-07-27T17:23:17+00:00
---
# community.windows.win_dns_zone module – Manage Windows Server DNS Zones

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
> see [Requirements](win_dns_zone_module.md#ansible-collections-community-windows-win-dns-zone-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_dns_zone`.

- [Synopsis](win_dns_zone_module.md#synopsis)
- [Requirements](win_dns_zone_module.md#requirements)
- [Parameters](win_dns_zone_module.md#parameters)
- [Examples](win_dns_zone_module.md#examples)
- [Return Values](win_dns_zone_module.md#return-values)

## [Synopsis](win_dns_zone_module.md#id1)

- Manage Windows Server DNS Zones
- Adds, Removes and Modifies DNS Zones - Primary, Secondary, Forwarder & Stub
- Task should be delegated to a Windows DNS Server

## [Requirements](win_dns_zone_module.md#id2)

The below requirements are needed on the host that executes this module.

- This module requires Windows Server 2012R2 or Newer

## [Parameters](win_dns_zone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dns_servers**  list / elements=string | Specifies an list of IP addresses of the primary servers of the zone.  DNS queries for a forwarded zone are sent to primary servers.  Required if l(type=secondary), l(type=forwarder) or l(type=stub), otherwise ignored.  At least one server is required. |
| **dynamic_update**  string | Specifies how a zone handles dynamic updates.  Secure DNS updates are available only for Active Directory-integrated zones.  When not specified during new zone creation, Windows will default this to l(none).  Choices:   - `"secure"` - `"none"` - `"nonsecureandsecure"` |
| **forwarder_timeout**  integer | Specifies a length of time, in seconds, that a DNS server waits for a remote DNS server to resolve a query.  Accepts integer values between 0 and 15.  If the provided value is not valid, it will be omitted and a warning will be issued. |
| **name**  string / required | Fully qualified name of the DNS zone. |
| **replication**  string | Specifies the replication scope for the DNS zone.  l(replication=forest) will replicate the DNS zone to all domain controllers in the Active Directory forest.  l(replication=domain) will replicate the DNS zone to all domain controllers in the Active Directory domain.  l(replication=none) disables Active Directory integration and creates a local file with the name of the zone.  This is the equivalent of selecting l(store the zone in Active Directory) in the GUI.  Choices:   - `"forest"` - `"domain"` - `"legacy"` - `"none"` |
| **state**  string | Specifies the desired state of the DNS zone.  When l(state=present) the module will attempt to create the specified DNS zone if it does not already exist.  When l(state=absent), the module will remove the specified DNS zone and all subsequent DNS records.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | Specifies the type of DNS zone.  When l(type=secondary), the DNS server will immediately attempt to perform a zone transfer from the servers in this list. If this initial transfer fails, then the zone will be left in an unworkable state. This module does not verify the initial transfer.  Choices:   - `"primary"` - `"secondary"` - `"stub"` - `"forwarder"` |

## [Examples](win_dns_zone_module.md#id4)

```yaml+jinja
- name: Ensure primary zone is present
  community.windows.win_dns_zone:
    name: wpinner.euc.vmware.com
    replication: domain
    type: primary
    state: present

- name: Ensure DNS zone is absent
  community.windows.win_dns_zone:
    name: jamals.euc.vmware.com
    state: absent

- name: Ensure forwarder has specific DNS servers
  community.windows.win_dns_zone:
    name: jamals.euc.vmware.com
    type: forwarder
    dns_servers:
      - 10.245.51.100
      - 10.245.51.101
      - 10.245.51.102

- name: Ensure stub zone has specific DNS servers
  community.windows.win_dns_zone:
    name: virajp.euc.vmware.com
    type: stub
    dns_servers:
      - 10.58.2.100
      - 10.58.2.101

- name: Ensure stub zone is converted to a secondary zone
  community.windows.win_dns_zone:
    name: virajp.euc.vmware.com
    type: secondary

- name: Ensure secondary zone is present with no replication
  community.windows.win_dns_zone:
    name: dgemzer.euc.vmware.com
    type: secondary
    replication: none
    dns_servers:
      - 10.19.20.1

- name: Ensure secondary zone is converted to a primary zone
  community.windows.win_dns_zone:
    name: dgemzer.euc.vmware.com
    type: primary
    replication: none
    dns_servers:
      - 10.19.20.1

- name: Ensure primary DNS zone is present without replication
  community.windows.win_dns_zone:
    name: basavaraju.euc.vmware.com
    replication: none
    type: primary

- name: Ensure primary DNS zone has nonsecureandsecure dynamic updates enabled
  community.windows.win_dns_zone:
    name: basavaraju.euc.vmware.com
    replication: none
    dynamic_update: nonsecureandsecure
    type: primary

- name: Ensure DNS zone is absent
  community.windows.win_dns_zone:
    name: marshallb.euc.vmware.com
    state: absent

- name: Ensure DNS zones are absent
  community.windows.win_dns_zone:
    name: "{{ item }}"
    state: absent
  loop:
    - jamals.euc.vmware.com
    - dgemzer.euc.vmware.com
    - wpinner.euc.vmware.com
    - marshallb.euc.vmware.com
    - basavaraju.euc.vmware.com
```

## [Return Values](win_dns_zone_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone**  dictionary | New/Updated DNS zone parameters  Returned: When l(state=present)  Sample: `{"dns_servers": null, "dynamic_update": null, "forwarder_timeout": null, "name": null, "paused": null, "replication": null, "reverse_lookup": null, "shutdown": null, "type": null, "zone_file": null}` |

### Authors

- Joe Zollo (@joezollo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
