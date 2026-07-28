---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_ntp_global module – NTP Global resource module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_ntp_global_module.html
fetched_at: 2026-07-28T01:38:55+00:00
---
# cisco.nxos.nxos_ntp_global module – NTP Global resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_ntp_global`.

New in cisco.nxos 2.6.0

- [Synopsis](nxos_ntp_global_module.md#synopsis)
- [Parameters](nxos_ntp_global_module.md#parameters)
- [Notes](nxos_ntp_global_module.md#notes)
- [Examples](nxos_ntp_global_module.md#examples)
- [Return Values](nxos_ntp_global_module.md#return-values)

## [Synopsis](nxos_ntp_global_module.md#id1)

- This module manages ntp configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ntp_global

## [Parameters](nxos_ntp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dict of ntp configuration. |
| **access_group**  dictionary | NTP access-group.  This option is unsupported on MDS switches. |
| **match_all**  boolean | Scan ACLs present in all ntp access groups.  **Choices:**   - `false` - `true` |
| **peer**  list / elements=dictionary | Access-group peer. |
| **access_list**  string | Name of access list. |
| **query_only**  list / elements=dictionary | Access-group query-only. |
| **access_list**  string | Name of access list. |
| **serve**  list / elements=dictionary | Access-group serve. |
| **access_list**  string | Name of access list. |
| **serve_only**  list / elements=dictionary | Access-group serve-only. |
| **access_list**  string | Name of access list. |
| **allow**  dictionary | Enable/Disable the packets. |
| **control**  dictionary | Control mode packets. |
| **rate_limit**  integer | Rate-limit delay. |
| **private**  boolean | Enable/Disable Private mode packets.  **Choices:**   - `false` - `true` |
| **authenticate**  boolean | Enable/Disable authentication.  **Choices:**   - `false` - `true` |
| **authentication_keys**  list / elements=dictionary | NTP authentication key. |
| **encryption**  integer | 0 for Clear text  7 for Encrypted |
| **id**  integer | Authentication key number (range 1-65535). |
| **key**  string | Authentication key. |
| **logging**  boolean | Enable/Disable logging of NTPD Events.  **Choices:**   - `false` - `true` |
| **master**  dictionary | Act as NTP master clock.  This option is unsupported on MDS switches. |
| **stratum**  integer | Stratum number. |
| **passive**  boolean | NTP passive command.  This option is unsupported on MDS switches.  **Choices:**   - `false` - `true` |
| **peers**  list / elements=dictionary | NTP Peers. |
| **key_id**  integer | Keyid to be used while communicating to this server. |
| **maxpoll**  integer | Maximum interval to poll a peer.  Poll interval in secs to a power of 2. |
| **minpoll**  integer | Minimum interval to poll a peer.  Poll interval in secs to a power of 2. |
| **peer**  string | Hostname/IP address of the NTP Peer. |
| **prefer**  boolean | Preferred Server.  **Choices:**   - `false` - `true` |
| **vrf**  aliases: use_vrf  string | Display per-VRF information.  This option is unsupported on MDS switches. |
| **servers**  list / elements=dictionary | NTP servers. |
| **key_id**  integer | Keyid to be used while communicating to this server. |
| **maxpoll**  integer | Maximum interval to poll a peer.  Poll interval in secs to a power of 2. |
| **minpoll**  integer | Minimum interval to poll a peer.  Poll interval in secs to a power of 2. |
| **prefer**  boolean | Preferred Server.  **Choices:**   - `false` - `true` |
| **server**  string | Hostname/IP address of the NTP Peer. |
| **vrf**  aliases: use_vrf  string | Display per-VRF information.  This option is not applicable for MDS switches. |
| **source**  string | Source of NTP packets.  This option is unsupported on MDS switches. |
| **source_interface**  string | Source interface sending NTP packets. |
| **trusted_keys**  list / elements=dictionary | NTP trusted-key number. |
| **key_id**  integer | Trusted-Key number. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config ntp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *replaced* and *overridden* have identical behaviour for this module.  Please refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_ntp_global_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6 on Cisco Nexus Switches.
> - This module works with connection `network_cli` and `httpapi`.
> - Tested against Cisco MDS NX-OS 9.2(2) with connection `network_cli`.

## [Examples](nxos_ntp_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# show running-config ntp
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_ntp_global: &id001
    config:
      access_group:
        peer:
          - access_list: PeerAcl1
        serve:
          - access_list: ServeAcl1
      authenticate: True
      authentication_keys:
        - id: 1001
          key: vagwwtKfkv
          encryption: 7
        - id: 1002
          key: vagwwtKfkvgthz
          encryption: 7
      logging: True
      master:
        stratum: 2
      peers:
        - peer: 192.0.2.1
          key_id: 1
          maxpoll: 15
          minpoll: 5
          vrf: default
        - peer: 192.0.2.2
          key_id: 2
          prefer: True
          vrf: siteA
      servers:
        - server: 198.51.100.1
          key_id: 2
          vrf: default
        - server: 203.0.113.1
          key_id: 1
          vrf: siteB

# Task output
# -------------
#  before: {}
#
#  commands:
#    - "ntp authenticate"
#    - "ntp logging"
#    - "ntp master 2"
#    - "ntp authentication-keys 1001 md5 vagwwtKfkv 7"
#    - "ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7"
#    - "ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15"
#    - "ntp peer 192.0.2.2 prefer use-vrf siteA key 2"
#    - "ntp server 198.51.100.1 use-vrf default key 2"
#    - "ntp server 203.0.113.1 use-vrf siteB key 1"
#    - "ntp access-group peer PeerAcl1"
#    - "ntp access-group serve ServeAcl1"
#
#  after:
#    access_group:
#      peer:
#        - access_list: PeerAcl1
#      serve:
#       - access_list: ServeAcl1
#    authenticate: True
#    authentication_keys:
#      - id: 1001
#        key: vagwwtKfkv
#        encryption: 7
#      - id: 1002
#        key: vagwwtKfkvgthz
#        encryption: 7
#    logging: True
#    master:
#     stratum: 2
#    peers:
#      - peer: 192.0.2.1
#        key_id: 1
#        maxpoll: 15
#        minpoll: 5
#        vrf: default
#      - peer: 192.0.2.2
#        key_id: 2
#        prefer: True
#        vrf: siteA
#    servers:
#      - server: 198.51.100.1
#        key_id: 2
#        vrf: default
#      - server: 203.0.113.1
#        key_id: 1
#        vrf: siteB

# After state:
# ------------
# nxos-9k-rdo# show running-config ntp
# ntp authenticate
# ntp logging
# ntp master 2
# ntp authentication-keys 1001 md5 vagwwtKfkv 7
# ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7
# ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15
# ntp peer 192.0.2.2 prefer use-vrf siteA key 2
# ntp server 198.51.100.1 use-vrf default key 2
# ntp server 203.0.113.1 use-vrf siteB key 1
# ntp access-group peer PeerAcl1
# ntp access-group serve ServeAcl1

# Using replaced

# Before state:
# ------------
# nxos-9k-rdo# show running-config ntp
# ntp authenticate
# ntp logging
# ntp master 2
# ntp authentication-keys 1001 md5 vagwwtKfkv 7
# ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7
# ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15
# ntp peer 192.0.2.2 prefer use-vrf siteA key 2
# ntp server 198.51.100.1 use-vrf default key 2
# ntp server 203.0.113.1 use-vrf siteB key 1
# ntp access-group peer PeerAcl1
# ntp access-group serve ServeAcl1

- name: Replace logging global configurations of listed logging global with provided configurations
  cisco.nxos.nxos_ntp_global:
    config:
      access_group:
        peer:
          - access_list: PeerAcl2
        serve:
          - access_list: ServeAcl2
      logging: True
      master:
        stratum: 2
      peers:
        - peer: 192.0.2.1
          key_id: 1
          maxpoll: 15
          minpoll: 5
          vrf: default
        - peer: 192.0.2.5
          key_id: 2
          prefer: True
          vrf: siteA
      servers:
        - server: 198.51.100.1
          key_id: 2
          vrf: default
    state: replaced

# Task output
# -------------
#  before:
#    access_group:
#      peer:
#        - access_list: PeerAcl1
#      serve:
#       - access_list: ServeAcl1
#    authenticate: True
#    authentication_keys:
#      - id: 1001
#        key: vagwwtKfkv
#        encryption: 7
#      - id: 1002
#        key: vagwwtKfkvgthz
#        encryption: 7
#    logging: True
#    master:
#     stratum: 2
#    peers:
#      - peer: 192.0.2.1
#        key_id: 1
#        maxpoll: 15
#        minpoll: 5
#        vrf: default
#      - peer: 192.0.2.2
#        key_id: 2
#        prefer: True
#        vrf: siteA
#    servers:
#      - server: 198.51.100.1
#        key_id: 2
#        vrf: default
#      - server: 203.0.113.1
#        key_id: 1
#        vrf: siteB
#
#  commands:
#    - "no ntp authenticate"
#    - "no ntp authentication-keys 1001 md5 vagwwtKfkv 7"
#    - "no ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7"
#    - "ntp peer 192.0.2.5 prefer use-vrf siteA key 2"
#    - "no ntp peer 192.0.2.2 prefer use-vrf siteA key 2"
#    - "no ntp server 203.0.113.1 use-vrf siteB key 1"
#    - "ntp access-group peer PeerAcl2"
#    - "no ntp access-group peer PeerAcl1"
#    - "ntp access-group serve ServeAcl2"
#    - "no ntp access-group serve ServeAcl1"
#
#  after:
#    access_group:
#      peer:
#        - access_list: PeerAcl2
#      serve:
#        - access_list: ServeAcl2
#    logging: True
#    master:
#      stratum: 2
#    peers:
#      - peer: 192.0.2.1
#        key_id: 1
#        maxpoll: 15
#        minpoll: 5
#        vrf: default
#      - peer: 192.0.2.5
#        key_id: 2
#        prefer: True
#        vrf: siteA
#    servers:
#      - server: 198.51.100.1
#        key_id: 2
#        vrf: default

# After state:
# ------------
# nxos-9k-rdo# show running-config ntp
# ntp logging
# ntp master 2
# ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15
# ntp peer 192.0.2.5 prefer use-vrf siteA key 2
# ntp server 198.51.100.1 use-vrf default key 2
# ntp access-group peer PeerAcl2
# ntp access-group serve ServeAcl2

# Using deleted to delete all logging configurations

# Before state:
# ------------
# nxos-9k-rdo# show running-config ntp

- name: Delete all logging configuration
  cisco.nxos.nxos_ntp_global:
    state: deleted

# Task output
# -------------
#  before:
#    access_group:
#      peer:
#        - access_list: PeerAcl1
#      serve:
#       - access_list: ServeAcl1
#    authenticate: True
#    authentication_keys:
#      - id: 1001
#        key: vagwwtKfkv
#        encryption: 7
#      - id: 1002
#        key: vagwwtKfkvgthz
#        encryption: 7
#    logging: True
#    master:
#     stratum: 2
#    peers:
#      - peer: 192.0.2.1
#        key_id: 1
#        maxpoll: 15
#        minpoll: 5
#        vrf: default
#      - peer: 192.0.2.2
#        key_id: 2
#        prefer: True
#        vrf: siteA
#    servers:
#      - server: 198.51.100.1
#        key_id: 2
#        vrf: default
#      - server: 203.0.113.1
#        key_id: 1
#        vrf: siteB
#
#  commands:
#    - "no ntp authenticate"
#    - "no ntp logging"
#    - "no ntp master 2"
#    - "no ntp authentication-keys 1001 md5 vagwwtKfkv 7"
#    - "no ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7"
#    - "no ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15"
#    - "no ntp peer 192.0.2.2 prefer use-vrf siteA key 2"
#    - "no ntp server 198.51.100.1 use-vrf default key 2"
#    - "no ntp server 203.0.113.1 use-vrf siteB key 1"
#    - "no ntp access-group peer PeerAcl1"
#    - "no ntp access-group serve ServeAcl1"
#
#  after: {}

# After state:
# ------------
# nxos-9k-rdo# show running-config ntp
# nxos-9k-rdo#

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_ntp_global:
    config:
      access_group:
        peer:
          - access_list: PeerAcl1
        serve:
          - access_list: ServeAcl1
      authenticate: True
      authentication_keys:
        - id: 1001
          key: vagwwtKfkv
          encryption: 7
        - id: 1002
          key: vagwwtKfkvgthz
          encryption: 7
      logging: True
      master:
        stratum: 2
      peers:
        - peer: 192.0.2.1
          key_id: 1
          maxpoll: 15
          minpoll: 5
          vrf: default
        - peer: 192.0.2.2
          key_id: 2
          prefer: True
          vrf: siteA
      servers:
        - server: 198.51.100.1
          key_id: 2
          vrf: default
        - server: 203.0.113.1
          key_id: 1
          vrf: siteB
    state: rendered

# Task Output (redacted)
# -----------------------
#  rendered:
#    - "ntp authenticate"
#    - "ntp logging"
#    - "ntp master 2"
#    - "ntp authentication-keys 1001 md5 vagwwtKfkv 7"
#    - "ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7"
#    - "ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15"
#    - "ntp peer 192.0.2.2 prefer use-vrf siteA key 2"
#    - "ntp server 198.51.100.1 use-vrf default key 2"
#    - "ntp server 203.0.113.1 use-vrf siteB key 1"
#    - "ntp access-group peer PeerAcl1"
#    - "ntp access-group serve ServeAcl1"

# Using parsed

# parsed.cfg
# ------------
# ntp authenticate
# ntp logging
# ntp master 2
# ntp authentication-keys 1001 md5 vagwwtKfkv 7
# ntp authentication-keys 1002 md5 vagwwtKfkvgthz 7
# ntp peer 192.0.2.1 use-vrf default key 1 minpoll 5 maxpoll 15
# ntp peer 192.0.2.2 prefer use-vrf siteA key 2
# ntp server 198.51.100.1 use-vrf default key 2
# ntp server 203.0.113.1 use-vrf siteB key 1
# ntp access-group peer PeerAcl1
# ntp access-group serve ServeAcl1

- name: Parse externally provided ntp configuration
  cisco.nxos.nxos_ntp_global:
    running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#    access_group:
#      peer:
#        - access_list: PeerAcl1
#      serve:
#       - access_list: ServeAcl1
#    authenticate: True
#    authentication_keys:
#      - id: 1001
#        key: vagwwtKfkv
#        encryption: 7
#      - id: 1002
#        key: vagwwtKfkvgthz
#        encryption: 7
#    logging: True
#    master:
#     stratum: 2
#    peers:
#      - peer: 192.0.2.1
#        key_id: 1
#        maxpoll: 15
#        minpoll: 5
#        vrf: default
#      - peer: 192.0.2.2
#        key_id: 2
#        prefer: True
#        vrf: siteA
#    servers:
#      - server: 198.51.100.1
#        key_id: 2
#        vrf: default
#      - server: 203.0.113.1
#        key_id: 1
#        vrf: siteB
```

## [Return Values](nxos_ntp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["ntp master stratum 2", "ntp peer 198.51.100.1 use-vrf test maxpoll 7", "ntp authentication-key 10 md5 wawyhanx2 7", "ntp access-group peer PeerAcl1", "ntp access-group peer PeerAcl2", "ntp access-group query-only QueryAcl1"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["ntp master stratum 2", "ntp peer 198.51.100.1 use-vrf test maxpoll 7", "ntp authentication-key 10 md5 wawyhanx2 7", "ntp access-group peer PeerAcl1", "ntp access-group peer PeerAcl2", "ntp access-group query-only QueryAcl1"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
