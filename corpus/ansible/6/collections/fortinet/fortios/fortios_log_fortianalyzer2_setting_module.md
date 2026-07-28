---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_log_fortianalyzer2_setting module – Global FortiAnalyzer settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_log_fortianalyzer2_setting_module.html
fetched_at: 2026-07-27T17:42:13+00:00
---
# fortinet.fortios.fortios_log_fortianalyzer2_setting module – Global FortiAnalyzer settings in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_log_fortianalyzer2_setting_module.md#ansible-collections-fortinet-fortios-fortios-log-fortianalyzer2-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_fortianalyzer2_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_log_fortianalyzer2_setting_module.md#synopsis)
- [Requirements](fortios_log_fortianalyzer2_setting_module.md#requirements)
- [Parameters](fortios_log_fortianalyzer2_setting_module.md#parameters)
- [Notes](fortios_log_fortianalyzer2_setting_module.md#notes)
- [Examples](fortios_log_fortianalyzer2_setting_module.md#examples)
- [Return Values](fortios_log_fortianalyzer2_setting_module.md#return-values)

## [Synopsis](fortios_log_fortianalyzer2_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify log_fortianalyzer2 feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_log_fortianalyzer2_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_log_fortianalyzer2_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **log_fortianalyzer2_setting**  dictionary | Global FortiAnalyzer settings. |
| **__change_ip**  integer | Hidden attribute. |
| **access_config**  string | Enable/disable FortiAnalyzer access to configuration and data.  Choices:   - `"enable"` - `"disable"` |
| **certificate**  string | Certificate used to communicate with FortiAnalyzer. Source certificate.local.name. |
| **certificate_verification**  string | Enable/disable identity verification of FortiAnalyzer by use of certificate.  Choices:   - `"enable"` - `"disable"` |
| **conn_timeout**  integer | FortiAnalyzer connection time-out in seconds (for status and log buffer). |
| **enc_algorithm**  string | Configure the level of SSL protection for secure communication with FortiAnalyzer.  Choices:   - `"high-medium"` - `"high"` - `"low"` |
| **faz_type**  integer | Hidden setting index of FortiAnalyzer. |
| **hmac_algorithm**  string | OFTP login hash algorithm.  Choices:   - `"sha256"` - `"sha1"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **ips_archive**  string | Enable/disable IPS packet archive logging.  Choices:   - `"enable"` - `"disable"` |
| **max_log_rate**  integer | FortiAnalyzer maximum log rate in MBps (0 = unlimited). |
| **mgmt_name**  string | Hidden management name of FortiAnalyzer. |
| **monitor_failure_retry_period**  integer | Time between FortiAnalyzer connection retries in seconds (for status and log buffer). |
| **monitor_keepalive_period**  integer | Time between OFTP keepalives in seconds (for status and log buffer). |
| **preshared_key**  string | Preshared-key used for auto-authorization on FortiAnalyzer. |
| **priority**  string | Set log transmission priority.  Choices:   - `"default"` - `"low"` |
| **reliable**  string | Enable/disable reliable logging to FortiAnalyzer.  Choices:   - `"enable"` - `"disable"` |
| **serial**  list / elements=dictionary | Serial numbers of the FortiAnalyzer. |
| **name**  string | Serial Number. |
| **server**  string | The remote FortiAnalyzer. |
| **source_ip**  string | Source IPv4 or IPv6 address used to communicate with FortiAnalyzer. |
| **ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  Choices:   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"TLSv1-3"` |
| **status**  string | Enable/disable logging to FortiAnalyzer.  Choices:   - `"enable"` - `"disable"` |
| **upload_day**  string | Day of week (month) to upload logs. |
| **upload_interval**  string | Frequency to upload log files to FortiAnalyzer.  Choices:   - `"daily"` - `"weekly"` - `"monthly"` |
| **upload_option**  string | Enable/disable logging to hard disk and then uploading to FortiAnalyzer.  Choices:   - `"store-and-upload"` - `"realtime"` - `"1-minute"` - `"5-minute"` |
| **upload_time**  string | Time to upload logs (hh:mm). |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_log_fortianalyzer2_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_log_fortianalyzer2_setting_module.md#id5)

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
  - name: Global FortiAnalyzer settings.
    fortios_log_fortianalyzer2_setting:
      vdom:  "{{ vdom }}"
      log_fortianalyzer2_setting:
        __change_ip: "127"
        access_config: "enable"
        certificate: "<your_own_value> (source certificate.local.name)"
        certificate_verification: "enable"
        conn_timeout: "10"
        enc_algorithm: "high-medium"
        faz_type: "2147483647"
        hmac_algorithm: "sha256"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        ips_archive: "enable"
        max_log_rate: "0"
        mgmt_name: "<your_own_value>"
        monitor_failure_retry_period: "5"
        monitor_keepalive_period: "5"
        preshared_key: "<your_own_value>"
        priority: "default"
        reliable: "enable"
        serial:
         -
            name: "default_name_22"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        ssl_min_proto_version: "default"
        status: "enable"
        upload_day: "<your_own_value>"
        upload_interval: "daily"
        upload_option: "store-and-upload"
        upload_time: "<your_own_value>"
```

## [Return Values](fortios_log_fortianalyzer2_setting_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
