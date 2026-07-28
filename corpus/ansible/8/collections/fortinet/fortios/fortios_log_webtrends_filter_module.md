---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_log_webtrends_filter module – Filters for WebTrends in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_log_webtrends_filter_module.html
fetched_at: 2026-07-28T02:26:28+00:00
---
# fortinet.fortios.fortios_log_webtrends_filter module – Filters for WebTrends in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_log_webtrends_filter_module.md#ansible-collections-fortinet-fortios-fortios-log-webtrends-filter-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_webtrends_filter`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_log_webtrends_filter_module.md#synopsis)
- [Requirements](fortios_log_webtrends_filter_module.md#requirements)
- [Parameters](fortios_log_webtrends_filter_module.md#parameters)
- [Notes](fortios_log_webtrends_filter_module.md#notes)
- [Examples](fortios_log_webtrends_filter_module.md#examples)
- [Return Values](fortios_log_webtrends_filter_module.md#return-values)

## [Synopsis](fortios_log_webtrends_filter_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify log_webtrends feature and filter category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_log_webtrends_filter_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_log_webtrends_filter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **log_webtrends_filter**  dictionary | Filters for WebTrends. |
| **anomaly**  string | Enable/disable anomaly logging.  **Choices:**   - `"enable"` - `"disable"` |
| **dns**  string | Enable/disable detailed DNS event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **filter**  string | Webtrends log filter. |
| **filter_type**  string | Include/exclude logs that match the filter.  **Choices:**   - `"include"` - `"exclude"` |
| **forward_traffic**  string | Enable/disable forward traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **free_style**  list / elements=dictionary | Free style filters. |
| **category**  string | Log category.  **Choices:**   - `"traffic"` - `"event"` - `"virus"` - `"webfilter"` - `"attack"` - `"spam"` - `"anomaly"` - `"voip"` - `"dlp"` - `"app-ctrl"` - `"waf"` - `"gtp"` - `"dns"` - `"ssh"` - `"ssl"` - `"file-filter"` - `"icap"` - `"virtual-patch"` - `"ztna"` |
| **filter**  string | Free style filter string. |
| **filter_type**  string | Include/exclude logs that match the filter.  **Choices:**   - `"include"` - `"exclude"` |
| **id**  integer / required | Entry ID. see <a href=’#notes’>Notes</a>. |
| **gtp**  string | Enable/disable GTP messages logging.  **Choices:**   - `"enable"` - `"disable"` |
| **local_traffic**  string | Enable/disable local in or out traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **multicast_traffic**  string | Enable/disable multicast traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **netscan_discovery**  string | Enable/disable netscan discovery event logging. |
| **netscan_vulnerability**  string | Enable/disable netscan vulnerability event logging. |
| **severity**  string | Lowest severity level to log to WebTrends.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **sniffer_traffic**  string | Enable/disable sniffer traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **ssh**  string | Enable/disable SSH logging.  **Choices:**   - `"enable"` - `"disable"` |
| **voip**  string | Enable/disable VoIP logging.  **Choices:**   - `"enable"` - `"disable"` |
| **ztna_traffic**  string | Enable/disable ztna traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_log_webtrends_filter_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_log_webtrends_filter_module.md#id5)

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
  - name: Filters for WebTrends.
    fortios_log_webtrends_filter:
      vdom:  "{{ vdom }}"
      log_webtrends_filter:
        anomaly: "enable"
        dns: "enable"
        filter: "<your_own_value>"
        filter_type: "include"
        forward_traffic: "enable"
        free_style:
         -
            category: "traffic"
            filter: "<your_own_value>"
            filter_type: "include"
            id:  "12"
        gtp: "enable"
        local_traffic: "enable"
        multicast_traffic: "enable"
        netscan_discovery: "<your_own_value>"
        netscan_vulnerability: "<your_own_value>"
        severity: "emergency"
        sniffer_traffic: "enable"
        ssh: "enable"
        voip: "enable"
        ztna_traffic: "enable"
```

## [Return Values](fortios_log_webtrends_filter_module.md#id6)

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
