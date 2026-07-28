---
collection: ansible
version: "6"
title: "community.network.ce_acl module – Manages base ACL configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_acl_module.html
fetched_at: 2026-07-27T17:17:13+00:00
---
# community.network.ce_acl module – Manages base ACL configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_acl`.

- [Synopsis](ce_acl_module.md#synopsis)
- [Parameters](ce_acl_module.md#parameters)
- [Notes](ce_acl_module.md#notes)
- [Examples](ce_acl_module.md#examples)
- [Return Values](ce_acl_module.md#return-values)

## [Synopsis](ce_acl_module.md#id1)

- Manages base ACL configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_acl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acl_description**  string | ACL description. The value is a string of 1 to 127 characters. |
| **acl_name**  string / required | ACL number or name. For a numbered rule group, the value ranging from 2000 to 2999 indicates a basic ACL. For a named rule group, the value is a string of 1 to 32 case-sensitive characters starting with a letter, spaces not supported. |
| **acl_num**  string | ACL number. The value is an integer ranging from 2000 to 2999. |
| **acl_step**  string | ACL step. The value is an integer ranging from 1 to 20. The default value is 5. |
| **frag_type**  string | Type of packet fragmentation.  Choices:   - `"fragment"` - `"clear_fragment"` |
| **log_flag**  boolean | Flag of logging matched data packets.  Choices:   - `false` ← (default) - `true` |
| **rule_action**  string | Matching mode of basic ACL rules.  Choices:   - `"permit"` - `"deny"` |
| **rule_description**  string | Description about an ACL rule. The value is a string of 1 to 127 characters. |
| **rule_id**  string | ID of a basic ACL rule in configuration mode. The value is an integer ranging from 0 to 4294967294. |
| **rule_name**  string | Name of a basic ACL rule. The value is a string of 1 to 32 characters. The value is case-insensitive, and cannot contain spaces or begin with an underscore (_). |
| **source_ip**  string | Source IP address. The value is a string of 0 to 255 characters.The default value is 0.0.0.0. The value is in dotted decimal notation. |
| **src_mask**  string | Mask of a source IP address. The value is an integer ranging from 1 to 32. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"delete_acl"` |
| **time_range**  string | Name of a time range in which an ACL rule takes effect. The value is a string of 1 to 32 characters. The value is case-insensitive, and cannot contain spaces. The name must start with an uppercase or lowercase letter. In addition, the word “all” cannot be specified as a time range name. |
| **vrf_name**  string | VPN instance name. The value is a string of 1 to 31 characters.The default value is _public_. |

## [Notes](ce_acl_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_acl_module.md#id4)

```yaml+jinja
- name: CloudEngine acl test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:

  - name: "Config ACL"
    community.network.ce_acl:
      state: present
      acl_name: 2200

  - name: "Undo ACL"
    community.network.ce_acl:
      state: delete_acl
      acl_name: 2200

  - name: "Config ACL base rule"
    community.network.ce_acl:
      state: present
      acl_name: 2200
      rule_name: test_rule
      rule_id: 111
      rule_action: permit
      source_ip: 10.10.10.10
      src_mask: 24
      frag_type: fragment
      time_range: wdz_acl_time

  - name: "undo ACL base rule"
    community.network.ce_acl:
      state: absent
      acl_name: 2200
      rule_name: test_rule
      rule_id: 111
      rule_action: permit
      source_ip: 10.10.10.10
      src_mask: 24
      frag_type: fragment
      time_range: wdz_acl_time
```

## [Return Values](ce_acl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"aclNumOrName": "test", "aclType": "Basic"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"acl_name": "test", "state": "delete_acl"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["undo acl name test"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
