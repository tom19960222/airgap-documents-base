---
collection: ansible
version: "8"
title: "community.network.ce_ntp_auth module – Manages NTP authentication configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_ntp_auth_module.html
fetched_at: 2026-07-28T01:55:46+00:00
---
# community.network.ce_ntp_auth module – Manages NTP authentication configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_ntp_auth`.

- [Synopsis](ce_ntp_auth_module.md#synopsis)
- [Parameters](ce_ntp_auth_module.md#parameters)
- [Notes](ce_ntp_auth_module.md#notes)
- [Examples](ce_ntp_auth_module.md#examples)
- [Return Values](ce_ntp_auth_module.md#return-values)

## [Synopsis](ce_ntp_auth_module.md#id1)

- Manages NTP authentication configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_ntp_auth

## [Parameters](ce_ntp_auth_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_mode**  string | Specify authentication algorithm.  **Choices:**   - `"hmac-sha256"` - `"md5"` |
| **auth_pwd**  string | Plain text with length of 1 to 255, encrypted text with length of 20 to 392. |
| **auth_type**  string | Whether the given password is in cleartext or has been encrypted. If in cleartext, the device will encrypt it before storing it.  **Choices:**   - `"text"` - `"encrypt"` ← (default) |
| **authentication**  string | Configure ntp authentication enable or unconfigure ntp authentication enable.  **Choices:**   - `"enable"` - `"disable"` |
| **key_id**  string / required | Authentication key identifier (numeric). |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **trusted_key**  string | Whether the given key is required to be supplied by a time source for the device to synchronize to the time source.  **Choices:**   - `"enable"` - `"disable"` ← (default) |

## [Notes](ce_ntp_auth_module.md#id3)

> **Note:**
>
> - If `state=absent`, the module will attempt to remove the given key configuration. If a matching key configuration isn’t found on the device, the module will fail.
> - If `state=absent` and `authentication=on`, authentication will be turned on.
> - If `state=absent` and `authentication=off`, authentication will be turned off.
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_ntp_auth_module.md#id4)

```yaml+jinja
- name: NTP AUTH test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: "Configure ntp authentication key-id"
    community.network.ce_ntp_auth:
      key_id: 32
      auth_mode: md5
      auth_pwd: 11111111111111111111111

  - name: "Configure ntp authentication key-id and trusted authentication keyid"
    community.network.ce_ntp_auth:
      key_id: 32
      auth_mode: md5
      auth_pwd: 11111111111111111111111
      trusted_key: enable

  - name: "Configure ntp authentication key-id and authentication enable"
    community.network.ce_ntp_auth:
      key_id: 32
      auth_mode: md5
      auth_pwd: 11111111111111111111111
      authentication: enable

  - name: "Unconfigure ntp authentication key-id and trusted authentication keyid"
    community.network.ce_ntp_auth:
      key_id: 32
      state: absent

  - name: "Unconfigure ntp authentication key-id and authentication enable"
    community.network.ce_ntp_auth:
      key_id: 32
      authentication: enable
      state: absent
```

## [Return Values](ce_ntp_auth_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of ntp authentication after module execution  **Returned:** always  **Sample:** `{"authentication": "off", "authentication-keyid": [{"auth_mode": "md5", "key_id": "1", "trusted_key": "disable"}, {"auth_mode": "md5", "key_id": "32", "trusted_key": "enable"}]}` |
| **existing**  dictionary | k/v pairs of existing ntp authentication  **Returned:** always  **Sample:** `{"authentication": "off", "authentication-keyid": [{"auth_mode": "md5", "key_id": "1", "trusted_key": "disable"}]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"auth_mode": "md5", "auth_pwd": "1111", "auth_type": "text", "authentication": "enable", "key_id": "32", "state": "present", "trusted_key": "enable"}` |
| **state**  string | state as sent in from the playbook  **Returned:** always  **Sample:** `"present"` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["ntp authentication-key 32 md5 1111", "ntp trusted-key 32", "ntp authentication enable"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
