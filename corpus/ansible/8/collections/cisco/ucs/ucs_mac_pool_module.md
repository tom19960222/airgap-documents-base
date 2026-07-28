---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_mac_pool module – Configures MAC address pools on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_mac_pool_module.html
fetched_at: 2026-07-28T01:39:34+00:00
---
# cisco.ucs.ucs_mac_pool module – Configures MAC address pools on Cisco UCS Manager

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
> see [Requirements](ucs_mac_pool_module.md#ansible-collections-cisco-ucs-ucs-mac-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_mac_pool`.

New in cisco.ucs 2.5

- [Synopsis](ucs_mac_pool_module.md#synopsis)
- [Requirements](ucs_mac_pool_module.md#requirements)
- [Parameters](ucs_mac_pool_module.md#parameters)
- [Examples](ucs_mac_pool_module.md#examples)

## [Synopsis](ucs_mac_pool_module.md#id1)

- Configures MAC address pools and MAC address blocks on Cisco UCS Manager.

## [Requirements](ucs_mac_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_mac_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | A description of the MAC pool.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **first_addr**  string | The first MAC address in the block of addresses.  This is the From field in the UCS Manager MAC Blocks menu. |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **last_addr**  string | The last MAC address in the block of addresses.  This is the To field in the UCS Manager Add MAC Blocks menu. |
| **name**  string / required | The name of the MAC pool.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the MAC pool is created. |
| **order**  string | The Assignment Order field.  This can be one of the following:  default - Cisco UCS Manager selects a random identity from the pool.  sequential - Cisco UCS Manager selects the lowest available identity from the pool.  **Choices:**   - `"default"` ← (default) - `"sequential"` |
| **org_dn**  string | The distinguished name (dn) of the organization where the resource is assigned.  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify MAC pool is present and will create if needed.  If `absent`, will verify MAC pool is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_mac_pool_module.md#id4)

```yaml+jinja
- name: Configure MAC address pool
  cisco.ucs.ucs_mac_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: mac-A
    first_addr: 00:25:B5:00:66:00
    last_addr: 00:25:B5:00:67:F3
    order: sequential

- name: Remove MAC address pool
  cisco.ucs.ucs_mac_pool:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: mac-A
    state: absent
```

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
