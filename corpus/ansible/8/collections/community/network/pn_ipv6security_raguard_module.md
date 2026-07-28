---
collection: ansible
version: "8"
title: "community.network.pn_ipv6security_raguard module – CLI command to create/modify/delete ipv6security-raguard"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_ipv6security_raguard_module.html
fetched_at: 2026-07-28T01:57:28+00:00
---
# community.network.pn_ipv6security_raguard module – CLI command to create/modify/delete ipv6security-raguard

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
> To use it in a playbook, specify: `community.network.pn_ipv6security_raguard`.

- [Synopsis](pn_ipv6security_raguard_module.md#synopsis)
- [Parameters](pn_ipv6security_raguard_module.md#parameters)
- [Examples](pn_ipv6security_raguard_module.md#examples)
- [Return Values](pn_ipv6security_raguard_module.md#return-values)

## [Synopsis](pn_ipv6security_raguard_module.md#id1)

- This module can be used to add ipv6 RA Guard Policy, Update ipv6 RA guard Policy and Remove ipv6 RA Guard Policy.

Aliases: network.netvisor.pn_ipv6security_raguard

## [Parameters](pn_ipv6security_raguard_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_access_list**  string | RA Guard Access List of Source IPs. |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_device**  string | RA Guard Device. host or router.  **Choices:**   - `"host"` - `"router"` |
| **pn_name**  string / required | RA Guard Policy Name. |
| **pn_prefix_list**  string | RA Guard Prefix List. |
| **pn_router_priority**  string | RA Guard Router Priority.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **state**  string | ipv6security-raguard configuration command.  **Choices:**   - `"present"` ← (default) - `"update"` - `"absent"` |

## [Examples](pn_ipv6security_raguard_module.md#id3)

```yaml+jinja
- name: Ipv6 security ragurad create
  community.network.pn_ipv6security_raguard:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_device: "host"

- name: Ipv6 security ragurad create
  community.network.pn_ipv6security_raguard:
    pn_cliswitch: "sw01"
    pn_name: "foo1"
    pn_device: "host"
    pn_access_list: "sample"
    pn_prefix_list: "sample"
    pn_router_priority: "low"

- name: Ipv6 security ragurad modify
  community.network.pn_ipv6security_raguard:
    pn_cliswitch: "sw01"
    pn_name: "foo1"
    pn_device: "router"
    pn_router_priority: "medium"
    state: "update"

- name: Ipv6 security ragurad delete
  community.network.pn_ipv6security_raguard:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    state: "absent"
```

## [Return Values](pn_ipv6security_raguard_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the ipv6security-raguard command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the ipv6security-raguard command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
