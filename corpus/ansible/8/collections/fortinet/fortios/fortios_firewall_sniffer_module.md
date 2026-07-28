---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_sniffer module – Configure sniffer in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_sniffer_module.html
fetched_at: 2026-07-28T02:25:10+00:00
---
# fortinet.fortios.fortios_firewall_sniffer module – Configure sniffer in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_sniffer_module.md#ansible-collections-fortinet-fortios-fortios-firewall-sniffer-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_sniffer`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_sniffer_module.md#synopsis)
- [Requirements](fortios_firewall_sniffer_module.md#requirements)
- [Parameters](fortios_firewall_sniffer_module.md#parameters)
- [Notes](fortios_firewall_sniffer_module.md#notes)
- [Examples](fortios_firewall_sniffer_module.md#examples)
- [Return Values](fortios_firewall_sniffer_module.md#return-values)

## [Synopsis](fortios_firewall_sniffer_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and sniffer category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_sniffer_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_sniffer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_sniffer**  dictionary | Configure sniffer. |
| **anomaly**  list / elements=dictionary | Configuration method to edit Denial of Service (DoS) anomaly settings. |
| **action**  string | Action taken when the threshold is reached.  **Choices:**   - `"pass"` - `"block"` - `"proxy"` |
| **log**  string | Enable/disable anomaly logging.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Anomaly name. |
| **quarantine**  string | Quarantine method.  **Choices:**   - `"none"` - `"attacker"` |
| **quarantine_expiry**  string | Duration of quarantine. (Format |
| **quarantine_log**  string | Enable/disable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this anomaly.  **Choices:**   - `"disable"` - `"enable"` |
| **threshold**  integer | Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action. |
| **threshold_default**  integer | Number of detected instances per minute which triggers action (1 - 2147483647). Note that each anomaly has a different threshold value assigned to it. |
| **application_list**  string | Name of an existing application list. Source application.list.name. |
| **application_list_status**  string | Enable/disable application control profile.  **Choices:**   - `"enable"` - `"disable"` |
| **av_profile**  string | Name of an existing antivirus profile. Source antivirus.profile.name. |
| **av_profile_status**  string | Enable/disable antivirus profile.  **Choices:**   - `"enable"` - `"disable"` |
| **casb_profile**  string | Name of an existing CASB profile. Source casb.profile.name. |
| **casb_profile_status**  string | Enable/disable CASB profile.  **Choices:**   - `"enable"` - `"disable"` |
| **dlp_profile**  string | Name of an existing DLP profile. Source dlp.profile.name. |
| **dlp_profile_status**  string | Enable/disable DLP profile.  **Choices:**   - `"enable"` - `"disable"` |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dlp_sensor_status**  string | Enable/disable DLP sensor.  **Choices:**   - `"enable"` - `"disable"` |
| **dsri**  string | Enable/disable DSRI.  **Choices:**   - `"enable"` - `"disable"` |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **emailfilter_profile_status**  string | Enable/disable emailfilter.  **Choices:**   - `"enable"` - `"disable"` |
| **file_filter_profile**  string | Name of an existing file-filter profile. Source file-filter.profile.name. |
| **file_filter_profile_status**  string | Enable/disable file filter.  **Choices:**   - `"enable"` - `"disable"` |
| **host**  string | Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240). |
| **id**  integer / required | Sniffer ID (0 - 9999). see <a href=’#notes’>Notes</a>. |
| **interface**  string | Interface name that traffic sniffing will take place on. Source system.interface.name. |
| **ip_threatfeed**  list / elements=dictionary | Name of an existing IP threat feed. |
| **name**  string / required | Threat feed name. Source system.external-resource.name. |
| **ip_threatfeed_status**  string | Enable/disable IP threat feed.  **Choices:**   - `"enable"` - `"disable"` |
| **ips_dos_status**  string | Enable/disable IPS DoS anomaly detection.  **Choices:**   - `"enable"` - `"disable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **ips_sensor_status**  string | Enable/disable IPS sensor.  **Choices:**   - `"enable"` - `"disable"` |
| **ipv6**  string | Enable/disable sniffing IPv6 packets.  **Choices:**   - `"enable"` - `"disable"` |
| **logtraffic**  string | Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy.  **Choices:**   - `"all"` - `"utm"` - `"disable"` |
| **max_packet_count**  integer | Maximum packet count (1 - 1000000). |
| **non_ip**  string | Enable/disable sniffing non-IP packets.  **Choices:**   - `"enable"` - `"disable"` |
| **port**  string | Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200). |
| **protocol**  string | Integer value for the protocol type as defined by IANA (0 - 255). |
| **scan_botnet_connections**  string | Enable/disable scanning of connections to Botnet servers.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **spamfilter_profile**  string | Name of an existing spam filter profile. Source spamfilter.profile.name. |
| **spamfilter_profile_status**  string | Enable/disable spam filter.  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable the active status of the sniffer.  **Choices:**   - `"enable"` - `"disable"` |
| **vlan**  string | List of VLANs to sniff. |
| **webfilter_profile**  string | Name of an existing web filter profile. Source webfilter.profile.name. |
| **webfilter_profile_status**  string | Enable/disable web filter profile.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_sniffer_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_sniffer_module.md#id5)

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
  - name: Configure sniffer.
    fortios_firewall_sniffer:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_sniffer:
        anomaly:
         -
            action: "pass"
            log: "enable"
            name: "default_name_6"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            status: "disable"
            threshold: "0"
            threshold_default: "0"
        application_list: "<your_own_value> (source application.list.name)"
        application_list_status: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        av_profile_status: "enable"
        casb_profile: "<your_own_value> (source casb.profile.name)"
        casb_profile_status: "enable"
        dlp_profile: "<your_own_value> (source dlp.profile.name)"
        dlp_profile_status: "enable"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dlp_sensor_status: "enable"
        dsri: "enable"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        emailfilter_profile_status: "enable"
        file_filter_profile: "<your_own_value> (source file-filter.profile.name)"
        file_filter_profile_status: "enable"
        host: "myhostname"
        id:  "29"
        interface: "<your_own_value> (source system.interface.name)"
        ip_threatfeed:
         -
            name: "default_name_32 (source system.external-resource.name)"
        ip_threatfeed_status: "enable"
        ips_dos_status: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        ips_sensor_status: "enable"
        ipv6: "enable"
        logtraffic: "all"
        max_packet_count: "4000"
        non_ip: "enable"
        port: "<your_own_value>"
        protocol: "<your_own_value>"
        scan_botnet_connections: "disable"
        spamfilter_profile: "<your_own_value> (source spamfilter.profile.name)"
        spamfilter_profile_status: "enable"
        status: "enable"
        vlan: "<your_own_value>"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webfilter_profile_status: "enable"
```

## [Return Values](fortios_firewall_sniffer_module.md#id6)

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
