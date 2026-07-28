---
collection: ansible
version: "8"
title: "community.network.ce_netstream_aging module – Manages timeout mode of NetStream on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_netstream_aging_module.html
fetched_at: 2026-07-28T01:55:42+00:00
---
# community.network.ce_netstream_aging module – Manages timeout mode of NetStream on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_netstream_aging`.

- [Synopsis](ce_netstream_aging_module.md#synopsis)
- [Parameters](ce_netstream_aging_module.md#parameters)
- [Notes](ce_netstream_aging_module.md#notes)
- [Examples](ce_netstream_aging_module.md#examples)
- [Return Values](ce_netstream_aging_module.md#return-values)

## [Synopsis](ce_netstream_aging_module.md#id1)

- Manages timeout mode of NetStream on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_netstream_aging

## [Parameters](ce_netstream_aging_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **manual_slot**  string | Specifies the slot number of netstream manual timeout. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout_interval**  string | Netstream timeout interval. If is active type the interval is 1-60. If is inactive ,the interval is 5-600.  **Default:** `30` |
| **timeout_type**  string | Netstream timeout type.  **Choices:**   - `"active"` - `"inactive"` - `"tcp-session"` - `"manual"` |
| **type**  string | Specifies the packet type of netstream timeout active interval.  **Choices:**   - `"ip"` - `"vxlan"` |

## [Notes](ce_netstream_aging_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_netstream_aging_module.md#id4)

```yaml+jinja
- name: Netstream aging module test
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

  - name: Configure netstream ip timeout active interval , the interval is 40 minutes.
    community.network.ce_netstream_aging:
      timeout_interval: 40
      type: ip
      timeout_type: active
      state: present
      provider: "{{ cli }}"

  - name: Configure netstream vxlan timeout active interval , the interval is 40 minutes.
    community.network.ce_netstream_aging:
      timeout_interval: 40
      type: vxlan
      timeout_type: active
      active_state: present
      provider: "{{ cli }}"

  - name: Delete netstream ip timeout active interval , set the ip timeout interval to 30 minutes.
    community.network.ce_netstream_aging:
      type: ip
      timeout_type: active
      state: absent
      provider: "{{ cli }}"

  - name: Delete netstream vxlan timeout active interval , set the vxlan timeout interval to 30 minutes.
    community.network.ce_netstream_aging:
      type: vxlan
      timeout_type: active
      state: absent
      provider: "{{ cli }}"

  - name: Enable netstream ip tcp session timeout.
    community.network.ce_netstream_aging:
      type: ip
      timeout_type: tcp-session
      state: present
      provider: "{{ cli }}"

  - name: Enable netstream vxlan tcp session timeout.
    community.network.ce_netstream_aging:
      type: vxlan
      timeout_type: tcp-session
      state: present
      provider: "{{ cli }}"

  - name: Disable netstream ip tcp session timeout.
    community.network.ce_netstream_aging:
      type: ip
      timeout_type: tcp-session
      state: absent
      provider: "{{ cli }}"

  - name: Disable netstream vxlan tcp session timeout.
    community.network.ce_netstream_aging:
      type: vxlan
      timeout_type: tcp-session
      state: absent
      provider: "{{ cli }}"
```

## [Return Values](ce_netstream_aging_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"active_timeout": [{"ip": 30, "vxlan": 30}], "inactive_timeout": [{"ip": 30, "vxlan": 30}], "tcp_timeout": [{"ip": "disable", "vxlan": "disable"}]}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"active_timeout": [{"ip": "40", "vxlan": 30}], "inactive_timeout": [{"ip": 30, "vxlan": 30}], "tcp_timeout": [{"ip": "disable", "vxlan": "disable"}]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"state": "absent", "timeout_interval": "40", "timeout_type": "active", "type": "ip"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["undo netstream timeout ip active 40"]` |

### Authors

- YangYang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
