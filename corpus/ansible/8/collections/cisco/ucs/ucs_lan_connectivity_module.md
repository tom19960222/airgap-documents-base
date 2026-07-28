---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_lan_connectivity module – Configures LAN Connectivity Policies on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_lan_connectivity_module.html
fetched_at: 2026-07-28T01:39:33+00:00
---
# cisco.ucs.ucs_lan_connectivity module – Configures LAN Connectivity Policies on Cisco UCS Manager

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
> see [Requirements](ucs_lan_connectivity_module.md#ansible-collections-cisco-ucs-ucs-lan-connectivity-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_lan_connectivity`.

New in cisco.ucs 2.5

- [Synopsis](ucs_lan_connectivity_module.md#synopsis)
- [Requirements](ucs_lan_connectivity_module.md#requirements)
- [Parameters](ucs_lan_connectivity_module.md#parameters)
- [Examples](ucs_lan_connectivity_module.md#examples)

## [Synopsis](ucs_lan_connectivity_module.md#id1)

- Configures LAN Connectivity Policies on Cisco UCS Manager.

## [Requirements](ucs_lan_connectivity_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_lan_connectivity_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A description of the LAN Connectivity Policy.  Cisco recommends including information about where and when to use the policy.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **iscsi_vnic_list**  string  *added in cisco.ucs 2.8* | List of iSCSI vNICs used by the LAN Connectivity Policy. |
| **iscsi_adapter_policy**  string | The iSCSI adapter policy associated with this iSCSI vNIC. |
| **mac_address**  string | The MAC address associated with this iSCSI vNIC.  If the MAC address is not set, Cisco UCS Manager uses a derived MAC address.  **Default:** `"derived"` |
| **name**  string / required | The name of the iSCSI vNIC. |
| **overlay_vnic**  string | The LAN vNIC associated with this iSCSI vNIC. |
| **state**  string | If `present`, will verify iscsi vnic is configured within policy. If `absent`, will verify iscsi vnic is absent from policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vlan_name**  string | The VLAN used for the iSCSI vNIC.  **Default:** `"default"` |
| **name**  string / required | The name of the LAN Connectivity Policy.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the policy is created. |
| **org_dn**  string | Org dn (distinguished name)  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify LAN Connectivity Policies are present and will create if needed.  If `absent`, will verify LAN Connectivity Policies are absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **vnic_list**  string  *added in cisco.ucs 2.8* | List of vNICs used by the LAN Connectivity Policy.  vNICs used by the LAN Connectivity Policy must be created from a vNIC template. |
| **adapter_policy**  string | The name of the Ethernet adapter policy.  A user defined policy can be used, or one of the system defined policies. |
| **name**  string / required | The name of the vNIC. |
| **order**  string | String specifying the vNIC assignment order (e.g., ‘1’, ‘2’).  **Default:** `"unspecified"` |
| **state**  string | If `present`, will verify vnic is configured within policy. If `absent`, will verify vnic is absent from policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vnic_template**  string / required | The name of the vNIC template. |

## [Examples](ucs_lan_connectivity_module.md#id4)

```yaml+jinja
- name: Configure LAN Connectivity Policy
  cisco.ucs.ucs_lan_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-FC-Boot
    vnic_list:
    - name: eno1
      vnic_template: Cntr-Template
      adapter_policy: Linux
    - name: eno2
      vnic_template: Container-NFS-A
      adapter_policy: Linux
    - name: eno3
      vnic_template: Container-NFS-B
      adapter_policy: Linux
    iscsi_vnic_list:
    - name: iSCSIa
      overlay_vnic: eno1
      iscsi_adapter_policy: default
      vlan_name: Container-MGMT-VLAN
    - name: iSCSIb
      overlay_vnic: eno3
      iscsi_adapter_policy: default
      vlan_name: Container-TNT-A-NFS

- name: Remove LAN Connectivity Policy
  cisco.ucs.ucs_lan_connectivity:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: Cntr-FC-Boot
    state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
