---
collection: ansible
version: "8"
title: "community.network.ce_dldp module – Manages global DLDP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_dldp_module.html
fetched_at: 2026-07-28T01:55:20+00:00
---
# community.network.ce_dldp module – Manages global DLDP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_dldp`.

- [Synopsis](ce_dldp_module.md#synopsis)
- [Parameters](ce_dldp_module.md#parameters)
- [Notes](ce_dldp_module.md#notes)
- [Examples](ce_dldp_module.md#examples)
- [Return Values](ce_dldp_module.md#return-values)

## [Synopsis](ce_dldp_module.md#id1)

- Manages global DLDP configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_dldp

## [Parameters](ce_dldp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_mode**  string | Specifies authentication algorithm of DLDP.  **Choices:**   - `"md5"` - `"simple"` - `"sha"` - `"hmac-sha256"` - `"none"` |
| **auth_pwd**  string | Specifies authentication password. The value is a string of 1 to 16 case-sensitive plaintexts or 24/32/48/108/128 case-sensitive encrypted characters. The string excludes a question mark (?). |
| **enable**  string | Set global DLDP enable state.  **Choices:**   - `"enable"` - `"disable"` |
| **reset**  string | Specify whether reset DLDP state of disabled interfaces.  **Choices:**   - `"enable"` - `"disable"` |
| **time_internal**  string | Specifies the interval for sending Advertisement packets. The value is an integer ranging from 1 to 100, in seconds. The default interval for sending Advertisement packets is 5 seconds. |
| **work_mode**  string | Set global DLDP work-mode.  **Choices:**   - `"enhance"` - `"normal"` |

## [Notes](ce_dldp_module.md#id3)

> **Note:**
>
> - The relevant configurations will be deleted if DLDP is disabled using enable=disable.
> - When using auth_mode=none, it will restore the default DLDP authentication mode. By default, DLDP packets are not authenticated.
> - By default, the working mode of DLDP is enhance, so you are advised to use work_mode=enhance to restore default DLDP working mode.
> - The default interval for sending Advertisement packets is 5 seconds, so you are advised to use time_interval=5 to restore default DLDP interval.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_dldp_module.md#id4)

```yaml+jinja
- name: DLDP test
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

  - name: "Configure global DLDP enable state"
    community.network.ce_dldp:
      enable: enable
      provider: "{{ cli }}"

  - name: "Configure DLDP work-mode and ensure global DLDP state is already enabled"
    community.network.ce_dldp:
      enable: enable
      work_mode: normal
      provider: "{{ cli }}"

  - name: "Configure advertisement message time interval in seconds and ensure global DLDP state is already enabled"
    community.network.ce_dldp:
      enable: enable
      time_interval: 6
      provider: "{{ cli }}"

  - name: "Configure a DLDP authentication mode and ensure global DLDP state is already enabled"
    community.network.ce_dldp:
      enable: enable
      auth_mode: md5
      auth_pwd: abc
      provider: "{{ cli }}"

  - name: "Reset DLDP state of disabled interfaces and ensure global DLDP state is already enabled"
    community.network.ce_dldp:
      enable: enable
      reset: enable
      provider: "{{ cli }}"
```

## [Return Values](ce_dldp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of global DLDP configuration after module execution  **Returned:** always  **Sample:** `{"enable": "enable", "reset": "enable", "time_internal": "12", "work_mode": "normal"}` |
| **existing**  dictionary | k/v pairs of existing global DLDP configuration  **Returned:** always  **Sample:** `{"enable": "disable", "reset": "disable", "time_internal": "5", "work_mode": "enhance"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"enable": "enable", "reset": "enable", "time_internal": "12", "work_mode": "normal"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["dldp enable", "dldp work-mode normal", "dldp interval 12", "dldp reset"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
