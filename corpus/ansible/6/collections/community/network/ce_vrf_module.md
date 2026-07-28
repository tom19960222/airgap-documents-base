---
collection: ansible
version: "6"
title: "community.network.ce_vrf module – Manages VPN instance on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vrf_module.html
fetched_at: 2026-07-27T17:17:56+00:00
---
# community.network.ce_vrf module – Manages VPN instance on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_vrf`.

- [Synopsis](ce_vrf_module.md#synopsis)
- [Parameters](ce_vrf_module.md#parameters)
- [Notes](ce_vrf_module.md#notes)
- [Examples](ce_vrf_module.md#examples)
- [Return Values](ce_vrf_module.md#return-values)

## [Synopsis](ce_vrf_module.md#id1)

- Manages VPN instance of HUAWEI CloudEngine switches.

## [Parameters](ce_vrf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the vrf, the string length is 1 - 242 . |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vrf**  string / required | VPN instance, the length of vrf name is 1 - 31, i.e. “test”, but can not be `_public_`. |

## [Notes](ce_vrf_module.md#id3)

> **Note:**
>
> - If *state=absent*, the route will be removed, regardless of the non-required options.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vrf_module.md#id4)

```yaml+jinja
- name: Vrf module test
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

  - name: Config a vpn install named vpna, description is test
    community.network.ce_vrf:
      vrf: vpna
      description: test
      state: present
      provider: "{{ cli }}"
  - name: Delete a vpn install named vpna
    community.network.ce_vrf:
      vrf: vpna
      state: absent
      provider: "{{ cli }}"
```

## [Return Values](ce_vrf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"description": "test", "present": "present", "vrf": "vpna"}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"description": "test", "state": "present", "vrf": "vpna"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["ip vpn-instance vpna", "description test"]` |

### Authors

- Yang yang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
