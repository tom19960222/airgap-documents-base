---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_router_route_map module – Configure route maps in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_router_route_map_module.html
fetched_at: 2026-07-27T17:43:12+00:00
---
# fortinet.fortios.fortios_router_route_map module – Configure route maps in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_route_map_module.md#ansible-collections-fortinet-fortios-fortios-router-route-map-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_route_map`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_route_map_module.md#synopsis)
- [Requirements](fortios_router_route_map_module.md#requirements)
- [Parameters](fortios_router_route_map_module.md#parameters)
- [Notes](fortios_router_route_map_module.md#notes)
- [Examples](fortios_router_route_map_module.md#examples)
- [Return Values](fortios_router_route_map_module.md#return-values)

## [Synopsis](fortios_router_route_map_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and route_map category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_route_map_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_router_route_map_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **router_route_map**  dictionary | Configure route maps. |
| **comments**  string | Optional comments. |
| **name**  string / required | Name. |
| **rule**  list / elements=dictionary | Rule. |
| **action**  string | Action.  Choices:   - `"permit"` - `"deny"` |
| **id**  integer | Rule ID. |
| **match_as_path**  string | Match BGP AS path list. Source router.aspath-list.name. |
| **match_community**  string | Match BGP community list. Source router.community-list.name. |
| **match_community_exact**  string | Enable/disable exact matching of communities.  Choices:   - `"enable"` - `"disable"` |
| **match_flags**  integer | BGP flag value to match (0 - 65535) |
| **match_interface**  string | Match interface configuration. Source system.interface.name. |
| **match_ip6_address**  string | Match IPv6 address permitted by access-list6 or prefix-list6. Source router.access-list6.name router.prefix-list6.name. |
| **match_ip6_nexthop**  string | Match next hop IPv6 address passed by access-list6 or prefix-list6. Source router.access-list6.name router.prefix-list6.name. |
| **match_ip_address**  string | Match IP address permitted by access-list or prefix-list. Source router.access-list.name router.prefix-list.name. |
| **match_ip_nexthop**  string | Match next hop IP address passed by access-list or prefix-list. Source router.access-list.name router.prefix-list.name. |
| **match_metric**  integer | Match metric for redistribute routes. |
| **match_origin**  string | Match BGP origin code.  Choices:   - `"none"` - `"egp"` - `"igp"` - `"incomplete"` |
| **match_route_type**  string | Match route type.  Choices:   - `"external-type1"` - `"external-type2"` - `"none"` - `"1"` - `"2"` |
| **match_tag**  integer | Match tag. |
| **match_vrf**  integer | Match VRF ID. |
| **set_aggregator_as**  integer | BGP aggregator AS. |
| **set_aggregator_ip**  string | BGP aggregator IP. |
| **set_aspath**  list / elements=dictionary | Prepend BGP AS path attribute. |
| **as**  string | AS number (0 - 4294967295). Use quotes for repeating numbers, For example, “1 1 2”. |
| **set_aspath_action**  string | Specify preferred action of set-aspath.  Choices:   - `"prepend"` - `"replace"` |
| **set_atomic_aggregate**  string | Enable/disable BGP atomic aggregate attribute.  Choices:   - `"enable"` - `"disable"` |
| **set_community**  list / elements=dictionary | BGP community attribute. |
| **community**  string | Attribute: AA|AA:NN|internet|local-AS|no-advertise|no-export. |
| **set_community_additive**  string | Enable/disable adding set-community to existing community.  Choices:   - `"enable"` - `"disable"` |
| **set_community_delete**  string | Delete communities matching community list. Source router.community-list.name. |
| **set_dampening_max_suppress**  integer | Maximum duration to suppress a route (1 - 255 min, 0 = unset). |
| **set_dampening_reachability_half_life**  integer | Reachability half-life time for the penalty (1 - 45 min, 0 = unset). |
| **set_dampening_reuse**  integer | Value to start reusing a route (1 - 20000, 0 = unset). |
| **set_dampening_suppress**  integer | Value to start suppressing a route (1 - 20000, 0 = unset). |
| **set_dampening_unreachability_half_life**  integer | Unreachability Half-life time for the penalty (1 - 45 min, 0 = unset). |
| **set_extcommunity_rt**  list / elements=dictionary | Route Target extended community. |
| **community**  string | AA:NN. |
| **set_extcommunity_soo**  list / elements=dictionary | Site-of-Origin extended community. |
| **community**  string | Community (format = AA:NN). |
| **set_flags**  integer | BGP flags value (0 - 65535) |
| **set_ip6_nexthop**  string | IPv6 global address of next hop. |
| **set_ip6_nexthop_local**  string | IPv6 local address of next hop. |
| **set_ip_nexthop**  string | IP address of next hop. |
| **set_local_preference**  integer | BGP local preference path attribute. |
| **set_metric**  integer | Metric value. |
| **set_metric_type**  string | Metric type.  Choices:   - `"external-type1"` - `"external-type2"` - `"none"` - `"1"` - `"2"` |
| **set_origin**  string | BGP origin code.  Choices:   - `"none"` - `"egp"` - `"igp"` - `"incomplete"` |
| **set_originator_id**  string | BGP originator ID attribute. |
| **set_priority**  integer | Priority for routing table. |
| **set_route_tag**  integer | Route tag for routing table. |
| **set_tag**  integer | Tag value. |
| **set_weight**  integer | BGP weight for routing table. |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_router_route_map_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_route_map_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure route maps.
    fortios_router_route_map:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      router_route_map:
        comments: "<your_own_value>"
        name: "default_name_4"
        rule:
         -
            action: "permit"
            id:  "7"
            match_as_path: "<your_own_value> (source router.aspath-list.name)"
            match_community: "<your_own_value> (source router.community-list.name)"
            match_community_exact: "enable"
            match_flags: "32767"
            match_interface: "<your_own_value> (source system.interface.name)"
            match_ip_address: "<your_own_value> (source router.access-list.name router.prefix-list.name)"
            match_ip_nexthop: "<your_own_value> (source router.access-list.name router.prefix-list.name)"
            match_ip6_address: "<your_own_value> (source router.access-list6.name router.prefix-list6.name)"
            match_ip6_nexthop: "<your_own_value> (source router.access-list6.name router.prefix-list6.name)"
            match_metric: ""
            match_origin: "none"
            match_route_type: "external-type1"
            match_tag: ""
            match_vrf: ""
            set_aggregator_as: "0"
            set_aggregator_ip: "<your_own_value>"
            set_aspath:
             -
                as: "<your_own_value>"
            set_aspath_action: "prepend"
            set_atomic_aggregate: "enable"
            set_community:
             -
                community: "<your_own_value>"
            set_community_additive: "enable"
            set_community_delete: "<your_own_value> (source router.community-list.name)"
            set_dampening_max_suppress: "0"
            set_dampening_reachability_half_life: "0"
            set_dampening_reuse: "0"
            set_dampening_suppress: "0"
            set_dampening_unreachability_half_life: "0"
            set_extcommunity_rt:
             -
                community: "<your_own_value>"
            set_extcommunity_soo:
             -
                community: "<your_own_value>"
            set_flags: "32767"
            set_ip_nexthop: "<your_own_value>"
            set_ip6_nexthop: "<your_own_value>"
            set_ip6_nexthop_local: "<your_own_value>"
            set_local_preference: ""
            set_metric: ""
            set_metric_type: "external-type1"
            set_origin: "none"
            set_originator_id: "<your_own_value>"
            set_priority: ""
            set_route_tag: ""
            set_tag: ""
            set_weight: ""
```

## [Return Values](fortios_router_route_map_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
