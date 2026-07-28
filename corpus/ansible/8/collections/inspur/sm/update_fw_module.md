---
collection: ansible
version: "8"
title: "inspur.sm.update_fw module – Update firmware."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/update_fw_module.html
fetched_at: 2026-07-28T02:39:23+00:00
---
# inspur.sm.update_fw module – Update firmware.

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
> To use it in a playbook, specify: `inspur.sm.update_fw`.

New in inspur.sm 0.1.0

- [Synopsis](update_fw_module.md#synopsis)
- [Parameters](update_fw_module.md#parameters)
- [Examples](update_fw_module.md#examples)
- [Return Values](update_fw_module.md#return-values)

## [Synopsis](update_fw_module.md#id1)

- Update firmware on Inspur server.

## [Parameters](update_fw_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dual_image**  string | (M5)update dual image(default) or not.  Only the M5 model supports this parameter.  **Choices:**   - `"single"` - `"dual"` ← (default) |
| **has_me**  integer | (M5-BIOS)update me or not when update bios,only work in INTEL platform,0-no,1-yes.  Only the M5 model supports this parameter.  **Choices:**   - `0` - `1` ← (default) |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **mode**  string | (BMC)active mode, Manual or Auto(default).  **Choices:**   - `"Auto"` ← (default) - `"Manual"` |
| **over_ride**  integer | Reserve Configrations,0-reserve, 1-override.  **Choices:**   - `0` ← (default) - `1` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **type**  string | Firmware type.  **Choices:**   - `"BMC"` - `"BIOS"` |
| **url**  string / required | Firmware image url. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](update_fw_module.md#id3)

```yaml+jinja
- name: Update fw test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "update bios"
    inspur.sm.update_fw:
      url: "/home/wbs/SA5112M5_BIOS_4.1.8_Standard_20200117.bin"
      type: "BIOS"
      provider: "{{ ism }}"

  - name: "update bmc"
    inspur.sm.update_fw:
      url: "/home/wbs/SA5112M5_BMC_4.17.7_Standard_20200430"
      mode: "Auto"
      type: "BMC"
      dual_image: "dual"
      provider: "{{ ism }}"
```

## [Return Values](update_fw_module.md#id4)

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
