---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_ntp_global module – Manage NTP configuration on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_ntp_global_module.html
fetched_at: 2026-07-28T02:39:45+00:00
---
# junipernetworks.junos.junos_ntp_global module – Manage NTP configuration on Junos devices.

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
> see [Requirements](junos_ntp_global_module.md#ansible-collections-junipernetworks-junos-junos-ntp-global-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_ntp_global`.

New in junipernetworks.junos 2.6.0

- [Synopsis](junos_ntp_global_module.md#synopsis)
- [Requirements](junos_ntp_global_module.md#requirements)
- [Parameters](junos_ntp_global_module.md#parameters)
- [Notes](junos_ntp_global_module.md#notes)
- [Examples](junos_ntp_global_module.md#examples)
- [Return Values](junos_ntp_global_module.md#return-values)

## [Synopsis](junos_ntp_global_module.md#id1)

- This module manages NTP configuration on devices running Junos.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ntp_global

## [Requirements](junos_ntp_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_ntp_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of NTP configuration. |
| **authentication_keys**  list / elements=dictionary | NTP authentication key. |
| **algorithm**  string | Authentication key type.  **Choices:**   - `"md5"` - `"sha1"` - `"sha256"` |
| **id**  integer | Authentication key number. |
| **key**  string | Authentication key value. |
| **boot_server**  string | Server to query during boot sequence. |
| **broadcast_client**  boolean | Listen to broadcast NTP.  **Choices:**   - `false` - `true` |
| **broadcasts**  list / elements=dictionary | Broadcast parameters. |
| **address**  string | Broadcast or multicast address to use. |
| **key**  string | Authentication key. |
| **routing_instance_name**  string | Routing intance name in which interface has address in broadcast subnet. |
| **ttl**  integer | TTL value to transmit. |
| **version**  integer | NTP version to use. |
| **interval_range**  integer | Set the minpoll and maxpoll interval range. |
| **multicast_client**  string | Listen to multicast NTP address. |
| **peers**  list / elements=dictionary | NTP Peers. |
| **key_id**  integer | Key-id to be used while communicating. |
| **peer**  string | Hostname/IP address of the NTP Peer. |
| **prefer**  boolean | Prefer this peer.  **Choices:**   - `false` - `true` |
| **version**  integer | NTP version to use. |
| **servers**  list / elements=dictionary | NTP Servers. |
| **key_id**  integer | Key-id to be used while communicating. |
| **prefer**  boolean | Prefer this peer_serv.  **Choices:**   - `false` - `true` |
| **routing_instance**  string | Routing instance through which server is reachable. |
| **server**  string | IP address or hostname of the server. |
| **version**  integer | NTP version to use. |
| **source_addresses**  list / elements=dictionary | Source-Address parameters. |
| **routing_instance**  string | Routing intance name in which source address is defined. |
| **source_address**  string | Use specified address as source address. |
| **threshold**  dictionary | Set the maximum threshold(sec) allowed for NTP adjustment. |
| **action**  string | Select actions for NTP abnormal adjustment.  **Choices:**   - `"accept"` - `"reject"` |
| **value**  integer | The maximum value(sec) allowed for NTP adjustment. |
| **trusted_keys**  list / elements=dictionary | List of trusted authentication keys. |
| **key_id**  integer | Trusted-Key number. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show system syslog**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"overridden"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_ntp_global_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_ntp_global_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
#
# [edit]
# vagrant@vsrx# show routing-instances
# rt1 {
#     description rt1;
# }
# rt2 {
- name: Merge provided NTP configuration into running configuration.
  junipernetworks.junos.junos_ntp_global:
    config:
      boot_server: '78.46.194.186'
      broadcasts:
        - address: '172.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt1'
        - address: '192.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt2'
      broadcast_client: true
      interval_range: 2
      multicast_client: "224.0.0.1"
      peers:
        - peer: "78.44.194.186"
        - peer: "172.44.194.186"
          key_id: 10000
          prefer: true
          version: 3
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
      source_addresses:
        - source_address: "172.45.194.186"
          routing_instance: 'rt1'
        - source_address: "171.45.194.186"
          routing_instance: 'rt2'
      threshold:
        value: 300
        action: "accept"
      trusted_keys:
        - key_id: 3000
        - key_id: 2000
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#           "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server><nc:broadcast>"
#           "<nc:name>172.16.255.255</nc:name><nc:key>50</nc:key><nc:routing-instance-name>rt1</nc:routing-instance-name>"
#           "<nc:ttl>200</nc:ttl><nc:version>3</nc:version></nc:broadcast><nc:broadcast><nc:name>192.16.255.255</nc:name>"
#           "<nc:key>50</nc:key><nc:routing-instance-name>rt2</nc:routing-instance-name><nc:ttl>200</nc:ttl>"
#           "<nc:version>3</nc:version></nc:broadcast><nc:broadcast-client/><nc:interval-range>2</nc:interval-range>"
#           "<nc:multicast-client>224.0.0.1</nc:multicast-client><nc:peer><nc:name>78.44.194.186</nc:name></nc:peer>"
#           "<nc:peer><nc:name>172.44.194.186</nc:name><nc:key>10000</nc:key><nc:prefer/><nc:version>3</nc:version>"
#           "</nc:peer><nc:server><nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>"
#           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name><nc:key>34</nc:key>"
#           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:source-address><nc:name>172.45.194.186</nc:name>"
#           "<nc:routing-instance>rt1</nc:routing-instance></nc:source-address><nc:source-address>"
#           "<nc:name>171.45.194.186</nc:name><nc:routing-instance>rt2</nc:routing-instance></nc:source-address>"
#           "<nc:threshold><nc:value>300</nc:value><nc:action>accept</nc:action></nc:threshold>"
#           "<nc:trusted-key>3000</nc:trusted-key><nc:trusted-key>2000</nc:trusted-key></nc:ntp></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;
#
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;

- name: Replaced running ntp global configuration with provided configuration
  junipernetworks.junos.junos_ntp_global:
    config:
      authentication_keys:
        - id: 2
          algorithm: 'md5'
          key: 'asdfghd'
        - id: 5
          algorithm: 'sha1'
          key: 'aasdad'
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ]
#     },
#     "before": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "changed": true,
#     "commands": [
#             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#             "<nc:ntp delete="delete"/><nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>
#             "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key><nc:name>5</nc:name>
#             "<nc:type>sha1</nc:type><nc:value>aasdad</nc:value></nc:authentication-key><nc:server>
#             "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>
#             "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>
#             "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server></nc:ntp></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
# authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA

# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;

- name: Override running ntp global configuration with provided configuration
  junipernetworks.junos.junos_ntp_global:
    config:
      authentication_keys:
        - id: 2
          algorithm: 'md5'
          key: 'asdfghd'
        - id: 5
          algorithm: 'sha1'
          key: 'aasdad'
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ]
#     },
#     "before": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "changed": true,
#     "commands": [
#             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#             "<nc:ntp delete="delete"/><nc:ntp><nc:authentication-key><nc:name>2</nc:name><nc:type>md5</nc:type>
#             "<nc:value>asdfghd</nc:value></nc:authentication-key><nc:authentication-key><nc:name>5</nc:name>
#             "<nc:type>sha1</nc:type><nc:value>aasdad</nc:value></nc:authentication-key><nc:server>
#             "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>
#             "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>
#             "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server></nc:ntp></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
# authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
# authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# authentication-key 2 type md5 value "$9$03aAB1hreW7NbO1rvMLVbgoJ"; ## SECRET-DATA
# authentication-key 5 type sha1 value "$9$DXiHmf5F/A0ZUjq.P3n"; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
#
- name: Delete running NTP global configuration
  junipernetworks.junos.junos_ntp_global:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$03aAB1hreW7NbO1rvMLVbgoJ"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$DXiHmf5F/A0ZUjq.P3n"
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#               "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#               "<nc:ntp delete="delete"/></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
#
# [edit]
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show system ntp
# boot-server 78.46.194.186;
# interval-range 2;
# peer 78.44.194.186;
# peer 172.44.194.186 key 10000 version 3 prefer; ## SECRET-DATA
# server 48.46.194.186 key 34 version 2 prefer routing-instance rt1; ## SECRET-DATA
# server 48.45.194.186 key 34 version 2 prefer; ## SECRET-DATA
# broadcast 172.16.255.255 routing-instance-name rt1 key 50 version 3 ttl 200;
# broadcast 192.16.255.255 routing-instance-name rt2 key 50 version 3 ttl 200;
# broadcast-client;
# multicast-client 224.0.0.1;
# trusted-key [ 3000 2000 ];
# threshold 300 action accept;
# source-address 172.45.194.186 routing-instance rt1;
# source-address 171.45.194.186 routing-instance rt2;
- name: Gather running NTP global configuration
  junipernetworks.junos.junos_ntp_global:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": {
#         "boot_server": "78.46.194.186",
#         "broadcast_client": true,
#         "broadcasts": [
#             {
#                 "address": "172.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt1",
#                 "ttl": 200,
#                 "version": 3
#             },
#             {
#                 "address": "192.16.255.255",
#                 "key": "50",
#                 "routing_instance_name": "rt2",
#                 "ttl": 200,
#                 "version": 3
#             }
#         ],
#         "interval_range": 2,
#         "multicast_client": "224.0.0.1",
#         "peers": [
#             {
#                 "peer": "78.44.194.186"
#             },
#             {
#                 "key_id": 10000,
#                 "peer": "172.44.194.186",
#                 "prefer": true,
#                 "version": 3
#             }
#         ],
#         "servers": [
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "routing_instance": "rt1",
#                 "server": "48.46.194.186",
#                 "version": 2
#             },
#             {
#                 "key_id": 34,
#                 "prefer": true,
#                 "server": "48.45.194.186",
#                 "version": 2
#             }
#         ],
#         "source_addresses": [
#             {
#                 "routing_instance": "rt1",
#                 "source_address": "172.45.194.186"
#             },
#             {
#                 "routing_instance": "rt2",
#                 "source_address": "171.45.194.186"
#             }
#         ],
#         "threshold": {
#             "action": "accept",
#             "value": 300
#         },
#         "trusted_keys": [
#             {"key_id": 2000},
#             {"key_id": 3000}
#         ]
#     },
#     "changed": false,
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_ntp_global:
    config:
      boot_server: '78.46.194.186'
      broadcasts:
        - address: '172.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt1'
        - address: '192.16.255.255'
          key: '50'
          ttl: 200
          version: 3
          routing_instance_name: 'rt2'
      broadcast_client: true
      interval_range: 2
      multicast_client: "224.0.0.1"
      peers:
        - peer: "78.44.194.186"
        - peer: "172.44.194.186"
          key_id: 10000
          prefer: true
          version: 3
      servers:
        - server: "48.46.194.186"
          key_id: 34
          prefer: true
          version: 2
          routing_instance: 'rt1'
        - server: "48.45.194.186"
          key_id: 34
          prefer: true
          version: 2
      source_addresses:
        - source_address: "172.45.194.186"
          routing_instance: 'rt1'
        - source_address: "171.45.194.186"
          routing_instance: 'rt2'
      threshold:
        value: 300
        action: "accept"
      trusted_keys:
        - 3000
        - 2000
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#           "<nc:ntp><nc:boot-server>78.46.194.186</nc:boot-server><nc:broadcast><nc:name>172.16.255.255</nc:name>"
#           "<nc:key>50</nc:key><nc:routing-instance-name>rt1</nc:routing-instance-name><nc:ttl>200</nc:ttl>"
#           "<nc:version>3</nc:version></nc:broadcast><nc:broadcast><nc:name>192.16.255.255</nc:name>"
#           "<nc:key>50</nc:key><nc:routing-instance-name>rt2</nc:routing-instance-name>"
#           "<nc:ttl>200</nc:ttl><nc:version>3</nc:version></nc:broadcast><nc:broadcast-client/>"
#           "<nc:interval-range>2</nc:interval-range><nc:multicast-client>224.0.0.1</nc:multicast-client><nc:peer>"
#           "<nc:name>78.44.194.186</nc:name></nc:peer><nc:peer><nc:name>172.44.194.186</nc:name>"
#           "<nc:key>10000</nc:key><nc:prefer/><nc:version>3</nc:version></nc:peer><nc:server>"
#           "<nc:name>48.46.194.186</nc:name><nc:key>34</nc:key><nc:routing-instance>rt1</nc:routing-instance>"
#           "<nc:prefer/><nc:version>2</nc:version></nc:server><nc:server><nc:name>48.45.194.186</nc:name>"
#           "<nc:key>34</nc:key><nc:prefer/><nc:version>2</nc:version></nc:server><nc:source-address>"
#           "<nc:name>172.45.194.186</nc:name><nc:routing-instance>rt1</nc:routing-instance></nc:source-address>"
#           "<nc:source-address><nc:name>171.45.194.186</nc:name><nc:routing-instance>rt2</nc:routing-instance>"
#           "</nc:source-address><nc:threshold><nc:value>300</nc:value><nc:action>accept</nc:action></nc:threshold>"
#           "<nc:trusted-key>3000</nc:trusted-key><nc:trusted-key>2000</nc:trusted-key></nc:ntp></nc:system>"
#     ]
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
#            <ntp>
#               <authentication-key>
#                  <name>2</name>
#                  <type>md5</type>
#                  <value>$9$GxDjqfT3CA0UjfzF6u0RhS</value>
#               </authentication-key>
#               <authentication-key>
#                  <name>5</name>
#                  <type>sha1</type>
#                  <value>$9$ZsUDk.mT3/toJGiHqQz</value>
#               </authentication-key>
#           </ntp>
#     </system>
#     </configuration>
# </rpc-reply>
#
- name: Parse NTP global running config
  junipernetworks.junos.junos_ntp_global:
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
#         "authentication_keys": [
#             {
#                 "algorithm": "md5",
#                 "id": 2,
#                 "key": "$9$GxDjqfT3CA0UjfzF6u0RhS"
#             },
#             {
#                 "algorithm": "sha1",
#                 "id": 5,
#                 "key": "$9$ZsUDk.mT3/toJGiHqQz"
#             }
#         ]
#     }
#
#
```

## [Return Values](junos_ntp_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:name>78.44.194.186</nc:name></nc:peer><nc:peer><nc:name>172.44.194.186</nc:name>", "xml 2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
