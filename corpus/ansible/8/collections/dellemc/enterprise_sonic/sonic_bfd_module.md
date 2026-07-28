---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_bfd module – Manage BFD configuration on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_bfd_module.html
fetched_at: 2026-07-28T02:03:26+00:00
---
# dellemc.enterprise_sonic.sonic_bfd module – Manage BFD configuration on SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bfd`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_bfd_module.md#synopsis)
- [Parameters](sonic_bfd_module.md#parameters)
- [Examples](sonic_bfd_module.md#examples)
- [Return Values](sonic_bfd_module.md#return-values)

## [Synopsis](sonic_bfd_module.md#id1)

- This module provides configuration management of BFD for devices running SONiC

## [Parameters](sonic_bfd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies BFD configurations |
| **multi_hops**  list / elements=dictionary | List of multi-hop sessions |
| **detect_multiplier**  integer | Number of missed packets to bring down a BFD session  **Default:** `3` |
| **enabled**  boolean | Enables BFD session when set to true  **Choices:**   - `false` - `true` ← (default) |
| **local_address**  string / required | Source IP address to be used for BFD sessions over the interface |
| **min_ttl**  integer | Minimum expected TTL on received packets  **Default:** `254` |
| **passive_mode**  boolean | Specifies BFD peer as passive when set to true  **Choices:**   - `false` ← (default) - `true` |
| **profile_name**  string | BFD profile name |
| **receive_interval**  integer | Specifies peer receive interval  **Default:** `300` |
| **remote_address**  string / required | IP address used by the remote system for the BFD session |
| **transmit_interval**  integer | Specifies peer transmit interval  **Default:** `300` |
| **vrf**  string / required | Name of the configured VRF on the device |
| **profiles**  list / elements=dictionary | List of preconfiguration profiles |
| **detect_multiplier**  integer | Number of missed packets to bring down a BFD session  **Default:** `3` |
| **echo_interval**  integer | Specifies echo interval  **Default:** `300` |
| **echo_mode**  boolean | Echo mode is enabled when set to true  **Choices:**   - `false` ← (default) - `true` |
| **enabled**  boolean | Enables BFD session when set to true  **Choices:**   - `false` - `true` ← (default) |
| **min_ttl**  integer | Minimum expected TTL on received packets  **Default:** `254` |
| **passive_mode**  boolean | Specifies BFD peer as passive when set to true  **Choices:**   - `false` ← (default) - `true` |
| **profile_name**  string / required | BFD profile name |
| **receive_interval**  integer | Specifies peer receive interval  **Default:** `300` |
| **transmit_interval**  integer | Specifies peer transmit interval  **Default:** `300` |
| **single_hops**  list / elements=dictionary | List of single-hop sessions |
| **detect_multiplier**  integer | Number of missed packets to bring down a BFD session  **Default:** `3` |
| **echo_interval**  integer | Specifies echo interval  **Default:** `300` |
| **echo_mode**  boolean | Echo mode is enabled when set to true  **Choices:**   - `false` ← (default) - `true` |
| **enabled**  boolean | Enables BFD session when set to true  **Choices:**   - `false` - `true` ← (default) |
| **interface**  string / required | Interface to use to contact peer |
| **local_address**  string / required | Source IP address to be used for BFD sessions over the interface |
| **passive_mode**  boolean | Specifies BFD peer as passive when set to true  **Choices:**   - `false` ← (default) - `true` |
| **profile_name**  string | BFD profile name |
| **receive_interval**  integer | Specifies peer receive interval  **Default:** `300` |
| **remote_address**  string / required | IP address used by the remote system for the BFD session |
| **transmit_interval**  integer | Specifies peer transmit interval  **Default:** `300` |
| **vrf**  string / required | Name of the configured VRF on the device |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_bfd_module.md#id3)

```yaml+jinja
# Using Merged
#
# Before state:
# -------------
#
# sonic# show bfd profile
# (No "bfd profile" configuration present)
# sonic# show bfd peers
# (No "bfd peers" configuration present)

  - name: Merge BFD configuration
    input:
      profiles:
        - profile_name: 'p1'
          enabled: True
          transmit_interval: 120
          receive_interval: 200
          detect_multiplier: 2
          passive_mode: True
          min_ttl: 140
          echo_interval: 150
          echo_mode: True
      single_hops:
        - remote_address: '196.88.6.1'
          vrf: 'default'
          interface: 'Ethernet20'
          local_address: '1.1.1.1'
          enabled: True
          transmit_interval: 50
          receive_interval: 80
          detect_multiplier: 4
          passive_mode: True
          echo_interval: 110
          echo_mode: True
          profile_name: 'p1'
      multi_hops:
        - remote_address: '192.40.1.3'
          vrf: 'default'
          local_address: '3.3.3.3'
          enabled: True
          transmit_interval: 75
          receive_interval: 100
          detect_multiplier: 3
          passive_mode: True
          min_ttl: 125
          profile_name: 'p1'
    state: merged

# After state:
# ------------
#
# sonic# show bfd profile
# BFD Profile:
#     Profile-name: p1
#         Enabled: True
#         Echo-mode: Enabled
#         Passive-mode: Enabled
#         Minimum-Ttl: 140
#         Detect-multiplier: 2
#         Receive interval: 200ms
#         Transmission interval: 120ms
#         Echo transmission interval: 150ms
# sonic# show bfd peers
# BFD Peers:
#
#     peer 192.40.1.3 multihop local-address 3.3.3.3 vrf default
#         ID: 989720421
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p1
#         Minimum TTL: 125
#         Status: down
#         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 2
#             Receive interval: 100ms
#             Transmission interval: 75ms
#             Echo transmission interval: ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms
#
#     peer 196.88.6.1 local-address 1.1.1.1 vrf default interface Ethernet20
#         ID: 1134635660
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p1
#         Status: down
#         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 4
#             Receive interval: 80ms
#             Transmission interval: 50ms
#             Echo transmission interval: 110ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms
#
#
# Using replaced
#
# Before state:
# -------------
#
# sonic# show bfd profile
# BFD Profile:
#     Profile-name: p1
#         Enabled: True
#         Echo-mode: Enabled
#         Passive-mode: Enabled
#         Minimum-Ttl: 140
#         Detect-multiplier: 2
#         Receive interval: 200ms
#         Transmission interval: 120ms
#         Echo transmission interval: 150ms
#     Profile-name: p2
#         Enabled: True
#         Echo-mode: Disabled
#         Passive-mode: Disabled
#         Minimum-Ttl: 254
#         Detect-multiplier: 3
#         Receive interval: 300ms
#         Transmission interval: 300ms
#         Echo transmission interval: 300ms

  - name: Replace BFD configuration
    input:
      profiles:
        - profile_name: 'p1'
          transmit_interval: 144
        - profile_name: 'p2'
          enabled: False
          transmit_interval: 110
          receive_interval: 235
          detect_multiplier: 5
          passive_mode: True
          min_ttl: 155
          echo_interval: 163
          echo_mode: True
    state: replaced

# After state:
# ------------
#
# sonic# show bfd profile
# BFD Profile:
#     Profile-name: p1
#         Enabled: True
#         Echo-mode: Enabled
#         Passive-mode: Enabled
#         Minimum-Ttl: 140
#         Detect-multiplier: 2
#         Receive interval: 200ms
#         Transmission interval: 144ms
#         Echo transmission interval: 150ms
#     Profile-name: p2
#         Enabled: False
#         Echo-mode: Enabled
#         Passive-mode: Enabled
#         Minimum-Ttl: 155
#         Detect-multiplier: 5
#         Receive interval: 235ms
#         Transmission interval: 110ms
#         Echo transmission interval: 163ms
#
#
# Using overridden
#
# Before state:
# -------------
#
# sonic# show bfd peers
# BFD Peers:
#
#     peer 192.40.1.3 multihop local-address 3.3.3.3 vrf default
#         ID: 989720421
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p1
#         Minimum TTL: 125
#         Status: down
#         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 2
#             Receive interval: 100ms
#             Transmission interval: 75ms
#             Echo transmission interval: ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms
#
#     peer 196.88.6.1 local-address 1.1.1.1 vrf default interface Ethernet20
#         ID: 1134635660
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p1
#         Status: down
#         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 4
#             Receive interval: 80ms
#             Transmission interval: 50ms
#             Echo transmission interval: 110ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms

  - name: Override BFD configuration
    input:
      single_hops:
        - remote_address: '172.68.2.1'
          vrf: 'default'
          interface: 'Ethernet16'
          local_address: '2.2.2.2'
          enabled: True
          transmit_interval: 60
          receive_interval: 88
          detect_multiplier: 6
          passive_mode: True
          echo_interval: 112
          echo_mode: True
          profile_name: 'p3'
      multi_hops:
        - remote_address: '186.42.1.2'
          vrf: 'default'
          local_address: '1.1.1.1'
          enabled: False
          transmit_interval: 85
          receive_interval: 122
          detect_multiplier: 4
          passive_mode: False
          min_ttl: 120
          profile_name: 'p3'
    state: overridden

# After state:
# ------------
#
# sonic# show bfd peers
# BFD Peers:
#
#     peer 186.42.1.2 multihop local-address 1.1.1.1 vrf default
#         ID: 989720421
#         Remote ID: 0
#         Passive mode: Disabled
#         Profile: p3
#         Minimum TTL: 120
#         Status: down
#         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 4
#             Receive interval: 122ms
#             Transmission interval: 85ms
#             Echo transmission interval: ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms
#
#     peer 172.68.2.1 local-address 2.2.2.2 vrf default interface Ethernet16
#         ID: 1134635660
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p3
#         Status: down
#         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 6
#             Receive interval: 88ms
#             Transmission interval: 60ms
#             Echo transmission interval: 112ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms
#
#
# Using deleted
#
# Before state:
# -------------
#
# sonic# show bfd profile
# BFD Profile:
#     Profile-name: p1
#         Enabled: True
#         Echo-mode: Enabled
#         Passive-mode: Enabled
#         Minimum-Ttl: 140
#         Detect-multiplier: 2
#         Receive interval: 200ms
#         Transmission interval: 120ms
#         Echo transmission interval: 150ms
# sonic# show bfd peers
# BFD Peers:
#
#     peer 192.40.1.3 multihop local-address 3.3.3.3 vrf default
#         ID: 989720421
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p1
#         Minimum TTL: 125
#         Status: down
#         Downtime: 0 day(s), 0 hour(s), 1 min(s), 46 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 2
#             Receive interval: 100ms
#             Transmission interval: 75ms
#             Echo transmission interval: ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms
#
#     peer 196.88.6.1 local-address 1.1.1.1 vrf default interface Ethernet20
#         ID: 1134635660
#         Remote ID: 0
#         Passive mode: Enabled
#         Profile: p1
#         Status: down
#         Downtime: 0 day(s), 1 hour(s), 50 min(s), 48 sec(s)
#         Diagnostics: ok
#         Remote diagnostics: ok
#         Peer Type: configured
#         Local timers:
#             Detect-multiplier: 4
#             Receive interval: 80ms
#             Transmission interval: 50ms
#             Echo transmission interval: 110ms
#         Remote timers:
#             Detect-multiplier: 3
#             Receive interval: 1000ms
#             Transmission interval: 1000ms
#             Echo transmission interval: 0ms

  - name: Delete BFD configuration
    input:
      profiles:
        - profile_name: 'p1'
          enabled: True
          transmit_interval: 120
          receive_interval: 200
          detect_multiplier: 2
          passive_mode: True
          min_ttl: 140
          echo_interval: 150
          echo_mode: True
      single_hops:
        - remote_address: '196.88.6.1'
          vrf: 'default'
          interface: 'Ethernet20'
          local_address: '1.1.1.1'
      multi_hops:
        - remote_address: '192.40.1.3'
          vrf: 'default'
          local_address: '3.3.3.3'
    state: deleted

# After state
# -----------
#
# sonic# show bfd profile
# BFD Profile:
#     Profile-name: p1
#         Enabled: True
#         Echo-mode: Disabled
#         Passive-mode: Disabled
#         Minimum-Ttl: 254
#         Detect-multiplier: 3
#         Receive interval: 300ms
#         Transmission interval: 300ms
#         Echo transmission interval: 300ms
# sonic# show bfd peers
# (No "bfd peers" configuration present)
```

## [Return Values](sonic_bfd_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Shade Talabi (@stalabi1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
