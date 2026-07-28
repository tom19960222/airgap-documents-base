---
collection: ansible
version: "6"
title: "community.network.ce_vrrp module – Manages VRRP interfaces on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vrrp_module.html
fetched_at: 2026-07-27T17:17:58+00:00
---
# community.network.ce_vrrp module – Manages VRRP interfaces on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_vrrp`.

- [Synopsis](ce_vrrp_module.md#synopsis)
- [Parameters](ce_vrrp_module.md#parameters)
- [Notes](ce_vrrp_module.md#notes)
- [Examples](ce_vrrp_module.md#examples)
- [Return Values](ce_vrrp_module.md#return-values)

## [Synopsis](ce_vrrp_module.md#id1)

- Manages VRRP interface attributes on HUAWEI CloudEngine devices.

## [Parameters](ce_vrrp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_flowdown**  boolean | Disable the flowdown function for service VRRP.  Choices:   - `false` ← (default) - `true` |
| **admin_ignore_if_down**  boolean | mVRRP ignores an interface Down event.  Choices:   - `false` ← (default) - `true` |
| **admin_interface**  string | Tracked mVRRP interface name. The value is a string of 1 to 63 characters. |
| **admin_vrid**  string | Tracked mVRRP ID. The value is an integer ranging from 1 to 255. |
| **advertise_interval**  string | Configured interval between sending advertisements, in milliseconds. Only the master router sends VRRP advertisements. The default value is 1000 milliseconds. |
| **auth_key**  string | This object is set based on the authentication type. When noAuthentication is specified, the value is empty. When simpleTextPassword or md5Authentication is specified, the value is a string of 1 to 8 characters in plaintext and displayed as a blank text for security. |
| **auth_mode**  string | Authentication type used for VRRP packet exchanges between virtual routers. The values are noAuthentication, simpleTextPassword, md5Authentication. The default value is noAuthentication.  Choices:   - `"simple"` - `"md5"` - `"none"` |
| **fast_resume**  string | mVRRP’s fast resume mode.  Choices:   - `"enable"` - `"disable"` |
| **gratuitous_arp_interval**  string | Interval at which gratuitous ARP packets are sent, in seconds. The value ranges from 30 to 1200.The default value is 300. |
| **holding_multiplier**  string | The configured holdMultiplier.The value is an integer ranging from 3 to 10. The default value is 3. |
| **interface**  string | Name of an interface. The value is a string of 1 to 63 characters. |
| **is_plain**  boolean | Select the display mode of an authentication key. By default, an authentication key is displayed in ciphertext.  Choices:   - `false` ← (default) - `true` |
| **preempt_timer_delay**  string | Preemption delay. The value is an integer ranging from 0 to 3600. The default value is 0. |
| **priority**  string | Configured VRRP priority. The value ranges from 1 to 254. The default value is 100. A larger value indicates a higher priority. |
| **recover_delay**  string | Delay in recovering after an interface goes Up. The delay is used for interface flapping suppression. The value is an integer ranging from 0 to 3600. The default value is 0 seconds. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **version**  string | VRRP version. The default version is v2.  Choices:   - `"v2"` - `"v3"` |
| **virtual_ip**  string | Virtual IP address. The value is a string of 0 to 255 characters. |
| **vrid**  string | VRRP backup group ID. The value is an integer ranging from 1 to 255.  Default: `"present"` |
| **vrrp_type**  string | Type of a VRRP backup group.  Choices:   - `"normal"` - `"member"` - `"admin"` |

## [Notes](ce_vrrp_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vrrp_module.md#id4)

```yaml+jinja
- name: Vrrp module test
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
  - name: Set vrrp version
    community.network.ce_vrrp:
      version: v3
      provider: "{{ cli }}"
  - name: Set vrrp gratuitous-arp interval
    community.network.ce_vrrp:
      gratuitous_arp_interval: 40
      mlag_id: 4
      provider: "{{ cli }}"
  - name: Set vrrp recover-delay
    community.network.ce_vrrp:
      recover_delay: 10
      provider: "{{ cli }}"
  - name: Set vrrp vrid virtual-ip
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      virtual_ip: 10.14.2.7
      provider: "{{ cli }}"
  - name: Set vrrp vrid admin
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      vrrp_type: admin
      provider: "{{ cli }}"
  - name: Set vrrp vrid fast_resume
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      fast_resume: enable
      provider: "{{ cli }}"
  - name: Set vrrp vrid holding-multiplier
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      holding_multiplier: 4
      provider: "{{ cli }}"
  - name: Set vrrp vrid preempt timer delay
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      preempt_timer_delay: 10
      provider: "{{ cli }}"
  - name: Set vrrp vrid admin-vrrp
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      admin_interface: 40GE2/0/9
      admin_vrid: 2
      vrrp_type: member
      provider: "{{ cli }}"
  - name: Set vrrp vrid authentication-mode
    community.network.ce_vrrp:
      interface: 40GE2/0/8
      vrid: 1
      is_plain: true
      auth_mode: simple
      auth_key: aaa
      provider: "{{ cli }}"
```

## [Return Values](ce_vrrp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"auth_mode": "simple", "interface": "40GE2/0/8", "is_plain": "true", "vrid": "1", "vrrp_type": "normal"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"auth_mode": "none", "interface": "40GE2/0/8", "is_plain": "false", "vrid": "1", "vrrp_type": "normal"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"auth_key": "aaa", "auth_mode": "simple", "interface": "40GE2/0/8", "is_plain": true, "state": "present", "vrid": "1"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `{"interface 40GE2/0/8": null, "vrrp vrid 1 authentication-mode simple plain aaa": null}` |

### Authors

- Li Yanfeng (@numone213)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
