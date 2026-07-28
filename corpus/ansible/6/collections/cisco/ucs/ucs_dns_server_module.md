---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_dns_server module – Configure DNS servers on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_dns_server_module.html
fetched_at: 2026-07-27T17:02:44+00:00
---
# cisco.ucs.ucs_dns_server module – Configure DNS servers on Cisco UCS Manager

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
> see [Requirements](ucs_dns_server_module.md#ansible-collections-cisco-ucs-ucs-dns-server-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_dns_server`.

New in cisco.ucs 2.8

- [Synopsis](ucs_dns_server_module.md#synopsis)
- [Requirements](ucs_dns_server_module.md#requirements)
- [Parameters](ucs_dns_server_module.md#parameters)
- [Examples](ucs_dns_server_module.md#examples)

## [Synopsis](ucs_dns_server_module.md#id1)

- Configure DNS servers on Cisco UCS Manager.

## [Requirements](ucs_dns_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_dns_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **delegate_to**  string | Where the module will be run  Default: `"localhost"` |
| **description**  aliases: descr  string | A user-defined description of the DNS server.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **dns_server**  aliases: name  string | DNS server IP address.  Enter a valid IPV4 Address.  UCS Manager supports up to 4 DNS Servers |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `absent`, will remove a DNS server.  If `present`, will add or update a DNS server.  Choices:   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |

## [Examples](ucs_dns_server_module.md#id4)

```yaml+jinja
- name: Configure DNS server
  cisco.ucs.ucs_dns_server:
    hostname: 172.16.143.150
    username: admin
    password: password
    dns_server: 10.10.10.10
    description: DNS Server IP address
    state: present
    delegate_to: localhost

- name: Remove DNS server
  cisco.ucs.ucs_dns_server:
    hostname: 172.16.143.150
    username: admin
    password: password
    dns_server: 10.10.10.10
    state: absent
    delegate_to: localhost
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
