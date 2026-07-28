---
collection: ansible
version: "6"
title: "community.network.ce_stp module – Manages STP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_stp_module.html
fetched_at: 2026-07-27T17:17:55+00:00
---
# community.network.ce_stp module – Manages STP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_stp`.

- [Synopsis](ce_stp_module.md#synopsis)
- [Parameters](ce_stp_module.md#parameters)
- [Notes](ce_stp_module.md#notes)
- [Examples](ce_stp_module.md#examples)
- [Return Values](ce_stp_module.md#return-values)

## [Synopsis](ce_stp_module.md#id1)

- Manages STP configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_stp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bpdu_filter**  string | Specify a port as a BPDU filter port.  Choices:   - `"enable"` - `"disable"` |
| **bpdu_protection**  string | Configure BPDU protection on an edge port. This function prevents network flapping caused by attack packets.  Choices:   - `"enable"` - `"disable"` |
| **cost**  string | Set the path cost of the current port. The default instance is 0. |
| **edged_port**  string | Set the current port as an edge port.  Choices:   - `"enable"` - `"disable"` |
| **interface**  string | Interface name. If the value is `all`, will apply configuration to all interfaces. if the value is a special name, only support input the full name. |
| **loop_protection**  string | Enable loop protection on the current port.  Choices:   - `"enable"` - `"disable"` |
| **root_protection**  string | Enable root protection on the current port.  Choices:   - `"enable"` - `"disable"` |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **stp_converge**  string | STP convergence mode. Fast means set STP aging mode to Fast. Normal means set STP aging mode to Normal.  Choices:   - `"fast"` - `"normal"` |
| **stp_enable**  string | Enable or disable STP on a switch.  Choices:   - `"enable"` - `"disable"` |
| **stp_mode**  string | Set an operation mode for the current MSTP process. The mode can be STP, RSTP, or MSTP.  Choices:   - `"stp"` - `"rstp"` - `"mstp"` |
| **tc_protection**  string | Configure the TC BPDU protection function for an MSTP process.  Choices:   - `"enable"` - `"disable"` |
| **tc_protection_interval**  string | Set the time the MSTP device takes to handle the maximum number of TC BPDUs and immediately refresh forwarding entries. The value is an integer ranging from 1 to 600, in seconds. |
| **tc_protection_threshold**  string | Set the maximum number of TC BPDUs that the MSTP can handle. The value is an integer ranging from 1 to 255. The default value is 1 on the switch. |

## [Notes](ce_stp_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_stp_module.md#id4)

```yaml+jinja
- name: CloudEngine stp test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:

  - name: "Config stp mode"
    community.network.ce_stp:
      state: present
      stp_mode: stp

  - name: "Undo stp mode"
    community.network.ce_stp:
      state: absent
      stp_mode: stp

  - name: "Enable bpdu protection"
    community.network.ce_stp:
      state: present
      bpdu_protection: enable

  - name: "Disable bpdu protection"
    community.network.ce_stp:
      state: present
      bpdu_protection: disable
```

## [Return Values](ce_stp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"bpdu_protection": "enable"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"bpdu_protection": "disable"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"bpdu_protection": "enable", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["stp bpdu-protection"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
