---
collection: ansible
version: "6"
title: "ansible.posix.firewalld_info module – Gather information about firewalld"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/firewalld_info_module.html
fetched_at: 2026-07-27T16:44:42+00:00
---
# ansible.posix.firewalld_info module – Gather information about firewalld

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ansible/posix) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](firewalld_info_module.md#ansible-collections-ansible-posix-firewalld-info-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.firewalld_info`.

- [Synopsis](firewalld_info_module.md#synopsis)
- [Requirements](firewalld_info_module.md#requirements)
- [Parameters](firewalld_info_module.md#parameters)
- [Examples](firewalld_info_module.md#examples)
- [Return Values](firewalld_info_module.md#return-values)

## [Synopsis](firewalld_info_module.md#id1)

- This module gathers information about firewalld rules.

## [Requirements](firewalld_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- firewalld >= 0.2.11
- python-firewall
- python-dbus

## [Parameters](firewalld_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active_zones**  boolean | Gather information about active zones.  Choices:   - `false` ← (default) - `true` |
| **zones**  list / elements=string | Gather information about specific zones.  If only works if `active_zones` is set to `false`. |

## [Examples](firewalld_info_module.md#id4)

```yaml+jinja
- name: Gather information about active zones
  ansible.posix.firewalld_info:
    active_zones: yes

- name: Gather information about specific zones
  ansible.posix.firewalld_info:
    zones:
      - public
      - external
      - internal
```

## [Return Values](firewalld_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **active_zones**  boolean | Gather active zones only if turn it `true`.  Returned: success  Sample: `false` |
| **collected_zones**  list / elements=string | A list of collected zones.  Returned: success  Sample: `["external", "internal"]` |
| **firewalld_info**  complex | Returns various information about firewalld configuration.  Returned: success |
| **default_zones**  string | The zone name of default zone.  Returned: success  Sample: `"public"` |
| **version**  string | The version information of firewalld.  Returned: success  Sample: `"0.8.2"` |
| **zones**  complex | A dict of zones to gather information.  Returned: success |
| **zone**  complex | The zone name registered in firewalld.  Returned: success  Sample: `"external"` |
| **forward**  boolean | The network interface forwarding.  This parameter supports on python-firewall 0.9.0(or later) and is not collected in earlier versions.  Returned: success  Sample: `false` |
| **forward_ports**  list / elements=string | A list of forwarding port pair with protocol.  Returned: success  Sample: `["icmp", "ipv6-icmp"]` |
| **icmp_block_inversion**  boolean | The ICMP block inversion to block all ICMP requests.  Returned: success  Sample: `false` |
| **icmp_blocks**  list / elements=string | A list of blocking icmp protocol.  Returned: success  Sample: `["echo-request"]` |
| **interfaces**  list / elements=string | A list of network interfaces.  Returned: success  Sample: `["eth0", "eth1"]` |
| **masquerade**  boolean | The network interface masquerading.  Returned: success  Sample: `false` |
| **ports**  list / elements=string | A list of network port with protocol.  Returned: success  Sample: `[["22", "tcp"], ["80", "tcp"]]` |
| **protocols**  list / elements=string | A list of network protocol.  Returned: success  Sample: `["icmp", "ipv6-icmp"]` |
| **rich_rules**  list / elements=string | A list of rich language rule.  Returned: success  Sample: `["rule protocol value=\"icmp\" reject", "rule priority=\"32767\" reject"]` |
| **services**  list / elements=string | A list of network services.  Returned: success  Sample: `["dhcp", "dns", "ssh"]` |
| **source_ports**  list / elements=string | A list of network source port with protocol.  Returned: success  Sample: `[["30000", "tcp"], ["30001", "tcp"]]` |
| **sources**  list / elements=string | A list of source network address.  Returned: success  Sample: `["172.16.30.0/24", "172.16.31.0/24"]` |
| **target**  string | A list of services in the zone.  Returned: success  Sample: `"ACCEPT"` |
| **undefined_zones**  list / elements=string | A list of undefined zones in `zones` option.  `undefined_zones` will be ignored for gathering process.  Returned: success  Sample: `["foo", "bar"]` |

### Authors

- Hideki Saito (@saito-hideki)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
