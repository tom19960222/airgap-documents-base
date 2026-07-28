---
collection: ansible
version: "6"
title: "inspur.ispim.edit_smtp module – Set SMTP information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/edit_smtp_module.html
fetched_at: 2026-07-27T17:51:50+00:00
---
# inspur.ispim.edit_smtp module – Set SMTP information

> **Note:**
>
> This module is part of the [inspur.ispim collection](https://galaxy.ansible.com/inspur/ispim) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.ispim`.
> You need further requirements to be able to use this module,
> see [Requirements](edit_smtp_module.md#ansible-collections-inspur-ispim-edit-smtp-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_smtp`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_smtp_module.md#synopsis)
- [Requirements](edit_smtp_module.md#requirements)
- [Parameters](edit_smtp_module.md#parameters)
- [Notes](edit_smtp_module.md#notes)
- [Examples](edit_smtp_module.md#examples)
- [Return Values](edit_smtp_module.md#return-values)

## [Synopsis](edit_smtp_module.md#id1)

- Set SMTP information on Inspur server.
- Only the M5 models support this feature.

## [Requirements](edit_smtp_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_smtp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **email**  string | Sender email. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **interface**  string / required | LAN Channel,eth0 is shared,eth1 is dedicated.  Choices:   - `"eth0"` - `"eth1"` - `"bond0"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **primary_auth**  string | Primary SMTP server authentication.  Choices:   - `"enable"` - `"disable"` |
| **primary_ip**  string | Primary SMTP server IP. |
| **primary_name**  string | Primary SMTP server name. |
| **primary_password**  string | Primary SMTP server Password,lenth be 4 to 64 bits,cannot contain ‘ ‘(space).  Required when *primary_auth=enable*. |
| **primary_port**  integer | Primary SMTP server port,The Identification for retry count configuration(1-65535). |
| **primary_status**  string | Primary SMTP Support.  Choices:   - `"enable"` - `"disable"` |
| **primary_username**  string | Primary SMTP server Username,lenth be 4 to 64 bits,  must start with letters and cannot contain ‘,’(comma) ‘:’(colon) ‘ ‘(space) ‘;’(semicolon) ‘\’(backslash). |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **secondary_auth**  string | S.econdary SMTP server authentication  Choices:   - `"enable"` - `"disable"` |
| **secondary_ip**  string | Secondary SMTP server IP. |
| **secondary_name**  string | Secondary SMTP server name. |
| **secondary_password**  string | Secondary SMTP server Password,lenth be 4 to 64 bits,cannot contain ‘ ‘(space).  Required when *secondary_auth=enable*. |
| **secondary_port**  integer | Secondary SMTP server port,The Identification for retry count configuration(1-65535). |
| **secondary_status**  string | Secondary SMTP Support.  Choices:   - `"enable"` - `"disable"` |
| **secondary_username**  string | Secondary SMTP server Username,lenth be 4 to 64 bits,  must start with letters and cannot contain ‘,’(comma) ‘:’(colon) ‘ ‘(space) ‘;’(semicolon) ‘\’(backslash). |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_smtp_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_smtp_module.md#id5)

```yaml+jinja
- name: Smtp test
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

  - name: "Set smtp information"
    inspur.ispim.edit_smtp:
      interface: "eth0"
      email: "inspur@Inspur.com"
      primary_status: "enable"
      primary_ip: "100.2.2.2"
      primary_name: "inspur"
      primary_auth: "disable"
      provider: "{{ ism }}"

  - name: "Set smtp information"
    inspur.ispim.edit_smtp:
      interface: "eth0"
      email: "inspur@Inspur.com"
      primary_status: "enable"
      primary_ip: "100.2.2.2"
      primary_name: "inspur"
      primary_auth: "enable"
      primary_username: "test"
      primary_password: my_password
      provider: "{{ ism }}"
```

## [Return Values](edit_smtp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

### Authors

- WangBaoshan (@ispim)

### Collection links

[Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
[Repository (Sources)](https://github.com/ispim/inspur.ispim)
