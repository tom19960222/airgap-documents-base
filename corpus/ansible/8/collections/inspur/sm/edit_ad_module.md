---
collection: ansible
version: "8"
title: "inspur.sm.edit_ad module – Set active directory information."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/edit_ad_module.html
fetched_at: 2026-07-28T02:38:10+00:00
---
# inspur.sm.edit_ad module – Set active directory information.

> **Note:**
>
> This module is part of the [inspur.sm collection](https://galaxy.ansible.com/ui/repo/published/inspur/sm/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.sm`.
>
> To use it in a playbook, specify: `inspur.sm.edit_ad`.

New in inspur.sm 0.1.0

- [Synopsis](edit_ad_module.md#synopsis)
- [Parameters](edit_ad_module.md#parameters)
- [Examples](edit_ad_module.md#examples)
- [Return Values](edit_ad_module.md#return-values)

## [Synopsis](edit_ad_module.md#id1)

- Set active directory information on Inspur server.

## [Parameters](edit_ad_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **addr1**  string | Domain Controller Server Address1. |
| **addr2**  string | Domain Controller Server Address2. |
| **addr3**  string | Domain Controller Server Address3. |
| **code**  string | Secret Password. |
| **domain**  string | User Domain Name. |
| **enable**  string | Active Directory Authentication Status.  **Choices:**   - `"enable"` - `"disable"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **name**  string | Secret Username. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **ssl_enable**  string | Active Directory SSL Status.  **Choices:**   - `"enable"` - `"disable"` |
| **timeout**  integer | The Time Out configuration(15-300). |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_ad_module.md#id3)

```yaml+jinja
- name: Ad test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set active directory information"
    inspur.sm.edit_ad:
      enable: "disable"
      provider: "{{ ism }}"

  - name: "Set active directory information"
    inspur.sm.edit_ad:
      enable: "enable"
      name: "inspur"
      code: "123456"
      timeout: 120
      domain: "inspur.com"
      addr1: "100.2.2.2"
      addr2: "100.2.2.3"
      addr3: "100.2.2.4"
      provider: "{{ ism }}"
```

## [Return Values](edit_ad_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  **Returned:** always |
| **message**  string | Messages returned after module execution.  **Returned:** always |
| **state**  string | Status after module execution.  **Returned:** always |

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

- [Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
- [Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
