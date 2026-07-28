---
collection: ansible
version: "6"
title: "inspur.sm.edit_power_budget module – Set power budget information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_power_budget_module.html
fetched_at: 2026-07-27T17:53:19+00:00
---
# inspur.sm.edit_power_budget module – Set power budget information.

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
> To use it in a playbook, specify: `inspur.sm.edit_power_budget`.

New in inspur.sm 0.1.0

- [Synopsis](edit_power_budget_module.md#synopsis)
- [Parameters](edit_power_budget_module.md#parameters)
- [Examples](edit_power_budget_module.md#examples)
- [Return Values](edit_power_budget_module.md#return-values)

## [Synopsis](edit_power_budget_module.md#id1)

- Set power budget information on Inspur server.

## [Parameters](edit_power_budget_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Type to action.  Required when *range=False*.  Choices:   - `"add"` - `"delete"` - `"open"` - `"close"` |
| **domain**  string | Domain id.  Required when *range=False*.  Choices:   - `"system"` - `"cpu"` |
| **end1**  integer | Pause period of add, end time,must be greater than start time,from 0 to 24. |
| **end2**  integer | Pause period of add, end time,must be greater than start time,from 0 to 24. |
| **end3**  integer | Pause period of add, end time,must be greater than start time,from 0 to 24. |
| **end4**  integer | Pause period of add, end time,must be greater than start time,from 0 to 24. |
| **end5**  integer | Pause period of add, end time,must be greater than start time,from 0 to 24. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **id**  integer | Policy id.  Required when *range=False*.  Choices:   - `1` - `2` - `3` - `4` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **range**  boolean | Range of power budget watts.  Choices:   - `false` ← (default) - `true` |
| **start1**  integer | Pause period of add, start time, from 0 to 24. |
| **start2**  integer | Pause period of add, start time, from 0 to 24. |
| **start3**  integer | Pause period of add, start time, from 0 to 24. |
| **start4**  integer | Pause period of add, start time, from 0 to 24. |
| **start5**  integer | Period of add, start time, from 0 to 24. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **watts**  integer | Power budget watts of add.  Required when *action=add*. |
| **week1**  list / elements=string | Pause period of add,repetition period,the input parameters are ‘Mon’,’Tue’,’Wed’,’Thur’,’Fri’,’Sat’,’Sun’,separated by commas,such as Mon,Wed,Fri. |
| **week2**  list / elements=string | Pause period of add,repetition period,the input parameters are ‘Mon’,’Tue’,’Wed’,’Thur’,’Fri’,’Sat’,’Sun’,separated by commas,such as Mon,Wed,Fri. |
| **week3**  list / elements=string | Pause period of add,repetition period,the input parameters are ‘Mon’,’Tue’,’Wed’,’Thur’,’Fri’,’Sat’,’Sun’,separated by commas,such as Mon,Wed,Fri. |
| **week4**  list / elements=string | Pause period of add,repetition period,the input parameters are ‘Mon’,’Tue’,’Wed’,’Thur’,’Fri’,’Sat’,’Sun’,separated by commas,such as Mon,Wed,Fri. |
| **week5**  list / elements=string | Pause period of add,repetition period,the input parameters are ‘Mon’,’Tue’,’Wed’,’Thur’,’Fri’,’Sat’,’Sun’,separated by commas,such as Mon,Wed,Fri. |

## [Examples](edit_power_budget_module.md#id3)

```yaml+jinja
- name: Power budget test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get power budget range"
    inspur.sm.edit_power_budget:
      range: True
      provider: "{{ ism }}"

  - name: "add power budget"
    inspur.sm.edit_power_budget:
      action: "add"
      id: 1
      watts: 1500
      start1: 2
      end1: 5
      week1:
        - Mon
        - Wed
        - Fri
      provider: "{{ ism }}"

  - name: "Set power budget status to open"
    inspur.sm.edit_power_budget:
      action: "open"
      id: 1
      provider: "{{ ism }}"

  - name: "Set power budget status to close"
    inspur.sm.edit_power_budget:
      action: "close"
      id: 1
      provider: "{{ ism }}"

  - name: "Delete power budget"
    inspur.sm.edit_power_budget:
      action: "delete"
      id: 1
      provider: "{{ ism }}"
```

## [Return Values](edit_power_budget_module.md#id4)

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
