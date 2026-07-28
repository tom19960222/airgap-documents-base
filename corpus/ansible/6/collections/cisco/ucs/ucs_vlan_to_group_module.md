---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_vlan_to_group module – Add VLANs to a VLAN Group. Requires VLAN and VLAN Group to already be created on UCS prior to running module."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_vlan_to_group_module.html
fetched_at: 2026-07-27T17:02:59+00:00
---
# cisco.ucs.ucs_vlan_to_group module – Add VLANs to a VLAN Group. Requires VLAN and VLAN Group to already be created on UCS prior to running module.

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
> see [Requirements](ucs_vlan_to_group_module.md#ansible-collections-cisco-ucs-ucs-vlan-to-group-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_vlan_to_group`.

New in cisco.ucs 2.10

- [Synopsis](ucs_vlan_to_group_module.md#synopsis)
- [Requirements](ucs_vlan_to_group_module.md#requirements)
- [Parameters](ucs_vlan_to_group_module.md#parameters)
- [Examples](ucs_vlan_to_group_module.md#examples)

## [Synopsis](ucs_vlan_to_group_module.md#id1)

- Add VLANs to VLAN Groups on Cisco UCS Manager.

## [Requirements](ucs_vlan_to_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_vlan_to_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify VLANs are present and will create if needed.  If `absent`, will verify VLANs are absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |
| **vlangroup**  string / required | The name assigned to the VLAN Group.  The VLAN Group name is case sensitive.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period). |
| **vlanname**  string / required | The name assigned to the VLAN.  The VLAN name is case sensitive.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period). |

## [Examples](ucs_vlan_to_group_module.md#id4)

```yaml+jinja
- name: Configure VLAN
  cisco.ucs.ucs_vlan_to_group:
    hostname: 1.1.1.1
    username: admin
    password: password
    vlangroup: VLANGROUP
    vlanname: VLANNAME
    state: present
- name: Remove VLAN
  cisco.ucs.ucs_vlan_to_group:
    hostname: 1.1.1.1
    username: admin
    password: password
    vlangroup: VLANGROUP
    vlanname: VLANNAME
    state: absent
```

### Authors

- Derrick Johnson @derricktj

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
