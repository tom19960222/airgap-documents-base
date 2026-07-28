---
collection: ansible
version: "8"
title: "cisco.asa.asa_ogs module – Object Group resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/asa/asa_ogs_module.html
fetched_at: 2026-07-28T01:21:09+00:00
---
# cisco.asa.asa_ogs module – Object Group resource module

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/ui/repo/published/cisco/asa/) (version 4.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_ogs`.

New in cisco.asa 1.0.0

- [Synopsis](asa_ogs_module.md#synopsis)
- [Parameters](asa_ogs_module.md#parameters)
- [Notes](asa_ogs_module.md#notes)
- [Examples](asa_ogs_module.md#examples)
- [Return Values](asa_ogs_module.md#return-values)

## [Synopsis](asa_ogs_module.md#id1)

- This module configures and manages Objects and Groups on ASA platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ogs

## [Parameters](asa_ogs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of Object Group options. |
| **object_groups**  list / elements=dictionary | The object groups. |
| **description**  string | The description for the object-group. |
| **group_object**  list / elements=string | Configure an object group as an object |
| **icmp_type**  dictionary | Configure an ICMP-type object |
| **icmp_object**  list / elements=string | Defines the ICMP types in the group.  **Choices:**   - `"alternate-address"` - `"conversion-error"` - `"echo"` - `"echo-reply"` - `"information-reply"` - `"information-request"` - `"mask-reply"` - `"mask-request"` - `"mobile-redirect"` - `"parameter-problem"` - `"redirect"` - `"router-advertisement"` - `"router-solicitation"` - `"source-quench"` - `"time-exceeded"` - `"timestamp-reply"` - `"timestamp-request"` - `"traceroute"` - `"unreachable"` |
| **name**  string / required | Specifies object-group ID |
| **network_object**  dictionary | Configure a network object |
| **address**  list / elements=string | Enter an IPv4 network address with space seperated netmask. |
| **host**  list / elements=string | Set this to specify a single host object. |
| **ipv6_address**  list / elements=string | Enter an IPv6 prefix. |
| **object**  list / elements=string | Enter this keyword to specify a network object |
| **port_object**  list / elements=dictionary | Configure a port object |
| **eq**  string | Enter this keyword to specify a port |
| **range**  dictionary | Enter this keyword to specify a range of ports |
| **end**  string | Specify the end of the port range. |
| **start**  string | Specify the start of the port range. |
| **protocol**  string | Specifies that object-group is for only specified protocol only.  Required when port-object need to be configured  **Choices:**   - `"tcp"` - `"tcp-udp"` - `"udp"` |
| **protocol_object**  dictionary | Configure a protocol object |
| **protocol**  list / elements=string | Defines the protocols in the group.  User can either specify protocols directly/protocol numbers(0-255) |
| **security_group**  dictionary | Configure a security-group |
| **sec_name**  list / elements=string | Enter this keyword to specify a security-group name. |
| **tag**  list / elements=string | Enter this keyword to specify a security-group tag. |
| **service_object**  dictionary | Configure a service object  NEW ‘services_object’ param is introduced at object_group level, please use the newer ‘services_object’ param defined at object_group level instead of ‘service_object’ param at object_group level, as ‘service_object’ option will get deprecated and removed in a future release. |
| **object**  string | Enter this keyword to specify a service object |
| **protocol**  list / elements=string | Defines the protocols in the group.  **Choices:**   - `"ah"` - `"eigrp"` - `"esp"` - `"gre"` - `"icmp"` - `"icmp6"` - `"igmp"` - `"igrp"` - `"ip"` - `"ipinip"` - `"ipsec"` - `"nos"` - `"ospf"` - `"pcp"` - `"pim"` - `"pptp"` - `"sctp"` - `"snp"` - `"tcp"` - `"tcp-udp"` - `"udp"` |
| **services_object**  list / elements=dictionary | Configure list of service objects  Newer OGs services_object param which will replace service_object param  Relased with version 2.1.0 |
| **destination_port**  dictionary | Keyword to specify destination port |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Port range operator |
| **end**  string | Specify the end of the port range. |
| **start**  string | Specify the start of the port range. |
| **object**  string | Enter this keyword to specify a service object |
| **protocol**  string | Defines the protocols in the group. |
| **source_port**  dictionary | Keyword to specify source port |
| **eq**  string | Match only packets on a given port number. |
| **gt**  string | Match only packets with a greater port number. |
| **lt**  string | Match only packets with a lower port number. |
| **neq**  string | Match only packets not on a given port number. |
| **range**  dictionary | Port range operator |
| **end**  string | Specify the end of the port range. |
| **start**  string | Specify the start of the port range. |
| **user_object**  dictionary | Configures single user, local or import user group |
| **user**  list / elements=dictionary | Configure a user objectUser name to configure a user object. |
| **domain**  string / required | User domain |
| **name**  string / required | Enter the name of the user |
| **user_group**  list / elements=dictionary | Configure a user group object. |
| **domain**  string / required | Group domain |
| **name**  string / required | Enter the name of the group |
| **object_type**  string / required | The object group type.  **Choices:**   - `"icmp-type"` - `"network"` - `"protocol"` - `"security"` - `"service"` - `"user"` |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](asa_ogs_module.md#id3)

> **Note:**
>
> - Tested against Cisco ASA Version 9.10(1)11
> - This module works with connection `network_cli`. See [ASA Platform Options](../network/user_guide/platform_asa.md).

## [Examples](asa_ogs_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_network_og
#  network-object host 198.51.100.1

- name: "Merge module attributes of given object-group"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: group_network_obj
            group_object:
              - test_og_network
          - name: test_og_network
            description: test_og_network
            network_object:
              host:
                - 192.0.2.1
                - 192.0.2.2
              address:
                - 192.0.2.0 255.255.255.0
                - 198.51.100.0 255.255.255.0
          - name: test_network_og
            description: test_network_og
            network_object:
              host:
                - 198.51.100.1
                - 198.51.100.2
              ipv6_address:
                - 2001:db8:3::/64
      - object_type: security
        object_groups:
          - name: test_og_security
            description: test_security
            security_group:
              sec_name:
                - test_1
                - test_2
              tag:
                - 10
                - 20
      - object_type: service
        object_groups:
          - name: O-Worker
            services_object:
              - protocol: tcp
                destination_port:
                  range:
                    start: 100
                    end: 200
              - protocol: tcp-udp
                source_port:
                  eq: 1234
                destination_port:
                  gt: nfs
          - name: O-UNIX-TCP
            protocol: tcp
            port_object:
              - eq: https
              - range:
                  start: 100
                  end: 400
      - object_type: user
        object_groups:
          - name: test_og_user
            description: test_user
            user_object:
              user:
                - name: new_user_1
                  domain: LOCAL
                - name: new_user_2
                  domain: LOCAL
    state: merged

# Commands fired:
# ---------------
#
# object-group security test_og_security
# description test_security
# security-group name test_1
# security-group name test_2
# security-group tag 10
# security-group tag 20
# object-group network group_network_obj
# group-object test_og_network
# object-group network test_og_network
# description test_og_network
# network-object 192.0.2.0 255.255.255.0
# network-object 198.51.100.0 255.255.255.0
# network-object host 192.0.2.1
# network-object host 192.0.2.2
# object-group network test_network_og
# network-object host 198.51.100.1
# network-object host 198.51.100.2
# network-object 2001:db8:3::/64
# object-group service O-Worker
# service-object tcp destination range 100 200
# service-object tcp source eq 1234 destination gt nfs
# object-group service O-UNIX-TCP tcp
# port-object eq https
# port-object range 100 400
# object-group user test_og_user
# description test_user
# user LOCAL\new_user_1
# user LOCAL\new_user_2

# After state:
# ------------
#
# ciscoasa# sh running-config object-group
# object-group network group_network_obj
#  group-object test_og_network
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
#  network-object host 198.51.100.1
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group service O-Worker
#  service-object tcp destination range 100 200
#  service-object tcp source eq 1234 destination gt nfs
# object-group service O-UNIX-TCP tcp
#  port-object eq https
#  port-object range 100 400
# object-group user test_og_user
#  description test_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

# Using Replaced

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group service O-Worker
#  service-object tcp destination range 100 200
#  service-object tcp source eq 1234 destination gt nfs
# object-group service O-UNIX-TCP tcp
#  port-object eq https
#  port-object range 100 400
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

- name: "Replace module attributes of given object-group"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
            description: test_og_network_replace
            network_object:
              host:
                - 198.51.100.1
              address:
                - 198.51.100.0 255.255.255.0
      - object_type: protocol
        object_groups:
          - name: test_og_protocol
            description: test_og_protocol
            protocol_object:
              protocol:
                - tcp
                - udp
    state: replaced

# Commands Fired:
# ---------------
#
# object-group protocol test_og_protocol
# description test_og_protocol
# protocol tcp
# protocol udp
# object-group network test_og_network
# description test_og_network_replace
# no network-object 192.0.2.0 255.255.255.0
# no network-object 198.51.100.0 255.255.255.0
# network-object 198.51.100.0 255.255.255.0
# no network-object host 192.0.2.1
# no network-object host 192.0.2.2
# network-object host 198.51.100.1

# After state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network_replace
#  network-object host 198.51.100.1
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group service O-Worker
#  service-object tcp destination range 100 200
#  service-object tcp source eq 1234 destination gt nfs
# object-group service O-UNIX-TCP tcp
#  port-object eq https
#  port-object range 100 400
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2
# object-group protocol test_og_protocol
#  protocol-object tcp
#  protocol-object udp

# Using Overridden

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group service O-Worker
#  service-object tcp destination range 100 200
#  service-object tcp source eq 1234 destination gt nfs
# object-group service O-UNIX-TCP tcp
#  port-object eq https
#  port-object range 100 400
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

- name: "Overridden module attributes of given object-group"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
            description: test_og_network_override
            network_object:
              host:
                - 198.51.100.1
              address:
                - 198.51.100.0 255.255.255.0
          - name: ANSIBLE_TEST
            network_object:
              object:
                - TEST1
                - TEST2
      - object_type: protocol
        object_groups:
          - name: test_og_protocol
            description: test_og_protocol
            protocol_object:
              protocol:
                - tcp
                - udp
    state: overridden

# Commands Fired:
# ---------------
#
# no object-group security test_og_security
# no object-group service O-Worker
# no object-group service O-UNIX-TCP
# no object-group user test_og_user
# object-group protocol test_og_protocol
# description test_og_protocol
# protocol tcp
# protocol udp
# object-group network test_og_network
# description test_og_network_override
# no network-object 192.0.2.0 255.255.255.0
# no network-object 198.51.100.0 255.255.255.0
# network-object 198.51.100.0 255.255.255.0
# no network-object host 192.0.2.1
# no network-object host 192.0.2.2
# network-object host 198.51.100.1
# no object-group network test_network_og
# object-group network ANSIBLE_TEST
# network-object object TEST1
# network-object object TEST2

# After state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network_override
#  network-object host 198.51.100.1
#  network-object 198.51.100.0 255.255.255.0
# object-group network ANSIBLE_TEST
#  network-object object TEST1
#  network-object object TEST2
# object-group protocol test_og_protocol
#  protocol-object tcp
#  protocol-object udp

# Using Deleted

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group service O-Worker
#  service-object tcp destination range 100 200
#  service-object tcp source eq 1234 destination gt nfs
# object-group service O-UNIX-TCP tcp
#  port-object eq https
#  port-object range 100 400
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

- name: "Delete given module attributes"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
          - name: test_network_og
      - object_type: security
        object_groups:
          - name: test_og_security
      - object_type: service
        object_groups:
          - name: O-UNIX-TCP
    state: deleted

# Commands Fired:
# ---------------
#
# no object-group network test_og_network
# no object-group network test_network_og
# no object-group security test_og_security
# no object-group service O-UNIX-TCP

# After state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2
# object-group service O-Worker
#  service-object tcp destination range 100 200
#  service-object tcp source eq 1234 destination gt nfs

# Using DELETED without any config passed
# "(NOTE: This will delete all of configured resource module attributes)"

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

- name: Delete ALL configured module attributes
  cisco.asa.asa_ogs:
    config:
    state: deleted

# Commands Fired:
# ---------------
#
# no object-group network test_og_network
# no object-group network test_network_og
# no object-group security test_og_security
# no object-group user test_og_user

# After state:
# -------------
#
# ciscoasa# sh running-config object-group

# Using Gathered

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

- name: Gather listed OGs with provided configurations
  cisco.asa.asa_ogs:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "object_groups": [
#                 {
#                     "description": "test_security",
#                     "name": "test_og_security",
#                     "security_group": {
#                         "sec_name": [
#                             "test_2",
#                             "test_1"
#                         ],
#                         "tag": [
#                             10,
#                             20
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "security"
#         },
#         {
#             "object_groups": [
#                 {
#                     "description": "test_network_og",
#                     "name": "test_network_og",
#                     "network_object": {
#                         "host": [
#                             "198.51.100.1",
#                             "198.51.100.2"
#                         ],
#                         "ipv6_address": [
#                             "2001:db8:3::/64"
#                         ]
#                     }
#                 },
#                 {
#                     "description": "test_og_network",
#                     "name": "test_og_network",
#                     "network_object": {
#                         "address": [
#                             "192.0.2.0 255.255.255.0",
#                             "198.51.100.0 255.255.255.0"
#                         ],
#                         "host": [
#                             "192.0.2.1",
#                             "192.0.2.2"
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "network"
#         },
#         {
#             "object_groups": [
#                 {
#                     "description": "test_user",
#                     "name": "test_og_user",
#                     "user_object": {
#                         "user": [
#                             {
#                                 "domain": "LOCAL",
#                                 "name": "new_user_1"
#                             },
#                             {
#                                 "domain": "LOCAL",
#                                 "name": "new_user_2"
#                             }
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "user"
#         }
#     ]

# After state:
# ------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 198.51.100.1
#  network-object host 198.51.100.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\new_user_1
#  user LOCAL\new_user_2

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
            description: test_og_network
            network_object:
              host:
                - 192.0.2.1
                - 192.0.2.2
              address:
                - 192.0.2.0 255.255.255.0
                - 198.51.100.0 255.255.255.0
          - name: test_network_og
            description: test_network_og
            network_object:
              host:
                - 198.51.100.1
                - 198.51.100.2
              ipv6_address:
                - 2001:db8:3::/64
      - object_type: security
        object_groups:
          - name: test_og_security
            description: test_security
            security_group:
              sec_name:
                - test_1
                - test_2
              tag:
                - 10
                - 20
      - object_type: user
        object_groups:
          - name: test_og_user
            description: test_user
            user_object:
              user:
                - name: new_user_1
                  domain: LOCAL
                - name: new_user_2
                  domain: LOCAL
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "object-group security test_og_security",
#         "description test_security",
#         "security-group name test_1",
#         "security-group name test_2",
#         "security-group tag 10",
#         "security-group tag 20",
#         "object-group network test_og_network",
#         "description test_og_network",
#         "network-object 192.0.2.0 255.255.255.0",
#         "network-object 198.51.100.0 255.255.255.0",
#         "network-object host 192.0.2.1",
#         "network-object host 192.0.2.2",
#         "object-group network test_network_og",
#         "description test_network_og",
#         "network-object host 198.51.100.1",
#         "network-object host 198.51.100.2",
#         "network-object 2001:db8:3::/64",
#         "object-group user test_og_user",
#         "description test_user",
#         "user LOCAL\new_user_1",
#         "user LOCAL\new_user_2"
#     ]

# Using Parsed

# parsed.cfg
#
# object-group network test_og_network
#   description test_og_network
#   network-object host 192.0.2.1
#   network-object 192.0.2.0 255.255.255.0
# object-group network test_network_og
#   network-object 2001:db8:3::/64
# object-group service test_og_service
#   service-object tcp-udp

- name: Parse the commands for provided configuration
  cisco.asa.asa_ogs:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "object_groups": [
#                 {
#                     "name": "test_network_og"
#                 },
#                 {
#                     "description": "test_og_network",
#                     "name": "test_og_network",
#                     "network_object": {
#                         "host": [
#                             "192.0.2.2"
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "network"
#         },
#         {
#             "object_groups": [
#                 {
#                     "name": "test_og_service",
#                     "service_object": {
#                         "protocol": [
#                             "tcp-udp",
#                             "ipinip"
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "service"
#         }
#     ]
```

## [Return Values](asa_ogs_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  **Returned:** always  **Sample:** `["object-group network test_network_og", "description test_network_og", "network-object host 192.0.2.1"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
