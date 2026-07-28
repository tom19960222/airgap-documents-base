---
collection: ansible
version: "8"
title: "cisco.ise.personas_promote_primary module – Promote a node as the primary node"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/personas_promote_primary_module.html
fetched_at: 2026-07-28T01:30:01+00:00
---
# cisco.ise.personas_promote_primary module – Promote a node as the primary node

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](personas_promote_primary_module.md#ansible-collections-cisco-ise-personas-promote-primary-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.personas_promote_primary`.

New in cisco.ise 0.0.8

- [Synopsis](personas_promote_primary_module.md#synopsis)
- [Requirements](personas_promote_primary_module.md#requirements)
- [Parameters](personas_promote_primary_module.md#parameters)
- [Notes](personas_promote_primary_module.md#notes)
- [See Also](personas_promote_primary_module.md#see-also)
- [Examples](personas_promote_primary_module.md#examples)
- [Return Values](personas_promote_primary_module.md#return-values)

## [Synopsis](personas_promote_primary_module.md#id1)

- Promote a node as the primary node

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](personas_promote_primary_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.25.1
- python >= 3.5

## [Parameters](personas_promote_primary_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ip**  string | The IP address of the primary node |
| **ise_verify**  boolean | Whether or not to verify the identity of the node.  **Choices:**   - `false` - `true` |
| **ise_version**  string | The version of the ISE node. |
| **ise_wait_on_rate_limit**  boolean | Whether or not to wait on rate limit  **Choices:**   - `false` - `true` |
| **password**  string | The password to log into the primary node. |
| **username**  string | The username to log into the primary node. |

## [Notes](personas_promote_primary_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`

## [See Also](personas_promote_primary_module.md#id5)

> **See also:**
>
> cisco.ise.plugins.modules.personas_promote_primary
> :   The official documentation on the **cisco.ise.plugins.modules.personas_promote_primary** module.

## [Examples](personas_promote_primary_module.md#id6)

```yaml+jinja
- name: Promote primary node
  cisco.ise.personas_promote_primary:
    ip: 10.1.1.1
    username: admin
    password: Cisco123
```

## [Return Values](personas_promote_primary_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  string | A string stating that the node was promoted to primary  **Returned:** always  **Sample:** `"Primary node was successfully updated"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
