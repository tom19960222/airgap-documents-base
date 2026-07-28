---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_router_routemap module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_router_routemap_module.html
fetched_at: 2026-07-27T17:34:35+00:00
---
# fortinet.fortimanager.fmgr_router_routemap module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_router_routemap`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_router_routemap_module.md#synopsis)
- [Parameters](fmgr_router_routemap_module.md#parameters)
- [Notes](fmgr_router_routemap_module.md#notes)
- [Examples](fmgr_router_routemap_module.md#examples)
- [Return Values](fmgr_router_routemap_module.md#return-values)

## [Synopsis](fmgr_router_routemap_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_router_routemap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **router_routemap**  dictionary | the top level parameters set |
| **comments**  string | no description |
| **name**  string | no description |
| **rule**  list / elements=string | description |
| **action**  string | no description  Choices:   - `"permit"` - `"deny"` |
| **id**  integer | no description |
| **match-as-path**  string | no description |
| **match-community**  string | no description |
| **match-community-exact**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **match-flags**  integer | no description |
| **match-interface**  string | no description |
| **match-ip-address**  string | no description |
| **match-ip-nexthop**  string | no description |
| **match-ip6-address**  string | no description |
| **match-ip6-nexthop**  string | no description |
| **match-metric**  string | no description |
| **match-origin**  string | no description  Choices:   - `"none"` - `"egp"` - `"igp"` - `"incomplete"` |
| **match-route-type**  string | no description  Choices:   - `"1"` - `"2"` - `"none"` - `"external-type1"` - `"external-type2"` |
| **match-tag**  string | no description |
| **match-vrf**  integer | no description |
| **set-aggregator-as**  integer | no description |
| **set-aggregator-ip**  string | no description |
| **set-aspath**  string | description |
| **set-aspath-action**  string | no description  Choices:   - `"prepend"` - `"replace"` |
| **set-atomic-aggregate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **set-community**  string | description |
| **set-community-additive**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **set-community-delete**  string | no description |
| **set-dampening-max-suppress**  integer | no description |
| **set-dampening-reachability-half-life**  integer | no description |
| **set-dampening-reuse**  integer | no description |
| **set-dampening-suppress**  integer | no description |
| **set-dampening-unreachability-half-life**  integer | no description |
| **set-extcommunity-rt**  string | description |
| **set-extcommunity-soo**  string | description |
| **set-flags**  integer | no description |
| **set-ip-nexthop**  string | no description |
| **set-ip6-nexthop**  string | no description |
| **set-ip6-nexthop-local**  string | no description |
| **set-local-preference**  string | no description |
| **set-metric**  string | no description |
| **set-metric-type**  string | no description  Choices:   - `"1"` - `"2"` - `"none"` - `"external-type1"` - `"external-type2"` |
| **set-origin**  string | no description  Choices:   - `"none"` - `"egp"` - `"igp"` - `"incomplete"` |
| **set-originator-id**  string | no description |
| **set-priority**  integer | no description |
| **set-route-tag**  string | no description |
| **set-tag**  string | no description |
| **set-weight**  string | no description |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_router_routemap_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_router_routemap_module.md#id4)

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
   - name: no description
     fmgr_router_routemap:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        router_routemap:
           comments: <value of string>
           name: <value of string>
           rule:
             -
                 action: <value in [permit, deny]>
                 id: <value of integer>
                 match-as-path: <value of string>
                 match-community: <value of string>
                 match-community-exact: <value in [disable, enable]>
                 match-flags: <value of integer>
                 match-interface: <value of string>
                 match-ip-address: <value of string>
                 match-ip-nexthop: <value of string>
                 match-ip6-address: <value of string>
                 match-ip6-nexthop: <value of string>
                 match-metric: <value of string>
                 match-origin: <value in [none, egp, igp, ...]>
                 match-route-type: <value in [1, 2, none, ...]>
                 match-tag: <value of string>
                 match-vrf: <value of integer>
                 set-aggregator-as: <value of integer>
                 set-aggregator-ip: <value of string>
                 set-aspath: <value of string>
                 set-aspath-action: <value in [prepend, replace]>
                 set-atomic-aggregate: <value in [disable, enable]>
                 set-community: <value of string>
                 set-community-additive: <value in [disable, enable]>
                 set-community-delete: <value of string>
                 set-dampening-max-suppress: <value of integer>
                 set-dampening-reachability-half-life: <value of integer>
                 set-dampening-reuse: <value of integer>
                 set-dampening-suppress: <value of integer>
                 set-dampening-unreachability-half-life: <value of integer>
                 set-extcommunity-rt: <value of string>
                 set-extcommunity-soo: <value of string>
                 set-flags: <value of integer>
                 set-ip-nexthop: <value of string>
                 set-ip6-nexthop: <value of string>
                 set-ip6-nexthop-local: <value of string>
                 set-local-preference: <value of string>
                 set-metric: <value of string>
                 set-metric-type: <value in [1, 2, none, ...]>
                 set-origin: <value in [none, egp, igp, ...]>
                 set-originator-id: <value of string>
                 set-priority: <value of integer>
                 set-route-tag: <value of string>
                 set-tag: <value of string>
                 set-weight: <value of string>
```

## [Return Values](fmgr_router_routemap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
