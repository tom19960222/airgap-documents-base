---
collection: ansible
version: "6"
title: "inspur.sm.edit_pdisk module – Set physical disk."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_pdisk_module.html
fetched_at: 2026-07-27T17:53:18+00:00
---
# inspur.sm.edit_pdisk module – Set physical disk.

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
> To use it in a playbook, specify: `inspur.sm.edit_pdisk`.

New in inspur.sm 0.1.0

- [Synopsis](edit_pdisk_module.md#synopsis)
- [Parameters](edit_pdisk_module.md#parameters)
- [Examples](edit_pdisk_module.md#examples)
- [Return Values](edit_pdisk_module.md#return-values)

## [Synopsis](edit_pdisk_module.md#id1)

- Set physical disk on Inspur server.

## [Parameters](edit_pdisk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Action while set physical drive hotspare.  Required when *Info=None* and *option=HS*.  Only the M5 model supports this parameter.  Choices:   - `"remove"` - `"global"` - `"dedicate"` |
| **ctrl_id**  integer | Raid controller ID.  Required when *Info=None*. |
| **device_id**  integer | physical drive id.  Required when *Info=None*. |
| **duration**  integer | duration range is 1-255,physical drive under PMC raid controller.  Required when *option=LOC*.  Only the M6 model supports this parameter. |
| **encl**  string | IsEnclAffinity while set physical drive hotspare.  Required when *Info=None* and *option=HS* and *action=dedicate*.  Only the M5 model supports this parameter.  Choices:   - `"yes"` - `"no"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **info**  string | Show controller and pdisk info.  Choices:   - `"show"` |
| **logical_drivers**  list / elements=integer | Logical Drivers while set physical drive hotspare, input multiple Logical Drivers index like 0,1,2…..  Required when *Info=None* and *option=HS* and *action=dedicate*.  Only the M5 model supports this parameter. |
| **option**  string | Set operation options fo physical disk,  UG is Unconfigured Good,UB is Unconfigured Bad,  OFF is offline,FAIL is Failed,RBD is Rebuild,  ON is Online,JB is JBOD,ES is Drive Erase stop,  EM is Drive Erase Simple,EN is Drive Erase Normal,  ET is Drive Erase Through,LOC is Locate,STL is Stop Locate,  HS is Hot spare.  Required when *Info=None*.  Only the M5 model supports `HS` Settings.  Choices:   - `"UG"` - `"UB"` - `"OFF"` - `"FAIL"` - `"RBD"` - `"ON"` - `"JB"` - `"ES"` - `"EM"` - `"EN"` - `"ET"` - `"LOC"` - `"STL"` - `"HS"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **revertible**  string | IsRevertible while set physical drive hotspare.  Required when *Info=None* and *option=HS* and *action=dedicate*.  Only the M5 model supports this parameter.  Choices:   - `"yes"` - `"no"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_pdisk_module.md#id3)

```yaml+jinja
- name: Edit pdisk test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Show pdisk information"
    inspur.sm.edit_pdisk:
      info: "show"
      provider: "{{ ism }}"

  - name: "Edit pdisk"
    inspur.sm.edit_pdisk:
      ctrl_id: 0
      device_id: 1
      option: "LOC"
      provider: "{{ ism }}"

  - name: "M5 Edit pdisk"
    inspur.sm.edit_pdisk:
      ctrl_id: 0
      device_id: 1
      option: "HS"
      action: "dedicate"
      revertible: "yes"
      encl: "yes"
      logical_drivers: 1
      provider: "{{ ism }}"
```

## [Return Values](edit_pdisk_module.md#id4)

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
