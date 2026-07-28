---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_bgp_global module – BGP Global resource module."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_bgp_global_module.html
fetched_at: 2026-07-27T17:01:40+00:00
---
# cisco.nxos.nxos_bgp_global module – BGP Global resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp_global`.

New in cisco.nxos 1.4.0

- [Synopsis](nxos_bgp_global_module.md#synopsis)
- [Parameters](nxos_bgp_global_module.md#parameters)
- [Notes](nxos_bgp_global_module.md#notes)
- [Examples](nxos_bgp_global_module.md#examples)
- [Return Values](nxos_bgp_global_module.md#return-values)

## [Synopsis](nxos_bgp_global_module.md#id1)

- This module manages global BGP configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_bgp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of BGP process configuration. |
| **affinity_group**  dictionary | Configure an affinity group. |
| **group_id**  integer | Affinity Group ID. |
| **as_number**  string | Autonomous System Number of the router. |
| **bestpath**  dictionary | Define the default bestpath selection algorithm. |
| **always_compare_med**  boolean | Compare MED on paths from different AS.  Choices:   - `false` - `true` |
| **as_path**  dictionary | AS-Path. |
| **ignore**  boolean | Ignore AS-Path during bestpath selection.  Choices:   - `false` - `true` |
| **multipath_relax**  boolean | Relax AS-Path restriction when choosing multipaths.  Choices:   - `false` - `true` |
| **compare_neighborid**  boolean | When more paths are available than max path config, use neighborid as tie-breaker.  Choices:   - `false` - `true` |
| **compare_routerid**  boolean | Compare router-id for identical EBGP paths.  Choices:   - `false` - `true` |
| **cost_community_ignore**  boolean | Ignore cost communities in bestpath selection.  Choices:   - `false` - `true` |
| **igp_metric_ignore**  boolean | Ignore IGP metric for next-hop during bestpath selection.  Choices:   - `false` - `true` |
| **med**  dictionary | MED |
| **confed**  boolean | Compare MED only from paths originated from within a confederation.  Choices:   - `false` - `true` |
| **missing_as_worst**  boolean | Treat missing MED as highest MED.  Choices:   - `false` - `true` |
| **non_deterministic**  boolean | Not always pick the best-MED path among paths from same AS.  Choices:   - `false` - `true` |
| **cluster_id**  string | Configure Route Reflector Cluster-ID. |
| **confederation**  dictionary | AS confederation parameters. |
| **identifier**  string | Set routing domain confederation AS. |
| **peers**  list / elements=string | Peer ASs in BGP confederation. |
| **disable_policy_batching**  dictionary | Disable batching evaluation of outbound policy for a peer. |
| **ipv4**  dictionary | IPv4 address-family settings. |
| **prefix_list**  string | Name of prefix-list to apply. |
| **ipv6**  dictionary | IPv6 address-family settings. |
| **prefix_list**  string | Name of prefix-list to apply. |
| **nexthop**  boolean | Batching based on nexthop.  Choices:   - `false` - `true` |
| **set**  boolean | Set policy batching.  Choices:   - `false` - `true` |
| **dynamic_med_interval**  integer | Sets the interval for dampening of med changes. |
| **enforce_first_as**  boolean | Enforce neighbor AS is the first AS in AS-PATH attribute (EBGP).  Choices:   - `false` - `true` |
| **enhanced_error**  boolean | Enable BGP Enhanced error handling.  Choices:   - `false` - `true` |
| **fabric_soo**  string | Fabric site of origin. |
| **fast_external_fallover**  boolean | Immediately reset the session if the link to a directly connected BGP peer goes down.  Choices:   - `false` - `true` |
| **flush_routes**  boolean | Flush routes in RIB upon controlled restart.  Choices:   - `false` - `true` |
| **graceful_restart**  dictionary | Configure Graceful Restart functionality. |
| **helper**  boolean | Configure Graceful Restart Helper mode functionality.  Choices:   - `false` - `true` |
| **restart_time**  integer | Maximum time for restart advertised to peers. |
| **set**  boolean | Enable graceful-restart.  Choices:   - `false` - `true` |
| **stalepath_time**  integer | Maximum time to keep a restarting peer’s stale routes. |
| **graceful_shutdown**  dictionary | Graceful-shutdown for BGP protocol. |
| **activate**  dictionary | Send graceful-shutdown community on all routes. |
| **route_map**  string | Apply route-map to modify attributes for outbound. |
| **set**  boolean | Activiate graceful-shutdown.  Choices:   - `false` - `true` |
| **aware**  boolean | Lower preference of routes carrying graceful-shutdown community.  Choices:   - `false` - `true` |
| **isolate**  dictionary | Isolate this router from BGP perspective. |
| **include_local**  boolean | Withdraw both local and remote BGP routes.  Choices:   - `false` - `true` |
| **set**  boolean | Withdraw remote BGP routes to isolate this router.  Choices:   - `false` - `true` |
| **log_neighbor_changes**  boolean | Log a message for neighbor up/down event.  Choices:   - `false` - `true` |
| **maxas_limit**  integer | Allow AS-PATH attribute from EBGP neighbor imposing a limit on number of ASes. |
| **neighbor_down**  dictionary | Handle BGP neighbor down event, due to various reasons. |
| **fib_accelerate**  boolean | Accelerate the hardware updates for IP/IPv6 adjacencies for neighbor.  Choices:   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Configure BGP neighbors. |
| **bfd**  dictionary | Bidirectional Fast Detection for the neighbor. |
| **multihop**  dictionary | Multihop session. |
| **interval**  dictionary | Configure BFD session interval parameters. |
| **min_rx_interval**  integer | Minimum RX interval. |
| **multiplier**  integer | Detect Multiplier. |
| **tx_interval**  integer | TX interval in milliseconds. |
| **set**  boolean | Set BFD multihop.  Choices:   - `false` - `true` |
| **set**  boolean | Set BFD for this neighbor.  Choices:   - `false` - `true` |
| **singlehop**  boolean | Single-hop session.  Choices:   - `false` - `true` |
| **bmp_activate_server**  integer | Specify server ID for activating BMP monitoring for the peer. |
| **capability**  dictionary | Capability. |
| **suppress_4_byte_as**  boolean | Suppress 4-byte AS Capability.  Choices:   - `false` - `true` |
| **description**  string | Neighbor specific descripion. |
| **disable_connected_check**  boolean | Disable check for directly connected peer.  Choices:   - `false` - `true` |
| **dont_capability_negotiate**  boolean | Don’t negotiate capability with this neighbor.  Choices:   - `false` - `true` |
| **dscp**  string | Set dscp value for tcp transport. |
| **dynamic_capability**  boolean | Dynamic Capability  Choices:   - `false` - `true` |
| **ebgp_multihop**  integer | Specify multihop TTL for remote peer. |
| **graceful_shutdown**  dictionary | Graceful-shutdown for this neighbor. |
| **activate**  dictionary | Send graceful-shutdown community. |
| **route_map**  string | Apply route-map to modify attributes for outbound. |
| **set**  boolean | Set activate.  Choices:   - `false` - `true` |
| **inherit**  dictionary | Inherit a template. |
| **peer**  string | Peer template to inherit. |
| **peer_session**  string | Peer-session template to inherit. |
| **local_as**  string | Specify the local-as number for the eBGP neighbor. |
| **log_neighbor_changes**  dictionary | Log message for neighbor up/down event. |
| **disable**  boolean | Disable logging of neighbor up/down event.  Choices:   - `false` - `true` |
| **set**  boolean | Set log-neighbor-changes.  Choices:   - `false` - `true` |
| **low_memory**  dictionary | Behaviour in low memory situations. |
| **exempt**  boolean | Do not shutdown this peer when under memory pressure.  Choices:   - `false` - `true` |
| **neighbor_address**  string / required | IP address/Prefix of the neighbor or interface. |
| **neighbor_affinity_group**  dictionary | Configure an affinity group. |
| **group_id**  integer | Affinity Group ID. |
| **password**  dictionary | Configure a password for neighbor. |
| **encryption**  integer | 0 specifies an UNENCRYPTED neighbor password.  3 specifies an 3DES ENCRYPTED neighbor password will follow.  7 specifies a Cisco type 7 ENCRYPTED neighbor password will follow. |
| **key**  string | Authentication password. |
| **path_attribute**  list / elements=dictionary | BGP path attribute optional filtering. |
| **action**  string | Action.  Choices:   - `"discard"` - `"treat-as-withdraw"` |
| **range**  dictionary | Path attribute range. |
| **end**  integer | Path attribute range end value. |
| **start**  integer | Path attribute range start value. |
| **type**  integer | Path attribute type |
| **peer_type**  string | Neighbor facing  Choices:   - `"fabric-border-leaf"` - `"fabric-external"` |
| **remote_as**  string | Specify Autonomous System Number of the neighbor. |
| **remove_private_as**  dictionary | Remove private AS number from outbound updates. |
| **all**  boolean | All.  Choices:   - `false` - `true` |
| **replace_as**  boolean | Replace.  Choices:   - `false` - `true` |
| **set**  boolean | Remove private AS.  Choices:   - `false` - `true` |
| **shutdown**  boolean | Administratively shutdown this neighbor.  Choices:   - `false` - `true` |
| **timers**  dictionary | Configure keepalive and hold timers. |
| **holdtime**  integer | Holdtime (seconds). |
| **keepalive**  integer | Keepalive interval (seconds). |
| **transport**  dictionary | BGP transport connection. |
| **connection_mode**  dictionary | Specify type of connection. |
| **passive**  boolean | Allow passive connection setup only.  Choices:   - `false` - `true` |
| **ttl_security**  dictionary | Enable TTL Security Mechanism. |
| **hops**  integer | Specify hop count for remote peer. |
| **update_source**  string | Specify source of BGP session and updates. |
| **nexthop**  dictionary | Nexthop resolution options. |
| **suppress_default_resolution**  boolean | Prohibit use of default route for nexthop address resolution.  Choices:   - `false` - `true` |
| **rd**  dictionary | Secondary Route Distinguisher for vxlan multisite border gateway. |
| **dual**  boolean | Generate Secondary RD for all VRFs and L2VNIs.  Choices:   - `false` - `true` |
| **id**  integer | Specify 2 byte value for ID. |
| **reconnect_interval**  integer | Configure connection reconnect interval. |
| **router_id**  string | Specify the IP address to use as router-id. |
| **shutdown**  boolean | Administratively shutdown BGP protocol.  Choices:   - `false` - `true` |
| **suppress_fib_pending**  boolean | Advertise only routes that are programmed in hardware to peers.  Choices:   - `false` - `true` |
| **timers**  dictionary | Configure bgp related timers. |
| **bestpath_limit**  dictionary | Configure timeout for first bestpath after restart. |
| **always**  boolean | Configure update-delay-always option.  Choices:   - `false` - `true` |
| **timeout**  integer | Bestpath timeout (seconds). |
| **bgp**  dictionary | Configure different bgp keepalive and holdtimes. |
| **holdtime**  integer | Holdtime (seconds). |
| **keepalive**  integer | Keepalive interval (seconds). |
| **prefix_peer_timeout**  integer | Prefix Peer timeout (seconds). |
| **prefix_peer_wait**  integer | Configure wait timer for a prefix peer. |
| **vrfs**  list / elements=dictionary | Virtual Router Context configurations. |
| **allocate_index**  integer | Configure allocate-index. |
| **bestpath**  dictionary | Define the default bestpath selection algorithm. |
| **always_compare_med**  boolean | Compare MED on paths from different AS.  Choices:   - `false` - `true` |
| **as_path**  dictionary | AS-Path. |
| **ignore**  boolean | Ignore AS-Path during bestpath selection.  Choices:   - `false` - `true` |
| **multipath_relax**  boolean | Relax AS-Path restriction when choosing multipaths.  Choices:   - `false` - `true` |
| **compare_neighborid**  boolean | When more paths are available than max path config, use neighborid as tie-breaker.  Choices:   - `false` - `true` |
| **compare_routerid**  boolean | Compare router-id for identical EBGP paths.  Choices:   - `false` - `true` |
| **cost_community_ignore**  boolean | Ignore cost communities in bestpath selection.  Choices:   - `false` - `true` |
| **igp_metric_ignore**  boolean | Ignore IGP metric for next-hop during bestpath selection.  Choices:   - `false` - `true` |
| **med**  dictionary | MED |
| **confed**  boolean | Compare MED only from paths originated from within a confederation.  Choices:   - `false` - `true` |
| **missing_as_worst**  boolean | Treat missing MED as highest MED.  Choices:   - `false` - `true` |
| **non_deterministic**  boolean | Not always pick the best-MED path among paths from same AS.  Choices:   - `false` - `true` |
| **cluster_id**  string | Configure Route Reflector Cluster-ID. |
| **confederation**  dictionary | AS confederation parameters. |
| **identifier**  string | Set routing domain confederation AS. |
| **peers**  list / elements=string | Peer ASs in BGP confederation. |
| **graceful_restart**  dictionary | Configure Graceful Restart functionality. |
| **helper**  boolean | Configure Graceful Restart Helper mode functionality.  Choices:   - `false` - `true` |
| **restart_time**  integer | Maximum time for restart advertised to peers. |
| **set**  boolean | Enable graceful-restart.  Choices:   - `false` - `true` |
| **stalepath_time**  integer | Maximum time to keep a restarting peer’s stale routes. |
| **local_as**  string | Specify the local-as for this vrf. |
| **log_neighbor_changes**  boolean | Log a message for neighbor up/down event.  Choices:   - `false` - `true` |
| **maxas_limit**  integer | Allow AS-PATH attribute from EBGP neighbor imposing a limit on number of ASes. |
| **neighbor_down**  dictionary | Handle BGP neighbor down event, due to various reasons. |
| **fib_accelerate**  boolean | Accelerate the hardware updates for IP/IPv6 adjacencies for neighbor.  Choices:   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Configure BGP neighbors. |
| **bfd**  dictionary | Bidirectional Fast Detection for the neighbor. |
| **multihop**  dictionary | Multihop session. |
| **interval**  dictionary | Configure BFD session interval parameters. |
| **min_rx_interval**  integer | Minimum RX interval. |
| **multiplier**  integer | Detect Multiplier. |
| **tx_interval**  integer | TX interval in milliseconds. |
| **set**  boolean | Set BFD multihop.  Choices:   - `false` - `true` |
| **set**  boolean | Set BFD for this neighbor.  Choices:   - `false` - `true` |
| **singlehop**  boolean | Single-hop session.  Choices:   - `false` - `true` |
| **bmp_activate_server**  integer | Specify server ID for activating BMP monitoring for the peer. |
| **capability**  dictionary | Capability. |
| **suppress_4_byte_as**  boolean | Suppress 4-byte AS Capability.  Choices:   - `false` - `true` |
| **description**  string | Neighbor specific descripion. |
| **disable_connected_check**  boolean | Disable check for directly connected peer.  Choices:   - `false` - `true` |
| **dont_capability_negotiate**  boolean | Don’t negotiate capability with this neighbor.  Choices:   - `false` - `true` |
| **dscp**  string | Set dscp value for tcp transport. |
| **dynamic_capability**  boolean | Dynamic Capability  Choices:   - `false` - `true` |
| **ebgp_multihop**  integer | Specify multihop TTL for remote peer. |
| **graceful_shutdown**  dictionary | Graceful-shutdown for this neighbor. |
| **activate**  dictionary | Send graceful-shutdown community. |
| **route_map**  string | Apply route-map to modify attributes for outbound. |
| **set**  boolean | Set activate.  Choices:   - `false` - `true` |
| **inherit**  dictionary | Inherit a template. |
| **peer**  string | Peer template to inherit. |
| **peer_session**  string | Peer-session template to inherit. |
| **local_as**  string | Specify the local-as number for the eBGP neighbor. |
| **log_neighbor_changes**  dictionary | Log message for neighbor up/down event. |
| **disable**  boolean | Disable logging of neighbor up/down event.  Choices:   - `false` - `true` |
| **set**  boolean | Set log-neighbor-changes.  Choices:   - `false` - `true` |
| **low_memory**  dictionary | Behaviour in low memory situations. |
| **exempt**  boolean | Do not shutdown this peer when under memory pressure.  Choices:   - `false` - `true` |
| **neighbor_address**  string / required | IP address/Prefix of the neighbor or interface. |
| **neighbor_affinity_group**  dictionary | Configure an affinity group. |
| **group_id**  integer | Affinity Group ID. |
| **password**  dictionary | Configure a password for neighbor. |
| **encryption**  integer | 0 specifies an UNENCRYPTED neighbor password.  3 specifies an 3DES ENCRYPTED neighbor password will follow.  7 specifies a Cisco type 7 ENCRYPTED neighbor password will follow. |
| **key**  string | Authentication password. |
| **path_attribute**  list / elements=dictionary | BGP path attribute optional filtering. |
| **action**  string | Action.  Choices:   - `"discard"` - `"treat-as-withdraw"` |
| **range**  dictionary | Path attribute range. |
| **end**  integer | Path attribute range end value. |
| **start**  integer | Path attribute range start value. |
| **type**  integer | Path attribute type |
| **peer_type**  string | Neighbor facing  Choices:   - `"fabric-border-leaf"` - `"fabric-external"` |
| **remote_as**  string | Specify Autonomous System Number of the neighbor. |
| **remove_private_as**  dictionary | Remove private AS number from outbound updates. |
| **all**  boolean | All.  Choices:   - `false` - `true` |
| **replace_as**  boolean | Replace.  Choices:   - `false` - `true` |
| **set**  boolean | Remove private AS.  Choices:   - `false` - `true` |
| **shutdown**  boolean | Administratively shutdown this neighbor.  Choices:   - `false` - `true` |
| **timers**  dictionary | Configure keepalive and hold timers. |
| **holdtime**  integer | Holdtime (seconds). |
| **keepalive**  integer | Keepalive interval (seconds). |
| **transport**  dictionary | BGP transport connection. |
| **connection_mode**  dictionary | Specify type of connection. |
| **passive**  boolean | Allow passive connection setup only.  Choices:   - `false` - `true` |
| **ttl_security**  dictionary | Enable TTL Security Mechanism. |
| **hops**  integer | Specify hop count for remote peer. |
| **update_source**  string | Specify source of BGP session and updates. |
| **reconnect_interval**  integer | Configure connection reconnect interval. |
| **router_id**  string | Specify the IP address to use as router-id. |
| **timers**  dictionary | Configure bgp related timers. |
| **bestpath_limit**  dictionary | Configure timeout for first bestpath after restart. |
| **always**  boolean | Configure update-delay-always option.  Choices:   - `false` - `true` |
| **timeout**  integer | Bestpath timeout (seconds). |
| **bgp**  dictionary | Configure different bgp keepalive and holdtimes. |
| **holdtime**  integer | Holdtime (seconds). |
| **keepalive**  integer | Keepalive interval (seconds). |
| **prefix_peer_timeout**  integer | Prefix Peer timeout (seconds). |
| **prefix_peer_wait**  integer | Configure wait timer for a prefix peer. |
| **vrf**  string | VRF name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^router bgp’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  State *purged* removes all the BGP configurations from the target device. Use caution with this state.  State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely. Thereby, preserving address-family related configurations under BGP context.  Running states *deleted* and *replaced* will result in an error if there are address-family configuration lines present under a neighbor, or a vrf context that is to be removed. Please use the [cisco.nxos.nxos_bgp_af](nxos_bgp_af_module.md#ansible-collections-cisco-nxos-nxos-bgp-af-module) or [cisco.nxos.nxos_bgp_neighbor_af](nxos_bgp_neighbor_af_module.md#ansible-collections-cisco-nxos-nxos-bgp-neighbor-af-module) modules for prior cleanup.  States *merged* and *replaced* will result in a failure if BGP is already configured with a different ASN than what is provided in the task. In such cases, please use state *purged* to remove the existing BGP process and proceed further.  Refer to examples for more details.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"purged"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_bgp_global_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6.
> - Unsupported for Cisco MDS
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_bgp_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# Nexus9000v#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_bgp_global:
    config:
      as_number: 65563
      router_id: 192.168.1.1
      bestpath:
        as_path:
          multipath_relax: True
        compare_neighborid: True
        cost_community_ignore: True
      confederation:
        identifier: 42
        peers:
          - 65020
          - 65030
          - 65040
      log_neighbor_changes: True
      maxas_limit: 20
      neighbors:
        - neighbor_address: 192.168.1.100
          neighbor_affinity_group:
            group_id: 160
          bmp_activate_server: 1
          remote_as: 65563
          description: NBR-1
          low_memory:
            exempt: True
        - neighbor_address: 192.168.1.101
          remote_as: 65563
          password:
            encryption: 7
            key: 12090404011C03162E
      neighbor_down:
        fib_accelerate: True
      vrfs:
        - vrf: site-1
          allocate_index: 5000
          local_as: 200
          log_neighbor_changes: True
          neighbors:
            - neighbor_address: 198.51.100.1
              description: site-1-nbr-1
              password:
                encryption: 3
                key: 13D4D3549493D2877B1DC116EE27A6BE
              remote_as: 65562
            - neighbor_address: 198.51.100.2
              remote_as: 65562
              description: site-1-nbr-2
        - vrf: site-2
          local_as: 300
          log_neighbor_changes: True
          neighbors:
            - neighbor_address: 203.0.113.2
              description: site-2-nbr-1
              password:
                encryption: 3
                key: AF92F4C16A0A0EC5BDF56CF58BC030F6
              remote_as: 65568
          neighbor_down:
            fib_accelerate: True

# Task output
# -------------
# before: {}
#
# commands:
#  - router bgp 65563
#  - bestpath as-path multipath-relax
#  - bestpath compare-neighborid
#  - bestpath cost-community ignore
#  - confederation identifier 42
#  - log-neighbor-changes
#  - maxas-limit 20
#  - neighbor-down fib-accelerate
#  - router-id 192.168.1.1
#  - confederation peers 65020 65030 65040
#  - neighbor 192.168.1.100
#  - remote-as 65563
#  - affinity-group 160
#  - bmp-activate-server 1
#  - description NBR-1
#  - low-memory exempt
#  - neighbor 192.168.1.101
#  - remote-as 65563
#  - password 7 12090404011C03162E
#  - vrf site-1
#  - allocate-index 5000
#  - local-as 200
#  - log-neighbor-changes
#  - neighbor 198.51.100.1
#  - remote-as 65562
#  - description site-1-nbr-1
#  - password 3 13D4D3549493D2877B1DC116EE27A6BE
#  - neighbor 198.51.100.2
#  - remote-as 65562
#  - description site-1-nbr-2
#  - vrf site-2
#  - local-as 300
#  - log-neighbor-changes
#  - neighbor-down fib-accelerate
#  - neighbor 203.0.113.2
#  - remote-as 65568
#  - description site-2-nbr-1
#  - password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6
#
# after:
#    as_number: '65563'
#    bestpath:
#      as_path:
#        multipath_relax: true
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65040'
#    log_neighbor_changes: true
#    maxas_limit: 20
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    - neighbor_address: 192.168.1.101
#      password:
#        encryption: 7
#        key: 12090404011C03162E
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - allocate_index: 5000
#      local_as: '200'
#      log_neighbor_changes: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 198.51.100.1
#        password:
#          encryption: 3
#          key: 13D4D3549493D2877B1DC116EE27A6BE
#        remote_as: '65562'
#      - description: site-1-nbr-2
#        neighbor_address: 198.51.100.2
#        remote_as: '65562'
#      vrf: site-1
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - description: site-2-nbr-1
#        neighbor_address: 203.0.113.2
#        password:
#          encryption: 3
#          key: AF92F4C16A0A0EC5BDF56CF58BC030F6
#        remote_as: '65568'
#      vrf: site-2

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65040
#   bestpath as-path multipath-relax
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 20
#   log-neighbor-changes
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   neighbor 192.168.1.101
#     remote-as 65563
#     password 7 12090404011C03162E
#   vrf site-1
#     local-as 200
#     log-neighbor-changes
#     allocate-index 5000
#     neighbor 198.51.100.1
#       remote-as 65562
#       description site-1-nbr-1
#       password 3 13D4D3549493D2877B1DC116EE27A6BE
#     neighbor 198.51.100.2
#       remote-as 65562
#       description site-1-nbr-2
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       remote-as 65568
#       description site-2-nbr-1
#       password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6

# Using replaced

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65040
#   bestpath as-path multipath-relax
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 20
#   log-neighbor-changes
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   neighbor 192.168.1.101
#     remote-as 65563
#     password 7 12090404011C03162E
#   vrf site-1
#     local-as 200
#     log-neighbor-changes
#     allocate-index 5000
#     neighbor 198.51.100.1
#       remote-as 65562
#       description site-1-nbr-1
#       password 3 13D4D3549493D2877B1DC116EE27A6BE
#     neighbor 198.51.100.2
#       remote-as 65562
#       description site-1-nbr-2
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       remote-as 65568
#       description site-2-nbr-1
#       password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6

- name: Replace BGP configuration with provided configuration
  cisco.nxos.nxos_bgp_global:
    config:
      as_number: 65563
      router_id: 192.168.1.1
      bestpath:
        compare_neighborid: True
        cost_community_ignore: True
      confederation:
        identifier: 42
        peers:
          - 65020
          - 65030
          - 65050
      maxas_limit: 40
      neighbors:
        - neighbor_address: 192.168.1.100
          neighbor_affinity_group:
            group_id: 160
          bmp_activate_server: 1
          remote_as: 65563
          description: NBR-1
          low_memory:
            exempt: True
      neighbor_down:
        fib_accelerate: True
      vrfs:
        - vrf: site-2
          local_as: 300
          log_neighbor_changes: True
          neighbors:
            - neighbor_address: 203.0.113.2
              password:
                encryption: 7
                key: 12090404011C03162E
          neighbor_down:
            fib_accelerate: True
    state: replaced

# Task output
# -------------
#  before:
#    as_number: '65563'
#    bestpath:
#      as_path:
#        multipath_relax: true
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65040'
#    log_neighbor_changes: true
#    maxas_limit: 20
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    - neighbor_address: 192.168.1.101
#      password:
#        encryption: 7
#        key: 12090404011C03162E
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - allocate_index: 5000
#      local_as: '200'
#      log_neighbor_changes: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 198.51.100.1
#        password:
#          encryption: 3
#          key: 13D4D3549493D2877B1DC116EE27A6BE
#        remote_as: '65562'
#      - description: site-1-nbr-2
#        neighbor_address: 198.51.100.2
#        remote_as: '65562'
#      vrf: site-1
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - description: site-2-nbr-1
#        neighbor_address: 203.0.113.2
#        password:
#          encryption: 3
#          key: AF92F4C16A0A0EC5BDF56CF58BC030F6
#        remote_as: '65568'
#      vrf: site-2
#
# commands:
#  - router bgp 65563
#  - no bestpath as-path multipath-relax
#  - no log-neighbor-changes
#  - maxas-limit 40
#  - no confederation peers 65020 65030 65040
#  - confederation peers 65020 65030 65050
#  - no neighbor 192.168.1.101
#  - vrf site-2
#  - neighbor 203.0.113.2
#  - no remote-as 65568
#  - no description site-2-nbr-1
#  - password 7 12090404011C03162E
#  - no vrf site-1

#  after:
#    as_number: '65563'
#    bestpath:
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65050'
#    maxas_limit: 40
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - neighbor_address: 203.0.113.2
#        password:
#          encryption: 7
#          key: 12090404011C03162E
#      vrf: site-2
#
# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65050
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 40
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       password 7 12090404011C03162E

# Using deleted

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65040
#   bestpath as-path multipath-relax
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 20
#   log-neighbor-changes
#   address-family ipv4 unicast
#     default-metric 400
#     suppress-inactive
#     default-information originate
#   address-family ipv6 multicast
#     wait-igp-convergence
#     redistribute eigrp eigrp-1 route-map site-1-rmap
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   neighbor 192.168.1.101
#     remote-as 65563
#     password 7 12090404011C03162E
#   vrf site-1
#     local-as 200
#     log-neighbor-changes
#     allocate-index 5000
#     address-family ipv4 multicast
#       maximum-paths 40
#       dampen-igp-metric 1200
#     neighbor 198.51.100.1
#       remote-as 65562
#       description site-1-nbr-1
#       password 3 13D4D3549493D2877B1DC116EE27A6BE
#     neighbor 198.51.100.2
#       remote-as 65562
#       description site-1-nbr-2
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       remote-as 65568
#       description site-1-nbr-1
#       password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6

- name: Delete BGP configurations handled by this module
  cisco.nxos.nxos_bgp_global:
    state: deleted

# Task output
# -------------

# before:
#    as_number: '65563'
#    bestpath:
#      as_path:
#        multipath_relax: true
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65040'
#    log_neighbor_changes: true
#    maxas_limit: 20
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    - neighbor_address: 192.168.1.101
#      password:
#        encryption: 7
#        key: 12090404011C03162E
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - allocate_index: 5000
#      local_as: '200'
#      log_neighbor_changes: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 198.51.100.1
#        password:
#          encryption: 3
#          key: 13D4D3549493D2877B1DC116EE27A6BE
#        remote_as: '65562'
#      - description: site-1-nbr-2
#        neighbor_address: 198.51.100.2
#        remote_as: '65562'
#      vrf: site-1
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 203.0.113.2
#        password:
#          encryption: 3
#          key: AF92F4C16A0A0EC5BDF56CF58BC030F6
#        remote_as: '65568'
#      vrf: site-2
#
# commands:
#   - router bgp 65563
#   - no bestpath as-path multipath-relax
#   - no bestpath compare-neighborid
#   - no bestpath cost-community ignore
#   - no confederation identifier 42
#   - no log-neighbor-changes
#   - no maxas-limit 20
#   - no neighbor-down fib-accelerate
#   - no router-id 192.168.1.1
#   - no confederation peers 65020 65030 65040
#   - no neighbor 192.168.1.100
#   - no neighbor 192.168.1.101
#   - no vrf site-1
#   - no vrf site-2
#
#  after:
#    as_number: '65563'
#
# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   address-family ipv4 unicast
#     default-metric 400
#     suppress-inactive
#     default-information originate
#   address-family ipv6 multicast
#     wait-igp-convergence
#     redistribute eigrp eigrp-1 route-map site-1-rmap
#

# Using purged

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65040
#   bestpath as-path multipath-relax
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 20
#   log-neighbor-changes
#   address-family ipv4 unicast
#     default-metric 400
#     suppress-inactive
#     default-information originate
#   address-family ipv6 multicast
#     wait-igp-convergence
#     redistribute eigrp eigrp-1 route-map site-1-rmap
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   neighbor 192.168.1.101
#     remote-as 65563
#     password 7 12090404011C03162E
#   vrf site-1
#     local-as 200
#     log-neighbor-changes
#     allocate-index 5000
#     address-family ipv4 multicast
#       maximum-paths 40
#       dampen-igp-metric 1200
#     neighbor 198.51.100.1
#       remote-as 65562
#       description site-1-nbr-1
#       password 3 13D4D3549493D2877B1DC116EE27A6BE
#     neighbor 198.51.100.2
#       remote-as 65562
#       description site-1-nbr-2
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       remote-as 65568
#       description site-1-nbr-1
#       password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6

- name: Purge all BGP configurations from the device
  cisco.nxos.nxos_bgp_global:
    state: purged

# Task output
# -------------

# before:
#    as_number: '65563'
#    bestpath:
#      as_path:
#        multipath_relax: true
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65040'
#    log_neighbor_changes: true
#    maxas_limit: 20
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    - neighbor_address: 192.168.1.101
#      password:
#        encryption: 7
#        key: 12090404011C03162E
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - allocate_index: 5000
#      local_as: '200'
#      log_neighbor_changes: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 198.51.100.1
#        password:
#          encryption: 3
#          key: 13D4D3549493D2877B1DC116EE27A6BE
#        remote_as: '65562'
#      - description: site-1-nbr-2
#        neighbor_address: 198.51.100.2
#        remote_as: '65562'
#      vrf: site-1
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 203.0.113.2
#        password:
#          encryption: 3
#          key: AF92F4C16A0A0EC5BDF56CF58BC030F6
#        remote_as: '65568'
#      vrf: site-2
#
# commands:
#   - no router bgp 65563
#
#  after: {}
#
# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# Nexus9000v#

# Using rendered

- name: Render platform specific configuration lines (without connecting to the device)
  cisco.nxos.nxos_bgp_global:
    config:
      as_number: 65563
      router_id: 192.168.1.1
      bestpath:
        as_path:
          multipath_relax: True
        compare_neighborid: True
        cost_community_ignore: True
      confederation:
        identifier: 42
        peers:
          - 65020
          - 65030
          - 65040
      log_neighbor_changes: True
      maxas_limit: 20
      neighbors:
        - neighbor_address: 192.168.1.100
          neighbor_affinity_group:
            group_id: 160
          bmp_activate_server: 1
          remote_as: 65563
          description: NBR-1
          low_memory:
            exempt: True
        - neighbor_address: 192.168.1.101
          remote_as: 65563
          password:
            encryption: 7
            key: 12090404011C03162E
      neighbor_down:
        fib_accelerate: True
      vrfs:
        - vrf: site-1
          allocate_index: 5000
          local_as: 200
          log_neighbor_changes: True
          neighbors:
            - neighbor_address: 198.51.100.1
              description: site-1-nbr-1
              password:
                encryption: 3
                key: 13D4D3549493D2877B1DC116EE27A6BE
              remote_as: 65562
            - neighbor_address: 198.51.100.2
              remote_as: 65562
              description: site-1-nbr-2
        - vrf: site-2
          local_as: 300
          log_neighbor_changes: True
          neighbors:
            - neighbor_address: 203.0.113.2
              description: site-1-nbr-1
              password:
                encryption: 3
                key: AF92F4C16A0A0EC5BDF56CF58BC030F6
              remote_as: 65568
          neighbor_down:
            fib_accelerate: True

# Task Output (redacted)
# -----------------------
# rendered:
#   - router bgp 65563
#   - bestpath as-path multipath-relax
#   - bestpath compare-neighborid
#   - bestpath cost-community ignore
#   - confederation identifier 42
#   - log-neighbor-changes
#   - maxas-limit 20
#   - neighbor-down fib-accelerate
#   - router-id 192.168.1.1
#   - confederation peers 65020 65030 65040
#   - neighbor 192.168.1.100
#   - remote-as 65563
#   - affinity-group 160
#   - bmp-activate-server 1
#   - description NBR-1
#   - low-memory exempt
#   - neighbor 192.168.1.101
#   - remote-as 65563
#   - password 7 12090404011C03162E
#   - vrf site-1
#   - allocate-index 5000
#   - local-as 200
#   - log-neighbor-changes
#   - neighbor 198.51.100.1
#   - remote-as 65562
#   - description site-1-nbr-1
#   - password 3 13D4D3549493D2877B1DC116EE27A6BE
#   - neighbor 198.51.100.2
#   - remote-as 65562
#   - description site-1-nbr-2
#   - vrf site-2
#   - local-as 300
#   - log-neighbor-changes
#   - neighbor-down fib-accelerate
#   - neighbor 203.0.113.2
#   - remote-as 65568
#   - description site-1-nbr-1
#   - password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6

# Using parsed

# parsed.cfg
# ------------
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65040
#   bestpath as-path multipath-relax
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 20
#   log-neighbor-changes
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   neighbor 192.168.1.101
#     remote-as 65563
#     password 7 12090404011C03162E
#   vrf site-1
#     local-as 200
#     log-neighbor-changes
#     allocate-index 5000
#     neighbor 198.51.100.1
#       remote-as 65562
#       description site-1-nbr-1
#       password 3 13D4D3549493D2877B1DC116EE27A6BE
#     neighbor 198.51.100.2
#       remote-as 65562
#       description site-1-nbr-2
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       remote-as 65568
#       description site-1-nbr-1
#       password 3 AF92F4C16A0A0EC5BDF56CF58BC030F6

- name: Parse externally provided BGP config
  cisco.nxos.nxos_bgp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
#  parsed:
#    as_number: '65563'
#    bestpath:
#      as_path:
#        multipath_relax: true
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65040'
#    log_neighbor_changes: true
#    maxas_limit: 20
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    - neighbor_address: 192.168.1.101
#      password:
#        encryption: 7
#        key: 12090404011C03162E
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - allocate_index: 5000
#      local_as: '200'
#      log_neighbor_changes: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 198.51.100.1
#        password:
#          encryption: 3
#          key: 13D4D3549493D2877B1DC116EE27A6BE
#        remote_as: '65562'
#      - description: site-1-nbr-2
#        neighbor_address: 198.51.100.2
#        remote_as: '65562'
#      vrf: site-1
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - description: site-1-nbr-1
#        neighbor_address: 203.0.113.2
#        password:
#          encryption: 3
#          key: AF92F4C16A0A0EC5BDF56CF58BC030F6
#        remote_as: '65568'
#      vrf: site-2

# Using gathered

# existing config
#
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65563
#   router-id 192.168.1.1
#   confederation identifier 42
#   confederation peers 65020 65030 65050
#   bestpath cost-community ignore
#   bestpath compare-neighborid
#   neighbor-down fib-accelerate
#   maxas-limit 40
#   neighbor 192.168.1.100
#     low-memory exempt
#     bmp-activate-server 1
#     remote-as 65563
#     description NBR-1
#     affinity-group 160
#   vrf site-1
#   vrf site-2
#     local-as 300
#     neighbor-down fib-accelerate
#     log-neighbor-changes
#     neighbor 203.0.113.2
#       password 7 12090404011C03162E

- name: Gather BGP facts using gathered
  cisco.nxos.nxos_bgp_global:
    state: gathered

# Task output (redacted)
# -----------------------
#  gathered:
#    as_number: '65563'
#    bestpath:
#      compare_neighborid: true
#      cost_community_ignore: true
#    confederation:
#      identifier: '42'
#      peers:
#      - '65020'
#      - '65030'
#      - '65050'
#    maxas_limit: 40
#    neighbor_down:
#      fib_accelerate: true
#    neighbors:
#    - bmp_activate_server: 1
#      description: NBR-1
#      low_memory:
#        exempt: true
#      neighbor_address: 192.168.1.100
#      neighbor_affinity_group:
#        group_id: 160
#      remote_as: '65563'
#    router_id: 192.168.1.1
#    vrfs:
#    - vrf: site-1
#    - local_as: '300'
#      log_neighbor_changes: true
#      neighbor_down:
#        fib_accelerate: true
#      neighbors:
#      - neighbor_address: 203.0.113.2
#        password:
#          encryption: 7
#          key: 12090404011C03162E
#      vrf: site-2

# Remove a neighbor having AF configurations with state replaced (will fail)

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   log-neighbor-changes
#   maxas-limit 20
#   router-id 198.51.100.2
#   neighbor 203.0.113.2
#     address-family ipv4 unicast
#       next-hop-self
#     remote-as 65538
#     affinity-group 160
#     description NBR-1
#     low-memory exempt
#   neighbor 192.0.2.1
#     remote-as 65537
#     password 7 12090404011C03162E

- name: Remove a neighbor having AF configurations (should fail)
  cisco.nxos.nxos_bgp_global:
    config:
      as_number: 65536
      router_id: 198.51.100.2
      maxas_limit: 20
      log_neighbor_changes: True
      neighbors:
        - neighbor_address: 192.0.2.1
          remote_as: 65537
          password:
            encryption: 7
            key: 12090404011C03162E
    state: replaced

# Task output (redacted)
# -----------------------
# fatal: [Nexus9000v]: FAILED! => changed=false
#    msg: Neighbor 203.0.113.2 has address-family configurations.
#         Please use the nxos_bgp_neighbor_af module to remove those first.

# Remove a VRF having AF configurations with state replaced (will fail)

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   log-neighbor-changes
#   maxas-limit 20
#   router-id 198.51.100.2
#   neighbor 192.0.2.1
#     remote-as 65537
#     password 7 12090404011C03162E
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#     neighbor 203.0.113.2
#       remote-as 65538
#       affinity-group 160
#       description NBR-1
#       low-memory exempt
#   vrf site-2
#     neighbor-down fib-accelerate

- name: Remove a VRF having AF configurations (should fail)
  cisco.nxos.nxos_bgp_global:
    config:
      as_number: 65536
      router_id: 198.51.100.2
      maxas_limit: 20
      log_neighbor_changes: True
      neighbors:
        - neighbor_address: 192.0.2.1
          remote_as: 65537
          password:
            encryption: 7
            key: 12090404011C03162E
      vrfs:
        - vrf: site-2
          neighbor_down:
            fib_accelerate: True
    state: replaced

# Task output (redacted)
# -----------------------
# fatal: [Nexus9000v]: FAILED! => changed=false
#    msg: VRF site-1 has address-family configurations.
#         Please use the nxos_bgp_af module to remove those first.
```

## [Return Values](nxos_bgp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["router bgp 65563", "maxas-limit 20", "router-id 192.168.1.1", "confederation peers 65020 65030 65040", "neighbor 192.168.1.100", "remote-as 65563", "affinity-group 160", "bmp-activate-server 1", "description NBR-1", "low-memory exempt", "vrf site-1", "log-neighbor-changes", "neighbor 198.51.100.1", "remote-as 65562", "description site-1-nbr-1", "password 3 13D4D3549493D2877B1DC116EE27A6BE"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
