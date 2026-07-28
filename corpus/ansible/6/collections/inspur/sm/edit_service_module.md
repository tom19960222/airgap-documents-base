---
collection: ansible
version: "6"
title: "inspur.sm.edit_service module – Set service settings."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_service_module.html
fetched_at: 2026-07-27T17:53:25+00:00
---
# inspur.sm.edit_service module – Set service settings.

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
> To use it in a playbook, specify: `inspur.sm.edit_service`.

New in inspur.sm 0.1.0

- [Synopsis](edit_service_module.md#synopsis)
- [Parameters](edit_service_module.md#parameters)
- [Examples](edit_service_module.md#examples)
- [Return Values](edit_service_module.md#return-values)

## [Synopsis](edit_service_module.md#id1)

- Set service settings on Inspur server.

## [Parameters](edit_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **interface**  string | It shows the interface in which service is running.  The user can choose any one of the available interfaces.  Only the M5 model supports this parameter.  Choices:   - `"eth0"` - `"eth1"` - `"both"` - `"bond0"` |
| **non_secure_port**  integer | Used to configure non secure port number for the service.  Port value ranges from 1 to 65535. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **secure_port**  integer | Used to configure secure port number for the service.  Port value ranges from 1 to 65535. |
| **service_name**  string / required | Displays service name of the selected slot(readonly).  The *vnc* option is not supported in M5.  The *fd-media/telnet/snmp* option is not supported in M6.  Choices:   - `"web"` - `"kvm"` - `"cd-media"` - `"fd-media"` - `"hd-media"` - `"ssh"` - `"telnet"` - `"solssh"` - `"snmp"` - `"vnc"` |
| **state**  string | Displays the current status of the service, either active or inactive state.  Check this option to start the inactive service.  Choices:   - `"active"` - `"inactive"` |
| **timeout**  integer | Displays the session timeout value of the service.  For web, SSH and telnet service, user can configure the session timeout value.  Web timeout value ranges from 300 to 1800 seconds.  SSH and Telnet timeout value ranges from 60 to 1800 seconds.  timeout value should be in multiples of 60 seconds. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_service_module.md#id3)

```yaml+jinja
- name: Edit service test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Edit kvm"
    inspur.sm.edit_service:
      service_name: "kvm"
      state: "active"
      timeout: "1200"
      provider: "{{ ism }}"
```

## [Return Values](edit_service_module.md#id4)

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
