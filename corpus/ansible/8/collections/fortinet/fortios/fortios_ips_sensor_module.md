---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_ips_sensor module – Configure IPS sensor in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_ips_sensor_module.html
fetched_at: 2026-07-28T02:25:42+00:00
---
# fortinet.fortios.fortios_ips_sensor module – Configure IPS sensor in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_ips_sensor_module.md#ansible-collections-fortinet-fortios-fortios-ips-sensor-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_ips_sensor`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_ips_sensor_module.md#synopsis)
- [Requirements](fortios_ips_sensor_module.md#requirements)
- [Parameters](fortios_ips_sensor_module.md#parameters)
- [Notes](fortios_ips_sensor_module.md#notes)
- [Examples](fortios_ips_sensor_module.md#examples)
- [Return Values](fortios_ips_sensor_module.md#return-values)

## [Synopsis](fortios_ips_sensor_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify ips feature and sensor category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_ips_sensor_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_ips_sensor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **ips_sensor**  dictionary | Configure IPS sensor. |
| **block_malicious_url**  string | Enable/disable malicious URL blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **entries**  list / elements=dictionary | IPS sensor filter. |
| **action**  string | Action taken with traffic in which signatures are detected.  **Choices:**   - `"pass"` - `"block"` - `"reset"` - `"default"` |
| **application**  list / elements=string | Operating systems to be protected. Use all for every application and other for unlisted application. |
| **cve**  list / elements=dictionary | List of CVE IDs of the signatures to add to the sensor. |
| **cve_entry**  string / required | CVE IDs or CVE wildcards. |
| **default_action**  string | Signature default action filter.  **Choices:**   - `"all"` - `"pass"` - `"block"` |
| **default_status**  string | Signature default status filter.  **Choices:**   - `"all"` - `"enable"` - `"disable"` |
| **exempt_ip**  list / elements=dictionary | Traffic from selected source or destination IP addresses is exempt from this signature. |
| **dst_ip**  string | Destination IP address and netmask (applies to packet matching the signature). |
| **id**  integer / required | Exempt IP ID. see <a href=’#notes’>Notes</a>. |
| **src_ip**  string | Source IP address and netmask (applies to packet matching the signature). |
| **id**  integer / required | Rule ID in IPS database (0 - 4294967295). see <a href=’#notes’>Notes</a>. |
| **last_modified**  string | Filter by signature last modified date. Formats: before <date>, after <date>, between <start-date> <end-date>. |
| **location**  list / elements=string | Protect client or server traffic. |
| **log**  string | Enable/disable logging of signatures included in filter.  **Choices:**   - `"disable"` - `"enable"` |
| **log_attack_context**  string | Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer.  **Choices:**   - `"disable"` - `"enable"` |
| **log_packet**  string | Enable/disable packet logging. Enable to save the packet that triggers the filter. You can download the packets in pcap format for diagnostic use.  **Choices:**   - `"disable"` - `"enable"` |
| **os**  list / elements=string | Operating systems to be protected. Use all for every operating system and other for unlisted operating systems. |
| **protocol**  list / elements=string | Protocols to be examined. Use all for every protocol and other for unlisted protocols. |
| **quarantine**  string | Quarantine method.  **Choices:**   - `"none"` - `"attacker"` |
| **quarantine_expiry**  string | Duration of quarantine. (Format |
| **quarantine_log**  string | Enable/disable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **rate_count**  integer | Count of the rate. |
| **rate_duration**  integer | Duration (sec) of the rate. |
| **rate_mode**  string | Rate limit mode.  **Choices:**   - `"periodical"` - `"continuous"` |
| **rate_track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` - `"dhcp-client-mac"` - `"dns-domain"` |
| **rule**  list / elements=dictionary | Identifies the predefined or custom IPS signatures to add to the sensor. |
| **id**  integer / required | Rule IPS. see <a href=’#notes’>Notes</a>. |
| **severity**  list / elements=string | Relative severity of the signature, from info to critical. Log messages generated by the signature include the severity. |
| **status**  string | Status of the signatures included in filter. Only those filters with a status to enable are used.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **vuln_type**  list / elements=dictionary | List of signature vulnerability types to filter by. |
| **id**  integer / required | Vulnerability type ID. see <a href=’#notes’>Notes</a>. |
| **extended_log**  string | Enable/disable extended logging.  **Choices:**   - `"enable"` - `"disable"` |
| **filter**  list / elements=dictionary | IPS sensor filter. |
| **action**  string | Action of selected rules.  **Choices:**   - `"pass"` - `"block"` - `"reset"` - `"default"` |
| **application**  string | Vulnerable application filter. |
| **location**  string | Vulnerability location filter. |
| **log**  string | Enable/disable logging of selected rules.  **Choices:**   - `"disable"` - `"enable"` |
| **log_packet**  string | Enable/disable packet logging of selected rules.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Filter name. |
| **os**  string | Vulnerable OS filter. |
| **protocol**  string | Vulnerable protocol filter. |
| **quarantine**  string | Quarantine IP or interface.  **Choices:**   - `"none"` - `"attacker"` |
| **quarantine_expiry**  integer | Duration of quarantine in minute. |
| **quarantine_log**  string | Enable/disable logging of selected quarantine.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Vulnerability severity filter. |
| **status**  string | Selected rules status.  **Choices:**   - `"disable"` - `"enable"` - `"default"` |
| **name**  string / required | Sensor name. |
| **override**  list / elements=dictionary | IPS override rule. |
| **action**  string | Action of override rule.  **Choices:**   - `"pass"` - `"block"` - `"reset"` |
| **exempt_ip**  list / elements=dictionary | Exempted IP. |
| **dst_ip**  string | Destination IP address and netmask. |
| **id**  integer / required | Exempt IP ID. see <a href=’#notes’>Notes</a>. |
| **src_ip**  string | Source IP address and netmask. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **log_packet**  string | Enable/disable packet logging.  **Choices:**   - `"disable"` - `"enable"` |
| **quarantine**  string | Quarantine IP or interface.  **Choices:**   - `"none"` - `"attacker"` |
| **quarantine_expiry**  integer | Duration of quarantine in minute. |
| **quarantine_log**  string | Enable/disable logging of selected quarantine.  **Choices:**   - `"disable"` - `"enable"` |
| **rule_id**  integer / required | Override rule ID. see <a href=’#notes’>Notes</a>. |
| **status**  string | Enable/disable status of override rule.  **Choices:**   - `"disable"` - `"enable"` |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **scan_botnet_connections**  string | Block or monitor connections to Botnet servers, or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_ips_sensor_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_ips_sensor_module.md#id5)

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
  - name: Configure IPS sensor.
    fortios_ips_sensor:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      ips_sensor:
        block_malicious_url: "disable"
        comment: "Comment."
        entries:
         -
            action: "pass"
            application: "<your_own_value>"
            cve:
             -
                cve_entry: "<your_own_value>"
            default_action: "all"
            default_status: "all"
            exempt_ip:
             -
                dst_ip: "<your_own_value>"
                id:  "14"
                src_ip: "<your_own_value>"
            id:  "16"
            last_modified: "<your_own_value>"
            location: "<your_own_value>"
            log: "disable"
            log_attack_context: "disable"
            log_packet: "disable"
            os: "<your_own_value>"
            protocol: "<your_own_value>"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            rate_count: "0"
            rate_duration: "60"
            rate_mode: "periodical"
            rate_track: "none"
            rule:
             -
                id:  "32"
            severity: "<your_own_value>"
            status: "disable"
            vuln_type:
             -
                id:  "36"
        extended_log: "enable"
        filter:
         -
            action: "pass"
            application: "<your_own_value>"
            location: "<your_own_value>"
            log: "disable"
            log_packet: "disable"
            name: "default_name_44"
            os: "<your_own_value>"
            protocol: "<your_own_value>"
            quarantine: "none"
            quarantine_expiry: "1073741823"
            quarantine_log: "disable"
            severity: "<your_own_value>"
            status: "disable"
        name: "default_name_52"
        override:
         -
            action: "pass"
            exempt_ip:
             -
                dst_ip: "<your_own_value>"
                id:  "57"
                src_ip: "<your_own_value>"
            log: "disable"
            log_packet: "disable"
            quarantine: "none"
            quarantine_expiry: "1073741823"
            quarantine_log: "disable"
            rule_id: "<you_own_value>"
            status: "disable"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        scan_botnet_connections: "disable"
```

## [Return Values](fortios_ips_sensor_module.md#id6)

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
