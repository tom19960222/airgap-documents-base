---
collection: ansible
version: "6"
title: "community.network.ce_multicast_global module – Manages multicast global configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_multicast_global_module.html
fetched_at: 2026-07-27T17:17:39+00:00
---
# community.network.ce_multicast_global module – Manages multicast global configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_multicast_global`.

New in community.network 0.2.0

- [Synopsis](ce_multicast_global_module.md#synopsis)
- [Parameters](ce_multicast_global_module.md#parameters)
- [Notes](ce_multicast_global_module.md#notes)
- [Examples](ce_multicast_global_module.md#examples)
- [Return Values](ce_multicast_global_module.md#return-values)

## [Synopsis](ce_multicast_global_module.md#id1)

- Manages multicast global on HUAWEI CloudEngine switches.

## [Parameters](ce_multicast_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aftype**  string / required | Destination ip address family type of static route.  Choices:   - `"v4"` - `"v6"` |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | VPN instance of destination ip address. |

## [Notes](ce_multicast_global_module.md#id3)

> **Note:**
>
> - If no vrf is supplied, vrf is set to default.
> - If *state=absent*, the route will be removed, regardless of the non-required parameters.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module works with connection `netconf`.

## [Examples](ce_multicast_global_module.md#id4)

```yaml+jinja
---
  - name: Multicast routing-enable
    community.network.ce_multicast_global:
      aftype: v4
      state: absent
      provider: "{{ cli }}"
  - name: Multicast routing-enable
    community.network.ce_multicast_global:
      aftype: v4
      state: present
      provider: "{{ cli }}"
  - name: Multicast routing-enable
    community.network.ce_multicast_global:
      aftype: v4
      vrf: vrf1
      provider: "{{ cli }}"
```

## [Return Values](ce_multicast_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"addressFamily": "ipv4unicast", "state": "present", "vrfName": "_public_"}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"addressFamily": "ipv4unicast", "state": "present", "vrfName": "_public_"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["multicast routing-enable"]` |

### Authors

- xuxiaowei0512 (@xuxiaowei0512)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
