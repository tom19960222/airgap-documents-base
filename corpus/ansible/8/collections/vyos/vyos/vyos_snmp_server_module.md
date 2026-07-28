---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_snmp_server module – Manages snmp_server resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_snmp_server_module.html
fetched_at: 2026-07-28T02:59:25+00:00
---
# vyos.vyos.vyos_snmp_server module – Manages snmp_server resource module

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_snmp_server`.

New in vyos.vyos 2.7.0

- [Synopsis](vyos_snmp_server_module.md#synopsis)
- [Parameters](vyos_snmp_server_module.md#parameters)
- [Notes](vyos_snmp_server_module.md#notes)
- [Examples](vyos_snmp_server_module.md#examples)
- [Return Values](vyos_snmp_server_module.md#return-values)

## [Synopsis](vyos_snmp_server_module.md#id1)

- This module manages the snmp server attributes of Vyos network devices

## [Parameters](vyos_snmp_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | SNMP server configuration. |
| **communities**  list / elements=dictionary | Community name configuration. |
| **authorization_type**  string | Authorization type (rw or ro)  **Choices:**   - `"ro"` - `"rw"` |
| **clients**  list / elements=string | IP address of SNMP client allowed to contact system |
| **name**  string | Community name |
| **networks**  list / elements=string | Subnet of SNMP client(s) allowed to contact system |
| **contact**  string | Person to contact about the system. |
| **description**  string | Description information |
| **listen_addresses**  list / elements=dictionary | IP address to listen for incoming SNMP requests |
| **address**  string | IP address to listen for incoming SNMP requests. |
| **port**  integer | Port for SNMP service |
| **location**  string | Location information |
| **smux_peer**  string | Register a subtree for SMUX-based processing. |
| **snmp_v3**  dictionary | Simple Network Management Protocol (SNMP) v3 |
| **engine_id**  string | Specifies the EngineID as a hex value |
| **groups**  list / elements=dictionary | Specifies the group with name groupname |
| **group**  string | Specifies the group with name groupname |
| **mode**  string | Defines the read/write access  **Choices:**   - `"ro"` - `"rw"` |
| **seclevel**  string | Defines security level  **Choices:**   - `"auth"` - `"priv"` |
| **view**  string | Defines the name of view |
| **trap_targets**  list / elements=dictionary | Defines SNMP target for inform or traps for IP |
| **address**  string | IP/IPv6 address of trap target |
| **authentication**  dictionary | Defines the authentication |
| **encrypted_key**  string | Defines the encrypted password for authentication |
| **plaintext_key**  string | Defines the clear text password for authentication |
| **type**  string | Defines the protocol using for authentication  **Choices:**   - `"md5"` - `"sha"` |
| **engine_id**  string | Defines the engineID. |
| **port**  integer | Specifies the TCP/UDP port of a destination for SNMP traps/informs. |
| **privacy**  dictionary | Defines the privacy |
| **encrypted_key**  string | Defines the encrypted password for privacy |
| **plaintext_key**  string | Defines the clear text password for privacy |
| **type**  string | Defines the protocol using for privacy  **Choices:**   - `"des"` - `"aes"` |
| **protocol**  string | Defines protocol for notification between TCP and UDP  **Choices:**   - `"tcp"` - `"udp"` |
| **type**  string | Specifies the type of notification between inform and trap  **Choices:**   - `"inform"` - `"trap"` |
| **tsm**  dictionary | Specifies that the snmpd uses encryption |
| **local_key**  string | Defines the server certificate fingerprint or key-file name. |
| **port**  integer | Defines the port for tsm. |
| **users**  list / elements=dictionary | Defines username for authentication |
| **authentication**  dictionary | Defines the authentication |
| **encrypted_key**  string | Defines the encrypted password for authentication |
| **plaintext_key**  string | Defines the clear text password for authentication |
| **type**  string | Defines the protocol using for authentication  **Choices:**   - `"md5"` - `"sha"` |
| **engine_id**  string | Defines the engineID. |
| **group**  string | Specifies group for user name |
| **mode**  string | Specifies the mode for access rights of user, read only or write  **Choices:**   - `"ro"` - `"rw"` |
| **privacy**  dictionary | Defines the privacy |
| **encrypted_key**  string | Defines the encrypted password for privacy |
| **plaintext_key**  string | Defines the clear text password for privacy |
| **type**  string | Defines the protocol using for privacy  **Choices:**   - `"des"` - `"aes"` |
| **tsm_key**  string | Specifies finger print or file name of TSM certificate. |
| **user**  string | Specifies the user with name username |
| **views**  list / elements=dictionary | Specifies the view with name viewname |
| **exclude**  string | Exclude is optional argument. |
| **mask**  string | Defines a bit-mask that is indicating which subidentifiers of the associated subtree OID should be regarded as significant. |
| **oid**  string | Specify oid |
| **view**  string | view name |
| **trap_source**  string | SNMP trap source address |
| **trap_target**  dictionary | Address of trap target |
| **address**  string | Address of trap target |
| **community**  string | Community used when sending trap information |
| **port**  integer | Destination port used for trap notification |
| **running_config**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Please refer to examples for more details. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](vyos_snmp_server_module.md#id3)

> **Note:**
>
> - Tested against vyos 1.1.8
> - This module works with connection `network_cli`.
> - The Configuration defaults of the Vyos network devices are supposed to hinder idempotent behavior of plays

## [Examples](vyos_snmp_server_module.md#id4)

```yaml+jinja
# Using merged
# Before State:

# vyos@vyos:~$ show configuration commands | grep snmp
# vyos@vyos:~$

  - name: Merge provided configuration with device configuration
    vyos.vyos.vyos_snmp_server:
      config:
        communities:
          - name: "switches"
            authorization_type: "rw"
          - name: "bridges"
            clients: ["1.1.1.1", "12.1.1.10"]
        contact: "admin2@ex.com"
        listen_addresses:
          - address: "20.1.1.1"
          - address: "100.1.2.1"
            port: 33
        snmp_v3:
          users:
            - user: admin_user
              authentication:
                plaintext_key: "abc1234567"
                type: "sha"
              privacy:
                plaintext_key: "abc1234567"
                type: "aes"

      state: merged

# After State:

# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges client '1.1.1.1'
# set service snmp community bridges client '12.1.1.10'
# set service snmp community switches authorization 'rw'
# set service snmp contact 'admin2@ex.com'
# set service snmp listen-address 20.1.1.1
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# vyos@vyos:~$
#
# Module Execution:
#
# "after": {
#         "communities": [
#             {
#                 "clients": [
#                     "1.1.1.1",
#                     "12.1.1.10"
#                 ],
#                 "name": "bridges"
#             },
#             {
#                 "authorization_type": "rw",
#                 "name": "switches"
#             }
#         ],
#         "contact": "admin2@ex.com",
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             },
#             {
#                 "address": "20.1.1.1"
#             }
#         ],
#         "snmp_v3": {
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 }
#             ]
#         }
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "set service snmp community switches authorization rw",
#         "set service snmp community bridges client 1.1.1.1",
#         "set service snmp community bridges client 12.1.1.10",
#         "set service snmp listen-address 20.1.1.1",
#         "set service snmp listen-address 100.1.2.1 port 33",
#         "set service snmp v3 user admin_user auth type sha",
#         "set service snmp v3 user admin_user auth plaintext-key ********",
#         "set service snmp v3 user admin_user privacy type aes",
#         "set service snmp v3 user admin_user privacy plaintext-key ********",
#         "set service snmp contact admin2@ex.com"
#     ],
#

# using Replaced:

# Before State
# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges client '1.1.1.1'
# set service snmp community bridges client '12.1.1.10'
# set service snmp community switches authorization 'rw'
# set service snmp contact 'admin2@ex.com'
# set service snmp listen-address 20.1.1.1
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# vyos@vyos:~$

  - name: Replace
    vyos.vyos.vyos_snmp_server:
      config:
        communities:
          - name: "bridges"
            networks: ["1.1.1.0/24", "12.1.1.0/24"]
        location: "RDU, NC"
        listen_addresses:
          - address: "100.1.2.1"
            port: 33
        snmp_v3:
          groups:
            - group: "default"
              view: "default"
          users:
            - user: admin_user
              authentication:
                plaintext_key: "abc1234567"
                type: "sha"
              privacy:
                plaintext_key: "abc1234567"
                type: "aes"
              group: "default"
            - user: guest_user2
              authentication:
                plaintext_key: "opq1234567"
                type: "sha"
              privacy:
                plaintext_key: "opq1234567"
                type: "aes"
          views:
            - view: "default"
              oid: 1

      state: replaced

# After State:
# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges network '1.1.1.0/24'
# set service snmp community bridges network '12.1.1.0/24'
# set service snmp community switches
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp location 'RDU, NC'
# set service snmp v3 group default view 'default'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user group 'default'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# set service snmp v3 user guest_user2 auth plaintext-key 'opq1234567'
# set service snmp v3 user guest_user2 auth type 'sha'
# set service snmp v3 user guest_user2 privacy plaintext-key 'opq1234567'
# set service snmp v3 user guest_user2 privacy type 'aes'
# set service snmp v3 view default oid 1
# vyos@vyos:~$
#
#
# Module Execution:
# "after": {
#         "communities": [
#             {
#                 "name": "bridges",
#                 "networks": [
#                     "1.1.1.0/24",
#                     "12.1.1.0/24"
#                 ]
#             },
#             {
#                 "name": "switches"
#             }
#         ],
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             }
#         ],
#         "location": "RDU, NC",
#         "snmp_v3": {
#             "groups": [
#                 {
#                     "group": "default",
#                     "view": "default"
#                 }
#             ],
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "group": "default",
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 },
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "guest_user2"
#                 }
#             ],
#             "views": [
#                 {
#                     "oid": "1",
#                     "view": "default"
#                 }
#             ]
#         }
#     },
#     "before": {
#         "communities": [
#             {
#                 "clients": [
#                     "1.1.1.1",
#                     "12.1.1.10"
#                 ],
#                 "name": "bridges"
#             },
#             {
#                 "authorization_type": "rw",
#                 "name": "switches"
#             }
#         ],
#         "contact": "admin2@ex.com",
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             },
#             {
#                 "address": "20.1.1.1"
#             }
#         ],
#         "snmp_v3": {
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 }
#             ]
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete service snmp contact admin2@ex.com",
#         "delete service snmp listen-address 20.1.1.1",
#         "delete service snmp community switches authorization rw",
#         "delete service snmp community bridges client 12.1.1.10",
#         "delete service snmp community bridges client 1.1.1.1",
#         "set service snmp community bridges network 1.1.1.0/24",
#         "set service snmp community bridges network 12.1.1.0/24",
#         "set service snmp v3 group default view default",
#         "set service snmp v3 user admin_user group default",
#         "set service snmp v3 user guest_user2 auth type sha",
#         "set service snmp v3 user guest_user2 auth plaintext-key ********",
#         "set service snmp v3 user guest_user2 privacy type aes",
#         "set service snmp v3 user guest_user2 privacy plaintext-key ********",
#         "set service snmp v3 view default oid 1",
#         "set service snmp location 'RDU, NC'"
#     ],

# Using overridden:
# Before State
# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges client '1.1.1.1'
# set service snmp community bridges client '12.1.1.10'
# set service snmp community switches authorization 'rw'
# set service snmp contact 'admin2@ex.com'
# set service snmp listen-address 20.1.1.1
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# vyos@vyos:~$

  - name: Override config
    vyos.vyos.vyos_snmp_server:
      config:
        communities:
          - name: "bridges"
            networks: ["1.1.1.0/24", "12.1.1.0/24"]
        location: "RDU, NC"
        listen_addresses:
          - address: "100.1.2.1"
            port: 33
        snmp_v3:
          groups:
            - group: "default"
              view: "default"
          users:
            - user: admin_user
              authentication:
                plaintext_key: "abc1234567"
                type: "sha"
              privacy:
                plaintext_key: "abc1234567"
                type: "aes"
              group: "default"
            - user: guest_user2
              authentication:
                plaintext_key: "opq1234567"
                type: "sha"
              privacy:
                plaintext_key: "opq1234567"
                type: "aes"
          views:
            - view: "default"
              oid: 1

      state: overridden

# After State:
# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges network '1.1.1.0/24'
# set service snmp community bridges network '12.1.1.0/24'
# set service snmp community switches
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp location 'RDU, NC'
# set service snmp v3 group default view 'default'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user group 'default'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# set service snmp v3 user guest_user2 auth plaintext-key 'opq1234567'
# set service snmp v3 user guest_user2 auth type 'sha'
# set service snmp v3 user guest_user2 privacy plaintext-key 'opq1234567'
# set service snmp v3 user guest_user2 privacy type 'aes'
# set service snmp v3 view default oid 1
# vyos@vyos:~$
#
#
# Module Execution:
# "after": {
#         "communities": [
#             {
#                 "name": "bridges",
#                 "networks": [
#                     "1.1.1.0/24",
#                     "12.1.1.0/24"
#                 ]
#             },
#             {
#                 "name": "switches"
#             }
#         ],
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             }
#         ],
#         "location": "RDU, NC",
#         "snmp_v3": {
#             "groups": [
#                 {
#                     "group": "default",
#                     "view": "default"
#                 }
#             ],
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "group": "default",
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 },
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "guest_user2"
#                 }
#             ],
#             "views": [
#                 {
#                     "oid": "1",
#                     "view": "default"
#                 }
#             ]
#         }
#     },
#     "before": {
#         "communities": [
#             {
#                 "clients": [
#                     "1.1.1.1",
#                     "12.1.1.10"
#                 ],
#                 "name": "bridges"
#             },
#             {
#                 "authorization_type": "rw",
#                 "name": "switches"
#             }
#         ],
#         "contact": "admin2@ex.com",
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             },
#             {
#                 "address": "20.1.1.1"
#             }
#         ],
#         "snmp_v3": {
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 }
#             ]
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete service snmp contact admin2@ex.com",
#         "delete service snmp listen-address 20.1.1.1",
#         "delete service snmp community switches authorization rw",
#         "delete service snmp community bridges client 12.1.1.10",
#         "delete service snmp community bridges client 1.1.1.1",
#         "set service snmp community bridges network 1.1.1.0/24",
#         "set service snmp community bridges network 12.1.1.0/24",
#         "set service snmp v3 group default view default",
#         "set service snmp v3 user admin_user group default",
#         "set service snmp v3 user guest_user2 auth type sha",
#         "set service snmp v3 user guest_user2 auth plaintext-key ********",
#         "set service snmp v3 user guest_user2 privacy type aes",
#         "set service snmp v3 user guest_user2 privacy plaintext-key ********",
#         "set service snmp v3 view default oid 1",
#         "set service snmp location 'RDU, NC'"
#     ],

# Using deleted:

# Before State:
# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges network '1.1.1.0/24'
# set service snmp community bridges network '12.1.1.0/24'
# set service snmp community switches
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp location 'RDU, NC'
# set service snmp v3 group default view 'default'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user group 'default'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# set service snmp v3 user guest_user2 auth plaintext-key 'opq1234567'
# set service snmp v3 user guest_user2 auth type 'sha'
# set service snmp v3 user guest_user2 privacy plaintext-key 'opq1234567'
# set service snmp v3 user guest_user2 privacy type 'aes'
# set service snmp v3 view default oid 1
# vyos@vyos:~$

  - name: Delete Config
    vyos.vyos.vyos_snmp_server:
      state: deleted

# After State:
# vyos@vyos:~$ show configuration commands | grep snmp
# vyos@vyos:~$
#
# Module Execution:
# "after": {},
#     "before": {
#         "communities": [
#             {
#                 "name": "bridges",
#                 "networks": [
#                     "1.1.1.0/24",
#                     "12.1.1.0/24"
#                 ]
#             },
#             {
#                 "name": "switches"
#             }
#         ],
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             }
#         ],
#         "location": "RDU, NC",
#         "snmp_v3": {
#             "groups": [
#                 {
#                     "group": "default",
#                     "view": "default"
#                 }
#             ],
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "group": "default",
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 },
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "guest_user2"
#                 }
#             ],
#             "views": [
#                 {
#                     "oid": "1",
#                     "view": "default"
#                 }
#             ]
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete service snmp"
#     ],

# Using rendered:
  - name: Render provided configuration
    vyos.vyos.vyos_snmp_server:
      config:
        communities:
          - name: "switches"
            authorization_type: "rw"
          - name: "bridges"
            clients: ["1.1.1.1", "12.1.1.10"]
        contact: "admin2@ex.com"
        listen_addresses:
          - address: "20.1.1.1"
          - address: "100.1.2.1"
            port: 33
        snmp_v3:
          users:
            - user: admin_user
              authentication:
                plaintext_key: "abc1234567"
                type: "sha"
              privacy:
                plaintext_key: "abc1234567"
                type: "aes"

      state: rendered

# Module Execution:
#  "rendered": [
#         "set service snmp community switches authorization rw",
#         "set service snmp community bridges client 1.1.1.1",
#         "set service snmp community bridges client 12.1.1.10",
#         "set service snmp listen-address 20.1.1.1",
#         "set service snmp listen-address 100.1.2.1 port 33",
#         "set service snmp v3 user admin_user auth type sha",
#         "set service snmp v3 user admin_user auth plaintext-key ********",
#         "set service snmp v3 user admin_user privacy type aes",
#         "set service snmp v3 user admin_user privacy plaintext-key ********",
#         "set service snmp contact admin2@ex.com"
#     ]
#

# Using Gathered:
# Before State:

# vyos@vyos:~$ show configuration commands | grep snmp
# set service snmp community bridges client '1.1.1.1'
# set service snmp community bridges client '12.1.1.10'
# set service snmp community switches authorization 'rw'
# set service snmp contact 'admin2@ex.com'
# set service snmp listen-address 20.1.1.1
# set service snmp listen-address 100.1.2.1 port '33'
# set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
# set service snmp v3 user admin_user auth type 'sha'
# set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
# set service snmp v3 user admin_user privacy type 'aes'
# vyos@vyos:~$

  - name: gather configs
    vyos.vyos.vyos_snmp_server:
      state: gathered

# Module Execution:
#   "gathered": {
#         "communities": [
#             {
#                 "clients": [
#                     "1.1.1.1",
#                     "12.1.1.10"
#                 ],
#                 "name": "bridges"
#             },
#             {
#                 "authorization_type": "rw",
#                 "name": "switches"
#             }
#         ],
#         "contact": "admin2@ex.com",
#         "listen_addresses": [
#             {
#                 "address": "100.1.2.1",
#                 "port": 33
#             },
#             {
#                 "address": "20.1.1.1"
#             }
#         ],
#         "snmp_v3": {
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "admin_user"
#                 }
#             ]
#         }
#     },

# Using parsed:

# _parsed_snmp.cfg
# set service snmp community routers authorization 'ro'
# set service snmp community routers client '203.0.113.10'
# set service snmp community routers client '203.0.113.20'
# set service snmp community routers network '192.0.2.0/24'
# set service snmp community routers network '2001::/64'
# set service snmp contact 'admin@example.com'
# set service snmp listen-address 172.16.254.36 port '161'
# set service snmp listen-address 2001::1
# set service snmp location 'UK, London'
# set service snmp trap-target 203.0.113.10
# set service snmp v3 engineid '000000000000000000000002'
# set service snmp v3 group default mode 'ro'
# set service snmp v3 group default view 'default'
# set service snmp v3 user vyos auth plaintext-key 'vyos12345678'
# set service snmp v3 user vyos auth type 'sha'
# set service snmp v3 user vyos group 'default'
# set service snmp v3 user vyos privacy plaintext-key 'vyos12345678'
# set service snmp v3 user vyos privacy type 'aes'
# set service snmp v3 view default oid 1

  - name: parse configs
    vyos.vyos.vyos_snmp_server:
      running_config: "{{ lookup('file', './_parsed_snmp.cfg') }}"
      state: parsed

# Module Execution:
# "parsed": {
#         "communities": [
#             {
#                 "authorization_type": "ro",
#                 "clients": [
#                     "203.0.113.10",
#                     "203.0.113.20"
#                 ],
#                 "name": "routers",
#                 "networks": [
#                     "192.0.2.0/24",
#                     "2001::/64"
#                 ]
#             }
#         ],
#         "contact": "admin@example.com",
#         "listen_addresses": [
#             {
#                 "address": "172.16.254.36",
#                 "port": 161
#             },
#             {
#                 "address": "2001::1"
#             }
#         ],
#         "location": "UK, London",
#         "snmp_v3": {
#             "engine_id": "000000000000000000000002",
#             "groups": [
#                 {
#                     "group": "default",
#                     "mode": "ro",
#                     "view": "default"
#                 }
#             ],
#             "users": [
#                 {
#                     "authentication": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "sha"
#                     },
#                     "group": "default",
#                     "privacy": {
#                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
#                         "type": "aes"
#                     },
#                     "user": "vyos"
#                 }
#             ],
#             "views": [
#                 {
#                     "oid": "1",
#                     "view": "default"
#                 }
#             ]
#         },
#         "trap_target": {
#             "address": "203.0.113.10"
#         }
#     }
#
```

## [Return Values](vyos_snmp_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["set service snmp community routers authorization 'ro' set service snmp community routers client '203.0.113.10' set service snmp community routers client '203.0.113.20' set service snmp community routers network '192.0.2.0/24'"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["set service snmp community routers authorization 'ro' set service snmp community routers client '203.0.113.10' set service snmp community routers client '203.0.113.20' set service snmp community routers network '192.0.2.0/24'"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
