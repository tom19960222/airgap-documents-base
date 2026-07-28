---
collection: ansible
version: "8"
title: "community.network.ce_ospf module – Manages configuration of an OSPF instance on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_ospf_module.html
fetched_at: 2026-07-28T01:55:47+00:00
---
# community.network.ce_ospf module – Manages configuration of an OSPF instance on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_ospf`.

- [Synopsis](ce_ospf_module.md#synopsis)
- [Parameters](ce_ospf_module.md#parameters)
- [Notes](ce_ospf_module.md#notes)
- [Examples](ce_ospf_module.md#examples)
- [Return Values](ce_ospf_module.md#return-values)

## [Synopsis](ce_ospf_module.md#id1)

- Manages configuration of an OSPF instance on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_ospf

## [Parameters](ce_ospf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **addr**  string | Specifies the address of the network segment where the interface resides. The value is in dotted decimal notation. |
| **area**  string | Specifies the area ID. The area with the area-id being 0 is a backbone area. Valid values are a string, formatted as an IP address (i.e. “0.0.0.0”) or as an integer between 1 and 4294967295. |
| **auth_key_id**  string | Authentication key id when `auth_mode` is ‘hmac-sha256’, ‘md5’ or ‘hmac-md5. Valid value is an integer is in the range from 1 to 255. |
| **auth_mode**  string | Specifies the authentication type.  **Choices:**   - `"none"` - `"hmac-sha256"` - `"md5"` - `"hmac-md5"` - `"simple"` |
| **auth_text_md5**  string | Specifies a password for MD5, HMAC-MD5, or HMAC-SHA256 authentication. The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| **auth_text_simple**  string | Specifies a password for simple authentication. The value is a string of 1 to 8 characters. |
| **mask**  string | IP network wildcard bits in decimal format between 0 and 32. |
| **max_load_balance**  string | The maximum number of paths for forward packets over multiple paths. Valid value is an integer in the range from 1 to 64. |
| **nexthop_addr**  string | IPv4 address for configure next-hop address’s weight. Valid values are a string, formatted as an IP address. |
| **nexthop_weight**  string | Indicates the weight of the next hop. The smaller the value is, the higher the preference of the route is. It is an integer that ranges from 1 to 254. |
| **process_id**  string / required | Specifies a process ID. The value is an integer ranging from 1 to 4294967295. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_ospf_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_ospf_module.md#id4)

```yaml+jinja
- name: Ospf module test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: Configure ospf
    community.network.ce_ospf:
      process_id: 1
      area: 100
      state: present
```

## [Return Values](ce_ospf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"areas": [{"areaId": "0.0.0.100", "areaType": "Normal"}], "max_load_balance": "32", "nexthops": [], "process_id": "1"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"areas": [], "max_load_balance": "32", "nexthops": [], "process_id": "1"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"area": "100", "process_id": "1"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["ospf 1", "area 0.0.0.100"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
