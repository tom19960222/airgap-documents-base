---
collection: ansible
version: "8"
title: "community.network.ce_bfd_global module – Manages BFD global configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_bfd_global_module.html
fetched_at: 2026-07-28T01:55:14+00:00
---
# community.network.ce_bfd_global module – Manages BFD global configuration on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_bfd_global`.

- [Synopsis](ce_bfd_global_module.md#synopsis)
- [Parameters](ce_bfd_global_module.md#parameters)
- [Notes](ce_bfd_global_module.md#notes)
- [Examples](ce_bfd_global_module.md#examples)
- [Return Values](ce_bfd_global_module.md#return-values)

## [Synopsis](ce_bfd_global_module.md#id1)

- Manages BFD global configuration on HUAWEI CloudEngine devices.

Aliases: network.cloudengine.ce_bfd_global

## [Parameters](ce_bfd_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bfd_enable**  string | Enables the global Bidirectional Forwarding Detection (BFD) function.  **Choices:**   - `"enable"` - `"disable"` |
| **damp_init_wait_time**  string | Specifies an initial flapping suppression time for a BFD session. The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 2000. |
| **damp_max_wait_time**  string | Specifies a maximum flapping suppression time for a BFD session. The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 15000. |
| **damp_second_wait_time**  string | Specifies a secondary flapping suppression time for a BFD session. The value is an integer ranging from 1 to 3600000, in milliseconds. The default value is 5000. |
| **default_ip**  string | Specifies the default multicast IP address. The value ranges from 224.0.0.107 to 224.0.0.250. |
| **delay_up_time**  string | Specifies the delay before a BFD session becomes Up. The value is an integer ranging from 1 to 600, in seconds. The default value is 0, indicating that a BFD session immediately becomes Up. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tos_exp_dynamic**  string | Indicates the priority of BFD control packets for dynamic BFD sessions. The value is an integer ranging from 0 to 7. The default priority is 7, which is the highest priority of BFD control packets. |
| **tos_exp_static**  string | Indicates the priority of BFD control packets for static BFD sessions. The value is an integer ranging from 0 to 7. The default priority is 7, which is the highest priority of BFD control packets. |

## [Notes](ce_bfd_global_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bfd_global_module.md#id4)

```yaml+jinja
- name: Bfd global module test
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
  - name: Enable the global BFD function
    community.network.ce_bfd_global:
      bfd_enable: enable
      provider: '{{ cli }}'

  - name: Set the default multicast IP address to 224.0.0.150
    community.network.ce_bfd_global:
      bfd_enable: enable
      default_ip: 224.0.0.150
      state: present
      provider: '{{ cli }}'

  - name: Set the priority of BFD control packets for dynamic and static BFD sessions
    community.network.ce_bfd_global:
      bfd_enable: enable
      tos_exp_dynamic: 5
      tos_exp_static: 6
      state: present
      provider: '{{ cli }}'

  - name: Disable the global BFD function
    community.network.ce_bfd_global:
      bfd_enable: disable
      provider: '{{ cli }}'
```

## [Return Values](ce_bfd_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"global": {"bfdEnable": "true", "dampInitWaitTime": "2000", "dampMaxWaitTime": "12000", "dampSecondWaitTime": "5000", "defaultIp": "224.0.0.184", "delayUpTimer": null, "tosExp": "7", "tosExpStatic": "7"}}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"global": {"bfdEnable": "false", "dampInitWaitTime": "2000", "dampMaxWaitTime": "12000", "dampSecondWaitTime": "5000", "defaultIp": "224.0.0.184", "delayUpTimer": null, "tosExp": "7", "tosExpStatic": "7"}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"bfd_enalbe": "enable", "damp_init_wait_time": null, "damp_max_wait_time": null, "damp_second_wait_time": null, "default_ip": null, "delayUpTimer": null, "state": "present", "tos_exp_dynamic": null, "tos_exp_static": null}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bfd"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
