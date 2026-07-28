---
collection: ansible
version: "6"
title: "community.network.ce_lldp module – Manages LLDP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_lldp_module.html
fetched_at: 2026-07-27T17:17:35+00:00
---
# community.network.ce_lldp module – Manages LLDP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_lldp`.

New in community.network 0.2.0

- [Synopsis](ce_lldp_module.md#synopsis)
- [Parameters](ce_lldp_module.md#parameters)
- [Notes](ce_lldp_module.md#notes)
- [Examples](ce_lldp_module.md#examples)
- [Return Values](ce_lldp_module.md#return-values)

## [Synopsis](ce_lldp_module.md#id1)

- Manages LLDP configuration on HUAWEI CloudEngine switches.

## [Parameters](ce_lldp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bind_name**  string | Binding interface name. |
| **fast_count**  integer | The number of LLDP messages sent to the neighbor nodes by the specified device. |
| **hold_multiplier**  integer | Time multiplier for device information in neighbor devices. |
| **interval**  integer | Frequency at which LLDP advertisements are sent (in seconds). |
| **lldpenable**  string | Set global LLDP enable state.  Choices:   - `"enabled"` - `"disabled"` |
| **management_address**  string | The management IP address of LLDP. |
| **mdn_notification_interval**  integer | Delay time for sending MDN neighbor information change alarm. |
| **mdnstatus**  string | Set global MDN enable state.  Choices:   - `"rxOnly"` - `"disabled"` |
| **notification_interval**  integer | Suppression time for sending LLDP alarm. |
| **restart_delay**  integer | Specifies the delay time of the interface LLDP module from disabled state to re enable. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **transmit_delay**  integer | Delay time for sending LLDP messages. |

## [Notes](ce_lldp_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_lldp_module.md#id4)

```yaml+jinja
- name: "Configure global LLDP enable state"
  community.network.ce_lldp:
    lldpenable: enabled

- name: "Configure global MDN enable state"
  community.network.ce_lldp:
    mdnstatus: rxOnly

- name: "Configure LLDP transmit interval and ensure global LLDP state is already enabled"
  community.network.ce_lldp:
    enable: enable
    interval: 32

- name: "Configure LLDP transmit multiplier hold and ensure global LLDP state is already enabled"
  community.network.ce_lldp:
    enable: enable
    hold_multiplier: 5

- name: "Configure the delay time of the interface LLDP module from disabled state to re enable"
  community.network.ce_lldp:
    enable: enable
    restart_delay: 3

- name: "Reset the delay time for sending LLDP messages"
  community.network.ce_lldp:
    enable: enable
    transmit_delay: 4

- name: "Configure device to send neighbor device information change alarm delay time"
  community.network.ce_lldp:
    lldpenable: enabled
    notification_interval: 6

- name: "Configure the number of LLDP messages sent to the neighbor nodes by the specified device"
  community.network.ce_lldp:
    enable: enable
    fast_count: 5

- name: "Configure the delay time for sending MDN neighbor information change alarm"
  community.network.ce_lldp:
    enable: enable
    mdn_notification_interval: 6
- name: "Configuring the management IP address of LLDP"
  community.network.ce_lldp:
    enable: enable
    management_address: 10.1.0.1

- name: "Configuring LLDP to manage the binding relationship between IP addresses and interfaces"
  community.network.ce_lldp:
    enable: enable
    bind_name: LoopBack2
```

## [Return Values](ce_lldp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of global LLDP configuration after module execution.  Returned: always  Sample: `{"bind_name": "LoopBack2", "fast_count": "5", "hold_multiplier": "5", "interval": "32", "lldpenable": "enabled", "management_address": "10.1.0.1", "mdn_notification_interval": "6", "mdnstatus": "rxOnly", "notification_interval": "6", "restart_delay": "3", "transmit_delay": "4"}` |
| **existing**  dictionary | k/v pairs of existing global LLDP configuration.  Returned: always  Sample: `{"lldpenable": "disabled", "mdnstatus": "disabled"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"bind_name": "LoopBack2", "fast_count": "5", "hold_multiplier": "5", "interval": "32", "lldpenable": "enabled", "management_address": "10.1.0.1", "mdn_notification_interval": "6", "mdnstatus": "rxOnly", "notification_interval": "6", "restart_delay": "3", "state": "present", "transmit_delay": "4"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["lldp enable", "lldp mdn enable", "lldp transmit interval 32", "lldp transmit multiplier 5", "lldp restart 3", "lldp transmit delay 4", "lldp trap-interval 6", "lldp fast-count 5", "lldp mdn trap-interval 6", "lldp management-address 10.1.0.1", "lldp management-address bind interface LoopBack 2"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
