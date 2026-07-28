---
collection: ansible
version: "8"
title: "inspur.sm.ad_group module – Manage active directory group information."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/ad_group_module.html
fetched_at: 2026-07-28T02:37:46+00:00
---
# inspur.sm.ad_group module – Manage active directory group information.

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
> To use it in a playbook, specify: `inspur.sm.ad_group`.

New in inspur.sm 1.1.0

- [Synopsis](ad_group_module.md#synopsis)
- [Parameters](ad_group_module.md#parameters)
- [Examples](ad_group_module.md#examples)
- [Return Values](ad_group_module.md#return-values)

## [Synopsis](ad_group_module.md#id1)

- Manage active directory group information on Inspur server.

## [Parameters](ad_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain**  string | Group domain. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **kvm**  string | Kvm privilege.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Group name. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **pri**  string | Group privilege.  **Choices:**   - `"administrator"` - `"user"` - `"operator"` - `"oem"` - `"none"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | Whether the active directory group should exist or not, taking action if the state is different from what is stated.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **vm**  string | Vmedia privilege.  **Choices:**   - `"enable"` - `"disable"` |

## [Examples](ad_group_module.md#id3)

```yaml+jinja
- name: Ad group test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Add active directory group information"
    inspur.sm.ad_group:
      state: "present"
      name: "wbs"
      domain: "inspur.com"
      pri: "administrator"
      kvm: "enable"
      vm: "disable"
      provider: "{{ ism }}"

  - name: "Set active directory group information"
    inspur.sm.ad_group:
      state: "present"
      name: "wbs"
      pri: "user"
      kvm: "disable"
      provider: "{{ ism }}"

  - name: "Delete active directory group information"
    inspur.sm.ad_group:
      state: "absent"
      name: "wbs"
      provider: "{{ ism }}"
```

## [Return Values](ad_group_module.md#id4)

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
