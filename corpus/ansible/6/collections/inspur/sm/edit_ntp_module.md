---
collection: ansible
version: "6"
title: "inspur.sm.edit_ntp module – Set NTP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_ntp_module.html
fetched_at: 2026-07-27T17:53:17+00:00
---
# inspur.sm.edit_ntp module – Set NTP.

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
> To use it in a playbook, specify: `inspur.sm.edit_ntp`.

New in inspur.sm 0.1.0

- [Synopsis](edit_ntp_module.md#synopsis)
- [Parameters](edit_ntp_module.md#parameters)
- [Examples](edit_ntp_module.md#examples)
- [Return Values](edit_ntp_module.md#return-values)

## [Synopsis](edit_ntp_module.md#id1)

- Set NTP on Inspur server.

## [Parameters](edit_ntp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_date**  string | Date auto synchronize.  Choices:   - `"enable"` - `"disable"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **max_variety**  integer | NTP Maximum jump time(minute),max variety(1-60).  Only the M6 model supports this parameter. |
| **ntp_time**  string | NTP time(YYYYmmddHHMMSS).  Only the M5 model supports this parameter. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **server1**  string | NTP Server1(ipv4 or ipv6 or domain name), set when auto_dateis enable. |
| **server2**  string | NTP Server2(ipv4 or ipv6 or domain name), set when auto_date is enable. |
| **server3**  string | NTP Server3(ipv4 or ipv6 or domain name), set when auto_date is enable. |
| **server4**  string | NTP Server1(ipv4 or ipv6 or domain name), set when auto_dateis enable. |
| **server5**  string | NTP Server2(ipv4 or ipv6 or domain name), set when auto_date is enable. |
| **server6**  string | NTP Server3(ipv4 or ipv6 or domain name), set when auto_date is enable. |
| **syn_cycle**  integer | NTP syn cycle(minute),sync cycle(5-1440). |
| **time_zone**  string | UTC time zone,chose from {-12, -11.5, -11, … ,11,11.5,12}. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_ntp_module.md#id3)

```yaml+jinja
- name: NTP test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set ntp"
    inspur.sm.edit_ntp:
      auto_date: "enable"
      server2: "time.nist.gov"
      provider: "{{ ism }}"

  - name: "Set ntp"
    inspur.sm.edit_ntp:
      auto_date: "disable"
      ntp_time: "20200609083600"
      provider: "{{ ism }}"

  - name: "set ntp"
    inspur.sm.edit_ntp:
      time_zone: 8
      provider: "{{ ism }}"
```

## [Return Values](edit_ntp_module.md#id4)

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
