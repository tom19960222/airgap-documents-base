---
collection: ansible
version: "6"
title: "inspur.ispim.edit_kvm module – Set KVM"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/edit_kvm_module.html
fetched_at: 2026-07-27T17:51:36+00:00
---
# inspur.ispim.edit_kvm module – Set KVM

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
> see [Requirements](edit_kvm_module.md#ansible-collections-inspur-ispim-edit-kvm-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_kvm`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_kvm_module.md#synopsis)
- [Requirements](edit_kvm_module.md#requirements)
- [Parameters](edit_kvm_module.md#parameters)
- [Notes](edit_kvm_module.md#notes)
- [Examples](edit_kvm_module.md#examples)
- [Return Values](edit_kvm_module.md#return-values)

## [Synopsis](edit_kvm_module.md#id1)

- Set KVM on Inspur server.

## [Requirements](edit_kvm_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_kvm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **automatic_off**  string | Automatically OFF Server Monitor, When KVM Launches.  Choices:   - `"enable"` - `"disable"` |
| **client_type**  string | Client Type.  Only the M6 model supports this parameter.  Choices:   - `"vnc"` - `"viewer"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **keyboard_language**  string | Select the Keyboard Language.  AD is Auto Detect, DA is Danish, NL-BE is Dutch Belgium, NL-NL is Dutch Netherland,  GB is English UK ,US is English US, FI is Finnish, FR-BE is French Belgium, FR is French France,  DE is German Germany, DE-CH is German Switzerland, IT is Italian, JP is Japanese,  NO is Norwegian, PT is Portuguese, ES is Spanish, SV is Swedish, TR_F is Turkish F, TR_Q is Turkish Q.  Choices:   - `"AD"` - `"DA"` - `"NL-BE"` - `"NL-NL"` - `"GB"` - `"US"` - `"FI"` - `"FR-BE"` - `"FR"` - `"DE"` - `"DE-CH"` - `"IT"` - `"JP"` - `"ON"` - `"PT"` - `"EC"` - `"SV"` - `"TR_F"` - `"TR_Q"` |
| **kvm_encryption**  string | Encrypt KVM packets.  Choices:   - `"enable"` - `"disable"` |
| **local_monitor_off**  string | Server Monitor OFF Feature Status.  Choices:   - `"enable"` - `"disable"` |
| **media_attach**  string | Two types of VM attach mode are available.  Attach is Immediately attaches Virtual Media to the server upon bootup.  Auto is Attaches Virtual Media to the server only when a virtual media session is started.  Choices:   - `"attach"` - `"auto"` |
| **non_secure**  string | Enable/disable Non Secure Connection Type.  Only the M6 model supports this parameter.  Required when *client_type=vnc*.  Choices:   - `"enable"` - `"disable"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **retry_count**  integer | Number of times to be retried in case a KVM failure occurs.Retry count ranges from 1 to 20. |
| **retry_time_interval**  integer | The Identification for retry time interval configuration (5-30) seconds. |
| **ssh_vnc**  string | Enable/disable VNC over SSH in BMC.  Only the M6 model supports this parameter.  Required when *client_type=vnc*.  Choices:   - `"enable"` - `"disable"` |
| **stunnel_vnc**  string | Enable/disable VNC over Stunnel in BMC.  Only the M6 model supports this parameter.  Required when *client_type=vnc*.  Choices:   - `"enable"` - `"disable"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_kvm_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_kvm_module.md#id5)

```yaml+jinja
- name: KVM test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set KVM"
    inspur.ispim.edit_kvm:
      kvm_encryption: "enable"
      media_attach: "auto"
      keyboard_language: "AD"
      retry_count: 13
      retry_time_interval: 10
      local_monitor_off: "enable"
      automatic_off: "enable"
      provider: "{{ ism }}"
```

## [Return Values](edit_kvm_module.md#id6)

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
