---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_snmp_hosts module – Configures SNMP host parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_snmp_hosts_module.html
fetched_at: 2026-07-27T17:55:40+00:00
---
# mellanox.onyx.onyx_snmp_hosts module – Configures SNMP host parameters

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
> To use it in a playbook, specify: `mellanox.onyx.onyx_snmp_hosts`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_snmp_hosts_module.md#synopsis)
- [Parameters](onyx_snmp_hosts_module.md#parameters)
- [Examples](onyx_snmp_hosts_module.md#examples)
- [Return Values](onyx_snmp_hosts_module.md#return-values)

## [Synopsis](onyx_snmp_hosts_module.md#id1)

- This module provides declarative management of SNMP hosts protocol params on Mellanox ONYX network devices.

## [Parameters](onyx_snmp_hosts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hosts**  list / elements=string | List of snmp hosts |
| **auth_password**  string | The password needed to configure the auth type. |
| **auth_type**  string | Configures SNMP v3 security parameters, specifying passwords in a nother parameter (auth_password) (passwords are always stored encrypted).  Choices:   - `"md5"` - `"sha"` - `"sha224"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **enabled**  boolean | Temporarily Enables/Disables sending of all notifications to this host.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the host. |
| **notification_type**  string | Configures the type of sending notification to the specified host.  Choices:   - `"trap"` - `"inform"` |
| **port**  string | Overrides default target port for this host. |
| **privacy_password**  string | The password needed to configure the privacy type. |
| **privacy_type**  string | Specifys SNMP v3 privacy settings for this user.  Choices:   - `"3des"` - `"aes-128"` - `"aes-192"` - `"aes-192-cfb"` - `"aes-256"` - `"aes-256-cfb"` - `"des"` |
| **state**  string | Used to decide if you want to delete the specified host or not.  Choices:   - `"present"` - `"absent"` |
| **user_name**  string | Specifys username for this inform sink. |
| **version**  string | Specifys SNMP version of informs to send.  Choices:   - `"1"` - `"2c"` - `"3"` |

## [Examples](onyx_snmp_hosts_module.md#id3)

```yaml+jinja
- name: Enables snmp host
  onyx_snmp_hosts:
      hosts:
       - name: 1.1.1.1
         enabled: true

- name: Configures snmp host with version 2c
  onyx_snmp_hosts:
      hosts:
         - name: 2.3.2.4
           enabled: true
           notification_type: trap
           port: 66
           version: 2c

- name: Configures snmp host with version 3 and configures it with user as sara
  onyx_snmp_hosts:
       hosts:
         - name: 2.3.2.4
           enabled: true
           notification_type: trap
           port: 66
           version: 3
           user_name: sara
           auth_type: sha
           auth_password: jnbdfijbdsf
           privacy_type: 3des
           privacy_password: nojfd8uherwiugfh

- name: Deletes the snmp host
  onyx_snmp_hosts:
        hosts:
          - name: 2.3.2.4
            state: absent
```

## [Return Values](onyx_snmp_hosts_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["snmp-server host <host_name> disable", "no snmp-server host <host_name> disable", "snmp-server host <host_name> informs port <port_number> version <version_number>", "snmp-server host <host_name> traps port <port_number> version <version_number>", "snmp-server host <host_name> informs port <port_number> version <version_number>  user <user_name> auth <auth_type> <auth_password> priv <privacy_type> <privacy_password>", "snmp-server host <host_name> traps port <port_number> version <version_number>  user <user_name> auth <auth_type> <auth_password> priv <privacy_type> <privacy_password>", "no snmp-server host <host_name>."]` |

### Authors

- Sara Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
