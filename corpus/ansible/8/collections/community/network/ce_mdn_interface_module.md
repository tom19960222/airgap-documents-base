---
collection: ansible
version: "8"
title: "community.network.ce_mdn_interface module – Manages MDN configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_mdn_interface_module.html
fetched_at: 2026-07-28T01:55:37+00:00
---
# community.network.ce_mdn_interface module – Manages MDN configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_mdn_interface`.

New in community.network 0.2.0

- [Synopsis](ce_mdn_interface_module.md#synopsis)
- [Parameters](ce_mdn_interface_module.md#parameters)
- [Notes](ce_mdn_interface_module.md#notes)
- [Examples](ce_mdn_interface_module.md#examples)
- [Return Values](ce_mdn_interface_module.md#return-values)

## [Synopsis](ce_mdn_interface_module.md#id1)

- Manages MDN configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_mdn_interface

## [Parameters](ce_mdn_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ifname**  string | Interface name. |
| **lldpenable**  string | Set global LLDP enable state.  **Choices:**   - `"enabled"` - `"disabled"` |
| **mdnstatus**  string | Set interface MDN enable state.  **Choices:**   - `"rxOnly"` - `"disabled"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_mdn_interface_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module works with connection `netconf`.

## [Examples](ce_mdn_interface_module.md#id4)

```yaml+jinja
- name: "Configure global LLDP enable state"
  community.network.ce_mdn_interface:
    lldpenable: enabled

- name: "Configure interface MDN enable state"
  community.network.ce_mdn_interface:
    ifname: 10GE1/0/1
    mdnstatus: rxOnly
```

## [Return Values](ce_mdn_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of global LLDP configration after module execution  **Returned:** always  **Sample:** `{"ifname": "10GE1/0/1", "lldpenable": "enabled", "mdnstatus": "rxOnly"}` |
| **existing**  dictionary | k/v pairs of existing global LLDP configration  **Returned:** always  **Sample:** `{"ifname": "10GE1/0/1", "lldpenable": "enabled", "mdnstatus": "disabled"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"ifname": "10GE1/0/1", "lldpenable": "enabled", "mdnstatus": "rxOnly", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["interface 10ge 1/0/1", "lldp mdn enable"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
