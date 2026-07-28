---
collection: ansible
version: "8"
title: "community.network.ipadm_addr module – Manage IP addresses on an interface on Solaris/illumos systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ipadm_addr_module.html
fetched_at: 2026-07-28T01:56:56+00:00
---
# community.network.ipadm_addr module – Manage IP addresses on an interface on Solaris/illumos systems

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ipadm_addr`.

- [Synopsis](ipadm_addr_module.md#synopsis)
- [Parameters](ipadm_addr_module.md#parameters)
- [Examples](ipadm_addr_module.md#examples)
- [Return Values](ipadm_addr_module.md#return-values)

## [Synopsis](ipadm_addr_module.md#id1)

- Create/delete static/dynamic IP addresses on network interfaces on Solaris/illumos systems.
- Up/down static/dynamic IP addresses on network interfaces on Solaris/illumos systems.
- Manage IPv6 link-local addresses on network interfaces on Solaris/illumos systems.

Aliases: network.illumos.ipadm_addr

## [Parameters](ipadm_addr_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  aliases: addr  string | Specifiies an IP address to configure in CIDR notation. |
| **addrobj**  string / required | Specifies an unique IP address on the system. |
| **addrtype**  string | Specifiies a type of IP address to configure.  **Choices:**   - `"static"` ← (default) - `"dhcp"` - `"addrconf"` |
| **state**  string | Create/delete/enable/disable an IP address on the network interface.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"up"` - `"down"` - `"enabled"` - `"disabled"` - `"refreshed"` |
| **temporary**  boolean | Specifies that the configured IP address is temporary. Temporary IP addresses do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **wait**  string | Specifies the time in seconds we wait for obtaining address via DHCP.  **Default:** `60` |

## [Examples](ipadm_addr_module.md#id3)

```yaml+jinja
- name: Configure IP address 10.0.0.1 on e1000g0
  community.network.ipadm_addr: addr=10.0.0.1/32 addrobj=e1000g0/v4 state=present

- name: Delete addrobj
  community.network.ipadm_addr: addrobj=e1000g0/v4 state=absent

- name: Configure link-local IPv6 address
  community.network.ipadm_addr: addtype=addrconf addrobj=vnic0/v6

- name: Configure address via DHCP and wait 180 seconds for address obtaining
  community.network.ipadm_addr: addrobj=vnic0/dhcp addrtype=dhcp wait=180
```

## [Return Values](ipadm_addr_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | IP address  **Returned:** only if addrtype is ‘static’  **Sample:** `"1.3.3.7/32"` |
| **addrobj**  string | address object name  **Returned:** always  **Sample:** `"bge0/v4"` |
| **addrtype**  string | address type  **Returned:** always  **Sample:** `"static"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | specifies if operation will persist across reboots  **Returned:** always  **Sample:** `true` |
| **wait**  string | time we wait for DHCP  **Returned:** only if addrtype is ‘dhcp’  **Sample:** `"10"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
