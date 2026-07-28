---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_router_isis module – Configure IS-IS in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_router_isis_module.html
fetched_at: 2026-07-27T17:43:02+00:00
---
# fortinet.fortios.fortios_router_isis module – Configure IS-IS in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_router_isis_module.md#ansible-collections-fortinet-fortios-fortios-router-isis-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_isis`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_isis_module.md#synopsis)
- [Requirements](fortios_router_isis_module.md#requirements)
- [Parameters](fortios_router_isis_module.md#parameters)
- [Notes](fortios_router_isis_module.md#notes)
- [Examples](fortios_router_isis_module.md#examples)
- [Return Values](fortios_router_isis_module.md#return-values)

## [Synopsis](fortios_router_isis_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and isis category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_isis_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_router_isis_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **router_isis**  dictionary | Configure IS-IS. |
| **adjacency_check**  string | Enable/disable adjacency check.  Choices:   - `"enable"` - `"disable"` |
| **adjacency_check6**  string | Enable/disable IPv6 adjacency check.  Choices:   - `"enable"` - `"disable"` |
| **adv_passive_only**  string | Enable/disable IS-IS advertisement of passive interfaces only.  Choices:   - `"enable"` - `"disable"` |
| **adv_passive_only6**  string | Enable/disable IPv6 IS-IS advertisement of passive interfaces only.  Choices:   - `"enable"` - `"disable"` |
| **auth_keychain_l1**  string | Authentication key-chain for level 1 PDUs. Source router.key-chain.name. |
| **auth_keychain_l2**  string | Authentication key-chain for level 2 PDUs. Source router.key-chain.name. |
| **auth_mode_l1**  string | Level 1 authentication mode.  Choices:   - `"password"` - `"md5"` |
| **auth_mode_l2**  string | Level 2 authentication mode.  Choices:   - `"password"` - `"md5"` |
| **auth_password_l1**  string | Authentication password for level 1 PDUs. |
| **auth_password_l2**  string | Authentication password for level 2 PDUs. |
| **auth_sendonly_l1**  string | Enable/disable level 1 authentication send-only.  Choices:   - `"enable"` - `"disable"` |
| **auth_sendonly_l2**  string | Enable/disable level 2 authentication send-only.  Choices:   - `"enable"` - `"disable"` |
| **default_originate**  string | Enable/disable distribution of default route information.  Choices:   - `"enable"` - `"disable"` |
| **default_originate6**  string | Enable/disable distribution of default IPv6 route information.  Choices:   - `"enable"` - `"disable"` |
| **dynamic_hostname**  string | Enable/disable dynamic hostname.  Choices:   - `"enable"` - `"disable"` |
| **ignore_lsp_errors**  string | Enable/disable ignoring of LSP errors with bad checksums.  Choices:   - `"enable"` - `"disable"` |
| **is_type**  string | IS type.  Choices:   - `"level-1-2"` - `"level-1"` - `"level-2-only"` |
| **isis_interface**  list / elements=dictionary | IS-IS interface configuration. |
| **auth_keychain_l1**  string | Authentication key-chain for level 1 PDUs. Source router.key-chain.name. |
| **auth_keychain_l2**  string | Authentication key-chain for level 2 PDUs. Source router.key-chain.name. |
| **auth_mode_l1**  string | Level 1 authentication mode.  Choices:   - `"md5"` - `"password"` |
| **auth_mode_l2**  string | Level 2 authentication mode.  Choices:   - `"md5"` - `"password"` |
| **auth_password_l1**  string | Authentication password for level 1 PDUs. |
| **auth_password_l2**  string | Authentication password for level 2 PDUs. |
| **auth_send_only_l1**  string | Enable/disable authentication send-only for level 1 PDUs.  Choices:   - `"enable"` - `"disable"` |
| **auth_send_only_l2**  string | Enable/disable authentication send-only for level 2 PDUs.  Choices:   - `"enable"` - `"disable"` |
| **circuit_type**  string | IS-IS interface”s circuit type.  Choices:   - `"level-1-2"` - `"level-1"` - `"level-2"` |
| **csnp_interval_l1**  integer | Level 1 CSNP interval. |
| **csnp_interval_l2**  integer | Level 2 CSNP interval. |
| **hello_interval_l1**  integer | Level 1 hello interval. |
| **hello_interval_l2**  integer | Level 2 hello interval. |
| **hello_multiplier_l1**  integer | Level 1 multiplier for Hello holding time. |
| **hello_multiplier_l2**  integer | Level 2 multiplier for Hello holding time. |
| **hello_padding**  string | Enable/disable padding to IS-IS hello packets.  Choices:   - `"enable"` - `"disable"` |
| **lsp_interval**  integer | LSP transmission interval (milliseconds). |
| **lsp_retransmit_interval**  integer | LSP retransmission interval (sec). |
| **mesh_group**  string | Enable/disable IS-IS mesh group.  Choices:   - `"enable"` - `"disable"` |
| **mesh_group_id**  integer | Mesh group ID <0-4294967295>, 0: mesh-group blocked. |
| **metric_l1**  integer | Level 1 metric for interface. |
| **metric_l2**  integer | Level 2 metric for interface. |
| **name**  string | IS-IS interface name. Source system.interface.name. |
| **network_type**  string | IS-IS interface”s network type.  Choices:   - `"broadcast"` - `"point-to-point"` - `"loopback"` |
| **priority_l1**  integer | Level 1 priority. |
| **priority_l2**  integer | Level 2 priority. |
| **status**  string | Enable/disable interface for IS-IS.  Choices:   - `"enable"` - `"disable"` |
| **status6**  string | Enable/disable IPv6 interface for IS-IS.  Choices:   - `"enable"` - `"disable"` |
| **wide_metric_l1**  integer | Level 1 wide metric for interface. |
| **wide_metric_l2**  integer | Level 2 wide metric for interface. |
| **isis_net**  list / elements=dictionary | IS-IS net configuration. |
| **id**  integer | ISIS network ID. |
| **net**  string | IS-IS networks (format = xx.xxxx. .xxxx.xx.). |
| **lsp_gen_interval_l1**  integer | Minimum interval for level 1 LSP regenerating. |
| **lsp_gen_interval_l2**  integer | Minimum interval for level 2 LSP regenerating. |
| **lsp_refresh_interval**  integer | LSP refresh time in seconds. |
| **max_lsp_lifetime**  integer | Maximum LSP lifetime in seconds. |
| **metric_style**  string | Use old-style (ISO 10589) or new-style packet formats.  Choices:   - `"narrow"` - `"wide"` - `"transition"` - `"narrow-transition"` - `"narrow-transition-l1"` - `"narrow-transition-l2"` - `"wide-l1"` - `"wide-l2"` - `"wide-transition"` - `"wide-transition-l1"` - `"wide-transition-l2"` - `"transition-l1"` - `"transition-l2"` |
| **overload_bit**  string | Enable/disable signal other routers not to use us in SPF.  Choices:   - `"enable"` - `"disable"` |
| **overload_bit_on_startup**  integer | Overload-bit only temporarily after reboot. |
| **overload_bit_suppress**  list / elements=string | Suppress overload-bit for the specific prefixes.  Choices:   - `"external"` - `"interlevel"` |
| **redistribute**  list / elements=dictionary | IS-IS redistribute protocols. |
| **level**  string | Level.  Choices:   - `"level-1-2"` - `"level-1"` - `"level-2"` |
| **metric**  integer | Metric. |
| **metric_type**  string | Metric type.  Choices:   - `"external"` - `"internal"` |
| **protocol**  string | Protocol name. |
| **routemap**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **redistribute6**  list / elements=dictionary | IS-IS IPv6 redistribution for routing protocols. |
| **level**  string | Level.  Choices:   - `"level-1-2"` - `"level-1"` - `"level-2"` |
| **metric**  integer | Metric. |
| **metric_type**  string | Metric type.  Choices:   - `"external"` - `"internal"` |
| **protocol**  string | Protocol name. |
| **routemap**  string | Route map name. Source router.route-map.name. |
| **status**  string | Enable/disable redistribution.  Choices:   - `"enable"` - `"disable"` |
| **redistribute6_l1**  string | Enable/disable redistribution of level 1 IPv6 routes into level 2.  Choices:   - `"enable"` - `"disable"` |
| **redistribute6_l1_list**  string | Access-list for IPv6 route redistribution from l1 to l2. Source router.access-list6.name. |
| **redistribute6_l2**  string | Enable/disable redistribution of level 2 IPv6 routes into level 1.  Choices:   - `"enable"` - `"disable"` |
| **redistribute6_l2_list**  string | Access-list for IPv6 route redistribution from l2 to l1. Source router.access-list6.name. |
| **redistribute_l1**  string | Enable/disable redistribution of level 1 routes into level 2.  Choices:   - `"enable"` - `"disable"` |
| **redistribute_l1_list**  string | Access-list for route redistribution from l1 to l2. Source router.access-list.name. |
| **redistribute_l2**  string | Enable/disable redistribution of level 2 routes into level 1.  Choices:   - `"enable"` - `"disable"` |
| **redistribute_l2_list**  string | Access-list for route redistribution from l2 to l1. Source router.access-list.name. |
| **spf_interval_exp_l1**  string | Level 1 SPF calculation delay. |
| **spf_interval_exp_l2**  string | Level 2 SPF calculation delay. |
| **summary_address**  list / elements=dictionary | IS-IS summary addresses. |
| **id**  integer | Summary address entry ID. |
| **level**  string | Level.  Choices:   - `"level-1-2"` - `"level-1"` - `"level-2"` |
| **prefix**  string | Prefix. |
| **summary_address6**  list / elements=dictionary | IS-IS IPv6 summary address. |
| **id**  integer | Prefix entry ID. |
| **level**  string | Level.  Choices:   - `"level-1-2"` - `"level-1"` - `"level-2"` |
| **prefix6**  string | IPv6 prefix. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_router_isis_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_isis_module.md#id5)

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
  - name: Configure IS-IS.
    fortios_router_isis:
      vdom:  "{{ vdom }}"
      router_isis:
        adjacency_check: "enable"
        adjacency_check6: "enable"
        adv_passive_only: "enable"
        adv_passive_only6: "enable"
        auth_keychain_l1: "<your_own_value> (source router.key-chain.name)"
        auth_keychain_l2: "<your_own_value> (source router.key-chain.name)"
        auth_mode_l1: "password"
        auth_mode_l2: "password"
        auth_password_l1: "<your_own_value>"
        auth_password_l2: "<your_own_value>"
        auth_sendonly_l1: "enable"
        auth_sendonly_l2: "enable"
        default_originate: "enable"
        default_originate6: "enable"
        dynamic_hostname: "enable"
        ignore_lsp_errors: "enable"
        is_type: "level-1-2"
        isis_interface:
         -
            auth_keychain_l1: "<your_own_value> (source router.key-chain.name)"
            auth_keychain_l2: "<your_own_value> (source router.key-chain.name)"
            auth_mode_l1: "md5"
            auth_mode_l2: "md5"
            auth_password_l1: "<your_own_value>"
            auth_password_l2: "<your_own_value>"
            auth_send_only_l1: "enable"
            auth_send_only_l2: "enable"
            circuit_type: "level-1-2"
            csnp_interval_l1: "10"
            csnp_interval_l2: "10"
            hello_interval_l1: "10"
            hello_interval_l2: "10"
            hello_multiplier_l1: "3"
            hello_multiplier_l2: "3"
            hello_padding: "enable"
            lsp_interval: "33"
            lsp_retransmit_interval: "5"
            mesh_group: "enable"
            mesh_group_id: "0"
            metric_l1: "10"
            metric_l2: "10"
            name: "default_name_43 (source system.interface.name)"
            network_type: "broadcast"
            priority_l1: "64"
            priority_l2: "64"
            status: "enable"
            status6: "enable"
            wide_metric_l1: "10"
            wide_metric_l2: "10"
        isis_net:
         -
            id:  "52"
            net: "<your_own_value>"
        lsp_gen_interval_l1: "30"
        lsp_gen_interval_l2: "30"
        lsp_refresh_interval: "900"
        max_lsp_lifetime: "1200"
        metric_style: "narrow"
        overload_bit: "enable"
        overload_bit_on_startup: "0"
        overload_bit_suppress: "external"
        redistribute:
         -
            level: "level-1-2"
            metric: "0"
            metric_type: "external"
            protocol: "<your_own_value>"
            routemap: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        redistribute_l1: "enable"
        redistribute_l1_list: "<your_own_value> (source router.access-list.name)"
        redistribute_l2: "enable"
        redistribute_l2_list: "<your_own_value> (source router.access-list.name)"
        redistribute6:
         -
            level: "level-1-2"
            metric: "0"
            metric_type: "external"
            protocol: "<your_own_value>"
            routemap: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        redistribute6_l1: "enable"
        redistribute6_l1_list: "<your_own_value> (source router.access-list6.name)"
        redistribute6_l2: "enable"
        redistribute6_l2_list: "<your_own_value> (source router.access-list6.name)"
        spf_interval_exp_l1: "<your_own_value>"
        spf_interval_exp_l2: "<your_own_value>"
        summary_address:
         -
            id:  "87"
            level: "level-1-2"
            prefix: "<your_own_value>"
        summary_address6:
         -
            id:  "91"
            level: "level-1-2"
            prefix6: "<your_own_value>"
```

## [Return Values](fortios_router_isis_module.md#id6)

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
