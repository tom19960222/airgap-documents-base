---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_routing_instances module – Manage routing instances on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_routing_instances_module.html
fetched_at: 2026-07-27T17:54:34+00:00
---
# junipernetworks.junos.junos_routing_instances module – Manage routing instances on Junos devices.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_routing_instances_module.md#ansible-collections-junipernetworks-junos-junos-routing-instances-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_routing_instances`.

New in junipernetworks.junos 2.1.0

- [Synopsis](junos_routing_instances_module.md#synopsis)
- [Requirements](junos_routing_instances_module.md#requirements)
- [Parameters](junos_routing_instances_module.md#parameters)
- [Notes](junos_routing_instances_module.md#notes)
- [Examples](junos_routing_instances_module.md#examples)
- [Return Values](junos_routing_instances_module.md#return-values)

## [Synopsis](junos_routing_instances_module.md#id1)

- Manage routing instances on Junos network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_routing_instances_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_routing_instances_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided Routing instance configuration list. |
| **connector_id_advertise**  boolean | Advertise connector-id attribute.  Choices:   - `false` - `true` |
| **description**  string | Specify text description of routing instance. |
| **egress_protection**  dictionary | Egress instance protection dictionary. |
| **context_identifier**  string | Specify context identifier. |
| **protector**  boolean | Enable Edge Protector functionality for this VPN.  Choices:   - `false` - `true` |
| **instance_role**  string | Primary role of L2Backhaul-vpn router.  Choices:   - `"access"` - `"nni"` |
| **interfaces**  list / elements=dictionary | Interface name for this routing instance. |
| **name**  string | Specify name of the interface. |
| **protect_interface**  string | Specify name of the protected interface. |
| **l2vpn_id**  string | Layer-2 vpn-id for this instance. |
| **name**  string | Specify routing instance name. |
| **no_irb_layer_2_copy**  boolean | Disable transmission of layer-2 copy of packets of irb routing-interface.  Choices:   - `false` - `true` |
| **no_local_switching**  boolean | Disable vlan id normalization for interfaces.  Choices:   - `false` - `true` |
| **no_normalization**  boolean | Disable vlan id normalization for interfaces.  Choices:   - `false` - `true` |
| **no_vrf_advertise**  boolean | Disable vlan id normalization for interfaces.  Choices:   - `false` - `true` |
| **no_vrf_propagate_ttl**  boolean | Disable TTL propagation from IP to MPLS (on push) and MPLS to IP (on pop).  Choices:   - `false` - `true` |
| **qualified_bum_pruning_mode**  boolean | Enable BUM pruning for VPLS instance.  Choices:   - `false` - `true` |
| **route_distinguisher**  string | Route distinguisher for this instance |
| **routing_interface**  list / elements=string | Routing interface name for this routing-instance. |
| **type**  string | Specify instance type.  Choices:   - `"evpn"` - `"evpn-vpws"` - `"forwarding"` - `"l2backhaul-vpn"` - `"l2vpn"` - `"layer2-control"` - `"mac-vrf"` - `"mpls-forwarding"` - `"mpls-internet-multicast"` - `"no-forwarding"` - `"virtual-router"` - `"vpls"` - `"vrf"` |
| **vrf_exports**  list / elements=string | Export policy for VRF instance RIBs. |
| **vrf_imports**  list / elements=string | Import policy for VRF instance RIBs. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show routing-instances**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_routing_instances_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_routing_instances_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# admin# show routing-instances
#
# [edit]
# vagrant@vsrx# show policy-options
# policy-statement test-policy {
#     term t1 {
#         then reject;
#     }
# }
# policy-statement test-policy-1 {
#     term t1 {
#         then reject;
#     }
# }

- name: Merge Junos BGP address family configuration
  junipernetworks.junos.junos_routing_instances:
    config:
      - name: "test"
        type: "vrf"
        route_distinguisher: "10.58.255.1:37"
        vrf_imports:
          - "test-policy"
        vrf_exports:
          - "test-policy"
          - "test-policy-1"
        interfaces:
          - name: "sp-0/0/0.0"
          - name: "gr-0/0/0.0"
        connector_id_advertise: true
      - name: "forwardinst"
        type: "forwarding"
        description: "Configured by Ansible Content Team"
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#
# After state
# -----------
#
# admin# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.58.255.1:37;
#     vrf-import test-policy;
#     vrf-export [ test-policy test-policy-1 ];
#     connector-id-advertise;
# }
#
# Using gathered
#
# Before state
# ------------
#
# admin# show routing-instances
#
# [edit]
# admin# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.58.255.1:37;
#     vrf-import test-policy;
#     vrf-export [ test-policy test-policy-1 ];
#     connector-id-advertise;
# }
- name: Gather Junos routing-instances
  junipernetworks.junos.junos_routing_instances:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "description": "Configured by Ansible Content Team",
#             "name": "forwardinst",
#             "type": "forwarding"
#         },
#         {
#             "connector_id_advertise": true,
#             "interfaces": [
#                 {
#                     "name": "gr-0/0/0.0"
#                 },
#                 {
#                     "name": "sp-0/0/0.0"
#                 }
#             ],
#             "name": "test",
#             "route_distinguisher": "10.58.255.1:37",
#             "type": "vrf",
#             "vrf_exports": [
#                 "test-policy",
#                 "test-policy-1"
#             ],
#             "vrf_imports": [
#                 "test-policy"
#             ]
#         }
#     ]
#
# Using replaced
#
# Before state
# ------------
#
# admin# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.58.255.1:37;
#     vrf-import test-policy;
#     vrf-export [ test-policy test-policy-1 ];
#     connector-id-advertise;
# }

- name: Replace existing Junos routing instance config with provided config
  junipernetworks.junos.junos_routing_instances:
   config:
     address_family:
       - name: "test"
         type: "vrf"
         route_distinguisher: "10.57.255.1:37"
         vrf_imports:
           - "test-policy"
         vrf_exports:
           - "test-policy"
         interfaces:
           - name: "sp-0/0/0.0"
           - name: "gr-0/0/0.0"
         connector_id_advertise: false
         description: "Configured by Ansible Content Team"
   state: replaced

# After state
# -----------
#
# admin@vsrx# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     description "Configured by Ansible Content Team";
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.57.255.1:37;
#     vrf-import test-policy;
#     vrf-export test-policy;
# }

# Using overridden
#
# Before state
# ------------
#
# admin@vsrx# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     description "Configured by Ansible Content Team";
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.57.255.1:37;
#     vrf-import test-policy;
#     vrf-export test-policy;
# }

- name: Override Junos routing-instances configuration
  junipernetworks.junos.junos_routing_instances:
   config:
     - name: "test"
       type: "vrf"
       route_distinguisher: "10.58.255.1:37"
       vrf_imports:
         - "test-policy"
       vrf_exports:
         - "test-policy"
         - "test-policy-1"
       interfaces:
         - name: "sp-0/0/0.0"
         - name: "gr-0/0/0.0"
       connector_id_advertise: true
     - name: "forwardinst"
       type: "forwarding"
       description: "Configured by Ansible Content Team"
     - name: "vtest1"
       type: "virtual-router"
   state: overridden

# After state
# -----------
#
# admin@vsrx# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.58.255.1:37;
#     vrf-import test-policy;
#     vrf-export [ test-policy test-policy-1 ];
#     connector-id-advertise;
# }
# vtest1 {
#     instance-type virtual-router;
# }

# Using deleted
#
# Before state
# ------------
#
# admin@vsrx# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.58.255.1:37;
#     vrf-import test-policy;
#     vrf-export [ test-policy test-policy-1 ];
#     connector-id-advertise;
# }

- name: Delete provided junos routing-instamce
  junipernetworks.junos.junos_routing_instances:
   config:
     - name: "test"
   state: deleted

# After state
# -----------
#
# admin@vsrx# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }

# Using deleted without config
#
# Before state
# ------------
#
# admin@vsrx# show routing-instances
# forwardinst {
#     description "Configured by Ansible Content Team";
#     instance-type forwarding;
# }
# test {
#     instance-type vrf;
#     interface gr-0/0/0.0; ## 'gr-0/0/0.0' is not defined
#     interface sp-0/0/0.0; ## 'sp-0/0/0.0' is not defined
#     route-distinguisher 10.58.255.1:37;
#     vrf-import test-policy;
#     vrf-export [ test-policy test-policy-1 ];
#     connector-id-advertise;
# }
# vtest1 {
#     instance-type virtual-router;
# }

- name: Delete complete Junos routing-instances config
  junipernetworks.junos.junos_routing_instances:
   config:
   state: deleted

# After state
# -----------
#
# admin@vsrx# show routing-instances
#
# [edit]

- name: Gather Junos BGP address family config
  junipernetworks.junos.junos_routing_instances:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#         "address_family": [
#             {
#                 "af_type": [
#                     {
#                         "accepted_prefix_limit": {
#                             "idle_timeout_value": 2001,
#                             "limit_threshold": 98,
#                             "maximum": 20
#                         },
#                         "damping": true,
#                         "defer_initial_multipath_build": {
#                             "maximum_delay": 2
#                         },
#                         "type": "signaling"
#                     }
#                 ],
#                 "afi": "evpn"
#             },
#             {
#                 "af_type": [
#                     {
#                         "accepted_prefix_limit": {
#                             "idle_timeout_value": 2000,
#                             "limit_threshold": 99,
#                             "maximum": 20
#                         },
#                         "damping": true,
#                         "defer_initial_multipath_build": {
#                             "maximum_delay": 2
#                         },
#                         "delay_route_advertisements": {
#                             "max_delay_route_age": 20,
#                             "max_delay_routing_uptime": 32000,
#                             "min_delay_inbound_convergence": 32000,
#                             "min_delay_routing_uptime": 23000
#                         },
#                         "graceful_restart_forwarding_state_bit": "from-fib",
#                         "type": "any"
#                     },
#                     {
#                         "legacy_redirect_ip_action": {
#                             "receive": true,
#                             "send": true
#                         },
#                         "loops": 4,
#                         "no_install": true,
#                         "output_queue_priority_expedited": true,
#                         "secondary_independent_resolution": true,
#                         "type": "flow"
#                     },
#                     {
#                         "entropy_label": {
#                             "no_next_hop_validation": true
#                         },
#                         "explicit_null": {
#                             "connected_only": true
#                         },
#                         "per_group_label": true,
#                         "per_prefix_label": true,
#                         "prefix_limit": {
#                             "forever": true,
#                             "limit_threshold": 99,
#                             "maximum": 20
#                         },
#                         "resolve_vpn": true,
#                         "rib": "inet.3",
#                         "route_refresh_priority_priority": 3,
#                         "type": "labeled-unicast"
#                     },
#                     {
#                         "extended_nexthop": true,
#                         "extended_nexthop_color": true,
#                         "local_ipv4_address": "9.9.9.9",
#                         "type": "unicast"
#                     }
#                 ],
#                 "afi": "inet"
#             }
#         ]
#     }
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <routing-instances>
#             <instance>
#                 <name>forwardinst</name>
#                 <description>Configured by Ansible Content Team</description>
#                 <instance-type>forwarding</instance-type>
#             </instance>
#             <instance>
#                 <name>test</name>
#                 <instance-type>vrf</instance-type>
#                 <interface>
#                     <name>gr-0/0/0.0</name>
#                 </interface>
#                 <interface>
#                     <name>sp-0/0/0.0</name>
#                 </interface>
#                 <route-distinguisher>
#                     <rd-type>10.58.255.1:37</rd-type>
#                 </route-distinguisher>
#                 <vrf-import>test-policy</vrf-import>
#                 <vrf-export>test-policy</vrf-export>
#                 <vrf-export>test-policy-1</vrf-export>
#                 <connector-id-advertise/>
#             </instance>
#         </routing-instances>
#     </configuration>
# </rpc-reply>

- name: Parse routing instance running config
  junipernetworks.junos.junos_routing_instances:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  [
#         {
#             "description": "Configured by Ansible Content Team",
#             "name": "forwardinst",
#             "type": "forwarding"
#         },
#         {
#             "connector_id_advertise": true,
#             "interfaces": [
#                 {
#                     "name": "gr-0/0/0.0"
#                 },
#                 {
#                     "name": "sp-0/0/0.0"
#                 }
#             ],
#             "name": "test",
#             "route_distinguisher": "10.58.255.1:37",
#             "type": "vrf",
#             "vrf_exports": [
#                 "test-policy",
#                 "test-policy-1"
#             ],
#             "vrf_imports": [
#                 "test-policy"
#             ]
#         }
#     ]
#
#
# Using rendered
#
#
- name: Render the xml for provided  configuration
  junipernetworks.junos.junos_routing_instances:
    config:
      - name: "test"
        type: "vrf"
        route_distinguisher: "10.58.255.1:37"
        vrf_imports:
          - "test-policy"
        vrf_exports:
          - "test-policy"
          - "test-policy-1"
        interfaces:
          - name: "sp-0/0/0.0"
          - name: "gr-0/0/0.0"
        connector_id_advertise: true
      - name: "forwardinst"
        type: "forwarding"
        description: "Configured by Ansible Content Team"
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "<nc:routing-instances xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:instance><nc:name>test</nc:name><nc:connector-id-advertise/><nc:instance-type>vrf</nc:instance-type>
# <nc:interface><nc:name>sp-0/0/0.0</nc:name></nc:interface><nc:interface><nc:name>gr-0/0/0.0</nc:name></nc:interface>
# <nc:route-distinguisher><nc:rd-type>10.58.255.1:37</nc:rd-type></nc:route-distinguisher>
# <nc:vrf-import>test-policy</nc:vrf-import><nc:vrf-export>test-policy</nc:vrf-export>
# <nc:vrf-export>test-policy-1</nc:vrf-export></nc:instance>
# <nc:instance><nc:name>forwardinst</nc:name><nc:description>Configured by Ansible Content Team</nc:description>
# <nc:instance-type>forwarding</nc:instance-type></nc:instance></nc:routing-instances>"
```

## [Return Values](junos_routing_instances_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:routing-instances xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:instance> <nc:name>test</nc:name> <nc:connector-id-advertise/> <nc:instance-type>vrf</nc:instance-type> <nc:interface> <nc:name>sp-0/0/0.0</nc:name> </nc:interface> <nc:interface> <nc:name>gr-0/0/0.0</nc:name> </nc:interface> <nc:route-distinguisher> <nc:rd-type>10.58.255.1:37</nc:rd-type> </nc:route-distinguisher> <nc:vrf-import>test-policy</nc:vrf-import> <nc:vrf-export>test-policy</nc:vrf-export> <nc:vrf-export>test-policy-1</nc:vrf-export> </nc:instance> </routing-instances> </configuration> </rpc-reply>", "xml2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
