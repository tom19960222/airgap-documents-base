---
collection: ansible
version: "8"
title: "community.network.ce_mtu module – Manages MTU settings on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_mtu_module.html
fetched_at: 2026-07-28T01:55:39+00:00
---
# community.network.ce_mtu module – Manages MTU settings on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_mtu`.

- [Synopsis](ce_mtu_module.md#synopsis)
- [Parameters](ce_mtu_module.md#parameters)
- [Notes](ce_mtu_module.md#notes)
- [Examples](ce_mtu_module.md#examples)
- [Return Values](ce_mtu_module.md#return-values)

## [Synopsis](ce_mtu_module.md#id1)

- Manages MTU settings on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_mtu

## [Parameters](ce_mtu_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interface**  string | Full name of interface, i.e. 40GE1/0/22. |
| **jumbo_max**  string | Maximum frame size. The default value is 9216. The value is an integer and expressed in bytes. The value range is 1536 to 12224 for the CE12800 and 1536 to 12288 for ToR switches. |
| **jumbo_min**  string | Non-jumbo frame size threshold. The default value is 1518. The value is an integer that ranges from 1518 to jumbo_max, in bytes. |
| **mtu**  string | MTU for a specific interface. The value is an integer ranging from 46 to 9600, in bytes. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_mtu_module.md#id3)

> **Note:**
>
> - Either `sysmtu` param is required or `interface` AND `mtu` params are req’d.
> - `state=absent` unconfigures a given MTU if that value is currently present.
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_mtu_module.md#id4)

```yaml+jinja
- name: Mtu test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Config jumboframe on 40GE1/0/22"
    community.network.ce_mtu:
      interface: 40GE1/0/22
      jumbo_max: 9000
      jumbo_min: 8000
      provider: "{{ cli }}"

  - name: "Config mtu on 40GE1/0/22 (routed interface)"
    community.network.ce_mtu:
      interface: 40GE1/0/22
      mtu: 1600
      provider: "{{ cli }}"

  - name: "Config mtu on 40GE1/0/23 (switched interface)"
    community.network.ce_mtu:
      interface: 40GE1/0/22
      mtu: 9216
      provider: "{{ cli }}"

  - name: "Config mtu and jumboframe on 40GE1/0/22 (routed interface)"
    community.network.ce_mtu:
      interface: 40GE1/0/22
      mtu: 1601
      jumbo_max: 9001
      jumbo_min: 8001
      provider: "{{ cli }}"

  - name: "Unconfigure mtu and jumboframe on a given interface"
    community.network.ce_mtu:
      state: absent
      interface: 40GE1/0/22
      provider: "{{ cli }}"
```

## [Return Values](ce_mtu_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of mtu/sysmtu values after module execution  **Returned:** always  **Sample:** `{"jumbo_max": "9000", "jumbo_min": "8000", "mtu": "1700"}` |
| **existing**  dictionary | k/v pairs of existing mtu/sysmtu on the interface/system  **Returned:** always  **Sample:** `{"jumbo_max": "9216", "jumbo_min": "1518", "mtu": "1600"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"jumbo_max": "9000", "jumbo_min": "8000", "mtu": "1700"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["interface 40GE1/0/23", "mtu 1700", "jumboframe enable 9000 8000"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
