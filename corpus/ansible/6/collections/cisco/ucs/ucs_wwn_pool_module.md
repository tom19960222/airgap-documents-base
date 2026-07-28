---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_wwn_pool module – Configures WWNN or WWPN pools on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_wwn_pool_module.html
fetched_at: 2026-07-27T16:43:23+00:00
---
# cisco.ucs.ucs_wwn_pool module – Configures WWNN or WWPN pools on Cisco UCS Manager

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
> see [Requirements](ucs_wwn_pool_module.md#ansible-collections-cisco-ucs-ucs-wwn-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_wwn_pool`.

New in cisco.ucs 2.5

- [Synopsis](ucs_wwn_pool_module.md#synopsis)
- [Requirements](ucs_wwn_pool_module.md#requirements)
- [Parameters](ucs_wwn_pool_module.md#parameters)
- [Examples](ucs_wwn_pool_module.md#examples)

## [Synopsis](ucs_wwn_pool_module.md#id1)

- Configures WWNNs or WWPN pools on Cisco UCS Manager.

## [Requirements](ucs_wwn_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_wwn_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A description of the WWNN or WWPN pool.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **first_addr**  string | The first initiator in the World Wide Name (WWN) block.  This is the From field in the UCS Manager Add WWN Blocks menu. |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **last_addr**  string | The last initiator in the World Wide Name (WWN) block.  This is the To field in the UCS Manager Add WWN Blocks menu.  For WWxN pools, the pool size must be a multiple of ports-per-node + 1.  For example, if there are 7 ports per node, the pool size must be a multiple of 8.  If there are 63 ports per node, the pool size must be a multiple of 64. |
| **name**  string / required | The name of the World Wide Node Name (WWNN) or World Wide Port Name (WWPN) pool.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the WWNN or WWPN pool is created. |
| **order**  string | The Assignment Order field.  This can be one of the following:  default - Cisco UCS Manager selects a random identity from the pool.  sequential - Cisco UCS Manager selects the lowest available identity from the pool.  Choices:   - `"default"` ← (default) - `"sequential"` |
| **org_dn**  string | Org dn (distinguished name)  Default: `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **purpose**  string / required | Specify whether this is a node (WWNN) or port (WWPN) pool.  Optional if state is absent.  Choices:   - `"node"` - `"port"` |
| **state**  string | If `present`, will verify WWNNs/WWPNs are present and will create if needed.  If `absent`, will verify WWNNs/WWPNs are absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |

## [Examples](ucs_wwn_pool_module.md#id4)

```yaml+jinja
- name: Configure WWNN/WWPN pools
  cisco.ucs.ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWNN-Pool
    purpose: node
    first_addr: 20:00:00:25:B5:48:00:00
    last_addr: 20:00:00:25:B5:48:00:0F
- cisco.ucs.ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWPN-Pool-A
    purpose: port
    order: sequential
    first_addr: 20:00:00:25:B5:48:0A:00
    last_addr: 20:00:00:25:B5:48:0A:0F

- name: Remove WWNN/WWPN pools
  cisco.ucs.ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWNN-Pool
    state: absent
- cisco.ucs.ucs_wwn_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: WWPN-Pool-A
    state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
