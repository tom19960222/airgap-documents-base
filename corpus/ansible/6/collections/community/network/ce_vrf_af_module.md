---
collection: ansible
version: "6"
title: "community.network.ce_vrf_af module – Manages VPN instance address family on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vrf_af_module.html
fetched_at: 2026-07-27T17:17:57+00:00
---
# community.network.ce_vrf_af module – Manages VPN instance address family on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_vrf_af`.

- [Synopsis](ce_vrf_af_module.md#synopsis)
- [Parameters](ce_vrf_af_module.md#parameters)
- [Notes](ce_vrf_af_module.md#notes)
- [Examples](ce_vrf_af_module.md#examples)
- [Return Values](ce_vrf_af_module.md#return-values)

## [Synopsis](ce_vrf_af_module.md#id1)

- Manages VPN instance address family of HUAWEI CloudEngine switches.

## [Parameters](ce_vrf_af_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **evpn**  boolean | Is extend vpn or normal vpn.  Choices:   - `false` ← (default) - `true` |
| **route_distinguisher**  string | VPN instance route distinguisher,the RD used to distinguish same route prefix from different vpn. The RD must be setted before setting vpn_target_value. |
| **state**  string | Manage the state of the af.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vpn_target_state**  string | Manage the state of the vpn target.  Choices:   - `"present"` - `"absent"` |
| **vpn_target_type**  string | VPN instance vpn target type.  Choices:   - `"export_extcommunity"` - `"import_extcommunity"` |
| **vpn_target_value**  string | VPN instance target value. Such as X.X.X.X:number<0-65535> or number<0-65535>:number<0-4294967295> or number<0-65535>.number<0-65535>:number<0-65535> or number<65536-4294967295>:number<0-65535> but not support 0:0 and 0.0:0. |
| **vrf**  string / required | VPN instance. |
| **vrf_aftype**  string | VPN instance address family.  Choices:   - `"v4"` ← (default) - `"v6"` |

## [Notes](ce_vrf_af_module.md#id3)

> **Note:**
>
> - If *state=absent*, the vrf will be removed, regardless of the non-required parameters.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vrf_af_module.md#id4)

```yaml+jinja
- name: Vrf af module test
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

  - name: Config vpna, set address family is ipv4
    community.network.ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      state: present
      provider: "{{ cli }}"
  - name: Config vpna, delete address family is ipv4
    community.network.ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      state: absent
      provider: "{{ cli }}"
  - name: Config vpna, set address family is ipv4,rd=1:1,set vpn_target_type=export_extcommunity,vpn_target_value=2:2
    community.network.ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      route_distinguisher: 1:1
      vpn_target_type: export_extcommunity
      vpn_target_value: 2:2
      vpn_target_state: present
      state: present
      provider: "{{ cli }}"
  - name: Config vpna, set address family is ipv4,rd=1:1,delete vpn_target_type=export_extcommunity,vpn_target_value=2:2
    community.network.ce_vrf_af:
      vrf: vpna
      vrf_aftype: v4
      route_distinguisher: 1:1
      vpn_target_type: export_extcommunity
      vpn_target_value: 2:2
      vpn_target_state: absent
      state: present
      provider: "{{ cli }}"
```

## [Return Values](ce_vrf_af_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"route_distinguisher": ["1:1", "2:2"], "vpn_target_type": ["import_extcommunity", "3:3"], "vpn_target_value": [], "vrf": "vpna", "vrf_aftype": ["ipv4uni", "ipv6uni"]}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{"route_distinguisher": ["1:1", "2:2"], "vpn_target_type": [], "vpn_target_value": [], "vrf": "vpna", "vrf_aftype": ["ipv4uni", "ipv6uni"]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"evpn": "none", "state": "present", "vpn_targe_state": "absent", "vpn_target_type": "none", "vpn_target_value": "none", "vrf": "vpna", "vrf_aftype": "v4"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["ip vpn-instance vpna", "vpn-target 3:3 import_extcommunity"]` |

### Authors

- Yang yang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
