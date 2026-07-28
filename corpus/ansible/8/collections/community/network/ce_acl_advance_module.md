---
collection: ansible
version: "8"
title: "community.network.ce_acl_advance module – Manages advanced ACL configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_acl_advance_module.html
fetched_at: 2026-07-28T01:55:12+00:00
---
# community.network.ce_acl_advance module – Manages advanced ACL configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_acl_advance`.

- [Synopsis](ce_acl_advance_module.md#synopsis)
- [Parameters](ce_acl_advance_module.md#parameters)
- [Notes](ce_acl_advance_module.md#notes)
- [Examples](ce_acl_advance_module.md#examples)
- [Return Values](ce_acl_advance_module.md#return-values)

## [Synopsis](ce_acl_advance_module.md#id1)

- Manages advanced ACL configurations on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_acl_advance

## [Parameters](ce_acl_advance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acl_description**  string | ACL description. The value is a string of 1 to 127 characters. |
| **acl_name**  string / required | ACL number or name. For a numbered rule group, the value ranging from 3000 to 3999 indicates a advance ACL. For a named rule group, the value is a string of 1 to 32 case-sensitive characters starting with a letter, spaces not supported. |
| **acl_num**  string | ACL number. The value is an integer ranging from 3000 to 3999. |
| **acl_step**  string | ACL step. The value is an integer ranging from 1 to 20. The default value is 5. |
| **dest_ip**  string | Destination IP address. The value is a string of 0 to 255 characters.The default value is 0.0.0.0. The value is in dotted decimal notation. |
| **dest_mask**  string | Destination IP address mask. The value is an integer ranging from 1 to 32. |
| **dest_pool_name**  string | Name of a destination pool. The value is a string of 1 to 32 characters. |
| **dest_port_begin**  string | Start port number of the destination port. The value is an integer ranging from 0 to 65535. |
| **dest_port_end**  string | End port number of the destination port. The value is an integer ranging from 0 to 65535. |
| **dest_port_op**  string | Range type of the destination port.  **Choices:**   - `"lt"` - `"eq"` - `"gt"` - `"range"` |
| **dest_port_pool_name**  string | Name of a destination port pool. The value is a string of 1 to 32 characters. |
| **dscp**  string | Differentiated Services Code Point. The value is an integer ranging from 0 to 63. |
| **established**  boolean | Match established connections.  **Choices:**   - `false` ← (default) - `true` |
| **frag_type**  string | Type of packet fragmentation.  **Choices:**   - `"fragment"` - `"clear_fragment"` |
| **icmp_code**  string | ICMP message code. Data packets can be filtered based on the ICMP message code. The value is an integer ranging from 0 to 255. |
| **icmp_name**  string | ICMP name.  **Choices:**   - `"unconfiged"` - `"echo"` - `"echo-reply"` - `"fragmentneed-DFset"` - `"host-redirect"` - `"host-tos-redirect"` - `"host-unreachable"` - `"information-reply"` - `"information-request"` - `"net-redirect"` - `"net-tos-redirect"` - `"net-unreachable"` - `"parameter-problem"` - `"port-unreachable"` - `"protocol-unreachable"` - `"reassembly-timeout"` - `"source-quench"` - `"source-route-failed"` - `"timestamp-reply"` - `"timestamp-request"` - `"ttl-exceeded"` - `"address-mask-reply"` - `"address-mask-request"` - `"custom"` |
| **icmp_type**  string | ICMP type. This parameter is available only when the packet protocol is ICMP. The value is an integer ranging from 0 to 255. |
| **igmp_type**  string | Internet Group Management Protocol.  **Choices:**   - `"host-query"` - `"mrouter-adver"` - `"mrouter-solic"` - `"mrouter-termi"` - `"mtrace-resp"` - `"mtrace-route"` - `"v1host-report"` - `"v2host-report"` - `"v2leave-group"` - `"v3host-report"` |
| **log_flag**  boolean | Flag of logging matched data packets.  **Choices:**   - `false` ← (default) - `true` |
| **precedence**  string | Data packets can be filtered based on the priority field. The value is an integer ranging from 0 to 7. |
| **protocol**  string | Protocol type.  **Choices:**   - `"ip"` - `"icmp"` - `"igmp"` - `"ipinip"` - `"tcp"` - `"udp"` - `"gre"` - `"ospf"` |
| **rule_action**  string | Matching mode of basic ACL rules.  **Choices:**   - `"permit"` - `"deny"` |
| **rule_description**  string | Description about an ACL rule. |
| **rule_id**  string | ID of a basic ACL rule in configuration mode. The value is an integer ranging from 0 to 4294967294. |
| **rule_name**  string | Name of a basic ACL rule. The value is a string of 1 to 32 characters. |
| **source_ip**  string | Source IP address. The value is a string of 0 to 255 characters.The default value is 0.0.0.0. The value is in dotted decimal notation. |
| **src_mask**  string | Source IP address mask. The value is an integer ranging from 1 to 32. |
| **src_pool_name**  string | Name of a source pool. The value is a string of 1 to 32 characters. |
| **src_port_begin**  string | Start port number of the source port. The value is an integer ranging from 0 to 65535. |
| **src_port_end**  string | End port number of the source port. The value is an integer ranging from 0 to 65535. |
| **src_port_op**  string | Range type of the source port.  **Choices:**   - `"lt"` - `"eq"` - `"gt"` - `"range"` |
| **src_port_pool_name**  string | Name of a source port pool. The value is a string of 1 to 32 characters. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"delete_acl"` |
| **syn_flag**  string | TCP flag value. The value is an integer ranging from 0 to 63. |
| **tcp_flag_mask**  string | TCP flag mask value. The value is an integer ranging from 0 to 63. |
| **time_range**  string | Name of a time range in which an ACL rule takes effect. |
| **tos**  string | ToS value on which data packet filtering is based. The value is an integer ranging from 0 to 15. |
| **ttl_expired**  boolean | Whether TTL Expired is matched, with the TTL value of 1.  **Choices:**   - `false` ← (default) - `true` |
| **vrf_name**  string | VPN instance name. The value is a string of 1 to 31 characters.The default value is _public_. |

## [Notes](ce_acl_advance_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_acl_advance_module.md#id4)

```yaml+jinja
- name: CloudEngine advance acl test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Config ACL"
    community.network.ce_acl_advance:
      state: present
      acl_name: 3200
      provider: "{{ cli }}"

  - name: "Undo ACL"
    community.network.ce_acl_advance:
      state: delete_acl
      acl_name: 3200
      provider: "{{ cli }}"

  - name: "Config ACL advance rule"
    community.network.ce_acl_advance:
      state: present
      acl_name: test
      rule_name: test_rule
      rule_id: 111
      rule_action: permit
      protocol: tcp
      source_ip: 10.10.10.10
      src_mask: 24
      frag_type: fragment
      provider: "{{ cli }}"

  - name: "Undo ACL advance rule"
    community.network.ce_acl_advance:
      state: absent
      acl_name: test
      rule_name: test_rule
      rule_id: 111
      rule_action: permit
      protocol: tcp
      source_ip: 10.10.10.10
      src_mask: 24
      frag_type: fragment
      provider: "{{ cli }}"
```

## [Return Values](ce_acl_advance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{"aclNumOrName": "test", "aclType": "Advance"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"acl_name": "test", "state": "delete_acl"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["undo acl name test"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
