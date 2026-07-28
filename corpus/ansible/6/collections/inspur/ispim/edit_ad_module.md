---
collection: ansible
version: "6"
title: "inspur.ispim.edit_ad module – Set active directory information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/edit_ad_module.html
fetched_at: 2026-07-27T17:51:27+00:00
---
# inspur.ispim.edit_ad module – Set active directory information

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
> see [Requirements](edit_ad_module.md#ansible-collections-inspur-ispim-edit-ad-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_ad`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_ad_module.md#synopsis)
- [Requirements](edit_ad_module.md#requirements)
- [Parameters](edit_ad_module.md#parameters)
- [Notes](edit_ad_module.md#notes)
- [Examples](edit_ad_module.md#examples)
- [Return Values](edit_ad_module.md#return-values)

## [Synopsis](edit_ad_module.md#id1)

- Set active directory information on Inspur server.

## [Requirements](edit_ad_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_ad_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **addr1**  string | Domain Controller Server Address1. |
| **addr2**  string | Domain Controller Server Address2. |
| **addr3**  string | Domain Controller Server Address3. |
| **code**  string | Secret Password. |
| **domain**  string | User Domain Name. |
| **enable**  string | Active Directory Authentication Status.  Choices:   - `"enable"` - `"disable"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **name**  string | Secret Username. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **ssl_enable**  string | Active Directory SSL Status.  Choices:   - `"enable"` - `"disable"` |
| **timeout**  integer | The Time Out configuration(15-300).  Only the M5 model supports this parameter. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_ad_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_ad_module.md#id5)

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
    inspur.ispim.edit_ad:
      enable: "disable"
      provider: "{{ ism }}"

  - name: "Set active directory information"
    inspur.ispim.edit_ad:
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

## [Return Values](edit_ad_module.md#id6)

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
