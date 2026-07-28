---
collection: ansible
version: "8"
title: "ansible.netcommon.pop_ace filter – Remove ace entries from a acl source of truth."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/pop_ace_filter.html
fetched_at: 2026-07-28T01:09:21+00:00
---
# ansible.netcommon.pop_ace filter – Remove ace entries from a acl source of truth.

> **Note:**
>
> This filter plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.pop_ace`.

New in ansible.netcommon 5.1.0

- [Synopsis](pop_ace_filter.md#synopsis)
- [Keyword parameters](pop_ace_filter.md#keyword-parameters)
- [Notes](pop_ace_filter.md#notes)
- [Examples](pop_ace_filter.md#examples)

## [Synopsis](pop_ace_filter.md#id1)

- This plugin removes specific keys from a provided acl data.
- Using the parameters below - `acls_data | ansible.netcommon.pop_ace(filter_options=filter_options, match_criteria=match_criteria`)

## [Keyword parameters](pop_ace_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.pop_ace(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  any / required | This option represents a list of dictionaries of acls facts.  For example `acls_data | ansible.netcommon.pop_ace(filter_options=filter_options, match_criteria=match_criteria`), in this case `acls_data` represents this option. |
| **filter_options**  dictionary | Specify filtering options which drives the filter plugin. |
| **failed_when**  string | On missing it fails when there is no match with the ACL data supplied  On never it would never fail  **Choices:**   - `"missing"` ← (default) - `"never"` |
| **match_all**  boolean | When true ensures ace removed only when it matches all match criteria  **Choices:**   - `false` ← (default) - `true` |
| **remove**  string | Remove first removes one ace from each ACL entry on match  Remove all is more aggressive and removes more than one on match  **Choices:**   - `"first"` - `"all"` ← (default) |
| **match_criteria**  dictionary / required | Specify the matching configuration of the ACEs to remove. |
| **acl_name**  string | ACL name to match |
| **afi**  string / required | Specify afi to match |
| **destination**  string | Destination address/ host/ any of the ACE to natch |
| **grant**  string | Grant type permit or deny to match |
| **protocol**  string | Protocol name of the ACE to match |
| **sequence**  string | Sequence number of the ACE to match |
| **source**  string | Source address/ host/ any of the ACE to match |

## [Notes](pop_ace_filter.md#id3)

> **Note:**
>
> - The filter plugin has been tested with facts collected for acls resource module on Cisco IOSXE, IOSXR and NXOS.

## [Examples](pop_ace_filter.md#id4)

```yaml+jinja
##Playbook with filter plugin example
vars:
  filter_options:
    match_all: true
  match_criteria:
    afi: "ipv4"
    source: "192.0.2.0"
    destination: "192.0.3.0"
  acls_data:
    - acls:
        - aces:
            - destination:
                address: 192.0.3.0
                wildcard_bits: 0.0.0.255
              dscp: ef
              grant: deny
              protocol: icmp
              protocol_options:
                icmp:
                  traceroute: true
              sequence: 10
              source:
                address: 192.0.2.0
                wildcard_bits: 0.0.0.255
              ttl:
                eq: 10
            - destination:
                host: 198.51.110.0
                port_protocol:
                  eq: telnet
              grant: deny
              protocol: tcp
              protocol_options:
                tcp:
                  ack: true
              sequence: 20
              source:
                host: 198.51.100.0
          acl_type: extended
          name: "110"
        - aces:
            - destination:
                address: 198.51.101.0
                port_protocol:
                  eq: telnet
                wildcard_bits: 0.0.0.255
              grant: deny
              protocol: tcp
              protocol_options:
                tcp:
                  ack: true
              sequence: 10
              source:
                address: 198.51.100.0
                wildcard_bits: 0.0.0.255
              tos:
                service_value: 12
            - destination:
                address: 192.0.4.0
                port_protocol:
                  eq: www
                wildcard_bits: 0.0.0.255
              dscp: ef
              grant: deny
              protocol: tcp
              protocol_options:
                tcp:
                  ack: true
              sequence: 20
              source:
                address: 192.0.3.0
                wildcard_bits: 0.0.0.255
              ttl:
                lt: 20
          acl_type: extended
          name: "123"
        - aces:
            - grant: deny
              sequence: 10
              source:
                host: 192.168.1.200
            - grant: deny
              sequence: 20
              source:
                address: 192.168.2.0
                wildcard_bits: 0.0.0.255
          acl_type: standard
          name: std_acl
        - aces:
            - destination:
                address: 192.0.3.0
                port_protocol:
                  eq: www
                wildcard_bits: 0.0.0.255
              grant: deny
              option:
                traceroute: true
              protocol: tcp
              protocol_options:
                tcp:
                  fin: true
              sequence: 10
              source:
                address: 192.0.2.0
                wildcard_bits: 0.0.0.255
              ttl:
                eq: 10
          acl_type: extended
          name: test
      afi: ipv4
    - acls:
        - aces:
            - destination:
                any: true
                port_protocol:
                  eq: telnet
              dscp: af11
              grant: deny
              protocol: tcp
              protocol_options:
                tcp:
                  ack: true
              sequence: 10
              source:
                any: true
                port_protocol:
                  eq: www
          name: R1_TRAFFIC
      afi: ipv6

tasks:
  - name: Remove ace entries from a provided data
    ansible.builtin.debug:
      msg: "{{ acls_data | ansible.netcommon.pop_ace(filter_options=filter_options, match_criteria=match_criteria) }}"

##Output
# PLAY [Filter plugin example pop_ace] ******************************************************************************************************************

# TASK [Remove ace entries from a provided data] ***********************************************************************************************************
# ok: [xe_machine] =>
#   msg:
#     clean_acls:
#       acls:
#       - acls:
#         - aces:
#           - destination:
#               host: 198.51.110.0
#               port_protocol:
#                 eq: telnet
#             grant: deny
#             protocol: tcp
#             protocol_options:
#               tcp:
#                 ack: true
#             sequence: 20
#             source:
#               host: 198.51.100.0
#           name: '110'
#         - aces:
#           - destination:
#               address: 198.51.101.0
#               port_protocol:
#                 eq: telnet
#               wildcard_bits: 0.0.0.255
#             grant: deny
#             protocol: tcp
#             protocol_options:
#               tcp:
#                 ack: true
#             sequence: 10
#             source:
#               address: 198.51.100.0
#               wildcard_bits: 0.0.0.255
#             tos:
#               service_value: 12
#           - destination:
#               address: 192.0.4.0
#               port_protocol:
#                 eq: www
#               wildcard_bits: 0.0.0.255
#             dscp: ef
#             grant: deny
#             protocol: tcp
#             protocol_options:
#               tcp:
#                 ack: true
#             sequence: 20
#             source:
#               address: 192.0.3.0
#               wildcard_bits: 0.0.0.255
#             ttl:
#               lt: 20
#           name: '123'
#         - aces:
#           - grant: deny
#             sequence: 10
#             source:
#               host: 192.168.1.200
#           - grant: deny
#             sequence: 20
#             source:
#               address: 192.168.2.0
#               wildcard_bits: 0.0.0.255
#           name: std_acl
#         afi: ipv4
#       - acls:
#         - aces:
#           - destination:
#               any: true
#               port_protocol:
#                 eq: telnet
#             dscp: af11
#             grant: deny
#             protocol: tcp
#             protocol_options:
#               tcp:
#                 ack: true
#             sequence: 10
#             source:
#               any: true
#               port_protocol:
#                 eq: www
#           name: R1_TRAFFIC
#         afi: ipv6
#     removed_aces:
#       acls:
#       - acls:
#         - aces:
#           - destination:
#               address: 192.0.3.0
#               wildcard_bits: 0.0.0.255
#             dscp: ef
#             grant: deny
#             protocol: icmp
#             protocol_options:
#               icmp:
#                 traceroute: true
#             sequence: 10
#             source:
#               address: 192.0.2.0
#               wildcard_bits: 0.0.0.255
#             ttl:
#               eq: 10
#           name: '110'
#         - aces:
#           - destination:
#               address: 192.0.3.0
#               port_protocol:
#                 eq: www
#               wildcard_bits: 0.0.0.255
#             grant: deny
#             option:
#               traceroute: true
#             protocol: tcp
#             protocol_options:
#               tcp:
#                 fin: true
#             sequence: 10
#             source:
#               address: 192.0.2.0
#               wildcard_bits: 0.0.0.255
#             ttl:
#               eq: 10
#           name: test
#         afi: ipv4
#       - acls: []
#         afi: ipv6

##Playbook with workflow example
tasks:
  - name: Gather ACLs config from device existing ACLs config
    cisco.ios.ios_acls:
      state: gathered
    register: result_gathered

  - name: Setting host facts for pop_ace filter plugin
    ansible.builtin.set_fact:
      acls_facts: "{{ result_gathered.gathered }}"
      filter_options:
        match_all: true
      match_criteria:
        afi: "ipv4"
        source: "192.0.2.0"
        destination: "192.0.3.0"

  - name: Invoke pop_ace filter plugin
    ansible.builtin.set_fact:
      clean_acls: "{{ acls_facts | ansible.netcommon.pop_ace(filter_options=filter_options, match_criteria=match_criteria) }}"

  - name: Override ACLs config with device existing ACLs config
    cisco.ios.ios_acls:
      state: overridden
      config: "{{ clean_acls['clean_acls']['acls'] | from_yaml }}"

##Output

# PLAYBOOK: pop_ace_example.yml ***********************************************

# PLAY [Filter plugin example pop_ace] ****************************************

# TASK [Gather ACLs config with device existing ACLs config] *********************
# ok: [xe_machine] => changed=false
#   gathered:
#   - acls:
#     - aces:
#       - destination:
#           address: 192.0.3.0
#           wildcard_bits: 0.0.0.255
#         dscp: ef
#         grant: deny
#         protocol: icmp
#         protocol_options:
#           icmp:
#             traceroute: true
#         sequence: 10
#         source:
#           address: 192.0.2.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           eq: 10
#       - destination:
#           host: 198.51.110.0
#           port_protocol:
#             eq: telnet
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 20
#         source:
#           host: 198.51.100.0
#       acl_type: extended
#       name: '110'
#     - aces:
#       - destination:
#           address: 198.51.101.0
#           port_protocol:
#             eq: telnet
#           wildcard_bits: 0.0.0.255
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 10
#         source:
#           address: 198.51.100.0
#           wildcard_bits: 0.0.0.255
#         tos:
#           service_value: 12
#       - destination:
#           address: 192.0.4.0
#           port_protocol:
#             eq: www
#           wildcard_bits: 0.0.0.255
#         dscp: ef
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 20
#         source:
#           address: 192.0.3.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           lt: 20
#       acl_type: extended
#       name: '123'
#     - aces:
#       - grant: deny
#         sequence: 10
#         source:
#           host: 192.168.1.200
#       - grant: deny
#         sequence: 20
#         source:
#           address: 192.168.2.0
#           wildcard_bits: 0.0.0.255
#       acl_type: standard
#       name: std_acl
#     - aces:
#       - destination:
#           address: 192.0.3.0
#           port_protocol:
#             eq: www
#           wildcard_bits: 0.0.0.255
#         grant: deny
#         option:
#           traceroute: true
#         protocol: tcp
#         protocol_options:
#           tcp:
#             fin: true
#         sequence: 10
#         source:
#           address: 192.0.2.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           eq: 10
#       acl_type: extended
#       name: test
#     afi: ipv4
#   - acls:
#     - aces:
#       - destination:
#           any: true
#           port_protocol:
#             eq: telnet
#         dscp: af11
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 10
#         source:
#           any: true
#           port_protocol:
#             eq: www
#       name: R1_TRAFFIC
#     afi: ipv6
#   invocation:
#     module_args:
#       config: null
#       running_config: null
#       state: gathered

# TASK [Setting host facts for pop_ace filter plugin] *************************
# ok: [xe_machine] => changed=false
#   ansible_facts:
#     acls_facts:
#     - acls:
#       - aces:
#         - destination:
#             address: 192.0.3.0
#             wildcard_bits: 0.0.0.255
#           dscp: ef
#           grant: deny
#           protocol: icmp
#           protocol_options:
#             icmp:
#               traceroute: true
#           sequence: 10
#           source:
#             address: 192.0.2.0
#             wildcard_bits: 0.0.0.255
#           ttl:
#             eq: 10
#         - destination:
#             host: 198.51.110.0
#             port_protocol:
#               eq: telnet
#           grant: deny
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#           sequence: 20
#           source:
#             host: 198.51.100.0
#         acl_type: extended
#         name: '110'
#       - aces:
#         - destination:
#             address: 198.51.101.0
#             port_protocol:
#               eq: telnet
#             wildcard_bits: 0.0.0.255
#           grant: deny
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#           sequence: 10
#           source:
#             address: 198.51.100.0
#             wildcard_bits: 0.0.0.255
#           tos:
#             service_value: 12
#         - destination:
#             address: 192.0.4.0
#             port_protocol:
#               eq: www
#             wildcard_bits: 0.0.0.255
#           dscp: ef
#           grant: deny
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#           sequence: 20
#           source:
#             address: 192.0.3.0
#             wildcard_bits: 0.0.0.255
#           ttl:
#             lt: 20
#         acl_type: extended
#         name: '123'
#       - aces:
#         - grant: deny
#           sequence: 10
#           source:
#             host: 192.168.1.200
#         - grant: deny
#           sequence: 20
#           source:
#             address: 192.168.2.0
#             wildcard_bits: 0.0.0.255
#         acl_type: standard
#         name: std_acl
#       - aces:
#         - destination:
#             address: 192.0.3.0
#             port_protocol:
#               eq: www
#             wildcard_bits: 0.0.0.255
#           grant: deny
#           option:
#             traceroute: true
#           protocol: tcp
#           protocol_options:
#             tcp:
#               fin: true
#           sequence: 10
#           source:
#             address: 192.0.2.0
#             wildcard_bits: 0.0.0.255
#           ttl:
#             eq: 10
#         acl_type: extended
#         name: test
#       afi: ipv4
#     - acls:
#       - aces:
#         - destination:
#             any: true
#             port_protocol:
#               eq: telnet
#           dscp: af11
#           grant: deny
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#           sequence: 10
#           source:
#             any: true
#             port_protocol:
#               eq: www
#         name: R1_TRAFFIC
#       afi: ipv6
#     filter_options:
#       match_all: true
#     match_criteria:
#       afi: ipv4
#       destination: 192.0.3.0
#       source: 192.0.2.0

# TASK [Invoke pop_ace filter plugin] *****************************************
# ok: [xe_machine] => changed=false
#   ansible_facts:
#     clean_acls:
#       clean_acls:
#         acls:
#         - acls:
#           - aces:
#             - destination:
#                 host: 198.51.110.0
#                 port_protocol:
#                   eq: telnet
#               grant: deny
#               protocol: tcp
#               protocol_options:
#                 tcp:
#                   ack: true
#               sequence: 20
#               source:
#                 host: 198.51.100.0
#             name: '110'
#           - aces:
#             - destination:
#                 address: 198.51.101.0
#                 port_protocol:
#                   eq: telnet
#                 wildcard_bits: 0.0.0.255
#               grant: deny
#               protocol: tcp
#               protocol_options:
#                 tcp:
#                   ack: true
#               sequence: 10
#               source:
#                 address: 198.51.100.0
#                 wildcard_bits: 0.0.0.255
#               tos:
#                 service_value: 12
#             - destination:
#                 address: 192.0.4.0
#                 port_protocol:
#                   eq: www
#                 wildcard_bits: 0.0.0.255
#               dscp: ef
#               grant: deny
#               protocol: tcp
#               protocol_options:
#                 tcp:
#                   ack: true
#               sequence: 20
#               source:
#                 address: 192.0.3.0
#                 wildcard_bits: 0.0.0.255
#               ttl:
#                 lt: 20
#             name: '123'
#           - aces:
#             - grant: deny
#               sequence: 10
#               source:
#                 host: 192.168.1.200
#             - grant: deny
#               sequence: 20
#               source:
#                 address: 192.168.2.0
#                 wildcard_bits: 0.0.0.255
#             name: std_acl
#           afi: ipv4
#         - acls:
#           - aces:
#             - destination:
#                 any: true
#                 port_protocol:
#                   eq: telnet
#               dscp: af11
#               grant: deny
#               protocol: tcp
#               protocol_options:
#                 tcp:
#                   ack: true
#               sequence: 10
#               source:
#                 any: true
#                 port_protocol:
#                   eq: www
#             name: R1_TRAFFIC
#           afi: ipv6
#       removed_aces:
#         acls:
#         - acls:
#           - aces:
#             - destination:
#                 address: 192.0.3.0
#                 wildcard_bits: 0.0.0.255
#               dscp: ef
#               grant: deny
#               protocol: icmp
#               protocol_options:
#                 icmp:
#                   traceroute: true
#               sequence: 10
#               source:
#                 address: 192.0.2.0
#                 wildcard_bits: 0.0.0.255
#               ttl:
#                 eq: 10
#             name: '110'
#           - aces:
#             - destination:
#                 address: 192.0.3.0
#                 port_protocol:
#                   eq: www
#                 wildcard_bits: 0.0.0.255
#               grant: deny
#               option:
#                 traceroute: true
#               protocol: tcp
#               protocol_options:
#                 tcp:
#                   fin: true
#               sequence: 10
#               source:
#                 address: 192.0.2.0
#                 wildcard_bits: 0.0.0.255
#               ttl:
#                 eq: 10
#             name: test
#           afi: ipv4
#         - acls: []
#           afi: ipv6

# TASK [Override ACLs config with device existing ACLs config] *******************
# changed: [xe_machine] => changed=true
#   after:
#   - acls:
#     - aces:
#       - destination:
#           host: 198.51.110.0
#           port_protocol:
#             eq: telnet
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 20
#         source:
#           host: 198.51.100.0
#       acl_type: extended
#       name: '110'
#     - aces:
#       - destination:
#           address: 198.51.101.0
#           port_protocol:
#             eq: telnet
#           wildcard_bits: 0.0.0.255
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 10
#         source:
#           address: 198.51.100.0
#           wildcard_bits: 0.0.0.255
#         tos:
#           service_value: 12
#       - destination:
#           address: 192.0.4.0
#           port_protocol:
#             eq: www
#           wildcard_bits: 0.0.0.255
#         dscp: ef
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 20
#         source:
#           address: 192.0.3.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           lt: 20
#       acl_type: extended
#       name: '123'
#     - aces:
#       - grant: deny
#         sequence: 10
#         source:
#           host: 192.168.1.200
#       - grant: deny
#         sequence: 20
#         source:
#           address: 192.168.2.0
#           wildcard_bits: 0.0.0.255
#       acl_type: standard
#       name: std_acl
#     afi: ipv4
#   - acls:
#     - aces:
#       - destination:
#           any: true
#           port_protocol:
#             eq: telnet
#         dscp: af11
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 10
#         source:
#           any: true
#           port_protocol:
#             eq: www
#       name: R1_TRAFFIC
#     afi: ipv6
#   before:
#   - acls:
#     - aces:
#       - destination:
#           address: 192.0.3.0
#           wildcard_bits: 0.0.0.255
#         dscp: ef
#         grant: deny
#         protocol: icmp
#         protocol_options:
#           icmp:
#             traceroute: true
#         sequence: 10
#         source:
#           address: 192.0.2.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           eq: 10
#       - destination:
#           host: 198.51.110.0
#           port_protocol:
#             eq: telnet
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 20
#         source:
#           host: 198.51.100.0
#       acl_type: extended
#       name: '110'
#     - aces:
#       - destination:
#           address: 198.51.101.0
#           port_protocol:
#             eq: telnet
#           wildcard_bits: 0.0.0.255
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 10
#         source:
#           address: 198.51.100.0
#           wildcard_bits: 0.0.0.255
#         tos:
#           service_value: 12
#       - destination:
#           address: 192.0.4.0
#           port_protocol:
#             eq: www
#           wildcard_bits: 0.0.0.255
#         dscp: ef
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 20
#         source:
#           address: 192.0.3.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           lt: 20
#       acl_type: extended
#       name: '123'
#     - aces:
#       - grant: deny
#         sequence: 10
#         source:
#           host: 192.168.1.200
#       - grant: deny
#         sequence: 20
#         source:
#           address: 192.168.2.0
#           wildcard_bits: 0.0.0.255
#       acl_type: standard
#       name: std_acl
#     - aces:
#       - destination:
#           address: 192.0.3.0
#           port_protocol:
#             eq: www
#           wildcard_bits: 0.0.0.255
#         grant: deny
#         option:
#           traceroute: true
#         protocol: tcp
#         protocol_options:
#           tcp:
#             fin: true
#         sequence: 10
#         source:
#           address: 192.0.2.0
#           wildcard_bits: 0.0.0.255
#         ttl:
#           eq: 10
#       acl_type: extended
#       name: test
#     afi: ipv4
#   - acls:
#     - aces:
#       - destination:
#           any: true
#           port_protocol:
#             eq: telnet
#         dscp: af11
#         grant: deny
#         protocol: tcp
#         protocol_options:
#           tcp:
#             ack: true
#         sequence: 10
#         source:
#           any: true
#           port_protocol:
#             eq: www
#       name: R1_TRAFFIC
#     afi: ipv6
#   commands:
#   - ip access-list extended 110
#   - no 10 deny icmp 192.0.2.0 0.0.0.255 192.0.3.0 0.0.0.255 traceroute dscp ef ttl eq 10
#   - no ip access-list extended test
```

### Authors

- Sagar Paul (@KB-perByte)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
