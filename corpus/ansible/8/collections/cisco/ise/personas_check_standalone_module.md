---
collection: ansible
version: "8"
title: "cisco.ise.personas_check_standalone module – Ensure the node is in standalone mode"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/personas_check_standalone_module.html
fetched_at: 2026-07-28T01:30:00+00:00
---
# cisco.ise.personas_check_standalone module – Ensure the node is in standalone mode

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
> see [Requirements](personas_check_standalone_module.md#ansible-collections-cisco-ise-personas-check-standalone-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.personas_check_standalone`.

New in cisco.ise 0.0.8

- [Synopsis](personas_check_standalone_module.md#synopsis)
- [Requirements](personas_check_standalone_module.md#requirements)
- [Parameters](personas_check_standalone_module.md#parameters)
- [Notes](personas_check_standalone_module.md#notes)
- [See Also](personas_check_standalone_module.md#see-also)
- [Examples](personas_check_standalone_module.md#examples)
- [Return Values](personas_check_standalone_module.md#return-values)

## [Synopsis](personas_check_standalone_module.md#id1)

- Ensure the mode is in standalone mode

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](personas_check_standalone_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.25.1
- python >= 3.5

## [Parameters](personas_check_standalone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname for the node for which the certificate will be exported. |
| **ip**  string | The IP address of the node |
| **ise_verify**  boolean | Whether or not to verify the identity of the node.  **Choices:**   - `false` - `true` |
| **ise_version**  string | The version of the ISE node. |
| **ise_wait_on_rate_limit**  boolean | Whether or not to wait on rate limit  **Choices:**   - `false` - `true` |
| **password**  string | The password for the node. |
| **username**  string | The username for the node. |

## [Notes](personas_check_standalone_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`

## [See Also](personas_check_standalone_module.md#id5)

> **See also:**
>
> cisco.ise.plugins.modules.personas_check_standalone
> :   The official documentation on the **cisco.ise.plugins.modules.personas_check_standalone** module.

## [Examples](personas_check_standalone_module.md#id6)

```yaml+jinja
- name: Check if all nodes are in STANDALONE state
  cisco.ise.personas_check_standalone:
    ip: "{{ item.ip }}"
    username: admin
    password: cisco123
    hostname: "{{ item.hostname }}"
  loop:
    - ip: 10.1.1.1
      hostname: ise-pan-server-1
    - ip: 10.1.1.2
      hostname: ise-pan-server-2
    - ip: 10.1.1.3
      hostname: ise-psn-server-1
    - ip: 10.1.1.4
      hostname: ise-psn-server-2
```

## [Return Values](personas_check_standalone_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  string | A string stating that the node is in standalone mode  **Returned:** always  **Sample:** `"Node ise-pan-server-1 is in STANDALONE mode"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
