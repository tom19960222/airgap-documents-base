---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_multicast6 module – Configure IPv6 multicast in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_multicast6_module.html
fetched_at: 2026-07-28T02:26:48+00:00
---
# fortinet.fortios.fortios_router_multicast6 module – Configure IPv6 multicast in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_router_multicast6_module.md#ansible-collections-fortinet-fortios-fortios-router-multicast6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_multicast6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_multicast6_module.md#synopsis)
- [Requirements](fortios_router_multicast6_module.md#requirements)
- [Parameters](fortios_router_multicast6_module.md#parameters)
- [Notes](fortios_router_multicast6_module.md#notes)
- [Examples](fortios_router_multicast6_module.md#examples)
- [Return Values](fortios_router_multicast6_module.md#return-values)

## [Synopsis](fortios_router_multicast6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and multicast6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_multicast6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_multicast6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_multicast6**  dictionary | Configure IPv6 multicast. |
| **interface**  list / elements=dictionary | Protocol Independent Multicast (PIM) interfaces. |
| **hello_holdtime**  integer | Time before old neighbor information expires in seconds (1 - 65535). |
| **hello_interval**  integer | Interval between sending PIM hello messages in seconds (1 - 65535). |
| **name**  string / required | Interface name. Source system.interface.name. |
| **multicast_pmtu**  string | Enable/disable PMTU for IPv6 multicast.  **Choices:**   - `"enable"` - `"disable"` |
| **multicast_routing**  string | Enable/disable IPv6 multicast routing.  **Choices:**   - `"enable"` - `"disable"` |
| **pim_sm_global**  dictionary | PIM sparse-mode global settings. |
| **register_rate_limit**  integer | Limit of packets/sec per source registered through this RP (0 means unlimited). |
| **rp_address**  list / elements=dictionary | Statically configured RP addresses. |
| **id**  integer / required | ID of the entry. see <a href=’#notes’>Notes</a>. |
| **ip6_address**  string | RP router IPv6 address. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_multicast6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_multicast6_module.md#id5)

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
  - name: Configure IPv6 multicast.
    fortios_router_multicast6:
      vdom:  "{{ vdom }}"
      router_multicast6:
        interface:
         -
            hello_holdtime: ""
            hello_interval: "30"
            name: "default_name_6 (source system.interface.name)"
        multicast_pmtu: "enable"
        multicast_routing: "enable"
        pim_sm_global:
            register_rate_limit: "0"
            rp_address:
             -
                id:  "12"
                ip6_address: "<your_own_value>"
```

## [Return Values](fortios_router_multicast6_module.md#id6)

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
