---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_log_threat_weight module – Configure threat weight settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_log_threat_weight_module.html
fetched_at: 2026-07-28T02:26:27+00:00
---
# fortinet.fortios.fortios_log_threat_weight module – Configure threat weight settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_log_threat_weight_module.md#ansible-collections-fortinet-fortios-fortios-log-threat-weight-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_threat_weight`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_log_threat_weight_module.md#synopsis)
- [Requirements](fortios_log_threat_weight_module.md#requirements)
- [Parameters](fortios_log_threat_weight_module.md#parameters)
- [Notes](fortios_log_threat_weight_module.md#notes)
- [Examples](fortios_log_threat_weight_module.md#examples)
- [Return Values](fortios_log_threat_weight_module.md#return-values)

## [Synopsis](fortios_log_threat_weight_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify log feature and threat_weight category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_log_threat_weight_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_log_threat_weight_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **log_threat_weight**  dictionary | Configure threat weight settings. |
| **application**  list / elements=dictionary | Application-control threat weight settings. |
| **category**  integer | Application category. |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **level**  string | Threat weight score for Application events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **blocked_connection**  string | Threat weight score for blocked connections.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **botnet_connection_detected**  string | Threat weight score for detected botnet connections.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **failed_connection**  string | Threat weight score for failed connections.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **geolocation**  list / elements=dictionary | Geolocation-based threat weight settings. |
| **country**  string | Country code. |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **level**  string | Threat weight score for Geolocation-based events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **ips**  dictionary | IPS threat weight settings. |
| **critical_severity**  string | Threat weight score for IPS critical severity events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **high_severity**  string | Threat weight score for IPS high severity events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **info_severity**  string | Threat weight score for IPS info severity events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **low_severity**  string | Threat weight score for IPS low severity events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **medium_severity**  string | Threat weight score for IPS medium severity events.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **level**  dictionary | Score mapping for threat weight levels. |
| **critical**  integer | Critical level score value (1 - 100). |
| **high**  integer | High level score value (1 - 100). |
| **low**  integer | Low level score value (1 - 100). |
| **medium**  integer | Medium level score value (1 - 100). |
| **malware**  dictionary | Anti-virus malware threat weight settings. |
| **botnet_connection**  string | Threat weight score for detected botnet connections.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **command_blocked**  string | Threat weight score for blocked command detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **content_disarm**  string | Threat weight score for virus (content disarm) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **ems_threat_feed**  string | Threat weight score for virus (EMS threat feed) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **file_blocked**  string | Threat weight score for blocked file detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **fortiai**  string | Threat weight score for FortiAI-detected virus.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **fortindr**  string | Threat weight score for FortiNDR-detected virus.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **fortisandbox**  string | Threat weight score for FortiSandbox-detected virus.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **fsa_high_risk**  string | Threat weight score for FortiSandbox high risk malware detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **fsa_malicious**  string | Threat weight score for FortiSandbox malicious malware detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **fsa_medium_risk**  string | Threat weight score for FortiSandbox medium risk malware detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **inline_block**  string | Threat weight score for malware detected by inline block.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **malware_list**  string | Threat weight score for virus (malware list) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **mimefragmented**  string | Threat weight score for mimefragmented detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **oversized**  string | Threat weight score for oversized file detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **switch_proto**  string | Threat weight score for switch proto detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **virus_blocked**  string | Threat weight score for virus (blocked) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **virus_file_type_executable**  string | Threat weight score for virus (file type executable) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **virus_infected**  string | Threat weight score for virus (infected) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **virus_outbreak_prevention**  string | Threat weight score for virus (outbreak prevention) event.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **virus_scan_error**  string | Threat weight score for virus (scan error) detected.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **status**  string | Enable/disable the threat weight feature.  **Choices:**   - `"enable"` - `"disable"` |
| **url_block_detected**  string | Threat weight score for URL blocking.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **web**  list / elements=dictionary | Web filtering threat weight settings. |
| **category**  integer | Threat weight score for web category filtering matches. |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **level**  string | Threat weight score for web category filtering matches.  **Choices:**   - `"disable"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_log_threat_weight_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_log_threat_weight_module.md#id5)

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
  - name: Configure threat weight settings.
    fortios_log_threat_weight:
      vdom:  "{{ vdom }}"
      log_threat_weight:
        application:
         -
            category: "0"
            id:  "5"
            level: "disable"
        blocked_connection: "disable"
        botnet_connection_detected: "disable"
        failed_connection: "disable"
        geolocation:
         -
            country: "<your_own_value>"
            id:  "12"
            level: "disable"
        ips:
            critical_severity: "disable"
            high_severity: "disable"
            info_severity: "disable"
            low_severity: "disable"
            medium_severity: "disable"
        level:
            critical: "50"
            high: "30"
            low: "5"
            medium: "10"
        malware:
            botnet_connection: "disable"
            command_blocked: "disable"
            content_disarm: "disable"
            ems_threat_feed: "disable"
            file_blocked: "disable"
            fortiai: "disable"
            fortindr: "disable"
            fortisandbox: "disable"
            fsa_high_risk: "disable"
            fsa_malicious: "disable"
            fsa_medium_risk: "disable"
            inline_block: "disable"
            malware_list: "disable"
            mimefragmented: "disable"
            oversized: "disable"
            switch_proto: "disable"
            virus_blocked: "disable"
            virus_file_type_executable: "disable"
            virus_infected: "disable"
            virus_outbreak_prevention: "disable"
            virus_scan_error: "disable"
        status: "enable"
        url_block_detected: "disable"
        web:
         -
            category: "0"
            id:  "51"
            level: "disable"
```

## [Return Values](fortios_log_threat_weight_module.md#id6)

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
