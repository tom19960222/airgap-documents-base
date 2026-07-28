---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_router_static6 module – Configure IPv6 static routing tables in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_router_static6_module.html
fetched_at: 2026-07-28T02:26:58+00:00
---
# fortinet.fortios.fortios_router_static6 module – Configure IPv6 static routing tables in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_router_static6_module.md#ansible-collections-fortinet-fortios-fortios-router-static6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_static6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_static6_module.md#synopsis)
- [Requirements](fortios_router_static6_module.md#requirements)
- [Parameters](fortios_router_static6_module.md#parameters)
- [Notes](fortios_router_static6_module.md#notes)
- [Examples](fortios_router_static6_module.md#examples)
- [Return Values](fortios_router_static6_module.md#return-values)

## [Synopsis](fortios_router_static6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and static6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_static6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_router_static6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **router_static6**  dictionary | Configure IPv6 static routing tables. |
| **bfd**  string | Enable/disable Bidirectional Forwarding Detection (BFD).  **Choices:**   - `"enable"` - `"disable"` |
| **blackhole**  string | Enable/disable black hole.  **Choices:**   - `"enable"` - `"disable"` |
| **comment**  string | Optional comments. |
| **device**  string | Gateway out interface or tunnel. Source system.interface.name. |
| **devindex**  integer | Device index (0 - 4294967295). |
| **distance**  integer | Administrative distance (1 - 255). |
| **dst**  string | Destination IPv6 prefix. |
| **dstaddr**  string | Name of firewall address or address group. Source firewall.address6.name firewall.addrgrp6.name. |
| **dynamic_gateway**  string | Enable use of dynamic gateway retrieved from Router Advertisement (RA).  **Choices:**   - `"enable"` - `"disable"` |
| **gateway**  string | IPv6 address of the gateway. |
| **link_monitor_exempt**  string | Enable/disable withdrawal of this static route when link monitor or health check is down.  **Choices:**   - `"enable"` - `"disable"` |
| **priority**  integer | Administrative priority (1 - 65535). |
| **sdwan**  string | Enable/disable egress through the SD-WAN.  **Choices:**   - `"enable"` - `"disable"` |
| **sdwan_zone**  list / elements=dictionary | Choose SD-WAN Zone. |
| **name**  string / required | SD-WAN zone name. Source system.sdwan.zone.name. |
| **seq_num**  integer / required | Sequence number. see <a href=’#notes’>Notes</a>. |
| **status**  string | Enable/disable this static route.  **Choices:**   - `"enable"` - `"disable"` |
| **virtual_wan_link**  string | Enable/disable egress through the virtual-wan-link.  **Choices:**   - `"enable"` - `"disable"` |
| **vrf**  integer | Virtual Routing Forwarding ID. |
| **weight**  integer | Administrative weight (0 - 255). |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_router_static6_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the seq_num instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_static6_module.md#id5)

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
  - name: Configure IPv6 static routing tables.
    fortios_router_static6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      router_static6:
        bfd: "enable"
        blackhole: "enable"
        comment: "Optional comments."
        device: "<your_own_value> (source system.interface.name)"
        devindex: "0"
        distance: "10"
        dst: "<your_own_value>"
        dstaddr: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
        dynamic_gateway: "enable"
        gateway: "<your_own_value>"
        link_monitor_exempt: "enable"
        priority: "1024"
        sdwan: "enable"
        sdwan_zone:
         -
            name: "default_name_17 (source system.sdwan.zone.name)"
        seq_num: "<you_own_value>"
        status: "enable"
        virtual_wan_link: "enable"
        vrf: "unspecified"
        weight: "0"
```

## [Return Values](fortios_router_static6_module.md#id6)

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
