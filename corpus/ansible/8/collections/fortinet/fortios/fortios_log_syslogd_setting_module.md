---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_log_syslogd_setting module – Global settings for remote syslog server in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_log_syslogd_setting_module.html
fetched_at: 2026-07-28T02:26:22+00:00
---
# fortinet.fortios.fortios_log_syslogd_setting module – Global settings for remote syslog server in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_log_syslogd_setting_module.md#ansible-collections-fortinet-fortios-fortios-log-syslogd-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_syslogd_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_log_syslogd_setting_module.md#synopsis)
- [Requirements](fortios_log_syslogd_setting_module.md#requirements)
- [Parameters](fortios_log_syslogd_setting_module.md#parameters)
- [Notes](fortios_log_syslogd_setting_module.md#notes)
- [Examples](fortios_log_syslogd_setting_module.md#examples)
- [Return Values](fortios_log_syslogd_setting_module.md#return-values)

## [Synopsis](fortios_log_syslogd_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify log_syslogd feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_log_syslogd_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_log_syslogd_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **log_syslogd_setting**  dictionary | Global settings for remote syslog server. |
| **certificate**  string | Certificate used to communicate with Syslog server. Source certificate.local.name. |
| **custom_field_name**  list / elements=dictionary | Custom field name for CEF format logging. |
| **custom**  string | Field custom name [A-Za-z0-9_]. |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **name**  string | Field name [A-Za-z0-9_]. |
| **enc_algorithm**  string | Enable/disable reliable syslogging with TLS encryption.  **Choices:**   - `"high-medium"` - `"high"` - `"low"` - `"disable"` |
| **facility**  string | Remote syslog facility.  **Choices:**   - `"kernel"` - `"user"` - `"mail"` - `"daemon"` - `"auth"` - `"syslog"` - `"lpr"` - `"news"` - `"uucp"` - `"cron"` - `"authpriv"` - `"ftp"` - `"ntp"` - `"audit"` - `"alert"` - `"clock"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **format**  string | Log format.  **Choices:**   - `"default"` - `"csv"` - `"cef"` - `"rfc5424"` - `"json"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **max_log_rate**  integer | Syslog maximum log rate in MBps (0 = unlimited). |
| **mode**  string | Remote syslog logging over UDP/Reliable TCP.  **Choices:**   - `"udp"` - `"legacy-reliable"` - `"reliable"` |
| **port**  integer | Server listen port. |
| **priority**  string | Set log transmission priority.  **Choices:**   - `"default"` - `"low"` |
| **server**  string | Address of remote syslog server. |
| **source_ip**  string | Source IP address of syslog. |
| **ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  **Choices:**   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"TLSv1-3"` |
| **status**  string | Enable/disable remote syslog logging.  **Choices:**   - `"enable"` - `"disable"` |
| **syslog_type**  integer | Hidden setting index of Syslog. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_log_syslogd_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_log_syslogd_setting_module.md#id5)

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
  - name: Global settings for remote syslog server.
    fortios_log_syslogd_setting:
      vdom:  "{{ vdom }}"
      log_syslogd_setting:
        certificate: "<your_own_value> (source certificate.local.name)"
        custom_field_name:
         -
            custom: "<your_own_value>"
            id:  "6"
            name: "default_name_7"
        enc_algorithm: "high-medium"
        facility: "kernel"
        format: "default"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        max_log_rate: "0"
        mode: "udp"
        port: "514"
        priority: "default"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        ssl_min_proto_version: "default"
        status: "enable"
        syslog_type: "2147483647"
```

## [Return Values](fortios_log_syslogd_setting_module.md#id6)

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
