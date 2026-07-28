---
collection: ansible
version: "6"
title: "community.network.ce_startup module – Manages a system startup information on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_startup_module.html
fetched_at: 2026-07-27T17:17:53+00:00
---
# community.network.ce_startup module – Manages a system startup information on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_startup`.

- [Synopsis](ce_startup_module.md#synopsis)
- [Parameters](ce_startup_module.md#parameters)
- [Notes](ce_startup_module.md#notes)
- [Examples](ce_startup_module.md#examples)
- [Return Values](ce_startup_module.md#return-values)

## [Synopsis](ce_startup_module.md#id1)

- Manages a system startup information on HUAWEI CloudEngine switches.

## [Parameters](ce_startup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Display the startup information.  Choices:   - `"display"` |
| **cfg_file**  string | Name of the configuration file that is applied for the next startup. The value is a string of 5 to 255 characters.  Default: `"present"` |
| **patch_file**  string | Name of the patch file that is applied for the next startup. |
| **slot**  string | Position of the device.The value is a string of 1 to 32 characters. The possible value of slot is all, slave-board, or the specific slotID. |
| **software_file**  string | File name of the system software that is applied for the next startup. The value is a string of 5 to 255 characters. |

## [Notes](ce_startup_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_startup_module.md#id4)

```yaml+jinja
- name: Startup module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: Display startup information
    community.network.ce_startup:
      action: display
      provider: "{{ cli }}"

  - name: Set startup patch file
    community.network.ce_startup:
      patch_file: 2.PAT
      slot: all
      provider: "{{ cli }}"

  - name: Set startup software file
    community.network.ce_startup:
      software_file: aa.cc
      slot: 1
      provider: "{{ cli }}"

  - name: Set startup cfg file
    community.network.ce_startup:
      cfg_file: 2.cfg
      slot: 1
      provider: "{{ cli }}"
```

## [Return Values](ce_startup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"StartupInfos": null}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"configSysSoft": "flash:/CE12800-V200R002C20_issuB071.cc", "curentPatchFile": "NULL", "curentStartupFile": "NULL", "curentSysSoft": "flash:/CE12800-V200R002C20_issuB071.cc", "nextPatchFile": "flash:/1.PAT", "nextStartupFile": "flash:/1.cfg", "nextSysSoft": "flash:/CE12800-V200R002C20_issuB071.cc", "position": "5"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"patch_file": "2.PAT", "slot": "all"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `{"startup patch 2.PAT all": null}` |

### Authors

- Li Yanfeng (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
