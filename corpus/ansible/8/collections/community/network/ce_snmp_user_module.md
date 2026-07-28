---
collection: ansible
version: "8"
title: "community.network.ce_snmp_user module – Manages SNMP user configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_snmp_user_module.html
fetched_at: 2026-07-28T01:55:54+00:00
---
# community.network.ce_snmp_user module – Manages SNMP user configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_snmp_user`.

- [Synopsis](ce_snmp_user_module.md#synopsis)
- [Parameters](ce_snmp_user_module.md#parameters)
- [Notes](ce_snmp_user_module.md#notes)
- [Examples](ce_snmp_user_module.md#examples)
- [Return Values](ce_snmp_user_module.md#return-values)

## [Synopsis](ce_snmp_user_module.md#id1)

- Manages SNMP user configurations on CloudEngine switches.

Aliases: network.cloudengine.ce_snmp_user

## [Parameters](ce_snmp_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aaa_local_user**  string | Unique name to identify the local user. |
| **acl_number**  string | Access control list number. |
| **auth_key**  string | The authentication password. Password length, 8-255 characters. |
| **auth_protocol**  string | Authentication protocol.  **Choices:**   - `"noAuth"` - `"md5"` - `"sha"` |
| **priv_key**  string | The encryption password. Password length 8-255 characters. |
| **priv_protocol**  string | Encryption protocol.  **Choices:**   - `"noPriv"` - `"des56"` - `"3des168"` - `"aes128"` - `"aes192"` - `"aes256"` |
| **remote_engine_id**  string | Remote engine id of the USM user. |
| **user_group**  string | Name of the group where user belongs to. |
| **usm_user_name**  string | Unique name to identify the USM user. |

## [Notes](ce_snmp_user_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_snmp_user_module.md#id4)

```yaml+jinja
- name: CloudEngine snmp user test
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

  - name: "Config SNMP usm user"
    community.network.ce_snmp_user:
      state: present
      usm_user_name: wdz_snmp
      remote_engine_id: 800007DB03389222111200
      acl_number: 2000
      user_group: wdz_group
      provider: "{{ cli }}"

  - name: "Undo SNMP usm user"
    community.network.ce_snmp_user:
      state: absent
      usm_user_name: wdz_snmp
      remote_engine_id: 800007DB03389222111200
      acl_number: 2000
      user_group: wdz_group
      provider: "{{ cli }}"

  - name: "Config SNMP local user"
    community.network.ce_snmp_user:
      state: present
      aaa_local_user: wdz_user
      auth_protocol: md5
      auth_key: huawei123
      priv_protocol: des56
      priv_key: huawei123
      provider: "{{ cli }}"

  - name: "Config SNMP local user"
    community.network.ce_snmp_user:
      state: absent
      aaa_local_user: wdz_user
      auth_protocol: md5
      auth_key: huawei123
      priv_protocol: des56
      priv_key: huawei123
      provider: "{{ cli }}"
```

## [Return Values](ce_snmp_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"snmp local user": {"local_user_info": []}, "snmp usm user": {"usm_user_info": [{"aclNumber": "2000", "engineID": "800007DB03389222111200", "groupName": "wdz_group", "userName": "wdz_snmp"}]}}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{"snmp local user": {"local_user_info": []}, "snmp usm user": {"usm_user_info": []}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"acl_number": "2000", "remote_engine_id": "800007DB03389222111200", "state": "present", "user_group": "wdz_group", "usm_user_name": "wdz_snmp"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["snmp-agent remote-engineid 800007DB03389222111200 usm-user v3 wdz_snmp wdz_group acl 2000"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
