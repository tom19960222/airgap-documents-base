---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_interface_policy module – Configure IPv4 interface policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_interface_policy_module.html
fetched_at: 2026-07-28T02:24:28+00:00
---
# fortinet.fortios.fortios_firewall_interface_policy module – Configure IPv4 interface policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_interface_policy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-interface-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_interface_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_interface_policy_module.md#synopsis)
- [Requirements](fortios_firewall_interface_policy_module.md#requirements)
- [Parameters](fortios_firewall_interface_policy_module.md#parameters)
- [Notes](fortios_firewall_interface_policy_module.md#notes)
- [Examples](fortios_firewall_interface_policy_module.md#examples)
- [Return Values](fortios_firewall_interface_policy_module.md#return-values)

## [Synopsis](fortios_firewall_interface_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and interface_policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_interface_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_interface_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_interface_policy**  dictionary | Configure IPv4 interface policies. |
| **address_type**  string | Policy address type (IPv4 or IPv6).  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **application_list**  string | Application list name. Source application.list.name. |
| **application_list_status**  string | Enable/disable application control.  **Choices:**   - `"enable"` - `"disable"` |
| **av_profile**  string | Antivirus profile. Source antivirus.profile.name. |
| **av_profile_status**  string | Enable/disable antivirus.  **Choices:**   - `"enable"` - `"disable"` |
| **casb_profile**  string | CASB profile. Source casb.profile.name. |
| **casb_profile_status**  string | Enable/disable CASB.  **Choices:**   - `"enable"` - `"disable"` |
| **comments**  string | Comments. |
| **dlp_profile**  string | DLP profile name. Source dlp.profile.name. |
| **dlp_profile_status**  string | Enable/disable DLP.  **Choices:**   - `"enable"` - `"disable"` |
| **dlp_sensor**  string | DLP sensor name. Source dlp.sensor.name. |
| **dlp_sensor_status**  string | Enable/disable DLP.  **Choices:**   - `"enable"` - `"disable"` |
| **dsri**  string | Enable/disable DSRI.  **Choices:**   - `"enable"` - `"disable"` |
| **dstaddr**  list / elements=dictionary | Address object to limit traffic monitoring to network traffic sent to the specified address or range. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **emailfilter_profile**  string | Email filter profile. Source emailfilter.profile.name. |
| **emailfilter_profile_status**  string | Enable/disable email filter.  **Choices:**   - `"enable"` - `"disable"` |
| **interface**  string | Monitored interface name from available interfaces. Source system.zone.name system.interface.name. |
| **ips_sensor**  string | IPS sensor name. Source ips.sensor.name. |
| **ips_sensor_status**  string | Enable/disable IPS.  **Choices:**   - `"enable"` - `"disable"` |
| **label**  string | Label. |
| **logtraffic**  string | Logging type to be used in this policy (Options: all | utm | disable).  **Choices:**   - `"all"` - `"utm"` - `"disable"` |
| **policyid**  integer / required | Policy ID (0 - 4294967295). see <a href=’#notes’>Notes</a>. |
| **scan_botnet_connections**  string | Enable/disable scanning for connections to Botnet servers.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **service**  list / elements=dictionary | Service object from available options. |
| **name**  string / required | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **spamfilter_profile**  string | Antispam profile. Source spamfilter.profile.name. |
| **spamfilter_profile_status**  string | Enable/disable antispam.  **Choices:**   - `"enable"` - `"disable"` |
| **srcaddr**  list / elements=dictionary | Address object to limit traffic monitoring to network traffic sent from the specified address or range. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **status**  string | Enable/disable this policy.  **Choices:**   - `"enable"` - `"disable"` |
| **webfilter_profile**  string | Web filter profile. Source webfilter.profile.name. |
| **webfilter_profile_status**  string | Enable/disable web filtering.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_interface_policy_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the policyid instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_interface_policy_module.md#id5)

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
  - name: Configure IPv4 interface policies.
    fortios_firewall_interface_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_interface_policy:
        address_type: "ipv4"
        application_list: "<your_own_value> (source application.list.name)"
        application_list_status: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        av_profile_status: "enable"
        casb_profile: "<your_own_value> (source casb.profile.name)"
        casb_profile_status: "enable"
        comments: "<your_own_value>"
        dlp_profile: "<your_own_value> (source dlp.profile.name)"
        dlp_profile_status: "enable"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dlp_sensor_status: "enable"
        dsri: "enable"
        dstaddr:
         -
            name: "default_name_17 (source firewall.address.name firewall.addrgrp.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        emailfilter_profile_status: "enable"
        interface: "<your_own_value> (source system.zone.name system.interface.name)"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        ips_sensor_status: "enable"
        label: "<your_own_value>"
        logtraffic: "all"
        policyid: "<you_own_value>"
        scan_botnet_connections: "disable"
        service:
         -
            name: "default_name_28 (source firewall.service.custom.name firewall.service.group.name)"
        spamfilter_profile: "<your_own_value> (source spamfilter.profile.name)"
        spamfilter_profile_status: "enable"
        srcaddr:
         -
            name: "default_name_32 (source firewall.address.name firewall.addrgrp.name)"
        status: "enable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webfilter_profile_status: "enable"
```

## [Return Values](fortios_firewall_interface_policy_module.md#id6)

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
