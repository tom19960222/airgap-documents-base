---
collection: ansible
version: "6"
title: "inspur.sm.edit_smtp_com module – Set SMTP information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_smtp_com_module.html
fetched_at: 2026-07-27T17:53:26+00:00
---
# inspur.sm.edit_smtp_com module – Set SMTP information.

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
> To use it in a playbook, specify: `inspur.sm.edit_smtp_com`.

New in inspur.sm 1.2.0

- [Synopsis](edit_smtp_com_module.md#synopsis)
- [Parameters](edit_smtp_com_module.md#parameters)
- [Examples](edit_smtp_com_module.md#examples)
- [Return Values](edit_smtp_com_module.md#return-values)

## [Synopsis](edit_smtp_com_module.md#id1)

- Set SMTP com information on Inspur server.
- Only the M6 models support this feature.

## [Parameters](edit_smtp_com_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **asset_tag**  string | product asset label, |
| **email**  string | Sender email. |
| **event_level**  string | Events above this level will be sent. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **host_name**  string | Server name. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **serial_number**  string | Serial number. |
| **server_auth**  string | SMTP server authentication.  Choices:   - `"enable"` - `"disable"` |
| **server_ip**  string | SMTP server IP. |
| **server_password**  string | SMTP server Password,lenth be 4 to 64 bits,cannot contain ‘ ‘(space).  Required when *server_auth=enable*. |
| **server_port**  integer | SMTP server port,The Identification for retry count configuration(1-65535). |
| **server_secure_port**  integer | SMTP server sesure port,The Identification for retry count configuration(1-65535). |
| **server_username**  string | SMTP server Username,lenth be 4 to 64 bits,  must start with letters and cannot contain ‘,’(comma) ‘:’(colon) ‘ ‘(space) ‘;’(semicolon) ‘\’(backslash).  Required when *server_auth=enable*. |
| **ssl_tls_enable**  string | SMTP SSLTLS Enable.  *ssl_tls_enable=disable*, when *star_tls_enable=enable*.  Choices:   - `"enable"` - `"disable"` |
| **star_tls_enable**  string | SMTP STARTTLS Enable.  *star_tls_enable=disable*, when *ssl_tls_enable=enable*.  Choices:   - `"enable"` - `"disable"` |
| **status**  string / required | SMTP Support.  Choices:   - `"enable"` - `"disable"` |
| **subject**  string | Email theme. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_smtp_com_module.md#id3)

```yaml+jinja
- name: Smtp com test
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

  - name: "Set smtp com information"
    inspur.sm.edit_smtp_com:
      status: "disable"
      provider: "{{ ism }}"

  - name: "Set smtp com information"
    inspur.sm.edit_smtp_com:
      status: "enable"
      server_ip: "100.2.2.2"
      email: "inspur@Inspur.com"
      server_auth: "enable"
      server_username: "admin"
      server_password: "1234qwer!@#$"
      provider: "{{ ism }}"
```

## [Return Values](edit_smtp_com_module.md#id4)

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
