---
collection: ansible
version: "8"
title: "community.network.ce_aaa_server module – Manages AAA server global configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_aaa_server_module.html
fetched_at: 2026-07-28T01:55:10+00:00
---
# community.network.ce_aaa_server module – Manages AAA server global configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_aaa_server`.

- [Synopsis](ce_aaa_server_module.md#synopsis)
- [Parameters](ce_aaa_server_module.md#parameters)
- [Notes](ce_aaa_server_module.md#notes)
- [Examples](ce_aaa_server_module.md#examples)
- [Return Values](ce_aaa_server_module.md#return-values)

## [Synopsis](ce_aaa_server_module.md#id1)

- Manages AAA server global configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_aaa_server

## [Parameters](ce_aaa_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accounting_mode**  string | Accounting Mode.  **Choices:**   - `"invalid"` - `"hwtacacs"` - `"radius"` - `"none"` ← (default) |
| **acct_scheme_name**  string | Accounting scheme name. The value is a string of 1 to 32 characters. |
| **authen_scheme_name**  string | Name of an authentication scheme. The value is a string of 1 to 32 characters. |
| **author_scheme_name**  string | Name of an authorization scheme. The value is a string of 1 to 32 characters. |
| **domain_name**  string | Name of a domain. The value is a string of 1 to 64 characters. |
| **first_authen_mode**  string | Preferred authentication mode.  **Choices:**   - `"invalid"` - `"local"` ← (default) - `"hwtacacs"` - `"radius"` - `"none"` |
| **first_author_mode**  string | Preferred authorization mode.  **Choices:**   - `"invalid"` - `"local"` ← (default) - `"hwtacacs"` - `"if-authenticated"` - `"none"` |
| **hwtacas_template**  string | Name of a HWTACACS template. The value is a string of 1 to 32 case-insensitive characters. |
| **local_user_group**  string | Name of the user group where the user belongs. The user inherits all the rights of the user group. The value is a string of 1 to 32 characters. |
| **radius_server_group**  string | RADIUS server group’s name. The value is a string of 1 to 32 case-insensitive characters. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](ce_aaa_server_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_aaa_server_module.md#id4)

```yaml+jinja
- name: AAA server test
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

  - name: "Radius authentication Server Basic settings"
    community.network.ce_aaa_server:
      state: present
      authen_scheme_name: test1
      first_authen_mode: radius
      radius_server_group: test2
      provider: "{{ cli }}"

  - name: "Undo radius authentication Server Basic settings"
    community.network.ce_aaa_server:
      state: absent
      authen_scheme_name: test1
      first_authen_mode: radius
      radius_server_group: test2
      provider: "{{ cli }}"

  - name: "Hwtacacs accounting Server Basic settings"
    community.network.ce_aaa_server:
      state: present
      acct_scheme_name: test1
      accounting_mode: hwtacacs
      hwtacas_template: test2
      provider: "{{ cli }}"

  - name: "Undo hwtacacs accounting Server Basic settings"
    community.network.ce_aaa_server:
      state: absent
      acct_scheme_name: test1
      accounting_mode: hwtacacs
      hwtacas_template: test2
      provider: "{{ cli }}"
```

## [Return Values](ce_aaa_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"accounting scheme": [["hwtacacs", "test1"]], "hwtacacs template": ["huawei", "test2"]}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{"accounting scheme": [["hwtacacs"], ["default"]], "hwtacacs template": ["huawei"]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"accounting_mode": "hwtacacs", "acct_scheme_name": "test1", "hwtacas_template": "test2", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["accounting-scheme test1", "accounting-mode hwtacacs", "hwtacacs server template test2", "hwtacacs enable"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
