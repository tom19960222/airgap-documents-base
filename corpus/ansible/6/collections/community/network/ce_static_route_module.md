---
collection: ansible
version: "6"
title: "community.network.ce_static_route module – Manages static route configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_static_route_module.html
fetched_at: 2026-07-27T17:17:53+00:00
---
# community.network.ce_static_route module – Manages static route configuration on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_static_route`.

- [Synopsis](ce_static_route_module.md#synopsis)
- [Parameters](ce_static_route_module.md#parameters)
- [Notes](ce_static_route_module.md#notes)
- [Examples](ce_static_route_module.md#examples)
- [Return Values](ce_static_route_module.md#return-values)

## [Synopsis](ce_static_route_module.md#id1)

- Manages the static routes on HUAWEI CloudEngine switches.

## [Parameters](ce_static_route_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aftype**  string / required | Destination ip address family type of static route.  Choices:   - `"v4"` - `"v6"` |
| **description**  string | Name of the route. Used with the name parameter on the CLI. |
| **destvrf**  string | VPN instance of next hop ip address. |
| **mask**  string / required | Destination ip mask of static route. |
| **next_hop**  string | Next hop address of static route. |
| **nhp_interface**  string | Next hop interface full name of static route. |
| **pref**  string | Preference or administrative difference of route (range 1-255). |
| **prefix**  string / required | Destination ip address of static route. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag**  string | Route tag value (numeric). |
| **vrf**  string | VPN instance of destination ip address. |

## [Notes](ce_static_route_module.md#id3)

> **Note:**
>
> - If no vrf is supplied, vrf is set to default.
> - If *state=absent*, the route will be removed, regardless of the non-required parameters.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_static_route_module.md#id4)

```yaml+jinja
- name: Static route module test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:

  - name: Config a ipv4 static route, next hop is an address and that it has the proper description
    community.network.ce_static_route:
      prefix: 2.1.1.2
      mask: 24
      next_hop: 3.1.1.2
      description: 'Configured by Ansible'
      aftype: v4
  - name: Config a ipv4 static route ,next hop is an interface and that it has the proper description
    community.network.ce_static_route:
      prefix: 2.1.1.2
      mask: 24
      next_hop: 10GE1/0/1
      description: 'Configured by Ansible'
      aftype: v4
  - name: Config a ipv6 static route, next hop is an address and that it has the proper description
    community.network.ce_static_route:
      prefix: fc00:0:0:2001::1
      mask: 64
      next_hop: fc00:0:0:2004::1
      description: 'Configured by Ansible'
      aftype: v6
  - name: Config a ipv4 static route, next hop is an interface and that it has the proper description
    community.network.ce_static_route:
      prefix: fc00:0:0:2001::1
      mask: 64
      next_hop: 10GE1/0/1
      description: 'Configured by Ansible'
      aftype: v6
  - name: Config a VRF and set ipv4 static route, next hop is an address and that it has the proper description
    community.network.ce_static_route:
      vrf: vpna
      prefix: 2.1.1.2
      mask: 24
      next_hop: 3.1.1.2
      description: 'Configured by Ansible'
      aftype: v4
```

## [Return Values](ce_static_route_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"description": "testing", "mask": "24", "next_hop": "3.3.3.3", "pref": "100", "prefix": "192.168.20.0", "tag": "null"}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"description": "testing", "mask": "24", "next_hop": "3.3.3.3", "pref": "100", "prefix": "192.168.20.642", "vrf": "_public_"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["ip route-static 192.168.20.0 255.255.255.0 3.3.3.3 preference 100 description testing"]` |

### Authors

- Yang yang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
