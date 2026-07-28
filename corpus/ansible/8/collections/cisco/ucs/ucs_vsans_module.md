---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_vsans module – Configures VSANs on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_vsans_module.html
fetched_at: 2026-07-28T01:39:49+00:00
---
# cisco.ucs.ucs_vsans module – Configures VSANs on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_vsans_module.md#ansible-collections-cisco-ucs-ucs-vsans-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_vsans`.

New in cisco.ucs 2.5

- [Synopsis](ucs_vsans_module.md#synopsis)
- [Requirements](ucs_vsans_module.md#requirements)
- [Parameters](ucs_vsans_module.md#parameters)
- [Examples](ucs_vsans_module.md#examples)

## [Synopsis](ucs_vsans_module.md#id1)

- Configures VSANs on Cisco UCS Manager.

## [Requirements](ucs_vsans_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_vsans_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **fabric**  string | The fabric configuration of the VSAN. This can be one of the following:  common - The VSAN maps to the same VSAN ID in all available fabrics.  A - The VSAN maps to the a VSAN ID that exists only in fabric A.  B - The VSAN maps to the a VSAN ID that exists only in fabric B.  **Choices:**   - `"common"` ← (default) - `"A"` - `"B"` |
| **fc_zoning**  string | Fibre Channel zoning configuration for the Cisco UCS domain.  Fibre Channel zoning can be set to one of the following values:  disabled — The upstream switch handles Fibre Channel zoning, or Fibre Channel zoning is not implemented for the Cisco UCS domain.  enabled — Cisco UCS Manager configures and controls Fibre Channel zoning for the Cisco UCS domain.  If you enable Fibre Channel zoning, do not configure the upstream switch with any VSANs that are being used for Fibre Channel zoning.  **Choices:**   - `"disabled"` ← (default) - `"enabled"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name assigned to the VSAN.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the VSAN is created. |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify VSANs are present and will create if needed.  If `absent`, will verify VSANs are absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **vlan_id**  string / required | The unique string identifier assigned to the VLAN used for Fibre Channel connections.  Note that Cisco UCS Manager uses VLAN ‘4048’. See the UCS Manager configuration guide if you want to assign ‘4048’ to a VLAN.  Optional if state is absent. |
| **vsan_id**  string / required | The unique identifier assigned to the VSAN.  The ID can be a string between ‘1’ and ‘4078’, or between ‘4080’ and ‘4093’. ‘4079’ is a reserved VSAN ID.  In addition, if you plan to use FC end-host mode, the range between ‘3840’ to ‘4079’ is also a reserved VSAN ID range.  Optional if state is absent. |

## [Examples](ucs_vsans_module.md#id4)

```yaml+jinja
- name: Configure VSAN
  cisco.ucs.ucs_vsans:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vsan110
    fabric: common
    vsan_id: '110'
    vlan_id: '110'

- name: Remove VSAN
  cisco.ucs.ucs_vsans:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vsan110
    state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
