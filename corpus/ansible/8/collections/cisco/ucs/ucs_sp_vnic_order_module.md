---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_sp_vnic_order module – Configures vNIC order for service profiles and templates on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_sp_vnic_order_module.html
fetched_at: 2026-07-28T01:39:42+00:00
---
# cisco.ucs.ucs_sp_vnic_order module – Configures vNIC order for service profiles and templates on Cisco UCS Manager

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
> see [Requirements](ucs_sp_vnic_order_module.md#ansible-collections-cisco-ucs-ucs-sp-vnic-order-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_sp_vnic_order`.

New in cisco.ucs 2.1

- [Synopsis](ucs_sp_vnic_order_module.md#synopsis)
- [Requirements](ucs_sp_vnic_order_module.md#requirements)
- [Parameters](ucs_sp_vnic_order_module.md#parameters)
- [Examples](ucs_sp_vnic_order_module.md#examples)

## [Synopsis](ucs_sp_vnic_order_module.md#id1)

- Configures Configures vNIC order for service profiles and templates on Cisco UCS Manager

## [Requirements](ucs_sp_vnic_order_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_sp_vnic_order_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **org_dn**  string | root org dn |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **sp_name**  string | DN of the service profile |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **vnics**  string | List of vNIC order properties |
| **admin_vcon**  string | Name of the virtual connection  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"any"` |
| **name**  string / required | Name of the vNIC |
| **order**  string | vNIC connection order  **Choices:**   - `"unspecified"` - `"0-256"` |
| **state**  string | Desired state of the vNIC.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **transport**  string / required | transport medium  **Choices:**   - `"ethernet"` - `"fc"` |

## [Examples](ucs_sp_vnic_order_module.md#id4)

```yaml+jinja
- name: Configure vnic order
  cisco.ucs.ucs_sp_vnic_order:
    sp_name: my_sp
    vnics:
    - name: 'my_vnic'
      admin_vcon: '1'
      order: '1'
      transport: 'ethernet'
    hostname: 192.168.99.100
    username: admin
    password: password
- name: Configure vhba order
  cisco.ucs.ucs_sp_vnic_order:
    sp_name: my_sp
    vnics:
    - name: 'my_vhba'
      admin_vcon: '2'
      order: '1'
      transport: 'fc'
    hostname: 192.168.99.100
    username: admin
    password: password
- name: Configure vnic and vhba order
  cisco.ucs.ucs_sp_vnic_order:
    sp_name: my_sp
    vnics:
    - name: my_vhba
      admin_vcon: '2'
      order: '1'
      transport: fc
    - name: my_vnic
      admin_vcon: '1'
      order: '1'
      transport: ethernet
    hostname: 192.168.99.100
    username: admin
    password: password
- name: Remove vnic order configuration from my_vnic
  cisco.ucs.ucs_sp_vnic_order:
    sp_name: my_sp
    vnics:
    - name: 'my_vnic'
      transport: ethernet
      state: absent
    hostname: 192.168.99.100
    username: admin
    password: password
```

### Authors

- Brett Johnson (@sdbrett)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
