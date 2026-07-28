---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_snmp_users module – Configures SNMP User parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_snmp_users_module.html
fetched_at: 2026-07-27T17:55:41+00:00
---
# mellanox.onyx.onyx_snmp_users module – Configures SNMP User parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_snmp_users`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_snmp_users_module.md#synopsis)
- [Parameters](onyx_snmp_users_module.md#parameters)
- [Examples](onyx_snmp_users_module.md#examples)
- [Return Values](onyx_snmp_users_module.md#return-values)

## [Synopsis](onyx_snmp_users_module.md#id1)

- This module provides declarative management of SNMP Users protocol params on Mellanox ONYX network devices.

## [Parameters](onyx_snmp_users_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **users**  list / elements=string | List of snmp users |
| **auth_password**  string | The password needed to configure the hash type. |
| **auth_type**  string | Configures the hash type used to configure SNMP v3 security parameters.  Choices:   - `"md5"` - `"sha"` - `"sha224"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **capability_level**  string | Sets capability level for SET requests.  Choices:   - `"admin"` - `"monitor"` - `"unpriv"` - `"v_admin"` |
| **enabled**  boolean | Enables/Disables SNMP v3 access for the user.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the user. |
| **require_privacy**  boolean | Enables/Disables the Require privacy (encryption) for requests from this user  Choices:   - `false` - `true` |
| **set_access_enabled**  boolean | Enables/Disables SNMP SET requests for the user.  Choices:   - `false` - `true` |

## [Examples](onyx_snmp_users_module.md#id3)

```yaml+jinja
- name: Enables snmp user
  onyx_snmp_users:
    users:
       - name: sara
         enabled: true

- name: Enables snmp set requests
  onyx_snmp_users:
    users:
       - name: sara
         set_access_enabled: yes

- name: Enables user require privacy
  onyx_snmp_users:
    users:
       - name: sara
         require_privacy: true

- name: Configures user hash type
  onyx_snmp_users:
    users:
       - auth_type: md5
         auth_password: 1297sara1234sara

- name: Configures user capability_level
  onyx_snmp_users:
    users:
        - name: sara
          capability_level: admin
```

## [Return Values](onyx_snmp_users_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["snmp-server user <user_name> v3 enable", "no snmp-server user <user_name> v3 enable", "snmp-server user <user_name> v3 enable sets", "no snmp-server user <user_name> v3 enable sets", "snmp-server user <user_name> v3 require-privacy", "no snmp-server user <user_name> v3 require-privacy", "snmp-server user <user_name> v3 capability <capability_level>", "snmp-server user <user_name> v3 auth <hash_type> <password>"]` |

### Authors

- Sara Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
