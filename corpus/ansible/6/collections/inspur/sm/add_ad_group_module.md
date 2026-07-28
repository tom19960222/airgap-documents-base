---
collection: ansible
version: "6"
title: "inspur.sm.add_ad_group module – Add active directory group information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/add_ad_group_module.html
fetched_at: 2026-07-27T17:52:39+00:00
---
# inspur.sm.add_ad_group module – Add active directory group information.

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
> To use it in a playbook, specify: `inspur.sm.add_ad_group`.

New in inspur.sm 0.1.0

- [DEPRECATED](add_ad_group_module.md#deprecated)
- [Synopsis](add_ad_group_module.md#synopsis)
- [Parameters](add_ad_group_module.md#parameters)
- [Examples](add_ad_group_module.md#examples)
- [Return Values](add_ad_group_module.md#return-values)
- [Status](add_ad_group_module.md#status)

## [DEPRECATED](add_ad_group_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Merge functions into the [inspur.sm.ad_group](ad_group_module.md#ansible-collections-inspur-sm-ad-group-module) module.

Alternative:
:   Use [inspur.sm.ad_group](ad_group_module.md#ansible-collections-inspur-sm-ad-group-module) instead.

## [Synopsis](add_ad_group_module.md#id2)

- Add active directory group information on Inspur server.

## [Parameters](add_ad_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain**  string / required | Group domain. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **kvm**  string / required | Kvm privilege.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Group name. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **pri**  string / required | Group privilege.  Choices:   - `"administrator"` - `"user"` - `"operator"` - `"oem"` - `"none"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **vm**  string / required | Vmedia privilege.  Choices:   - `"enable"` - `"disable"` |

## [Examples](add_ad_group_module.md#id4)

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
    inspur.sm.add_ad_group:
      name: "wbs"
      domain: "inspur.com"
      pri: "administrator"
      kvm: "enable"
      vm: "disable"
      provider: "{{ ism }}"
```

## [Return Values](add_ad_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

## [Status](add_ad_group_module.md#id6)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](add_ad_group_module.md#deprecated).

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

[Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
[Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
