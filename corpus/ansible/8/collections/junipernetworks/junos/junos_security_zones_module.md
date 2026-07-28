---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_security_zones module – Manage security zones on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_security_zones_module.html
fetched_at: 2026-07-28T02:39:56+00:00
---
# junipernetworks.junos.junos_security_zones module – Manage security zones on Juniper JUNOS devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_security_zones_module.md#ansible-collections-junipernetworks-junos-junos-security-zones-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_security_zones`.

New in junipernetworks.junos 2.9.0

- [Synopsis](junos_security_zones_module.md#synopsis)
- [Requirements](junos_security_zones_module.md#requirements)
- [Parameters](junos_security_zones_module.md#parameters)
- [Notes](junos_security_zones_module.md#notes)
- [Examples](junos_security_zones_module.md#examples)
- [Return Values](junos_security_zones_module.md#return-values)

## [Synopsis](junos_security_zones_module.md#id1)

- This module provides declarative management of security zones on Juniper JUNOS devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: security_zones

## [Requirements](junos_security_zones_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_security_zones_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Dictionary of security zone parameters |
| **functional_zone_management**  dictionary | Functional zone to configure host for out of band management interfaces |
| **description**  string | Text description of zone |
| **host_inbound_traffic**  dictionary | Allowed system services & protocols |
| **protocols**  list / elements=dictionary | Protocol type of incoming traffic to accept |
| **except**  boolean | Disallow the specified protocol traffic  **Choices:**   - `false` - `true` |
| **name**  string | Type of incoming protocol to accept |
| **system_services**  list / elements=dictionary | Type of incoming system-service traffic to accept |
| **except**  boolean | Disallow the specified incoming system-service traffic  **Choices:**   - `false` - `true` |
| **name**  string | Type of incoming system-service traffic to accept |
| **interfaces**  list / elements=string | Interfaces that are part of this zone |
| **screen**  string | Name of ids option object applied to the zone |
| **zones**  list / elements=dictionary | Security zones |
| **address_book**  dictionary | Address book entries |
| **address_sets**  list / elements=dictionary | Define security address sets |
| **address_sets**  list / elements=string | Define an address-set name |
| **addresses**  list / elements=string | Addresses to be included in this set |
| **description**  string | Text description of address set |
| **name**  string | Name of address set |
| **addresses**  list / elements=dictionary | Define security addresses |
| **description**  string | Text description of address |
| **dns_name**  dictionary | DNS address name |
| **ipv4_only**  boolean | IPv4 dns address  **Choices:**   - `false` - `true` |
| **ipv6_only**  boolean | IPv6 dns address  **Choices:**   - `false` - `true` |
| **name**  string | Fully qualified hostname |
| **ip_prefix**  string | Numeric IPv4 or IPv6 address with prefix |
| **name**  string | Name of address |
| **range_address**  dictionary | Address range |
| **from**  string | Start of address range |
| **to**  string | End of address range |
| **wildcard_address**  string | Numeric IPv4 wildcard address with in the form of a.d.d.r/netmask |
| **advance_policy_based_routing_profile**  string | Enable Advance Policy Based Routing on this zone |
| **advanced_connection_tracking**  dictionary | Enable Advance Policy Based Routing on this zone |
| **mode**  string | Set connection tracking mode  **Choices:**   - `"allow-any-host"` - `"allow-target-host"` - `"allow-target-host-port"` |
| **timeout**  integer | Timeout value in seconds for advanced-connection-tracking table for this zone |
| **track_all_policies_to_this_zone**  boolean | Mandate all policies with to-zone set to this zone to do connection track table lookup  **Choices:**   - `false` - `true` |
| **application_tracking**  boolean | Enable Application tracking support for this zone  **Choices:**   - `false` - `true` |
| **description**  string | Text description of zone |
| **enable_reverse_reroute**  boolean | Enable Reverse route lookup when there is change in ingress interface  **Choices:**   - `false` - `true` |
| **host_inbound_traffic**  dictionary | Allowed system services & protocols |
| **protocols**  list / elements=dictionary | Protocol type of incoming traffic to accept |
| **except**  boolean | Disallow the specified protocol traffic  **Choices:**   - `false` - `true` |
| **name**  string | Type of incoming protocol to accept |
| **system_services**  list / elements=dictionary | Type of incoming system-service traffic to accept |
| **except**  boolean | Disallow the specified incoming system-service traffic  **Choices:**   - `false` - `true` |
| **name**  string | Type of incoming system-service traffic to accept |
| **interfaces**  list / elements=string | Interfaces that are part of this zone |
| **name**  string | Name of the security zone |
| **screen**  string | Name of ids option object applied to the zone |
| **source_identity_log**  boolean | Show user and group info in session log for this zone  **Choices:**   - `false` - `true` |
| **tcp_rst**  boolean | Send RST for NON-SYN packet not matching TCP session  **Choices:**   - `false` - `true` |
| **unidirectional_session_refreshing**  boolean | Enable unidirectional session refreshing on this zone  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the JunOS device by executing the command **show security policies**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required. behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show security policies detail* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](junos_security_zones_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_security_zones_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show security zones
#
# [edit]
# vagrant@vsrx# show security zones
#
- name: Merge the provided configuration with the exisiting running configuration
  junipernetworks.junos.junos_security_zones: &merged
    config:
      functional_zone_management:
        description: test description
        host_inbound_traffic:
          protocols:
            - name: all
            - name: bgp
              except: true
          system_services:
            - name: all
            - except: true
              name: dhcp
        interfaces:
          - ge-0/0/1.0
          - ge-0/0/2.0
        screen: test_screen
      security_zones:
        - address_book:
            address_sets:
              - addresses:
                  - test_adr1
                  - test_adr2
                name: test_adrset1
              - addresses:
                  - test_adr3
                  - test_adr4
                name: test_adrset2
              - address_sets:
                  - test_adrset1
                  - test_adrset2
                addresses:
                  - test_adr5
                description: test description
                name: test_adrset3
            addresses:
              - description: test desc
                ip_prefix: 10.0.0.0/24
                name: test_adr1
              - dns_name:
                  ipv6_only: true
                  name: 1.1.1.1
                name: test_adr2
              - name: test_adr3
                range_address:
                  from: 10.2.0.1
                  to: 10.2.0.2
              - name: test_adr4
                wildcard_address: 10.3.0.1/24
              - description: test desc
                ip_prefix: 10.1.0.0/24
                name: test_adr5
          advance_policy_based_routing_profile: test_profile
          application_tracking: true
          description: test description
          enable_reverse_reroute: true
          host_inbound_traffic:
            protocols:
              - name: all
              - except: true
                name: bgp
            system_services:
              - name: all
              - except: true
                name: dhcp
          interfaces:
            - ge-0/0/3.0
            - ge-0/0/4.0
          name: test_sec_zone1
          screen: test_screen
          source_identity_log: true
          tcp_rst: true
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#   "after": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     },
#     "security_zones": [
#         {
#             "address_book": {
#                 "address_sets": [
#                     {
#                         "addresses": [
#                             "test_adr1",
#                             "test_adr2"
#                         ],
#                         "name": "test_adrset1"
#                     },
#                     {
#                         "addresses": [
#                             "test_adr3",
#                             "test_adr4"
#                         ],
#                         "name": "test_adrset2"
#                     },
#                     {
#                         "address_sets": [
#                             "test_adrset1",
#                             "test_adrset2"
#                         ],
#                         "addresses": [
#                             "test_adr5"
#                         ],
#                         "description": "test description",
#                         "name": "test_adrset3"
#                     }
#                 ],
#                 "addresses": [
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.0.0.0/24",
#                         "name": "test_adr1"
#                     },
#                     {
#                         "dns_name": {
#                             "ipv6_only": true,
#                             "name": "1.1.1.1"
#                         },
#                         "name": "test_adr2"
#                     },
#                     {
#                         "name": "test_adr3",
#                         "range_address": {
#                             "from": "10.2.0.1",
#                             "to": "10.2.0.2"
#                         }
#                     },
#                     {
#                         "name": "test_adr4",
#                         "wildcard_address": "10.3.0.1/24"
#                     },
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.1.0.0/24",
#                         "name": "test_adr5"
#                     }
#                 ]
#             },
#             "advance_policy_based_routing_profile": "test_profile",
#             "application_tracking": true,
#             "description": "test description",
#             "enable_reverse_reroute": true,
#             "host_inbound_traffic": {
#                 "protocols": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "bgp"
#                     }
#                 ],
#                 "system_services": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "dhcp"
#                     }
#                 ]
#             },
#             "interfaces": [
#                 "ge-0/0/3.0",
#                 "ge-0/0/4.0"
#             ],
#             "name": "test_sec_zone1",
#             "screen": "test_screen",
#             "source_identity_log": true,
#             "tcp_rst": true
#         }
#     ]
# },
# "before": {},
# "changed": true,
# "commands":
# '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones><nc:functional-zone><nc:management><nc:description>t'
# 'est description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:na'
# 'me>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-services><nc:system-services><n'
# 'c:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/1.0</nc:name></nc'
# ':interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:screen></nc:management></nc:f'
# 'unctional-zone><nc:security-zone><nc:name>test_sec_zone1</nc:name><nc:address-book><nc:address><nc:name>test_adr1</nc:name><nc:i'
# 'p-prefix>10.0.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:address><nc:address><nc:name>test_adr2</nc:nam'
# 'e><nc:dns-name><nc:name>1.1.1.1</nc:name><nc:ipv6-only/></nc:dns-name></nc:address><nc:address><nc:name>test_adr3</nc:name><nc:r'
# 'ange-address><nc:name>10.2.0.1</nc:name><nc:to><nc:range-high>10.2.0.2</nc:range-high></nc:to></nc:range-address></nc:address><n'
# 'c:address><nc:name>test_adr4</nc:name><nc:wildcard-address><nc:name>10.3.0.1/24</nc:name></nc:wildcard-address></nc:address><nc:'
# 'address><nc:name>test_adr5</nc:name><nc:ip-prefix>10.1.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:addre'
# 'ss><nc:address-set><nc:name>test_adrset1</nc:name><nc:address><nc:name>test_adr1</nc:name></nc:address><nc:address><nc:name>test'
# '_adr2</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset2</nc:name><nc:address><nc:name>test_adr3</nc:n'
# 'ame></nc:address><nc:address><nc:name>test_adr4</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset3</nc'
# ':name><nc:address><nc:name>test_adr5</nc:name></nc:address><nc:address-set><nc:name>test_adrset1</nc:name></nc:address-set><nc:a'
# 'ddress-set><nc:name>test_adrset2</nc:name></nc:address-set><nc:description>test description</nc:description></nc:address-set></n'
# 'c:address-book><nc:advance-policy-based-routing-profile><nc:profile>test_profile</nc:profile></nc:advance-policy-based-routing-p'
# 'rofile><nc:application-tracking/><nc:description>test description</nc:description><nc:enable-reverse-reroute/><nc:host-inbound-t'
# 'raffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:sys'
# 'tem-services><nc:name>all</nc:name></nc:system-services><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-servi'
# 'ces></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/3.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/4.0</nc'
# ':name></nc:interfaces><nc:screen>test_screen</nc:screen><nc:source-identity-log/><nc:tcp-rst/></nc:security-zone></nc:zones></nc'
# ':security>'

# After state
# -----------
#
# vagrant@vsrx# show system ntp
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
# security-zone test_sec_zone1 {
#     description "test description";
#     tcp-rst;
#     address-book {
#         address test_adr1 {
#             description "test desc";
#             10.0.0.0/24;
#         }
#         address test_adr2 {
#             dns-name 1.1.1.1 {
#                 ipv6-only;
#             }
#         }
#         address test_adr3 {
#             range-address 10.2.0.1 {
#                 to {
#                     10.2.0.2;
#                 }
#             }
#         }
#         address test_adr4 {
#             wildcard-address 10.3.0.1/24;
#         }
#         address test_adr5 {
#             description "test desc";
#             10.1.0.0/24;
#         }
#         address-set test_adrset1 {
#             address test_adr1;
#             address test_adr2;
#         }
#         address-set test_adrset2 {
#             address test_adr3;
#             address test_adr4;
#         }
#         address-set test_adrset3 {
#             description "test description";
#             address test_adr5;
#             address-set test_adrset1;
#             address-set test_adrset2;
#         }
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     interfaces {
#         ge-0/0/3.0;
#         ge-0/0/4.0;
#     }
#     application-tracking;
#     source-identity-log;
#     advance-policy-based-routing-profile {
#         test_profile;
#     }
#     enable-reverse-reroute;
# }
#
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show security zones
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
# security-zone test_sec_zone1 {
#     description "test description";
#     tcp-rst;
#     address-book {
#         address test_adr1 {
#             description "test desc";
#             10.0.0.0/24;
#         }
#         address test_adr2 {
#             dns-name 1.1.1.1 {
#                 ipv6-only;
#             }
#         }
#         address test_adr3 {
#             range-address 10.2.0.1 {
#                 to {
#                     10.2.0.2;
#                 }
#             }
#         }
#         address test_adr4 {
#             wildcard-address 10.3.0.1/24;
#         }
#         address test_adr5 {
#             description "test desc";
#             10.1.0.0/24;
#         }
#         address-set test_adrset1 {
#             address test_adr1;
#             address test_adr2;
#         }
#         address-set test_adrset2 {
#             address test_adr3;
#             address test_adr4;
#         }
#         address-set test_adrset3 {
#             description "test description";
#             address test_adr5;
#             address-set test_adrset1;
#             address-set test_adrset2;
#         }
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     interfaces {
#         ge-0/0/3.0;
#         ge-0/0/4.0;
#     }
#     application-tracking;
#     source-identity-log;
#     advance-policy-based-routing-profile {
#         test_profile;
#     }
#     enable-reverse-reroute;
# }
#
#

- name: Replaced running security zones configuration with provided configuration
  junipernetworks.junos.junos_security_zones:
    config:
      functional_zone_management:
        description: test description
        host_inbound_traffic:
          protocols:
            - name: all
            - name: bgp
              except: true
          system_services:
            - name: all
            - except: true
              name: dhcp
          interfaces:
            - ge-0/0/1.0
            - ge-0/0/2.0
        screen: test_screen
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     }
# },
# "before": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     },
#     "security_zones": [
#         {
#             "address_book": {
#                 "address_sets": [
#                     {
#                         "addresses": [
#                             "test_adr1",
#                             "test_adr2"
#                         ],
#                         "name": "test_adrset1"
#                     },
#                     {
#                         "addresses": [
#                             "test_adr3",
#                             "test_adr4"
#                         ],
#                         "name": "test_adrset2"
#                     },
#                     {
#                         "address_sets": [
#                             "test_adrset1",
#                             "test_adrset2"
#                         ],
#                         "addresses": [
#                             "test_adr5"
#                         ],
#                         "description": "test description",
#                         "name": "test_adrset3"
#                     }
#                 ],
#                 "addresses": [
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.0.0.0/24",
#                         "name": "test_adr1"
#                     },
#                     {
#                         "dns_name": {
#                             "ipv6_only": true,
#                             "name": "1.1.1.1"
#                         },
#                         "name": "test_adr2"
#                     },
#                     {
#                         "name": "test_adr3",
#                         "range_address": {
#                             "from": "10.2.0.1",
#                             "to": "10.2.0.2"
#                         }
#                     },
#                     {
#                         "name": "test_adr4",
#                         "wildcard_address": "10.3.0.1/24"
#                     },
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.1.0.0/24",
#                         "name": "test_adr5"
#                     }
#                 ]
#             },
#             "advance_policy_based_routing_profile": "test_profile",
#             "application_tracking": true,
#             "description": "test description",
#             "enable_reverse_reroute": true,
#             "host_inbound_traffic": {
#                 "protocols": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "bgp"
#                     }
#                 ],
#                 "system_services": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "dhcp"
#                     }
#                 ]
#             },
#             "interfaces": [
#                 "ge-0/0/3.0",
#                 "ge-0/0/4.0"
#             ],
#             "name": "test_sec_zone1",
#             "screen": "test_screen",
#             "source_identity_log": true,
#             "tcp_rst": true
#         }
#     ]
# },
# "changed": true,
# "commands":
# '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones delete="delete"/><nc:zones><nc:functional-zone><nc'
# ':management><nc:description>test description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:p'
# 'rotocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-se'
# 'rvices><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:'
# 'name>ge-0/0/1.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:'
# 'screen></nc:management></nc:functional-zone></nc:zones></nc:security>'
#
#
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
#
#
# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show security zones
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
# security-zone test_sec_zone1 {
#     description "test description";
#     tcp-rst;
#     address-book {
#         address test_adr1 {
#             description "test desc";
#             10.0.0.0/24;
#         }
#         address test_adr2 {
#             dns-name 1.1.1.1 {
#                 ipv6-only;
#             }
#         }
#         address test_adr3 {
#             range-address 10.2.0.1 {
#                 to {
#                     10.2.0.2;
#                 }
#             }
#         }
#         address test_adr4 {
#             wildcard-address 10.3.0.1/24;
#         }
#         address test_adr5 {
#             description "test desc";
#             10.1.0.0/24;
#         }
#         address-set test_adrset1 {
#             address test_adr1;
#             address test_adr2;
#         }
#         address-set test_adrset2 {
#             address test_adr3;
#             address test_adr4;
#         }
#         address-set test_adrset3 {
#             description "test description";
#             address test_adr5;
#             address-set test_adrset1;
#             address-set test_adrset2;
#         }
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     interfaces {
#         ge-0/0/3.0;
#         ge-0/0/4.0;
#     }
#     application-tracking;
#     source-identity-log;
#     advance-policy-based-routing-profile {
#         test_profile;
#     }
#     enable-reverse-reroute;
# }
#
#

- name: Override running security zones configuration with provided configuration
  junipernetworks.junos.junos_security_zones:
    config:
      functional_zone_management:
        description: test description
        host_inbound_traffic:
          protocols:
            - name: all
            - name: bgp
              except: true
          system_services:
            - name: all
            - except: true
              name: dhcp
        interfaces:
          - ge-0/0/1.0
          - ge-0/0/2.0
        screen: test_screen
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     }
# },
# "before": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     },
#     "security_zones": [
#         {
#             "address_book": {
#                 "address_sets": [
#                     {
#                         "addresses": [
#                             "test_adr1",
#                             "test_adr2"
#                         ],
#                         "name": "test_adrset1"
#                     },
#                     {
#                         "addresses": [
#                             "test_adr3",
#                             "test_adr4"
#                         ],
#                         "name": "test_adrset2"
#                     },
#                     {
#                         "address_sets": [
#                             "test_adrset1",
#                             "test_adrset2"
#                         ],
#                         "addresses": [
#                             "test_adr5"
#                         ],
#                         "description": "test description",
#                         "name": "test_adrset3"
#                     }
#                 ],
#                 "addresses": [
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.0.0.0/24",
#                         "name": "test_adr1"
#                     },
#                     {
#                         "dns_name": {
#                             "ipv6_only": true,
#                             "name": "1.1.1.1"
#                         },
#                         "name": "test_adr2"
#                     },
#                     {
#                         "name": "test_adr3",
#                         "range_address": {
#                             "from": "10.2.0.1",
#                             "to": "10.2.0.2"
#                         }
#                     },
#                     {
#                         "name": "test_adr4",
#                         "wildcard_address": "10.3.0.1/24"
#                     },
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.1.0.0/24",
#                         "name": "test_adr5"
#                     }
#                 ]
#             },
#             "advance_policy_based_routing_profile": "test_profile",
#             "application_tracking": true,
#             "description": "test description",
#             "enable_reverse_reroute": true,
#             "host_inbound_traffic": {
#                 "protocols": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "bgp"
#                     }
#                 ],
#                 "system_services": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "dhcp"
#                     }
#                 ]
#             },
#             "interfaces": [
#                 "ge-0/0/3.0",
#                 "ge-0/0/4.0"
#             ],
#             "name": "test_sec_zone1",
#             "screen": "test_screen",
#             "source_identity_log": true,
#             "tcp_rst": true
#         }
#     ]
# },
# "changed": true,
# "commands":
# '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones delete="delete"/><nc:zones><nc:functional-zone><nc'
# ':management><nc:description>test description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:p'
# 'rotocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-se'
# 'rvices><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:'
# 'name>ge-0/0/1.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:'
# 'screen></nc:management></nc:functional-zone></nc:zones></nc:security>'
#
#
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
#
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show security zones
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
#
#
- name: Delete running security zones configuration
  junipernetworks.junos.junos_security_zones:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     }
# },
# "changed": true,
# "commands":
#   "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#   "<nc:zones delete="delete"/></nc:security>"
#
#
# After state
# -----------
#
# vagrant@vsrx# show security zones
#
# [edit]
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# functional-zone management {
#     interfaces {
#         ge-0/0/1.0;
#         ge-0/0/2.0;
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     description "test description";
# }
# security-zone test_sec_zone1 {
#     description "test description";
#     tcp-rst;
#     address-book {
#         address test_adr1 {
#             description "test desc";
#             10.0.0.0/24;
#         }
#         address test_adr2 {
#             dns-name 1.1.1.1 {
#                 ipv6-only;
#             }
#         }
#         address test_adr3 {
#             range-address 10.2.0.1 {
#                 to {
#                     10.2.0.2;
#                 }
#             }
#         }
#         address test_adr4 {
#             wildcard-address 10.3.0.1/24;
#         }
#         address test_adr5 {
#             description "test desc";
#             10.1.0.0/24;
#         }
#         address-set test_adrset1 {
#             address test_adr1;
#             address test_adr2;
#         }
#         address-set test_adrset2 {
#             address test_adr3;
#             address test_adr4;
#         }
#         address-set test_adrset3 {
#             description "test description";
#             address test_adr5;
#             address-set test_adrset1;
#             address-set test_adrset2;
#         }
#     }
#     screen test_screen;
#     host-inbound-traffic {
#         system-services {
#             all;
#             dhcp {
#                 except;
#             }
#         }
#         protocols {
#             all;
#             bgp {
#                 except;
#             }
#         }
#     }
#     interfaces {
#         ge-0/0/3.0;
#         ge-0/0/4.0;
#     }
#     application-tracking;
#     source-identity-log;
#     advance-policy-based-routing-profile {
#         test_profile;
#     }
#     enable-reverse-reroute;
# }
- name: Gather running security zones configuration
  junipernetworks.junos.junos_security_zones:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
# "gathered": {
#     "functional_zone_management": {
#         "description": "test description",
#         "host_inbound_traffic": {
#             "protocols": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "bgp"
#                 }
#             ],
#             "system_services": [
#                 {
#                     "name": "all"
#                 },
#                 {
#                     "except": true,
#                     "name": "dhcp"
#                 }
#             ]
#         },
#         "interfaces": [
#             "ge-0/0/1.0",
#             "ge-0/0/2.0"
#         ],
#         "screen": "test_screen"
#     },
#     "security_zones": [
#         {
#             "address_book": {
#                 "address_sets": [
#                     {
#                         "addresses": [
#                             "test_adr1",
#                             "test_adr2"
#                         ],
#                         "name": "test_adrset1"
#                     },
#                     {
#                         "addresses": [
#                             "test_adr3",
#                             "test_adr4"
#                         ],
#                         "name": "test_adrset2"
#                     },
#                     {
#                         "address_sets": [
#                             "test_adrset1",
#                             "test_adrset2"
#                         ],
#                         "addresses": [
#                             "test_adr5"
#                         ],
#                         "description": "test description",
#                         "name": "test_adrset3"
#                     }
#                 ],
#                 "addresses": [
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.0.0.0/24",
#                         "name": "test_adr1"
#                     },
#                     {
#                         "dns_name": {
#                             "ipv6_only": true,
#                             "name": "1.1.1.1"
#                         },
#                         "name": "test_adr2"
#                     },
#                     {
#                         "name": "test_adr3",
#                         "range_address": {
#                             "from": "10.2.0.1",
#                             "to": "10.2.0.2"
#                         }
#                     },
#                     {
#                         "name": "test_adr4",
#                         "wildcard_address": "10.3.0.1/24"
#                     },
#                     {
#                         "description": "test desc",
#                         "ip_prefix": "10.1.0.0/24",
#                         "name": "test_adr5"
#                     }
#                 ]
#             },
#             "advance_policy_based_routing_profile": "test_profile",
#             "application_tracking": true,
#             "description": "test description",
#             "enable_reverse_reroute": true,
#             "host_inbound_traffic": {
#                 "protocols": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "bgp"
#                     }
#                 ],
#                 "system_services": [
#                     {
#                         "name": "all"
#                     },
#                     {
#                         "except": true,
#                         "name": "dhcp"
#                     }
#                 ]
#             },
#             "interfaces": [
#                 "ge-0/0/3.0",
#                 "ge-0/0/4.0"
#             ],
#             "name": "test_sec_zone1",
#             "screen": "test_screen",
#             "source_identity_log": true,
#             "tcp_rst": true
#         }
#     ]
# }
# "changed": false,
#
#
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_security_zones:
    config:
      functional_zone_management:
        description: test description
        host_inbound_traffic:
          protocols:
            - name: all
            - name: bgp
              except: true
          system_services:
            - name: all
            - except: true
              name: dhcp
        interfaces:
          - ge-0/0/1.0
          - ge-0/0/2.0
        screen: test_screen
      security_zones:
        - address_book:
            address_sets:
              - addresses:
                  - test_adr1
                  - test_adr2
                name: test_adrset1
              - addresses:
                  - test_adr3
                  - test_adr4
                name: test_adrset2
              - address_sets:
                  - test_adrset1
                  - test_adrset2
              - addresses:
                  - test_adr5
                description: test description
                name: test_adrset3
            addresses:
              - description: test desc
                ip_prefix: 10.0.0.0/24
                name: test_adr1
              - dns_name:
                  ipv6_only: true
                  name: 1.1.1.1
                name: test_adr2
              - name: test_adr3
                range_address:
                  from: 10.2.0.1
                  to: 10.2.0.2
              - name: test_adr4
                wildcard_address: 10.3.0.1/24
              - description: test desc
                ip_prefix: 10.1.0.0/24
                name: test_adr5
          advance_policy_based_routing_profile: test_profile
          application_tracking: true
          description: test description
          enable_reverse_reroute: true
          host_inbound_traffic:
            protocols:
              - name: all
              - except: true
                name: bgp
            system_services:
              - name: all
              - except: true
                name: dhcp
          interfaces:
            - ge-0/0/3.0
            - ge-0/0/4.0
          name: test_sec_zone1
          screen: test_screen
          source_identity_log: true
          tcp_rst: true
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
# "rendered":
# '<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:zones><nc:functional-zone><nc:management><nc:description>t'
# 'est description</nc:description><nc:host-inbound-traffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:na'
# 'me>bgp</nc:name><nc:except/></nc:protocols><nc:system-services><nc:name>all</nc:name></nc:system-services><nc:system-services><n'
# 'c:name>dhcp</nc:name><nc:except/></nc:system-services></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/1.0</nc:name></nc'
# ':interfaces><nc:interfaces><nc:name>ge-0/0/2.0</nc:name></nc:interfaces><nc:screen>test_screen</nc:screen></nc:management></nc:f'
# 'unctional-zone><nc:security-zone><nc:name>test_sec_zone1</nc:name><nc:address-book><nc:address><nc:name>test_adr1</nc:name><nc:i'
# 'p-prefix>10.0.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:address><nc:address><nc:name>test_adr2</nc:nam'
# 'e><nc:dns-name><nc:name>1.1.1.1</nc:name><nc:ipv6-only/></nc:dns-name></nc:address><nc:address><nc:name>test_adr3</nc:name><nc:r'
# 'ange-address><nc:name>10.2.0.1</nc:name><nc:to><nc:range-high>10.2.0.2</nc:range-high></nc:to></nc:range-address></nc:address><n'
# 'c:address><nc:name>test_adr4</nc:name><nc:wildcard-address><nc:name>10.3.0.1/24</nc:name></nc:wildcard-address></nc:address><nc:'
# 'address><nc:name>test_adr5</nc:name><nc:ip-prefix>10.1.0.0/24</nc:ip-prefix><nc:description>test desc</nc:description></nc:addre'
# 'ss><nc:address-set><nc:name>test_adrset1</nc:name><nc:address><nc:name>test_adr1</nc:name></nc:address><nc:address><nc:name>test'
# '_adr2</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset2</nc:name><nc:address><nc:name>test_adr3</nc:n'
# 'ame></nc:address><nc:address><nc:name>test_adr4</nc:name></nc:address></nc:address-set><nc:address-set><nc:name>test_adrset3</nc'
# ':name><nc:address><nc:name>test_adr5</nc:name></nc:address><nc:address-set><nc:name>test_adrset1</nc:name></nc:address-set><nc:a'
# 'ddress-set><nc:name>test_adrset2</nc:name></nc:address-set><nc:description>test description</nc:description></nc:address-set></n'
# 'c:address-book><nc:advance-policy-based-routing-profile><nc:profile>test_profile</nc:profile></nc:advance-policy-based-routing-p'
# 'rofile><nc:application-tracking/><nc:description>test description</nc:description><nc:enable-reverse-reroute/><nc:host-inbound-t'
# 'raffic><nc:protocols><nc:name>all</nc:name></nc:protocols><nc:protocols><nc:name>bgp</nc:name><nc:except/></nc:protocols><nc:sys'
# 'tem-services><nc:name>all</nc:name></nc:system-services><nc:system-services><nc:name>dhcp</nc:name><nc:except/></nc:system-servi'
# 'ces></nc:host-inbound-traffic><nc:interfaces><nc:name>ge-0/0/3.0</nc:name></nc:interfaces><nc:interfaces><nc:name>ge-0/0/4.0</nc'
# ':name></nc:interfaces><nc:screen>test_screen</nc:screen><nc:source-identity-log/><nc:tcp-rst/></nc:security-zone></nc:zones></nc'
# ':security>'
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <security>
#             <zones>
#                 <functional-zone>
#                     <management>
#                         <description>test description</description>
#                         <host-inbound-traffic>
#                             <protocols>
#                                 <name>all</name>
#                             </protocols>
#                             <protocols>
#                                 <name>bgp</name>
#                                 <except />
#                             </protocols>
#                             <system-services>
#                                 <name>all</name>
#                             </system-services>
#                             <system-services>
#                                 <name>dhcp</name>
#                                 <except />
#                             </system-services>
#                         </host-inbound-traffic>
#                         <interfaces>
#                             <name>ge-0/0/1.0</name>
#                         </interfaces>
#                         <interfaces>
#                             <name>ge-0/0/2.0</name>
#                         </interfaces>
#                         <screen>test_screen</screen>
#                     </management>
#                 </functional-zone>
#                 <security-zone>
#                     <name>test_sec_zone1</name>
#                     <address-book>
#                         <address>
#                             <name>test_adr1</name>
#                             <ip-prefix>10.0.0.0/24</ip-prefix>
#                             <description>test desc</description>
#                         </address>
#                         <address>
#                             <name>test_adr2</name>
#                             <dns-name>
#                                 <name>1.1.1.1</name>
#                                 <ipv6-only />
#                             </dns-name>
#                         </address>
#                         <address>
#                             <name>test_adr3</name>
#                             <range-address>
#                                 <name>10.2.0.1</name>
#                                 <to>
#                                     <range-high>10.2.0.2</range-high>
#                                 </to>
#                             </range-address>
#                         </address>
#                         <address>
#                             <name>test_adr4</name>
#                             <wildcard-address>
#                                 <name>10.3.0.1/24</name>
#                             </wildcard-address>
#                         </address>
#                         <address>
#                             <name>test_adr5</name>
#                             <ip-prefix>10.1.0.0/24</ip-prefix>
#                             <description>test desc</description>
#                         </address>
#                         <address-set>
#                             <name>test_adrset1</name>
#                             <address>
#                                 <name>test_adr1</name>
#                             </address>
#                             <address>
#                                 <name>test_adr2</name>
#                             </address>
#                         </address-set>
#                         <address-set>
#                             <name>test_adrset2</name>
#                             <address>
#                                 <name>test_adr3</name>
#                             </address>
#                             <address>
#                                 <name>test_adr4</name>
#                             </address>
#                         </address-set>
#                         <address-set>
#                             <name>test_adrset3</name>
#                             <address>
#                                 <name>test_adr5</name>
#                             </address>
#                             <address-set>
#                                 <name>test_adrset1</name>
#                             </address-set>
#                             <address-set>
#                                 <name>test_adrset2</name>
#                             </address-set>
#                             <description>test description</description>
#                         </address-set>
#                     </address-book>
#                     <advance-policy-based-routing-profile>
#                         <profile>test_profile</profile>
#                     </advance-policy-based-routing-profile>
#                     <application-tracking />
#                     <description>test description</description>
#                     <enable-reverse-reroute />
#                     <host-inbound-traffic>
#                         <protocols>
#                             <name>all</name>
#                         </protocols>
#                         <protocols>
#                             <name>bgp</name>
#                             <except />
#                         </protocols>
#                         <system-services>
#                             <name>all</name>
#                         </system-services>
#                         <system-services>
#                             <name>dhcp</name>
#                             <except />
#                         </system-services>
#                     </host-inbound-traffic>
#                     <interfaces>
#                         <name>ge-0/0/3.0</name>
#                     </interfaces>
#                     <interfaces>
#                         <name>ge-0/0/4.0</name>
#                     </interfaces>
#                     <screen>test_screen</screen>
#                     <source-identity-log />
#                     <tcp-rst />
#                 </security-zone>
#             </zones>
#         </security>
#     </configuration>
# </rpc-reply>
#
- name: Parse security zones running config
  junipernetworks.junos.junos_security_zones:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#     "functional_zone_management": {
#         "description": "test description 2",
#         "host_inbound_traffic": {
#             "protocols": [{"name": "all"}, {"except": True, "name": "bgp"}, {"except": True, "name": "bfd"}],
#             "system_services": [{"name": "all"}, {"except": True, "name": "dhcp"}, {"except": True, "name": "dhcpv6"}],
#         },
#         "interfaces": ["ge-0/0/1.0", "ge-0/0/2.0"],
#         "screen": "test_screen",
#     },
#     "security_zones": [
#         {
#             "address_book": {
#                 "address_sets": [
#                     {"addresses": ["test_adr1", "test_adr2"], "name": "test_adrset1"},
#                     {"addresses": ["test_adr3", "test_adr4"], "name": "test_adrset2"},
#                     {
#                         "address_sets": ["test_adrset1", "test_adrset2"],
#                         "addresses": ["test_adr5"],
#                         "description": "test description",
#                         "name": "test_adrset3",
#                     },
#                 ],
#                 "addresses": [
#                     {"description": "test desc", "ip_prefix": "10.0.0.0/24", "name": "test_adr1"},
#                     {"dns_name": {"ipv6_only": True, "name": "1.1.1.1"}, "name": "test_adr2"},
#                     {"name": "test_adr3", "range_address": {"from": "10.2.0.1", "to": "10.2.0.2"}},
#                     {"name": "test_adr4", "wildcard_address": "10.3.0.1/24"},
#                     {"description": "test desc", "ip_prefix": "10.1.0.0/24", "name": "test_adr5"},
#                 ],
#             },
#             "advance_policy_based_routing_profile": "test_profile",
#             "application_tracking": True,
#             "description": "test description",
#             "enable_reverse_reroute": True,
#             "host_inbound_traffic": {
#                 "protocols": [{"name": "all"}, {"except": True, "name": "bgp"}],
#                 "system_services": [{"name": "all"}, {"except": True, "name": "dhcp"}],
#             },
#             "interfaces": ["ge-0/0/3.0", "ge-0/0/4.0"],
#             "name": "test_sec_zone1",
#             "screen": "test_screen",
#             "source_identity_log": True,
#             "tcp_rst": True,
#         },
#         {"name": "test_sec_zone2", "source_identity_log": True, "tcp_rst": True},
#     ],
# }
#
#
```

## [Return Values](junos_security_zones_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when state is *merged*, *replaced*, *overridden*, *deleted* or *purged*  **Sample:** `["<rpc-reply> <configuration> <security> <policies> <global> <policy> <name>test_glob_1</name> <match> <source-address>any-ipv6</source-address> <destination-address>any-ipv6</destination-address> <application>any</application> </match> <then> <deny /> </then> </policy> </global> </policies> </security> </configuration> </rpc-reply>"]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **parsed**  dictionary | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **rendered**  dictionary | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["<rpc-reply> <configuration> <security> <policies> <global> <policy> <name>test_glob_1</name> <match> <source-address>any-ipv6</source-address> <destination-address>any-ipv6</destination-address> <application>any</application> </match> <then> <deny /> </then> </policy> </global> </policies> </security> </configuration> </rpc-reply>"]` |

### Authors

- Pranav Bhatt (@pranav-bhatt)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
