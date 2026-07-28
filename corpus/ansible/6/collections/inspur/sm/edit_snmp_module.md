---
collection: ansible
version: "6"
title: "inspur.sm.edit_snmp module – Set snmp."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_snmp_module.html
fetched_at: 2026-07-27T17:53:28+00:00
---
# inspur.sm.edit_snmp module – Set snmp.

> **Note:**
>
> This module is part of the [inspur.sm collection](https://galaxy.ansible.com/inspur/sm) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.sm`.
>
> To use it in a playbook, specify: `inspur.sm.edit_snmp`.

New in inspur.sm 0.1.0

- [Synopsis](edit_snmp_module.md#synopsis)
- [Parameters](edit_snmp_module.md#parameters)
- [Examples](edit_snmp_module.md#examples)
- [Return Values](edit_snmp_module.md#return-values)

## [Synopsis](edit_snmp_module.md#id1)

- Set snmp on Inspur server.

## [Parameters](edit_snmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_password**  string | Set auth password of V3 trap or v3get/v3set,  Password is a string of 8 to 16 alpha-numeric characters.  Required when *auth_protocol* is either `SHA` or `MD5`. |
| **auth_protocol**  string | Choose authentication of V3 trap or v3get/v3set.  Choices:   - `"NONE"` - `"SHA"` - `"MD5"` |
| **community**  string | Community of v1/v2c or v1get/v1set/v2cget/v2cset.  Only the M5 models support this feature. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **priv_password**  string | Set privacy password of V3 trap or v3get/v3set,  password is a string of 8 to 16 alpha-numeric characters.  Required when *priv_protocol* is either `DES` or `AES`. |
| **priv_protocol**  string | Choose Privacy of V3 trap or v3get/v3set.  Choices:   - `"NONE"` - `"DES"` - `"AES"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **read_community**  string | Read Only Community,Community should between 1 and 16 characters.  Only the M6 models support this feature. |
| **read_write_community**  string | Read And Write Community,Community should between 1 and 16 characters.  Only the M6 models support this feature. |
| **snmp_status**  list / elements=string | NMP read/write status of customize,  the input parameters are ‘v1get’, ‘v1set’, ‘v2cget’, ‘v2cset’, ‘v3get’, ‘v3set’,separated by commas,such as v1get,v1set,v2cget.  Only the M5 models support this feature. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **v1status**  string | SNMP V1 enable.  Choices:   - `"enable"` - `"disable"` |
| **v2status**  string | SNMP V2 enable.  Choices:   - `"enable"` - `"disable"` |
| **v3status**  string | SNMP V3 enable.  Choices:   - `"enable"` - `"disable"` |
| **v3username**  string | Set user name of V3 trap or v3get/v3set. |
| **version**  integer | SNMP trap version option, 0 - ‘v1’, 1 - ‘v2c’, 2 - ‘v3’, 3 - ‘all’, 4 - ‘customize’.  Only the M5 models support this feature.  Choices:   - `0` - `1` - `2` - `3` - `4` |

## [Examples](edit_snmp_module.md#id3)

```yaml+jinja
- name: Snmp test
  hosts: ism
  no_log: true
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set snmp get/set"
    inspur.sm.edit_snmp:
      community: "test"
      v3username: "Inspur"
      provider: "{{ ism }}"
```

## [Return Values](edit_snmp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

[Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
[Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
