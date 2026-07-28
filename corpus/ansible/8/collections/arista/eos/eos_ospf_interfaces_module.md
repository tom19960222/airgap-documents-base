---
collection: ansible
version: "8"
title: "arista.eos.eos_ospf_interfaces module – OSPF Interfaces Resource Module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_ospf_interfaces_module.html
fetched_at: 2026-07-28T01:11:10+00:00
---
# arista.eos.eos_ospf_interfaces module – OSPF Interfaces Resource Module.

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_ospf_interfaces`.

New in arista.eos 1.1.0

- [Synopsis](eos_ospf_interfaces_module.md#synopsis)
- [Parameters](eos_ospf_interfaces_module.md#parameters)
- [Examples](eos_ospf_interfaces_module.md#examples)
- [Return Values](eos_ospf_interfaces_module.md#return-values)

## [Synopsis](eos_ospf_interfaces_module.md#id1)

- This module manages OSPF configuration of interfaces on devices running Arista EOS.

Aliases: ospf_interfaces

## [Parameters](eos_ospf_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPF configuration for interfaces. |
| **address_family**  list / elements=dictionary | OSPF settings on the interfaces in address-family context. |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF settings on the interfaces.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **area**  dictionary | Area associated with interface.  Valid only when afi = ipv4. |
| **area_id**  string / required | Area ID as a decimal or IP address format. |
| **authentication_key**  dictionary | Configure the authentication key for the interface.  Valid only when afi = ipv4. |
| **encryption**  string | 0 Specifies an UNENCRYPTED authentication key will follow.  7 Specifies a proprietry encryption type.` |
| **key**  string | password (up to 8 chars). |
| **authentication_v2**  dictionary | Authentication settings on the interface.  Valid only when afi = ipv4. |
| **message_digest**  boolean | Use message-digest authentication.  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable authentication on the interface.  **Choices:**   - `false` - `true` |
| **authentication_v3**  dictionary | Authentication settings on the interface.  Valid only when afi = ipv6. |
| **algorithm**  string | Encryption alsgorithm.  **Choices:**   - `"md5"` - `"sha1"` |
| **key**  string | 128 bit MD5 key or 140 bit SHA1 key. |
| **keytype**  string | Specifies if an unencrypted/hidden follows.  0 denotes unencrypted key.  7 denotes hidden key. |
| **passphrase**  string | Passphrase String for deriving keys for authentication and encryption. |
| **spi**  integer | IPsec Security Parameter Index. |
| **bfd**  boolean | Enable BFD.  **Choices:**   - `false` - `true` |
| **cost**  integer | metric associated with interface. |
| **dead_interval**  integer | Time interval to detect a dead router. |
| **encryption_v3**  dictionary | Authentication settings on the interface.  Valid only when afi = ipv6. |
| **algorithm**  string | algorithm.  **Choices:**   - `"md5"` - `"sha1"` |
| **encryption**  string | encryption type.  **Choices:**   - `"3des-cbc"` - `"aes-128-cbc"` - `"aes-192-cbc"` - `"aes-256-cbc"` - `"null"` |
| **key**  string | key |
| **keytype**  string | Specifies if an unencrypted/hidden follows.  0 denotes unencrypted key.  7 denotes hidden key. |
| **passphrase**  string | Passphrase String for deriving keys for authentication and encryption. |
| **spi**  integer | IPsec Security Parameter Index. |
| **hello_interval**  integer | Timer interval between transmission of hello packets. |
| **ip_params**  list / elements=dictionary | Specify parameters for IPv4/IPv6.  Valid only when afi = ipv6. |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF settings on the interfaces.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **area**  dictionary | Area associated with interface.  Valid only when afi = ipv4. |
| **area_id**  string / required | Area ID as a decimal or IP address format. |
| **bfd**  boolean | Enable BFD.  **Choices:**   - `false` - `true` |
| **cost**  integer | metric associated with interface. |
| **dead_interval**  integer | Time interval to detect a dead router. |
| **hello_interval**  integer | Timer interval between transmission of hello packets. |
| **mtu_ignore**  boolean | if true, Disable MTU check for Database Description packets.  **Choices:**   - `false` - `true` |
| **network**  string | Interface type. |
| **passive_interface**  boolean | Suppress routing updates in an interface.  **Choices:**   - `false` - `true` |
| **priority**  integer | Interface priority. |
| **retransmit_interval**  integer | LSA retransmission interval. |
| **transmit_delay**  integer | LSA transmission delay. |
| **message_digest_key**  dictionary | Message digest authentication password (key) settings. |
| **encryption**  string | 0 Specifies an UNENCRYPTED ospf password (key) will follow.  7 Specifies a proprietry encryption type. |
| **key**  string | Authentication key (upto 16 chars). |
| **key_id**  integer | Key ID. |
| **mtu_ignore**  boolean | if true, Disable MTU check for Database Description packets.  **Choices:**   - `false` - `true` |
| **network**  string | Interface type. |
| **passive_interface**  boolean | Suppress routing updates in an interface.  Valid only when afi = ipv6.  **Choices:**   - `false` - `true` |
| **priority**  integer | Interface priority. |
| **retransmit_interval**  integer | LSA retransmission interval. |
| **shutdown**  boolean | Shutdown OSPF on this interface.  **Choices:**   - `false` - `true` |
| **transmit_delay**  integer | LSA transmission delay. |
| **name**  string | Name/Identifier of the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Examples](eos_ospf_interfaces_module.md#id3)

```yaml+jinja
# Using merged

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# veos(config)#

- name: Merge provided configuration with device configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv4"
            area:
              area_id: "0.0.0.50"
            cost: 500
            mtu_ignore: true
          - afi: "ipv6"
            dead_interval: 44
            ip_params:
              - afi: "ipv6"
                mtu_ignore: true
                network: "point-to-point"
    state: merged

# Task output:
# ------------
# before: []
#
# commands:
# - interface Vlan1
# - ip ospf area 0.0.0.50
# - ip ospf cost 500
# - ip ospf mtu-ignore
# - ospfv3 dead-interval 44
# - ospfv3 ipv6 mtu-ignore
# - ospfv3 ipv6 network point-to-point
#
# after:
#   - address_family:
#     - afi: ipv4
#       area:
#         area_id: 0.0.0.50
#       cost: 500
#       mtu_ignore: true
#     - afi: ipv6
#       dead_interval: 44
#       ip_params:
#       - afi: ipv6
#         mtu_ignore: true
#         network: point-to-point
#     name: Vlan1

# After state:
# ------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf cost 500
#    ip ospf mtu-ignore
#    ip ospf area 0.0.0.50
#    ospfv3 dead-interval 44
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore

# Using replaced

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf cost 500
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ip ospf area 0.0.0.50
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 dead-interval 44
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: Replace device configuration with provided configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv6"
            cost: 44
            bfd: true
            ip_params:
              - afi: "ipv6"
                mtu_ignore: true
                network: "point-to-point"
                dead_interval: 56
    state: replaced

# Task output:
# ------------
# before:
#   - address_family:
#     - afi: ipv4
#       area:
#         area_id: 0.0.0.50
#       cost: 500
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       cost: 106
#       dead_interval: 44
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2
#
# commands:
# - interface Vlan1
# - no ip ospf cost 500
# - no ip ospf dead-interval 29
# - no ip ospf hello-interval 66
# - no ip ospf mtu-ignore
# - no ip ospf area 0.0.0.50
# - ospfv3 cost 44
# - ospfv3 bfd
# - ospfv3 authentication ipsec spi 30 md5 passphrase 7 7hl8FV3lZ6H1mAKpjL47hQ==
# - no ospfv3 ipv4 priority 45
# - no ospfv3 ipv4 area 0.0.0.5
# - ospfv3 ipv6 dead-interval 56
# - no ospfv3 ipv6 passive-interface
# - no ospfv3 ipv6 retransmit-interval 115
# - no ospfv3 hello-interval 77
# - no ospfv3 dead-interval 44
# - no ospfv3 transmit-delay 100
#
# after:
#   - address_family:
#     - afi: ipv6
#       bfd: true
#       cost: 44
#       ip_params:
#       - afi: ipv6
#         mtu_ignore: true
#         network: point-to-point
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# After state:
# ------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ospfv3 bfd
#    ospfv3 cost 44
#    no ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

# Using overidden

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ospfv3 bfd
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: Override device configuration with provided configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv6"
            cost: 44
            bfd: true
            ip_params:
              - afi: "ipv6"
                mtu_ignore: true
                network: "point-to-point"
                dead_interval: 56
    state: overridden

# Task output:
# ------------
# before:
#   - address_family:
#     - afi: ipv4
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       bfd: true
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2
#
# commands:
# - interface Vlan2
# - no ospfv3 ipv4 hello-interval 45
# - no ospfv3 ipv4 retransmit-interval 100
# - no ospfv3 ipv4 area 0.0.0.6
# - interface Vlan1
# - no ip ospf dead-interval 29
# - no ip ospf hello-interval 66
# - no ip ospf mtu-ignore
# - ospfv3 cost 44
# - ospfv3 authentication ipsec spi 30 md5 passphrase 7 7hl8FV3lZ6H1mAKpjL47hQ==
# - no ospfv3 ipv4 priority 45
# - no ospfv3 ipv4 area 0.0.0.5
# - no ospfv3 ipv6 passive-interface
# - no ospfv3 ipv6 retransmit-interval 115
# - no ospfv3 hello-interval 77
# - no ospfv3 transmit-delay 100
#
# after:
#   - address_family:
#     - afi: ipv6
#       bfd: true
#       cost: 44
#       ip_params:
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#     name: Vlan1

# After state:
# ------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ospfv3 bfd
#    ospfv3 cost 44
#    no ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore

# Using deleted

# Before state:
# -------------
# veos(config)#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ospfv3 bfd
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: Delete provided ospf interface config
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
    state: deleted

# Task output:
# ------------
# before:
#   - address_family:
#     - afi: ipv4
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       bfd: true
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# commands:
# - interface Vlan1
# - no ip ospf dead-interval 29
# - no ip ospf hello-interval 66
# - no ip ospf mtu-ignore
# - no ospfv3 bfd
# - no ospfv3 cost 106
# - no ospfv3 hello-interval 77
# - no ospfv3 transmit-delay 100
# - no ospfv3 ipv4 priority 45
# - no ospfv3 ipv4 area 0.0.0.5
# - no ospfv3 ipv6 passive-interface
# - no ospfv3 ipv6 dead-interval 56
# - no ospfv3 ipv6 retransmit-interval 115
# - no ospfv3 ipv6 network point-to-point
# - no ospfv3 ipv6 mtu-ignore
#
# after:
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# After state:
# ------------
# veos#show running-config | section interface | ospf
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

# Using parsed

# parsed.cfg
# ----------
# interface Vlan1
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ip ospf cost 500
#    ospfv3 bfd
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6
#

- name: parse provided config into structured facts
  arista.eos.eos_ospf_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Task output:
# ------------
# parsed:
#   - address_family:
#     - afi: ipv4
#       cost: 500
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       bfd: true
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# Using gathered:

# Device config:
# veos#show running-config | section interface | ospf
# interface Vlan1
#    ip ospf cost 500
#    ip ospf dead-interval 29
#    ip ospf hello-interval 66
#    ip ospf mtu-ignore
#    ip ospf area 0.0.0.50
#    ospfv3 cost 106
#    ospfv3 hello-interval 77
#    ospfv3 transmit-delay 100
#    ospfv3 ipv4 priority 45
#    ospfv3 ipv4 area 0.0.0.5
#    ospfv3 ipv6 passive-interface
#    ospfv3 ipv6 dead-interval 56
#    ospfv3 ipv6 retransmit-interval 115
#    ospfv3 ipv6 network point-to-point
#    ospfv3 ipv6 mtu-ignore
# !
# interface Vlan2
#    ospfv3 ipv4 hello-interval 45
#    ospfv3 ipv4 retransmit-interval 100
#    ospfv3 ipv4 area 0.0.0.6

- name: gather runnig config
  arista.eos.eos_ospf_interfaces:
    state: gathered

# Task output:
# ------------
# gathered:
#   - address_family:
#     - afi: ipv4
#       area:
#         area_id: 0.0.0.50
#       cost: 500
#       dead_interval: 29
#       hello_interval: 66
#       mtu_ignore: true
#     - afi: ipv6
#       cost: 106
#       hello_interval: 77
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.5
#         priority: 45
#       - afi: ipv6
#         dead_interval: 56
#         mtu_ignore: true
#         network: point-to-point
#         passive_interface: true
#         retransmit_interval: 115
#       transmit_delay: 100
#     name: Vlan1
#   - address_family:
#     - afi: ipv6
#       ip_params:
#       - afi: ipv4
#         area:
#           area_id: 0.0.0.6
#         hello_interval: 45
#         retransmit_interval: 100
#     name: Vlan2

# Using rendered

- name: Render provided configuration
  arista.eos.eos_ospf_interfaces:
    config:
      - name: "Vlan1"
        address_family:
          - afi: "ipv4"
            dead_interval: 29
            mtu_ignore: true
            hello_interval: 66
          - afi: "ipv6"
            hello_interval: 77
            cost: 106
            transmit_delay: 100
            ip_params:
              - afi: "ipv6"
                retransmit_interval: 115
                dead_interval: 56
                passive_interface: true
              - afi: "ipv4"
                area:
                  area_id: "0.0.0.5"
                priority: 45
      - name: "Vlan2"
        address_family:
          - afi: "ipv6"
            ip_params:
              - afi: "ipv4"
                area:
                  area_id: "0.0.0.6"
                hello_interval: 45
                retransmit_interval: 100
          - afi: "ipv4"
            message_digest_key:
              key_id: 200
              encryption: 7
              key: "hkdfhtu=="

    state: rendered

# Task output:
# ------------
# rendered:
# - interface Vlan1
# - ip ospf dead-interval 29
# - ip ospf mtu-ignore
# - ip ospf hello-interval 66
# - ospfv3 hello-interval 77
# - ospfv3 cost 106
# - ospfv3 transmit-delay 100
# - ospfv3 ipv4 area 0.0.0.5
# - ospfv3 ipv4 priority 45
# - ospfv3 ipv6 retransmit-interval 115
# - ospfv3 ipv6 dead-interval 56
# - ospfv3 ipv6 passive-interface
# - interface Vlan2
# - ip ospf message-digest-key 200 md5 7 hkdfhtu==
# - ospfv3 ipv4 area 0.0.0.6
# - ospfv3 ipv4 hello-interval 45
# - ospfv3 ipv4 retransmit-interval 100
```

## [Return Values](eos_ospf_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **before**  list / elements=string | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["interface Vlan1", "ip ospf dead-interval 29", "ip ospf mtu-ignore"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["interface Vlan1", "ip ospf dead-interval 29", "ip ospf mtu-ignore"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
