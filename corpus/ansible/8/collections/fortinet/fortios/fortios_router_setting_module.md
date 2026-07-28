---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_setting module – Configure router settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_setting_module.html
fetched_at: 2026-07-28T02:26:56+00:00
---
# fortinet.fortios.fortios_router_setting module – Configure router settings in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_setting_module.md#ansible-collections-fortinet-fortios-fortios-router-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_setting_module.md#synopsis)
- [Requirements](fortios_router_setting_module.md#requirements)
- [Parameters](fortios_router_setting_module.md#parameters)
- [Notes](fortios_router_setting_module.md#notes)
- [Examples](fortios_router_setting_module.md#examples)
- [Return Values](fortios_router_setting_module.md#return-values)

## [Synopsis](fortios_router_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_setting**  dictionary | Configure router settings. |
| **bgp_debug_flags**  string | bgp_debug_flags |
| **hostname**  string | Hostname for this virtual domain router. |
| **igmp_debug_flags**  string | igmp_debug_flags |
| **imi_debug_flags**  string | imi_debug_flags |
| **isis_debug_flags**  string | isis_debug_flags |
| **ospf6_debug_events_flags**  string | ospf6_debug_events_flags |
| **ospf6_debug_ifsm_flags**  string | ospf6_debug_ifsm_flags |
| **ospf6_debug_lsa_flags**  string | ospf6_debug_lsa_flags |
| **ospf6_debug_nfsm_flags**  string | ospf6_debug_nfsm_flags |
| **ospf6_debug_nsm_flags**  string | ospf6_debug_nsm_flags |
| **ospf6_debug_packet_flags**  string | ospf6_debug_packet_flags |
| **ospf6_debug_route_flags**  string | ospf6_debug_route_flags |
| **ospf_debug_events_flags**  string | ospf_debug_events_flags |
| **ospf_debug_ifsm_flags**  string | ospf_debug_ifsm_flags |
| **ospf_debug_lsa_flags**  string | ospf_debug_lsa_flags |
| **ospf_debug_nfsm_flags**  string | ospf_debug_nfsm_flags |
| **ospf_debug_nsm_flags**  string | ospf_debug_nsm_flags |
| **ospf_debug_packet_flags**  string | ospf_debug_packet_flags |
| **ospf_debug_route_flags**  string | ospf_debug_route_flags |
| **pimdm_debug_flags**  string | pimdm_debug_flags |
| **pimsm_debug_joinprune_flags**  string | pimsm_debug_joinprune_flags |
| **pimsm_debug_simple_flags**  string | pimsm_debug_simple_flags |
| **pimsm_debug_timer_flags**  string | pimsm_debug_timer_flags |
| **rip_debug_flags**  string | rip_debug_flags |
| **ripng_debug_flags**  string | ripng_debug_flags |
| **show_filter**  string | Prefix-list as filter for showing routes. Source router.prefix-list.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_setting_module.md#id5)

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
  - name: Configure router settings.
    fortios_router_setting:
      vdom:  "{{ vdom }}"
      router_setting:
        bgp_debug_flags: "<your_own_value>"
        hostname: "myhostname"
        igmp_debug_flags: "<your_own_value>"
        imi_debug_flags: "<your_own_value>"
        isis_debug_flags: "<your_own_value>"
        ospf_debug_events_flags: "<your_own_value>"
        ospf_debug_ifsm_flags: "<your_own_value>"
        ospf_debug_lsa_flags: "<your_own_value>"
        ospf_debug_nfsm_flags: "<your_own_value>"
        ospf_debug_nsm_flags: "<your_own_value>"
        ospf_debug_packet_flags: "<your_own_value>"
        ospf_debug_route_flags: "<your_own_value>"
        ospf6_debug_events_flags: "<your_own_value>"
        ospf6_debug_ifsm_flags: "<your_own_value>"
        ospf6_debug_lsa_flags: "<your_own_value>"
        ospf6_debug_nfsm_flags: "<your_own_value>"
        ospf6_debug_nsm_flags: "<your_own_value>"
        ospf6_debug_packet_flags: "<your_own_value>"
        ospf6_debug_route_flags: "<your_own_value>"
        pimdm_debug_flags: "<your_own_value>"
        pimsm_debug_joinprune_flags: "<your_own_value>"
        pimsm_debug_simple_flags: "<your_own_value>"
        pimsm_debug_timer_flags: "<your_own_value>"
        rip_debug_flags: "<your_own_value>"
        ripng_debug_flags: "<your_own_value>"
        show_filter: "<your_own_value> (source router.prefix-list.name)"
```

## [Return Values](fortios_router_setting_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
