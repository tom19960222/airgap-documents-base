---
collection: ansible
version: "6"
title: "community.network.pn_vrouter_loopback_interface module – CLI command to add/remove vrouter-loopback-interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_vrouter_loopback_interface_module.html
fetched_at: 2026-07-27T17:19:36+00:00
---
# community.network.pn_vrouter_loopback_interface module – CLI command to add/remove vrouter-loopback-interface

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
> To use it in a playbook, specify: `community.network.pn_vrouter_loopback_interface`.

- [Synopsis](pn_vrouter_loopback_interface_module.md#synopsis)
- [Parameters](pn_vrouter_loopback_interface_module.md#parameters)
- [Examples](pn_vrouter_loopback_interface_module.md#examples)
- [Return Values](pn_vrouter_loopback_interface_module.md#return-values)

## [Synopsis](pn_vrouter_loopback_interface_module.md#id1)

- This module can be used to add loopback interface to a vRouter or remove loopback interface from a vRouter.

## [Parameters](pn_vrouter_loopback_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_index**  string | loopback index from 1 to 255. |
| **pn_ip**  string / required | loopback IP address. |
| **pn_vrouter_name**  string / required | name of service config. |
| **state**  string | State the action to perform. Use `present` to add vrouter-loopback-interface and `absent` to remove vrouter-loopback-interface.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_vrouter_loopback_interface_module.md#id3)

```yaml+jinja
- name: Add vrouter loopback interface
  community.network.pn_vrouter_loopback_interface:
    state: "present"
    pn_cliswitch: "sw01"
    pn_vrouter_name: "sw01-vrouter"
    pn_ip: "192.168.10.1"

- name: Remove vrouter loopback interface
  community.network.pn_vrouter_loopback_interface:
    state: "absent"
    pn_cliswitch: "sw01"
    pn_vrouter_name: "sw01-vrouter"
    pn_ip: "192.168.10.1"
    pn_index: "2"
```

## [Return Values](pn_vrouter_loopback_interface_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error response from the vrouter-loopback-interface command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the vrouter-loopback-interface command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
