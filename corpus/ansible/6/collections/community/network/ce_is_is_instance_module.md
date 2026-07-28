---
collection: ansible
version: "6"
title: "community.network.ce_is_is_instance module – Manages isis process id configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_is_is_instance_module.html
fetched_at: 2026-07-27T17:17:32+00:00
---
# community.network.ce_is_is_instance module – Manages isis process id configuration on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_is_is_instance`.

New in community.network 0.2.0

- [Synopsis](ce_is_is_instance_module.md#synopsis)
- [Parameters](ce_is_is_instance_module.md#parameters)
- [Notes](ce_is_is_instance_module.md#notes)
- [Examples](ce_is_is_instance_module.md#examples)
- [Return Values](ce_is_is_instance_module.md#return-values)

## [Synopsis](ce_is_is_instance_module.md#id1)

- Manages isis process id, creates a isis instance id or deletes a process id on HUAWEI CloudEngine devices.

## [Parameters](ce_is_is_instance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **instance_id**  integer / required | Specifies the id of a isis process.The value is a number of 1 to 4294967295. |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vpn_name**  string | VPN Instance, associate the VPN instance with the corresponding IS-IS process. |

## [Notes](ce_is_is_instance_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module works with connection `netconf`.

## [Examples](ce_is_is_instance_module.md#id4)

```yaml+jinja
- name: Set isis process
  community.network.ce_is_is_instance:
    instance_id: 3
    state: present

- name: Unset isis process
  community.network.ce_is_is_instance:
    instance_id: 3
    state: absent

- name: Check isis process
  community.network.ce_is_is_instance:
    instance_id: 4294967296
    state: present

- name: Set vpn name
  community.network.ce_is_is_instance:
    instance_id: 22
    vpn_name: vpn1
    state: present

- name: Check vpn name
  community.network.ce_is_is_instance:
    instance_id: 22
    vpn_name: vpn1234567896321452212221556asdasdasdasdsadvdv
    state: present
```

## [Return Values](ce_is_is_instance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: always  Sample: `{"session": {"instance_id": 1, "vpn_name": null}}` |
| **existing**  dictionary | k/v pairs of existing configuration  Returned: always  Sample: `{"session": {}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"instance_id": 1, "vpn_name": null}` |
| **updates**  list / elements=string | commands sent to the device  Returned: always  Sample: `["isis 1"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
