---
collection: ansible
version: "8"
title: "community.network.dladm_iptun module – Manage IP tunnel interfaces on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/dladm_iptun_module.html
fetched_at: 2026-07-28T01:56:25+00:00
---
# community.network.dladm_iptun module – Manage IP tunnel interfaces on Solaris/illumos systems.

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
> To use it in a playbook, specify: `community.network.dladm_iptun`.

- [Synopsis](dladm_iptun_module.md#synopsis)
- [Parameters](dladm_iptun_module.md#parameters)
- [Examples](dladm_iptun_module.md#examples)
- [Return Values](dladm_iptun_module.md#return-values)

## [Synopsis](dladm_iptun_module.md#id1)

- Manage IP tunnel interfaces on Solaris/illumos systems.

Aliases: network.illumos.dladm_iptun

## [Parameters](dladm_iptun_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **local_address**  aliases: local  string | Literal IP address or hostname corresponding to the tunnel source. |
| **name**  string / required | IP tunnel interface name. |
| **remote_address**  aliases: remote  string | Literal IP address or hostname corresponding to the tunnel destination. |
| **state**  string | Create or delete Solaris/illumos VNIC.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **temporary**  boolean | Specifies that the IP tunnel interface is temporary. Temporary IP tunnel interfaces do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **type**  aliases: tunnel_type  string | Specifies the type of tunnel to be created.  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` - `"6to4"` |

## [Examples](dladm_iptun_module.md#id3)

```yaml+jinja
- name: Create IPv4 tunnel interface 'iptun0'
  community.network.dladm_iptun: name=iptun0 local_address=192.0.2.23 remote_address=203.0.113.10 state=present

- name: Change IPv4 tunnel remote address
  community.network.dladm_iptun: name=iptun0 type=ipv4 local_address=192.0.2.23 remote_address=203.0.113.11

- name: Create IPv6 tunnel interface 'tun0'
  community.network.dladm_iptun: name=tun0 type=ipv6 local_address=192.0.2.23 remote_address=203.0.113.42

- name: Remove 'iptun0' tunnel interface
  community.network.dladm_iptun: name=iptun0 state=absent
```

## [Return Values](dladm_iptun_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **local_address**  string | local IP address  **Returned:** always  **Sample:** `"1.1.1.1/32"` |
| **name**  string | tunnel interface name  **Returned:** always  **Sample:** `"iptun0"` |
| **remote_address**  string | remote IP address  **Returned:** always  **Sample:** `"2.2.2.2/32"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | specifies if operation will persist across reboots  **Returned:** always  **Sample:** `true` |
| **type**  string | tunnel type  **Returned:** always  **Sample:** `"ipv4"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
