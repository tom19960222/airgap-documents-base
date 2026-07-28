---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_ip_pool module – Configures IP address pools on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_ip_pool_module.html
fetched_at: 2026-07-28T01:39:33+00:00
---
# cisco.ucs.ucs_ip_pool module – Configures IP address pools on Cisco UCS Manager

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
> see [Requirements](ucs_ip_pool_module.md#ansible-collections-cisco-ucs-ucs-ip-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_ip_pool`.

New in cisco.ucs 2.5

- [Synopsis](ucs_ip_pool_module.md#synopsis)
- [Requirements](ucs_ip_pool_module.md#requirements)
- [Parameters](ucs_ip_pool_module.md#parameters)
- [Examples](ucs_ip_pool_module.md#examples)

## [Synopsis](ucs_ip_pool_module.md#id1)

- Configures IP address pools and blocks of IP addresses on Cisco UCS Manager.

## [Requirements](ucs_ip_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_ip_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | The user-defined description of the IP address pool.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **ip_blocks**  string | List of IPv4 blocks used by the IP Pool. |
| **default_gw**  string | The default gateway associated with the IPv4 addresses in the block.  **Default:** `"0.0.0.0"` |
| **first_addr**  string | The first IPv4 address in the IPv4 addresses block.  This is the From field in the UCS Manager Add IPv4 Blocks menu. |
| **last_addr**  string | The last IPv4 address in the IPv4 addresses block.  This is the To field in the UCS Manager Add IPv4 Blocks menu. |
| **primary_dns**  string | The primary DNS server that this block of IPv4 addresses should access.  **Default:** `"0.0.0.0"` |
| **secondary_dns**  string | The secondary DNS server that this block of IPv4 addresses should access.  **Default:** `"0.0.0.0"` |
| **subnet_mask**  string | The subnet mask associated with the IPv4 addresses in the block.  **Default:** `"255.255.255.0"` |
| **ipv6_blocks**  string | List of IPv6 blocks used by the IP Pool. |
| **ipv6_default_gw**  string | The default gateway associated with the IPv6 addresses in the block.  **Default:** `"::"` |
| **ipv6_first_addr**  string | The first IPv6 address in the IPv6 addresses block.  This is the From field in the UCS Manager Add IPv6 Blocks menu. |
| **ipv6_last_addr**  string | The last IPv6 address in the IPv6 addresses block.  This is the To field in the UCS Manager Add IPv6 Blocks menu. |
| **ipv6_prefix**  string | The network address prefix associated with the IPv6 addresses in the block.  **Default:** `"64"` |
| **ipv6_primary_dns**  string | The primary DNS server that this block of IPv6 addresses should access.  **Default:** `"::"` |
| **ipv6_secondary_dns**  string | The secondary DNS server that this block of IPv6 addresses should access.  **Default:** `"::"` |
| **name**  string / required | The name of the IP address pool.  This name can be between 1 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the IP address pool is created. |
| **order**  string | The Assignment Order field.  This can be one of the following:  default - Cisco UCS Manager selects a random identity from the pool.  sequential - Cisco UCS Manager selects the lowest available identity from the pool.  **Choices:**   - `"default"` ← (default) - `"sequential"` |
| **org_dn**  string | Org dn (distinguished name)  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify IP pool is present and will create if needed.  If `absent`, will verify IP pool is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_ip_pool_module.md#id4)

```yaml+jinja
- name: Configure IPv4 and IPv6 address pool
  cisco.ucs.ucs_ip_pool:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    name: ip-pool-01
    org_dn: org-root/org-level1
    ipv4_blocks:
    - first_addr: 192.168.10.1
      last_addr: 192.168.10.20
      subnet_mask: 255.255.255.128
      default_gw: 192.168.10.2
    - first_addr: 192.168.11.1
      last_addr: 192.168.11.20
      subnet_mask: 255.255.255.128
      default_gw: 192.168.11.2
    ipv6_blocks:
    - ipv6_first_addr: fe80::1cae:7992:d7a1:ed07
      ipv6_last_addr: fe80::1cae:7992:d7a1:edfe
      ipv6_default_gw: fe80::1cae:7992:d7a1:ecff
    - ipv6_first_addr: fe80::1cae:7992:d7a1:ec07
      ipv6_last_addr: fe80::1cae:7992:d7a1:ecfe
      ipv6_default_gw: fe80::1cae:7992:d7a1:ecff

- name: Delete IPv4 and IPv6 address pool blocks
  cisco.ucs.ucs_ip_pool:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    name: ip-pool-01
    org_dn: org-root/org-level1
    ipv4_blocks:
    - first_addr: 192.168.10.1
      last_addr: 192.168.10.20
      state: absent
    ipv6_blocks:
    - ipv6_first_addr: fe80::1cae:7992:d7a1:ec07
      ipv6_last_addr: fe80::1cae:7992:d7a1:ecfe
      state: absent

- name: Remove IPv4 and IPv6 address pool
  cisco.ucs.ucs_ip_pool:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    name: ip-pool-01
    state: absent
```

### Authors

- Brett Johnson (@sdbrett)
- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
