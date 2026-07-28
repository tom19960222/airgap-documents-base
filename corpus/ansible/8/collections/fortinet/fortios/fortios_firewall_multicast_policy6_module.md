---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_multicast_policy6 module – Configure IPv6 multicast NAT policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_multicast_policy6_module.html
fetched_at: 2026-07-28T02:24:51+00:00
---
# fortinet.fortios.fortios_firewall_multicast_policy6 module – Configure IPv6 multicast NAT policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_multicast_policy6_module.md#ansible-collections-fortinet-fortios-fortios-firewall-multicast-policy6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_multicast_policy6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_multicast_policy6_module.md#synopsis)
- [Requirements](fortios_firewall_multicast_policy6_module.md#requirements)
- [Parameters](fortios_firewall_multicast_policy6_module.md#parameters)
- [Notes](fortios_firewall_multicast_policy6_module.md#notes)
- [Examples](fortios_firewall_multicast_policy6_module.md#examples)
- [Return Values](fortios_firewall_multicast_policy6_module.md#return-values)

## [Synopsis](fortios_firewall_multicast_policy6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and multicast_policy6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_multicast_policy6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_multicast_policy6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_multicast_policy6**  dictionary | Configure IPv6 multicast NAT policies. |
| **action**  string | Accept or deny traffic matching the policy.  **Choices:**   - `"accept"` - `"deny"` |
| **auto_asic_offload**  string | Enable/disable offloading policy traffic for hardware acceleration.  **Choices:**   - `"enable"` - `"disable"` |
| **comments**  string | Comment. |
| **dstaddr**  list / elements=dictionary | IPv6 destination address name. |
| **name**  string / required | Address name. Source firewall.multicast-address6.name. |
| **dstintf**  string | IPv6 destination interface name. Source system.interface.name system.zone.name. |
| **end_port**  integer | Integer value for ending TCP/UDP/SCTP destination port in range (1 - 65535). |
| **id**  integer / required | Policy ID (0 - 4294967294). see <a href=’#notes’>Notes</a>. |
| **logtraffic**  string | Enable/disable logging traffic accepted by this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string | Policy name. |
| **protocol**  integer | Integer value for the protocol type as defined by IANA (0 - 255). |
| **srcaddr**  list / elements=dictionary | IPv6 source address name. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **srcintf**  string | IPv6 source interface name. Source system.interface.name system.zone.name. |
| **start_port**  integer | Integer value for starting TCP/UDP/SCTP destination port in range (1 - 65535). |
| **status**  string | Enable/disable this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_multicast_policy6_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_multicast_policy6_module.md#id5)

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
  - name: Configure IPv6 multicast NAT policies.
    fortios_firewall_multicast_policy6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_multicast_policy6:
        action: "accept"
        auto_asic_offload: "enable"
        comments: "<your_own_value>"
        dstaddr:
         -
            name: "default_name_7 (source firewall.multicast-address6.name)"
        dstintf: "<your_own_value> (source system.interface.name system.zone.name)"
        end_port: "65535"
        id:  "10"
        logtraffic: "enable"
        name: "default_name_12"
        protocol: "0"
        srcaddr:
         -
            name: "default_name_15 (source firewall.address6.name firewall.addrgrp6.name)"
        srcintf: "<your_own_value> (source system.interface.name system.zone.name)"
        start_port: "1"
        status: "enable"
        uuid: "<your_own_value>"
```

## [Return Values](fortios_firewall_multicast_policy6_module.md#id6)

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
