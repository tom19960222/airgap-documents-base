---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_ntp module – Manage NTP general configurations and ntp keys configurations on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_ntp_module.html
fetched_at: 2026-07-27T17:55:34+00:00
---
# mellanox.onyx.onyx_ntp module – Manage NTP general configurations and ntp keys configurations on Mellanox ONYX network devices

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_ntp`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_ntp_module.md#synopsis)
- [Parameters](onyx_ntp_module.md#parameters)
- [Examples](onyx_ntp_module.md#examples)
- [Return Values](onyx_ntp_module.md#return-values)

## [Synopsis](onyx_ntp_module.md#id1)

- This module provides declarative management of NTP & NTP Keys on Mellanox ONYX network devices.

## [Parameters](onyx_ntp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authenticate_state**  string | State of the NTP authentication configuration.  Choices:   - `"enabled"` - `"disabled"` |
| **ntp_authentication_keys**  list / elements=string | List of ntp authentication keys |
| **auth_key_encrypt_type**  string / required | encryption type used to configure ntp authentication key.  Choices:   - `"md5"` - `"sha1"` |
| **auth_key_id**  integer / required | Configures ntp key-id, range 1-65534 |
| **auth_key_password**  string / required | password used for ntp authentication key. |
| **auth_key_state**  string | Used to decide if you want to delete given ntp key or not  Choices:   - `"present"` - `"absent"` |
| **state**  string | State of the NTP configuration.  Choices:   - `"enabled"` - `"disabled"` |
| **trusted_keys**  list / elements=string | List of ntp trusted keys |

## [Examples](onyx_ntp_module.md#id3)

```yaml+jinja
- name: Configure NTP
  onyx_ntp:
    state: enabled
    authenticate_state: enabled
    ntp_authentication_keys:
            - auth_key_id: 1
              auth_key_encrypt_type: md5
              auth_key_password: 12345
              auth_key_state: absent
    trusted_keys: 1,2,3
```

## [Return Values](onyx_ntp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["ntp enable", "ntp disable", "ntp authenticate", "no ntp authenticate", "ntp authentication-key 1 md5 12345", "no ntp authentication-key 1", "ntp trusted-key 1,2,3"]` |

### Authors

- Sara-Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
