---
collection: ansible
version: "6"
title: "cisco.ise.personas_register_node module – Register a node to the primary"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/personas_register_node_module.html
fetched_at: 2026-07-27T16:58:39+00:00
---
# cisco.ise.personas_register_node module – Register a node to the primary

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](personas_register_node_module.md#ansible-collections-cisco-ise-personas-register-node-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.personas_register_node`.

New in cisco.ise 2.4.0

- [Synopsis](personas_register_node_module.md#synopsis)
- [Requirements](personas_register_node_module.md#requirements)
- [Parameters](personas_register_node_module.md#parameters)
- [Notes](personas_register_node_module.md#notes)
- [See Also](personas_register_node_module.md#see-also)
- [Examples](personas_register_node_module.md#examples)
- [Return Values](personas_register_node_module.md#return-values)

## [Synopsis](personas_register_node_module.md#id1)

- Register a node to the primary

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](personas_register_node_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.25.1
- python >= 3.5

## [Parameters](personas_register_node_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **fqdn**  string | The fully qualified domain name of the node. |
| **ise_verify**  boolean | Whether or not to verify the identity of the node.  Choices:   - `false` - `true` |
| **ise_version**  string | The version of the ISE node. |
| **ise_wait_on_rate_limit**  boolean | Whether or not to wait on rate limit  Choices:   - `false` - `true` |
| **password**  string | The password to log into the node. |
| **primary_ip**  string | The IP address of the primary node. |
| **primary_password**  string | The password for the primary node. |
| **primary_username**  string | The username for the primary node. |
| **roles**  list / elements=string | The roles to be fulfilled by this node. Possible roles are PrimaryAdmin, SecondaryAdmin, PrimaryMonitoring, SecondaryMonitoring, PrimaryDedicatedMonitoring, SecondaryDedicatedMonitoring, Standalone |
| **services**  list / elements=string | The services this node will run. Possible services are Session, Profiler, TC-NAC, SXP, DeviceAdmin, PassiveIdentity, pxGrid, pxGridCloud |
| **username**  string | The username to log into the node. |

## [Notes](personas_register_node_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`

## [See Also](personas_register_node_module.md#id5)

> **See also:**
>
> cisco.ise.plugins.modules.personas_register_node
> :   The official documentation on the **cisco.ise.plugins.modules.personas_register_node** module.

## [Examples](personas_register_node_module.md#id6)

```yaml+jinja
- name: Register the secondary node and PSN nodes to the cluster
  cisco.ise.personas_register_node:
    primary_ip: 10.1.1.1
    primary_username: admin
    primary_password: Cisco123
    fqdn: "{{ item.fqdn }}"
    username: admin
    password: cisco123
    roles: "{{ item.roles }}"
    services: "{{ item.services }}"
  loop:
    - fqdn: ise-pan-server-2.example.com
      roles:
        - SecondaryAdmin
        - SecondaryMonitoring
      services: []
    - fqdn: ise-psn-server-1.example.com
      roles: []
      services:
        - Session
        - Profiler
    - fqdn: ise-psn-server-2.example.com
      roles: []
      services:
        - Session
        - Profiler
```

## [Return Values](personas_register_node_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  string | A string stating that the node was successfully registered  Returned: always  Sample: `"Node ise-pan-server-2 updated successfully"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
