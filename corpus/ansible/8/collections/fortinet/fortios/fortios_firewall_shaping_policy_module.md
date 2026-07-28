---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_shaping_policy module – Configure shaping policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_shaping_policy_module.html
fetched_at: 2026-07-28T02:25:09+00:00
---
# fortinet.fortios.fortios_firewall_shaping_policy module – Configure shaping policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_shaping_policy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-shaping-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_shaping_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_shaping_policy_module.md#synopsis)
- [Requirements](fortios_firewall_shaping_policy_module.md#requirements)
- [Parameters](fortios_firewall_shaping_policy_module.md#parameters)
- [Notes](fortios_firewall_shaping_policy_module.md#notes)
- [Examples](fortios_firewall_shaping_policy_module.md#examples)
- [Return Values](fortios_firewall_shaping_policy_module.md#return-values)

## [Synopsis](fortios_firewall_shaping_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and shaping_policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_shaping_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_shaping_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **action**  string | the action indiactor to move an object in the list  **Choices:**   - `"move"` |
| **after**  string | mkey of target identifier |
| **before**  string | mkey of target identifier |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_shaping_policy**  dictionary | Configure shaping policies. |
| **app_category**  list / elements=dictionary | IDs of one or more application categories that this shaper applies application control traffic shaping to. |
| **id**  integer / required | Category IDs. see <a href=’#notes’>Notes</a>. |
| **app_group**  list / elements=dictionary | One or more application group names. |
| **name**  string / required | Application group name. Source application.group.name. |
| **application**  list / elements=dictionary | IDs of one or more applications that this shaper applies application control traffic shaping to. |
| **id**  integer / required | Application IDs. see <a href=’#notes’>Notes</a>. |
| **class_id**  integer | Traffic class ID. Source firewall.traffic-class.class-id. |
| **comment**  string | Comments. |
| **cos**  string | VLAN CoS bit pattern. |
| **cos_mask**  string | VLAN CoS evaluated bits. |
| **diffserv_forward**  string | Enable to change packet”s DiffServ values to the specified diffservcode-forward value.  **Choices:**   - `"enable"` - `"disable"` |
| **diffserv_reverse**  string | Enable to change packet”s reverse (reply) DiffServ values to the specified diffservcode-rev value.  **Choices:**   - `"enable"` - `"disable"` |
| **diffservcode_forward**  string | Change packet”s DiffServ to this value. |
| **diffservcode_rev**  string | Change packet”s reverse (reply) DiffServ to this value. |
| **dstaddr**  list / elements=dictionary | IPv4 destination address and address group names. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **dstaddr6**  list / elements=dictionary | IPv6 destination address and address group names. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **dstintf**  list / elements=dictionary | One or more outgoing (egress) interfaces. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **groups**  list / elements=dictionary | Apply this traffic shaping policy to user groups that have authenticated with the FortiGate. |
| **name**  string / required | Group name. Source user.group.name. |
| **id**  integer / required | Shaping policy ID (0 - 4294967295). see <a href=’#notes’>Notes</a>. |
| **internet_service**  string | Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service_custom**  list / elements=dictionary | Custom Internet Service name. |
| **name**  string / required | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_custom_group**  list / elements=dictionary | Custom Internet Service group name. |
| **name**  string / required | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string / required | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_id**  list / elements=dictionary | Internet Service ID. |
| **id**  integer / required | Internet Service ID. see <a href=’#notes’>Notes</a>. Source firewall.internet-service.id. |
| **internet_service_name**  list / elements=dictionary | Internet Service ID. |
| **name**  string / required | Internet Service name. Source firewall.internet-service-name.name. |
| **internet_service_src**  string | Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  **Choices:**   - `"enable"` - `"disable"` |
| **internet_service_src_custom**  list / elements=dictionary | Custom Internet Service source name. |
| **name**  string / required | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_src_custom_group**  list / elements=dictionary | Custom Internet Service source group name. |
| **name**  string / required | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_src_group**  list / elements=dictionary | Internet Service source group name. |
| **name**  string / required | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_src_id**  list / elements=dictionary | Internet Service source ID. |
| **id**  integer / required | Internet Service ID. see <a href=’#notes’>Notes</a>. Source firewall.internet-service.id. |
| **internet_service_src_name**  list / elements=dictionary | Internet Service source name. |
| **name**  string / required | Internet Service name. Source firewall.internet-service-name.name. |
| **ip_version**  string | Apply this traffic shaping policy to IPv4 or IPv6 traffic.  **Choices:**   - `"4"` - `"6"` |
| **name**  string | Shaping policy name. |
| **per_ip_shaper**  string | Per-IP traffic shaper to apply with this policy. Source firewall.shaper.per-ip-shaper.name. |
| **schedule**  string | Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **service**  list / elements=dictionary | Service and service group names. |
| **name**  string / required | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **srcaddr**  list / elements=dictionary | IPv4 source address and address group names. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **srcaddr6**  list / elements=dictionary | IPv6 source address and address group names. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **srcintf**  list / elements=dictionary | One or more incoming (ingress) interfaces. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **status**  string | Enable/disable this traffic shaping policy.  **Choices:**   - `"enable"` - `"disable"` |
| **tos**  string | ToS (Type of Service) value used for comparison. |
| **tos_mask**  string | Non-zero bit positions are used for comparison while zero bit positions are ignored. |
| **tos_negate**  string | Enable negated TOS match.  **Choices:**   - `"enable"` - `"disable"` |
| **traffic_shaper**  string | Traffic shaper to apply to traffic forwarded by the firewall policy. Source firewall.shaper.traffic-shaper.name. |
| **traffic_shaper_reverse**  string | Traffic shaper to apply to response traffic received by the firewall policy. Source firewall.shaper.traffic-shaper.name. |
| **traffic_type**  string | Traffic type.  **Choices:**   - `"forwarding"` - `"local-in"` - `"local-out"` |
| **url_category**  list / elements=dictionary | IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to. |
| **id**  integer / required | URL category ID. see <a href=’#notes’>Notes</a>. |
| **users**  list / elements=dictionary | Apply this traffic shaping policy to individual users that have authenticated with the FortiGate. |
| **name**  string / required | User name. Source user.local.name. |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **self**  string | mkey of self identifier |
| **state**  string | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_shaping_policy_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks
> - Adjust object order by moving self after(before) another.
> - Only one of [after, before] must be specified when action is moving an object.

## [Examples](fortios_firewall_shaping_policy_module.md#id5)

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
  - name: Configure shaping policies.
    fortios_firewall_shaping_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_shaping_policy:
        app_category:
         -
            id:  "4"
        app_group:
         -
            name: "default_name_6 (source application.group.name)"
        application:
         -
            id:  "8"
        class_id: "0"
        comment: "Comments."
        cos: "<your_own_value>"
        cos_mask: "<your_own_value>"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        dstaddr:
         -
            name: "default_name_18 (source firewall.address.name firewall.addrgrp.name)"
        dstaddr6:
         -
            name: "default_name_20 (source firewall.address6.name firewall.addrgrp6.name)"
        dstintf:
         -
            name: "default_name_22 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        groups:
         -
            name: "default_name_24 (source user.group.name)"
        id:  "25"
        internet_service: "enable"
        internet_service_custom:
         -
            name: "default_name_28 (source firewall.internet-service-custom.name)"
        internet_service_custom_group:
         -
            name: "default_name_30 (source firewall.internet-service-custom-group.name)"
        internet_service_group:
         -
            name: "default_name_32 (source firewall.internet-service-group.name)"
        internet_service_id:
         -
            id:  "34 (source firewall.internet-service.id)"
        internet_service_name:
         -
            name: "default_name_36 (source firewall.internet-service-name.name)"
        internet_service_src: "enable"
        internet_service_src_custom:
         -
            name: "default_name_39 (source firewall.internet-service-custom.name)"
        internet_service_src_custom_group:
         -
            name: "default_name_41 (source firewall.internet-service-custom-group.name)"
        internet_service_src_group:
         -
            name: "default_name_43 (source firewall.internet-service-group.name)"
        internet_service_src_id:
         -
            id:  "45 (source firewall.internet-service.id)"
        internet_service_src_name:
         -
            name: "default_name_47 (source firewall.internet-service-name.name)"
        ip_version: "4"
        name: "default_name_49"
        per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        service:
         -
            name: "default_name_53 (source firewall.service.custom.name firewall.service.group.name)"
        srcaddr:
         -
            name: "default_name_55 (source firewall.address.name firewall.addrgrp.name)"
        srcaddr6:
         -
            name: "default_name_57 (source firewall.address6.name firewall.addrgrp6.name)"
        srcintf:
         -
            name: "default_name_59 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        status: "enable"
        tos: "<your_own_value>"
        tos_mask: "<your_own_value>"
        tos_negate: "enable"
        traffic_shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_type: "forwarding"
        url_category:
         -
            id:  "68"
        users:
         -
            name: "default_name_70 (source user.local.name)"
        uuid: "<your_own_value>"

  - name: move firewall.shaping_policy
    fortios_firewall_shaping_policy:
      vdom:  "root"
      action: "move"
      self: "<mkey of self identifier>"
      after: "<mkey of target identifier>"
     #before: "<mkey of target identifier>"
```

## [Return Values](fortios_firewall_shaping_policy_module.md#id6)

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
