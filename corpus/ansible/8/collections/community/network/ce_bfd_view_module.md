---
collection: ansible
version: "8"
title: "community.network.ce_bfd_view module – Manages BFD session view configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_bfd_view_module.html
fetched_at: 2026-07-28T01:55:15+00:00
---
# community.network.ce_bfd_view module – Manages BFD session view configuration on HUAWEI CloudEngine devices.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_bfd_view`.

- [Synopsis](ce_bfd_view_module.md#synopsis)
- [Parameters](ce_bfd_view_module.md#parameters)
- [Notes](ce_bfd_view_module.md#notes)
- [Examples](ce_bfd_view_module.md#examples)
- [Return Values](ce_bfd_view_module.md#return-values)

## [Synopsis](ce_bfd_view_module.md#id1)

- Manages BFD session view configuration on HUAWEI CloudEngine devices.

Aliases: network.cloudengine.ce_bfd_view

## [Parameters](ce_bfd_view_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_down**  boolean | Enables the BFD session to enter the AdminDown state. By default, a BFD session is enabled. The default value is bool type.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Specifies the description of a BFD session. The value is a string of 1 to 51 case-sensitive characters with spaces. |
| **detect_multi**  string | Specifies the local detection multiplier of a BFD session. The value is an integer that ranges from 3 to 50. |
| **local_discr**  string | Specifies the local discriminator of a BFD session. The value is an integer that ranges from 1 to 16384. |
| **min_rx_interval**  string | Specifies the minimum interval for sending BFD packets. The value is an integer that ranges from 50 to 1000, in milliseconds. |
| **min_tx_interval**  string | Specifies the minimum interval for receiving BFD packets. The value is an integer that ranges from 50 to 1000, in milliseconds. |
| **remote_discr**  string | Specifies the remote discriminator of a BFD session. The value is an integer that ranges from 1 to 4294967295. |
| **session_name**  string / required | Specifies the name of a BFD session. The value is a string of 1 to 15 case-sensitive characters without spaces. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tos_exp**  string | Specifies a priority for BFD control packets. The value is an integer ranging from 0 to 7. The default value is 7, which is the highest priority. |
| **wtr_interval**  string | Specifies the WTR time of a BFD session. The value is an integer that ranges from 1 to 60, in minutes. The default value is 0. |

## [Notes](ce_bfd_view_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bfd_view_module.md#id4)

```yaml+jinja
- name: Bfd view module test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:
  - name: Set the local discriminator of a BFD session to 80 and the remote discriminator to 800
    community.network.ce_bfd_view:
      session_name: atob
      local_discr: 80
      remote_discr: 800
      state: present

  - name: Set the minimum interval for receiving BFD packets to 500 ms
    community.network.ce_bfd_view:
      session_name: atob
      min_rx_interval: 500
      state: present
```

## [Return Values](ce_bfd_view_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** always  **Sample:** `{"session": {"adminDown": "false", "createType": "SESS_STATIC", "description": null, "detectMulti": "3", "localDiscr": "80", "minRxInt": null, "minTxInt": null, "remoteDiscr": "800", "sessName": "atob", "tosExp": null, "wtrTimerInt": null}}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** always  **Sample:** `{"session": {"adminDown": "false", "createType": "SESS_STATIC", "description": null, "detectMulti": "3", "localDiscr": null, "minRxInt": null, "minTxInt": null, "remoteDiscr": null, "sessName": "atob", "tosExp": null, "wtrTimerInt": null}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"admin_down": false, "description": null, "detect_multi": null, "local_discr": 80, "min_rx_interval": null, "min_tx_interval": null, "remote_discr": 800, "session_name": "atob", "state": "present", "tos_exp": null, "wtr_interval": null}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bfd atob", "discriminator local 80", "discriminator remote 800"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
