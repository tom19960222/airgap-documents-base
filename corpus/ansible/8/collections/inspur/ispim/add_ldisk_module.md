---
collection: ansible
version: "8"
title: "inspur.ispim.add_ldisk module – Create logical disk"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/add_ldisk_module.html
fetched_at: 2026-07-28T02:36:14+00:00
---
# inspur.ispim.add_ldisk module – Create logical disk

> **Note:**
>
> This module is part of the [inspur.ispim collection](https://galaxy.ansible.com/ui/repo/published/inspur/ispim/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.ispim`.
> You need further requirements to be able to use this module,
> see [Requirements](add_ldisk_module.md#ansible-collections-inspur-ispim-add-ldisk-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.add_ldisk`.

New in inspur.ispim 1.0.0

- [Synopsis](add_ldisk_module.md#synopsis)
- [Requirements](add_ldisk_module.md#requirements)
- [Parameters](add_ldisk_module.md#parameters)
- [Notes](add_ldisk_module.md#notes)
- [Examples](add_ldisk_module.md#examples)
- [Return Values](add_ldisk_module.md#return-values)

## [Synopsis](add_ldisk_module.md#id1)

- Create logical disk on Inspur server.

## [Requirements](add_ldisk_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](add_ldisk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accelerator**  integer | Driver accelerator, 1 - 1h, 2 - 2h, 3 - 3h.  Required when *Info=None* and controller type is PMC.  **Choices:**   - `1` - `2` - `3` |
| **access**  integer | Access Policy, 1 - Read Write, 2 - Read Only, 3 - Blocked.  Required when *Info=None* and controller type is LSI.  **Choices:**   - `1` - `2` - `3` |
| **cache**  integer | Drive Cache, 1 - Unchanged, 2 - Enabled,3 - Disabled.  Required when *Info=None* and controller type is LSI.  **Choices:**   - `1` - `2` - `3` |
| **ctrl_id**  integer | Raid controller ID.  Required when *Info=None* and controller type is LSI or PMC. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **info**  string | Show controller and physical drive info.  **Choices:**   - `"show"` |
| **init**  integer | Init State, 1 - No Init, 2 - Quick Init, 3 - Full Init.  Required when *Info=None* and controller type is LSI.  **Choices:**   - `1` - `2` - `3` |
| **io**  integer | IO Policy, 1 - Direct IO, 2 - Cached IO.  Required when *Info=None* and controller type is LSI.  **Choices:**   - `1` - `2` |
| **level**  integer | RAID Level, 0 - RAID0, 1 - RAID1, 5 - RAID5, 6 - RAID6, 10 - RAID10.  Required when *Info=None* and controller type is LSI or PMC.  **Choices:**   - `0` - `1` - `5` - `6` - `10` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **r**  integer | Read Policy, 1 - Read Ahead, 2 - No Read Ahead.  Required when *Info=None* and controller type is LSI.  **Choices:**   - `1` - `2` |
| **select**  integer | Select Size, from 1 to 100.  Required when *Info=None* and controller type is LSI. |
| **size**  integer | Strip Size, 1 - 64k, 2 - 128k, 3 - 256k, 4 - 512k, 5 - 1024k.  Required when *Info=None* and controller type is LSI or PMC.  **Choices:**   - `1` - `2` - `3` - `4` - `5` |
| **slot**  list / elements=integer | Slot Num,input multiple slotNumber like 0,1,2….  Required when *Info=None* and controller type is LSI or PMC. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **vname**  string | Virtual drive name.  Required when *Info=None* and controller type is PMC or server model is M7. |
| **w**  integer | Write Policy, 1 - Write Throgh, 2 - Write Back, 3 - Write caching ok if bad BBU.  Required when *Info=None* and controller type is LSI.  **Choices:**   - `1` - `2` - `3` |

## [Notes](add_ldisk_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](add_ldisk_module.md#id5)

```yaml+jinja
- name: Add ldisk test
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
    inspur.ispim.add_ldisk:
      info: "show"
      provider: "{{ ism }}"

  - name: "Add ldisk"
    inspur.ispim.add_ldisk:
      ctrl_id: 0
      level: 1
      size: 1
      access: 1
      r: 1
      w: 1
      io: 1
      cache: 1
      init: 2
      select: 10
      slot: 0,1
      provider: "{{ ism }}"

  - name: "Add PMC  ldisk"
    inspur.ispim.add_ldisk:
      ctrl_id: 0
      level: 1
      size: 1
      accelerator: 1
      slot: 0,1
      vname: "test"
      provider: "{{ ism }}"
```

## [Return Values](add_ldisk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  **Returned:** always |
| **message**  string | Messages returned after module execution.  **Returned:** always |
| **state**  string | Status after module execution.  **Returned:** always |

### Authors

- WangBaoshan (@ispim)

### Collection links

- [Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
- [Repository (Sources)](https://github.com/ispim/inspur.ispim)
