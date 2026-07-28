---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_router_routemap_rule module – Rule."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_router_routemap_rule_module.html
fetched_at: 2026-07-28T02:16:33+00:00
---
# fortinet.fortimanager.fmgr_router_routemap_rule module – Rule.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_router_routemap_rule`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_router_routemap_rule_module.md#synopsis)
- [Parameters](fmgr_router_routemap_rule_module.md#parameters)
- [Notes](fmgr_router_routemap_rule_module.md#notes)
- [Examples](fmgr_router_routemap_rule_module.md#examples)
- [Return Values](fmgr_router_routemap_rule_module.md#return-values)

## [Synopsis](fmgr_router_routemap_rule_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_router_routemap_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **route-map**  string / required | the parameter (route-map) in requested url |
| **router_routemap_rule**  dictionary | the top level parameters set |
| **action**  string | Action.  **Choices:**   - `"permit"` - `"deny"` |
| **id**  integer / required | Rule ID. |
| **match-as-path**  string | Match BGP AS path list. |
| **match-community**  string | Match BGP community list. |
| **match-community-exact**  string | Enable/disable exact matching of communities.  **Choices:**   - `"disable"` - `"enable"` |
| **match-extcommunity**  string | Match BGP extended community list. |
| **match-extcommunity-exact**  string | Enable/disable exact matching of extended communities.  **Choices:**   - `"disable"` - `"enable"` |
| **match-flags**  integer | no description |
| **match-interface**  string | Match interface configuration. |
| **match-ip-address**  string | Match IP address permitted by access-list or prefix-list. |
| **match-ip-nexthop**  string | Match next hop IP address passed by access-list or prefix-list. |
| **match-ip6-address**  string | Match IPv6 address permitted by access-list6 or prefix-list6. |
| **match-ip6-nexthop**  string | Match next hop IPv6 address passed by access-list6 or prefix-list6. |
| **match-metric**  string | Match metric for redistribute routes. |
| **match-origin**  string | Match BGP origin code.  **Choices:**   - `"none"` - `"egp"` - `"igp"` - `"incomplete"` |
| **match-route-type**  string | Match route type.  **Choices:**   - `"1"` - `"2"` - `"none"` - `"external-type1"` - `"external-type2"` |
| **match-tag**  string | Match tag. |
| **match-vrf**  integer | Match VRF ID. |
| **set-aggregator-as**  integer | BGP aggregator AS. |
| **set-aggregator-ip**  string | BGP aggregator IP. |
| **set-aspath**  any | (list) no description |
| **set-aspath-action**  string | Specify preferred action of set-aspath.  **Choices:**   - `"prepend"` - `"replace"` |
| **set-atomic-aggregate**  string | Enable/disable BGP atomic aggregate attribute.  **Choices:**   - `"disable"` - `"enable"` |
| **set-community**  any | (list) no description |
| **set-community-additive**  string | Enable/disable adding set-community to existing community.  **Choices:**   - `"disable"` - `"enable"` |
| **set-community-delete**  string | Delete communities matching community list. |
| **set-dampening-max-suppress**  integer | Maximum duration to suppress a route |
| **set-dampening-reachability-half-life**  integer | Reachability half-life time for the penalty |
| **set-dampening-reuse**  integer | Value to start reusing a route |
| **set-dampening-suppress**  integer | Value to start suppressing a route |
| **set-dampening-unreachability-half-life**  integer | Unreachability Half-life time for the penalty |
| **set-extcommunity-rt**  any | (list) no description |
| **set-extcommunity-soo**  any | (list) no description |
| **set-flags**  integer | no description |
| **set-ip-nexthop**  string | IP address of next hop. |
| **set-ip-prefsrc**  string | IP address of preferred source. |
| **set-ip6-nexthop**  string | IPv6 global address of next hop. |
| **set-ip6-nexthop-local**  string | IPv6 local address of next hop. |
| **set-local-preference**  string | BGP local preference path attribute. |
| **set-metric**  string | Metric value. |
| **set-metric-type**  string | Metric type.  **Choices:**   - `"1"` - `"2"` - `"none"` - `"external-type1"` - `"external-type2"` |
| **set-origin**  string | BGP origin code.  **Choices:**   - `"none"` - `"egp"` - `"igp"` - `"incomplete"` |
| **set-originator-id**  string | BGP originator ID attribute. |
| **set-priority**  integer | Priority for routing table. |
| **set-route-tag**  string | Route tag for routing table. |
| **set-tag**  string | Tag value. |
| **set-vpnv4-nexthop**  string | IP address of VPNv4 next-hop. |
| **set-weight**  string | BGP weight for routing table. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_router_routemap_rule_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_router_routemap_rule_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Rule.
      fmgr_router_routemap_rule:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        route-map: <your own value>
        state: <value in [present, absent]>
        router_routemap_rule:
          action: <value in [permit, deny]>
          id: <integer>
          match-as-path: <string>
          match-community: <string>
          match-community-exact: <value in [disable, enable]>
          match-flags: <integer>
          match-interface: <string>
          match-ip-address: <string>
          match-ip-nexthop: <string>
          match-ip6-address: <string>
          match-ip6-nexthop: <string>
          match-metric: <string>
          match-origin: <value in [none, egp, igp, ...]>
          match-route-type: <value in [1, 2, none, ...]>
          match-tag: <string>
          match-vrf: <integer>
          set-aggregator-as: <integer>
          set-aggregator-ip: <string>
          set-aspath: <list or string>
          set-aspath-action: <value in [prepend, replace]>
          set-atomic-aggregate: <value in [disable, enable]>
          set-community: <list or string>
          set-community-additive: <value in [disable, enable]>
          set-community-delete: <string>
          set-dampening-max-suppress: <integer>
          set-dampening-reachability-half-life: <integer>
          set-dampening-reuse: <integer>
          set-dampening-suppress: <integer>
          set-dampening-unreachability-half-life: <integer>
          set-extcommunity-rt: <list or string>
          set-extcommunity-soo: <list or string>
          set-flags: <integer>
          set-ip-nexthop: <string>
          set-ip6-nexthop: <string>
          set-ip6-nexthop-local: <string>
          set-local-preference: <string>
          set-metric: <string>
          set-metric-type: <value in [1, 2, none, ...]>
          set-origin: <value in [none, egp, igp, ...]>
          set-originator-id: <string>
          set-priority: <integer>
          set-route-tag: <string>
          set-tag: <string>
          set-weight: <string>
          match-extcommunity: <string>
          match-extcommunity-exact: <value in [disable, enable]>
          set-ip-prefsrc: <string>
          set-vpnv4-nexthop: <string>
```

## [Return Values](fmgr_router_routemap_rule_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
