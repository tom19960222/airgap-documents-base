---
collection: ansible
version: "6"
title: "community.network.pn_fabric_local module – CLI command to modify fabric-local"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_fabric_local_module.html
fetched_at: 2026-07-27T17:19:21+00:00
---
# community.network.pn_fabric_local module – CLI command to modify fabric-local

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
> To use it in a playbook, specify: `community.network.pn_fabric_local`.

- [Synopsis](pn_fabric_local_module.md#synopsis)
- [Parameters](pn_fabric_local_module.md#parameters)
- [Examples](pn_fabric_local_module.md#examples)
- [Return Values](pn_fabric_local_module.md#return-values)

## [Synopsis](pn_fabric_local_module.md#id1)

- This module can be used to modify fabric local information.

## [Parameters](pn_fabric_local_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string / required | Target switch to run the CLI on. |
| **pn_control_network**  string | control plane network.  Choices:   - `"in-band"` - `"mgmt"` - `"vmgmt"` |
| **pn_fabric_advertisement_network**  string | network to send fabric advertisements on.  Choices:   - `"inband-mgmt"` - `"inband-only"` - `"inband-vmgmt"` - `"mgmt-only"` |
| **pn_fabric_network**  string | fabric administration network.  Choices:   - `"in-band"` - `"mgmt"` ← (default) - `"vmgmt"` |
| **pn_vlan**  string | VLAN assigned to fabric. |
| **state**  string | State the action to perform. Use `update` to modify the fabric-local.  Choices:   - `"update"` ← (default) |

## [Examples](pn_fabric_local_module.md#id3)

```yaml+jinja
- name: Fabric local module
  community.network.pn_fabric_local:
    pn_cliswitch: "sw01"
    pn_vlan: "500"

- name: Fabric local module
  community.network.pn_fabric_local:
    pn_cliswitch: "sw01"
    pn_fabric_advertisement_network: "mgmt-only"
```

## [Return Values](pn_fabric_local_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the fabric-local command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the fabric-local command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
