---
collection: ansible
version: "6"
title: "inspur.sm.download_auto_screenshot module – Download auto screenshots."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/download_auto_screenshot_module.html
fetched_at: 2026-07-27T17:52:58+00:00
---
# inspur.sm.download_auto_screenshot module – Download auto screenshots.

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
> To use it in a playbook, specify: `inspur.sm.download_auto_screenshot`.

New in inspur.sm 0.1.0

- [Synopsis](download_auto_screenshot_module.md#synopsis)
- [Parameters](download_auto_screenshot_module.md#parameters)
- [Examples](download_auto_screenshot_module.md#examples)
- [Return Values](download_auto_screenshot_module.md#return-values)

## [Synopsis](download_auto_screenshot_module.md#id1)

- Download auto screenshots on Inspur server.

## [Parameters](download_auto_screenshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **file_url**  string / required | Screen capture file path. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](download_auto_screenshot_module.md#id3)

```yaml+jinja
- name: Screen test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Download auto screenshots"
    inspur.sm.download_auto_screenshot:
      file_url: "/home/wbs/screen"
      provider: "{{ ism }}"
```

## [Return Values](download_auto_screenshot_module.md#id4)

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
