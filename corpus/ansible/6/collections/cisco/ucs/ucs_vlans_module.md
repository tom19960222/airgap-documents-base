---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_vlans module – Configures VLANs on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_vlans_module.html
fetched_at: 2026-07-27T17:03:00+00:00
---
# cisco.ucs.ucs_vlans module – Configures VLANs on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/cisco/ucs) (version 1.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_vlans_module.md#ansible-collections-cisco-ucs-ucs-vlans-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_vlans`.

New in cisco.ucs 2.5

- [Synopsis](ucs_vlans_module.md#synopsis)
- [Requirements](ucs_vlans_module.md#requirements)
- [Parameters](ucs_vlans_module.md#parameters)
- [Examples](ucs_vlans_module.md#examples)

## [Synopsis](ucs_vlans_module.md#id1)

- Configures VLANs on Cisco UCS Manager.

## [Requirements](ucs_vlans_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_vlans_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **fabric**  string | The fabric configuration of the VLAN. This can be one of the following:  common - The VLAN applies to both fabrics and uses the same configuration parameters in both cases.  A — The VLAN only applies to fabric A.  B — The VLAN only applies to fabric B.  For upstream disjoint L2 networks, Cisco recommends that you choose common to create VLANs that apply to both fabrics.  Choices:   - `"common"` ← (default) - `"A"` - `"B"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **id**  string / required | The unique string identifier assigned to the VLAN.  A VLAN ID can be between ‘1’ and ‘3967’, or between ‘4048’ and ‘4093’.  You cannot create VLANs with IDs from 4030 to 4047. This range of VLAN IDs is reserved.  The VLAN IDs you specify must also be supported on the switch that you are using.  VLANs in the LAN cloud and FCoE VLANs in the SAN cloud must have different IDs.  Optional if state is absent. |
| **multicast_policy**  string | The multicast policy associated with this VLAN.  This option is only valid if the Sharing Type field is set to None or Primary.  Default: `""` |
| **name**  string / required | The name assigned to the VLAN.  The VLAN name is case sensitive.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the VLAN is created. |
| **native**  string | Designates the VLAN as a native VLAN.  Choices:   - `"yes"` - `"no"` ← (default) |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **sharing**  string | The Sharing Type field.  Whether this VLAN is subdivided into private or secondary VLANs. This can be one of the following:  none - This VLAN does not have any secondary or private VLANs. This is a regular VLAN.  primary - This VLAN can have one or more secondary VLANs, as shown in the Secondary VLANs area. This VLAN is a primary VLAN in the private VLAN domain.  isolated - This is a private VLAN associated with a primary VLAN. This VLAN is an Isolated VLAN.  community - This VLAN can communicate with other ports on the same community VLAN as well as the promiscuous port. This VLAN is a Community VLAN.  Choices:   - `"none"` ← (default) - `"primary"` - `"isolated"` - `"community"` |
| **state**  string | If `present`, will verify VLANs are present and will create if needed.  If `absent`, will verify VLANs are absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |

## [Examples](ucs_vlans_module.md#id4)

```yaml+jinja
- name: Configure VLAN
  cisco.ucs.ucs_vlans:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vlan2
    id: '2'
    native: 'yes'

- name: Remove VLAN
  cisco.ucs.ucs_vlans:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vlan2
    state: absent
```

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
