---
collection: ansible
version: "6"
title: "ansible.windows.win_dns_client module – Configures DNS lookup on Windows hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_dns_client_module.html
fetched_at: 2026-07-27T16:44:53+00:00
---
# ansible.windows.win_dns_client module – Configures DNS lookup on Windows hosts

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_dns_client`.

- [Synopsis](win_dns_client_module.md#synopsis)
- [Parameters](win_dns_client_module.md#parameters)
- [Examples](win_dns_client_module.md#examples)

## [Synopsis](win_dns_client_module.md#id1)

- The [ansible.windows.win_dns_client](win_dns_client_module.md#ansible-collections-ansible-windows-win-dns-client-module) module configures the DNS client on Windows network adapters.

## [Parameters](win_dns_client_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adapter_names**  list / elements=string / required | Adapter name or list of adapter names for which to manage DNS settings (’\*’ is supported as a wildcard value).  The adapter name used is the connection caption in the Network Control Panel or the InterfaceAlias of `Get-DnsClientServerAddress`. |
| **dns_servers**  aliases: ipv4_addresses, ip_addresses, addresses  list / elements=string / required | Single or ordered list of DNS servers (IPv4 and IPv6 addresses) to configure for lookup.  An empty list will configure the adapter to use the DHCP-assigned values on connections where DHCP is enabled, or disable DNS lookup on statically-configured connections.  IPv6 DNS servers can only be set on Windows Server 2012 or newer, older hosts can only set IPv4 addresses. |

## [Examples](win_dns_client_module.md#id3)

```yaml+jinja
- name: Set a single address on the adapter named Ethernet
  ansible.windows.win_dns_client:
    adapter_names: Ethernet
    dns_servers: 192.168.34.5

- name: Set multiple lookup addresses on all visible adapters (usually physical adapters that are in the Up state), with debug logging to a file
  ansible.windows.win_dns_client:
    adapter_names: '*'
    dns_servers:
    - 192.168.34.5
    - 192.168.34.6
    log_path: C:\dns_log.txt

- name: Set IPv6 DNS servers on the adapter named Ethernet
  ansible.windows.win_dns_client:
    adapter_names: Ethernet
    dns_servers:
    - '2001:db8::2'
    - '2001:db8::3'

- name: Configure all adapters whose names begin with Ethernet to use DHCP-assigned DNS values
  ansible.windows.win_dns_client:
    adapter_names: 'Ethernet*'
    dns_servers: []
```

### Authors

- Matt Davis (@nitzmahone)
- Brian Scholer (@briantist)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
