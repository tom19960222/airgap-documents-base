---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_vlan_find module – Find VLANs on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_vlan_find_module.html
fetched_at: 2026-07-28T01:39:46+00:00
---
# cisco.ucs.ucs_vlan_find module – Find VLANs on Cisco UCS Manager

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
> see [Requirements](ucs_vlan_find_module.md#ansible-collections-cisco-ucs-ucs-vlan-find-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_vlan_find`.

New in cisco.ucs 2.9

- [Synopsis](ucs_vlan_find_module.md#synopsis)
- [Requirements](ucs_vlan_find_module.md#requirements)
- [Parameters](ucs_vlan_find_module.md#parameters)
- [Examples](ucs_vlan_find_module.md#examples)
- [Return Values](ucs_vlan_find_module.md#return-values)

## [Synopsis](ucs_vlan_find_module.md#id1)

- Find VLANs on Cisco UCS Manager based on different criteria.

## [Requirements](ucs_vlan_find_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_vlan_find_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **fabric**  string | The fabric configuration of the VLAN. This can be one of the following:  common - The VLAN applies to both fabrics and uses the same configuration parameters in both cases.  A — The VLAN only applies to fabric A.  B — The VLAN only applies to fabric B.  **Choices:**   - `"common"` ← (default) - `"A"` - `"B"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **pattern**  string | Regex pattern to find within the name property of the fabricVlan class.  This is required if `vlanid` parameter is not supplied. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **vlanid**  string | The unique string identifier assigned to the VLAN.  A VLAN ID can be between ‘1’ and ‘3967’, or between ‘4048’ and ‘4093’.  This is required if `pattern` parameter is not supplied. |

## [Examples](ucs_vlan_find_module.md#id4)

```yaml+jinja
- name: Get all vlans in fabric A
  cisco.ucs.ucs_vlan_find:
    hostname: 172.16.143.150
    username: admin
    password: password
    fabric: 'A'
    pattern: '.'
- name: Confirm if vlan 15 is present
  cisco.ucs.ucs_vlan_find:
    hostname: 172.16.143.150
    username: admin
    password: password
    vlanid: '15'
```

## [Return Values](ucs_vlan_find_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vlan_list**  list / elements=string | basic details of vlans found  **Returned:** on success  **Sample:** `[{"id": "0", "name": "vlcloud1"}]` |

### Authors

- David Martinez (@dx0xm)
- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
