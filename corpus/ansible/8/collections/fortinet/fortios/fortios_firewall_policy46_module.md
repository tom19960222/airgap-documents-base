---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_policy46 module – Configure IPv4 to IPv6 policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_policy46_module.html
fetched_at: 2026-07-28T02:24:54+00:00
---
# fortinet.fortios.fortios_firewall_policy46 module – Configure IPv4 to IPv6 policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_policy46_module.md#ansible-collections-fortinet-fortios-fortios-firewall-policy46-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_policy46`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_policy46_module.md#synopsis)
- [Requirements](fortios_firewall_policy46_module.md#requirements)
- [Parameters](fortios_firewall_policy46_module.md#parameters)
- [Notes](fortios_firewall_policy46_module.md#notes)
- [Examples](fortios_firewall_policy46_module.md#examples)
- [Return Values](fortios_firewall_policy46_module.md#return-values)

## [Synopsis](fortios_firewall_policy46_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and policy46 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_policy46_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_policy46_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_policy46**  dictionary | Configure IPv4 to IPv6 policies. |
| **action**  string | Accept or deny traffic matching the policy.  **Choices:**   - `"accept"` - `"deny"` |
| **comments**  string | Comment. |
| **dstaddr**  list / elements=dictionary | Destination address objects. |
| **name**  string / required | Address name. Source firewall.vip46.name firewall.vipgrp46.name. |
| **dstintf**  string | Destination interface name. Source system.interface.name system.zone.name. |
| **fixedport**  string | Enable/disable fixed port for this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **ippool**  string | Enable/disable use of IP Pools for source NAT.  **Choices:**   - `"enable"` - `"disable"` |
| **logtraffic**  string | Enable/disable traffic logging for this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **logtraffic_start**  string | Record logs when a session starts and ends.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string | Policy name. |
| **per_ip_shaper**  string | Per IP traffic shaper. Source firewall.shaper.per-ip-shaper.name. |
| **permit_any_host**  string | Enable/disable allowing any host.  **Choices:**   - `"enable"` - `"disable"` |
| **policyid**  integer / required | Policy ID (0 - 4294967294). see <a href=’#notes’>Notes</a>. |
| **poolname**  list / elements=dictionary | IP Pool names. |
| **name**  string / required | IP pool name. Source firewall.ippool6.name. |
| **schedule**  string | Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **service**  list / elements=dictionary | Service name. |
| **name**  string / required | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **srcaddr**  list / elements=dictionary | Source address objects. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **srcintf**  string | Source interface name. Source system.zone.name system.interface.name. |
| **status**  string | Enable/disable this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **tcp_mss_receiver**  integer | TCP Maximum Segment Size value of receiver (0 - 65535) |
| **tcp_mss_sender**  integer | TCP Maximum Segment Size value of sender (0 - 65535). |
| **traffic_shaper**  string | Traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **traffic_shaper_reverse**  string | Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_policy46_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the policyid instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_policy46_module.md#id5)

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
  - name: Configure IPv4 to IPv6 policies.
    fortios_firewall_policy46:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_policy46:
        action: "accept"
        comments: "<your_own_value>"
        dstaddr:
         -
            name: "default_name_6 (source firewall.vip46.name firewall.vipgrp46.name)"
        dstintf: "<your_own_value> (source system.interface.name system.zone.name)"
        fixedport: "enable"
        ippool: "enable"
        logtraffic: "enable"
        logtraffic_start: "enable"
        name: "default_name_12"
        per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
        permit_any_host: "enable"
        policyid: "<you_own_value>"
        poolname:
         -
            name: "default_name_17 (source firewall.ippool6.name)"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        service:
         -
            name: "default_name_20 (source firewall.service.custom.name firewall.service.group.name)"
        srcaddr:
         -
            name: "default_name_22 (source firewall.address.name firewall.addrgrp.name)"
        srcintf: "<your_own_value> (source system.zone.name system.interface.name)"
        status: "enable"
        tcp_mss_receiver: "0"
        tcp_mss_sender: "0"
        traffic_shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        uuid: "<your_own_value>"
```

## [Return Values](fortios_firewall_policy46_module.md#id6)

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
