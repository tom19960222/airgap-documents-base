---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_firewall_rule module – Manage AFM Firewall rules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_firewall_rule_module.html
fetched_at: 2026-07-27T17:26:44+00:00
---
# f5networks.f5_modules.bigip_firewall_rule module – Manage AFM Firewall rules

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_rule`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_rule_module.md#synopsis)
- [Parameters](bigip_firewall_rule_module.md#parameters)
- [Notes](bigip_firewall_rule_module.md#notes)
- [Examples](bigip_firewall_rule_module.md#examples)
- [Return Values](bigip_firewall_rule_module.md#return-values)

## [Synopsis](bigip_firewall_rule_module.md#id1)

- Manages firewall rules in an AFM (Advanced Firewall Manager) firewall policy. New rules will always be added to the end of the policy. Rules can be re-ordered using the `bigip_security_policy` module. Rules can also be pre-ordered using the `bigip_security_policy` module and then later updated using the `bigip_firewall_rule` module.

## [Parameters](bigip_firewall_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | Specifies the action for the firewall rule.  When `accept`, allows packets with the specified source, destination, and protocol to pass through the firewall. Packets that match the rule and are accepted, traverse the system as if the firewall is not present.  When `drop`, drops packets with the specified source, destination, and protocol. Dropping a packet is a silent action with no notification to the source or destination systems. Dropping the packet causes the connection to be retried until the retry threshold is reached.  When `reject`, rejects packets with the specified source, destination, and protocol. When a packet is rejected, the firewall sends a destination unreachable message to the sender.  When `accept-decisively`, allows packets with the specified source, destination, and protocol to pass through the firewall, and does not require any further processing by any of the further firewalls. Packets that match the rule and are accepted, traverse the system as if the firewall is not present. If the Rule List is applied to a virtual server, management IP, or self IP firewall rule, then Accept Decisively is equivalent to Accept.  When creating a new rule, if this parameter is not provided, the default is `reject`.  Choices:   - `"accept"` - `"drop"` - `"reject"` - `"accept-decisively"` |
| **description**  string | The rule description. |
| **destination**  list / elements=dictionary | Specifies packet destinations to which the rule applies.  Leaving this field blank applies the rule to all addresses and all ports.  You can specify the following destination items. An IPv4 or IPv6 address, an IPv4 or IPv6 address range, geographic location, VLAN, address list, port, port range, port list or address list.  You can specify a mix of different types of items for the source address. |
| **address**  string | Specifies a specific IP address. |
| **address_list**  string | Specifies an existing address list. |
| **address_range**  string | Specifies an address range. |
| **country**  string | Specifies a country code. |
| **port**  integer | Specifies a single numeric port.  This option is only valid when `protocol` is `tcp`(6) or `udp`(17). |
| **port_list**  string | Specifes an existing port list.  This option is only valid when `protocol` is `tcp`(6) or `udp`(17). |
| **port_range**  string | Specifies a range of ports, which is two port values separated by a hyphen. The port to the left of the hyphen should be less than the port to the right.  This option is only valid when `protocol` is `tcp`(6) or `udp`(17). |
| **icmp_message**  list / elements=dictionary | Specifies the Internet Control Message Protocol (ICMP) or ICMPv6 message `type` and `code` the rule uses.  This parameter is only relevant when `protocol` is either `icmp`(1) or `icmpv6`(58). |
| **code**  string | Specifies the code returned in response to the specified ICMP message type.  You can specify codes, each set appropriate to the associated type, such as No Code (0) (associated with Echo Reply (0)) and Host Unreachable (1) (associated with Destination Unreachable (3)), or you can specify `any` to indicate the system applies the rule for all codes in response to that specific ICMP message.  You can also specify an arbitrary code.  The ICMP protocol contains definitions for the existing message code and number pairs. |
| **type**  string | Specifies the type of ICMP message.  You can specify control messages, such as Echo Reply (0) and Destination Unreachable (3), or you can specify `any` to indicate the system applies the rule for all ICMP messages.  You can also specify an arbitrary ICMP message.  The ICMP protocol contains definitions for the existing message type and number pairs. |
| **irule**  string | Specifies an iRule that is applied to the firewall rule.  An iRule can be started when the firewall rule matches traffic. |
| **logging**  boolean | Specifies whether logging is enabled or disabled for the firewall rule.  When creating a new rule, if this parameter is not specified, the default if `no`.  Choices:   - `false` - `true` |
| **name**  string / required | Specifies the name of the rule. |
| **parent_policy**  string | The policy which contains the rule to be managed.  One of either `parent_policy` or `parent_rule_list` is required. |
| **parent_rule_list**  string | The rule list which contains the rule to be managed.  One of either `parent_policy` or `parent_rule_list` is required. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **protocol**  string | Specifies the protocol to which the rule applies.  Protocols may be specified by either their name or numeric value.  A special protocol value `any` can be specified to match any protocol. The numeric equivalent of this protocol is `255`. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **rule_list**  string | Specifies an existing rule list to use in the rule.  This parameter is mutually exclusive with many of the other individual-rule specific settings. This includes `logging`, `action`, `source`, `destination`, `irule'`, `protocol` and `logging`.  This parameter is only used when `parent_policy` is specified, otherwise it is ignored. |
| **schedule**  string | Specifies a schedule for the firewall rule.  You configure schedules to define days and times when the firewall rule is made active. |
| **source**  list / elements=dictionary | Specifies packet sources to which the rule applies.  Leaving this field blank applies the rule to all addresses and all ports.  You can specify the following source items. An IPv4 or IPv6 address, an IPv4 or IPv6 address range, geographic location, VLAN, address list, port, port range, port list or address list.  You can specify a mix of different types of items for the source address. |
| **address**  string | Specifies a specific IP address. |
| **address_list**  string | Specifies an existing address list. |
| **address_range**  string | Specifies an address range. |
| **country**  string | Specifies a country code. |
| **port**  integer | Specifies a single numeric port.  This option is only valid when `protocol` is `tcp`(6) or `udp`(17). |
| **port_list**  string | Specifes an existing port list.  This option is only valid when `protocol` is `tcp`(6) or `udp`(17). |
| **port_range**  string | Specifies a range of ports, which is two port values separated by a hyphen. The port to the left of the hyphen should be less than the port to the right.  This option is only valid when `protocol` is `tcp`(6) or `udp`(17). |
| **vlan**  string | Specifies VLANs to which the rule applies.  The VLAN source refers to the packet’s source. |
| **state**  string | When `state` is `present`, ensures the rule exists.  When `state` is `absent`, ensures the rule is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | Indicates the activity state of the rule or rule list.  When `disabled`, specifies the rule or rule list does not apply at all.  When `enabled`, specifies the system applies the firewall rule or rule list to the given context and addresses.  When `scheduled`, specifies the system applies the rule or rule list according to the specified schedule.  When creating a new rule, if this parameter is not provided, the default is `enabled`.  Choices:   - `"enabled"` - `"disabled"` - `"scheduled"` |

## [Notes](bigip_firewall_rule_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_rule_module.md#id4)

```yaml+jinja
- name: Create a new rule in the foo firewall policy
  bigip_firewall_rule:
    name: foo
    parent_policy: policy1
    protocol: tcp
    source:
      - address: 1.2.3.4
      - address: "::1"
      - address_list: foo-list1
      - address_range: 1.1.1.1-2.2.2.2
      - vlan: vlan1
      - country: US
      - port: 22
      - port_list: port-list1
      - port_range: 80-443
    destination:
      - address: 1.2.3.4
      - address: "::1"
      - address_list: foo-list1
      - address_range: 1.1.1.1-2.2.2.2
      - country: US
      - port: 22
      - port_list: port-list1
      - port_range: 80-443
    irule: irule1
    action: accept
    logging: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create an ICMP specific rule
  bigip_firewall_rule:
    name: foo
    protocol: icmp
    icmp_message:
      type: 0
    source:
      - country: US
    action: drop
    logging: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add a new policy rule that uses an existing rule list
  bigip_firewall_rule:
    name: foo
    parent_policy: foo_policy
    rule_list: rule-list1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **action**  string | The action for the firewall rule.  Returned: changed  Sample: `"drop"` |
| **description**  string | The rule description.  Returned: changed  Sample: `"MyRule"` |
| **destination**  complex | The packet destinations to which the rule applies.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **address**  string | A specific IP address.  Returned: changed  Sample: `"192.168.1.1"` |
| **address_list**  string | An existing address list.  Returned: changed  Sample: `"foo-list1"` |
| **address_range**  string | The address range.  Returned: changed  Sample: `"1.1.1.1-2.2.2.2"` |
| **country**  string | A country code.  Returned: changed  Sample: `"US"` |
| **port**  integer | Single numeric port.  Returned: changed  Sample: `8080` |
| **port_list**  string | An existing port list.  Returned: changed  Sample: `"port-list1"` |
| **port_range**  string | The port range.  Returned: changed  Sample: `"80-443"` |
| **icmp_message**  complex | The (ICMP) or ICMPv6 message `type` and `code` that the rule uses.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **code**  string | The code returned in response to the specified ICMP message type.  Returned: changed  Sample: `"1"` |
| **type**  string | The type of ICMP message.  Returned: changed  Sample: `"0"` |
| **irule**  string | The iRule that is applied to the firewall rule.  Returned: changed  Sample: `"_sys_auth_radius"` |
| **logging**  boolean | Enable or Disable logging for the firewall rule.  Returned: changed  Sample: `true` |
| **name**  string | Name of the rule.  Returned: changed  Sample: `"FooRule"` |
| **parent_policy**  string | The policy which contains the rule to be managed.  Returned: changed  Sample: `"FooPolicy"` |
| **parent_rule_list**  string | The rule list which contains the rule to be managed.  Returned: changed  Sample: `"FooRuleList"` |
| **protocol**  string | The protocol to which the rule applies.  Returned: changed  Sample: `"any"` |
| **rule_list**  string | An existing rule list to use in the parent policy.  Returned: changed  Sample: `"rule-list-1"` |
| **schedule**  string | The schedule for the firewall rule.  Returned: changed  Sample: `"Foo_schedule"` |
| **source**  complex | The packet sources to which the rule applies.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **address**  string | A specific IP address.  Returned: changed  Sample: `"192.168.1.1"` |
| **address_list**  string | An existing address list.  Returned: changed  Sample: `"foo-list1"` |
| **address_range**  string | The address range.  Returned: changed  Sample: `"1.1.1.1-2.2.2.2"` |
| **country**  string | A country code.  Returned: changed  Sample: `"US"` |
| **port**  integer | Single numeric port.  Returned: changed  Sample: `8080` |
| **port_list**  string | An existing port list.  Returned: changed  Sample: `"port-list1"` |
| **port_range**  string | The port range.  Returned: changed  Sample: `"80-443"` |
| **vlan**  string | Source VLANs for the packets.  Returned: changed  Sample: `"vlan1"` |
| **status**  string | The activity state of the rule or rule list.  Returned: changed  Sample: `"scheduled"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
