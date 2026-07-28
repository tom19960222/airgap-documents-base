---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_log_fact module – Retrieve log data of fortios log objects."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_log_fact_module.html
fetched_at: 2026-07-28T02:25:49+00:00
---
# fortinet.fortios.fortios_log_fact module – Retrieve log data of fortios log objects.

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
> see [Requirements](fortios_log_fact_module.md#ansible-collections-fortinet-fortios-fortios-log-fact-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_fact`.

New in fortinet.fortios 2.1.0

- [Synopsis](fortios_log_fact_module.md#synopsis)
- [Requirements](fortios_log_fact_module.md#requirements)
- [Parameters](fortios_log_fact_module.md#parameters)
- [Notes](fortios_log_fact_module.md#notes)
- [Examples](fortios_log_fact_module.md#examples)
- [Return Values](fortios_log_fact_module.md#return-values)

## [Synopsis](fortios_log_fact_module.md#id1)

- Retrieve log related to disk, memory, fortianalyzer and forticloud.

## [Requirements](fortios_log_fact_module.md#id2)

The below requirements are needed on the host that executes this module.

- install galaxy collection fortinet.fortios >= 2.1.0.

## [Parameters](fortios_log_fact_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **filters**  list / elements=string | A list of expressions to filter the returned results.  The items of the list are combined as LOGICAL AND with operator ampersand.  One item itself could be concatenated with a comma as LOGICAL OR. |
| **formatters**  list / elements=string | A list of fields to display for returned results. |
| **params**  dictionary | the parameter for each selector, see definition in above list. |
| **selector**  string | selector of the retrieved log type  **Choices:**   - `"disk_virus_archive"` - `"memory_virus_archive"` - `"fortianalyzer_virus_archive"` - `"forticloud_virus_archive"` - `"disk_ips_archive"` - `"disk_app-ctrl_archive"` - `"memory_ips_archive"` - `"memory_app-ctrl_archive"` - `"fortianalyzer_ips_archive"` - `"fortianalyzer_app-ctrl_archive"` - `"forticloud_ips_archive"` - `"forticloud_app-ctrl_archive"` - `"disk_ips_archive-download"` - `"disk_app-ctrl_archive-download"` - `"memory_ips_archive-download"` - `"memory_app-ctrl_archive-download"` - `"fortianalyzer_ips_archive-download"` - `"fortianalyzer_app-ctrl_archive-download"` - `"forticloud_ips_archive-download"` - `"forticloud_app-ctrl_archive-download"` - `"disk_virus_raw"` - `"disk_webfilter_raw"` - `"disk_waf_raw"` - `"disk_ips_raw"` - `"disk_anomaly_raw"` - `"disk_app-ctrl_raw"` - `"disk_cifs_raw"` - `"disk_emailfilter_raw"` - `"disk_dlp_raw"` - `"disk_voip_raw"` - `"disk_gtp_raw"` - `"disk_dns_raw"` - `"disk_ssh_raw"` - `"disk_ssl_raw"` - `"disk_file-filter_raw"` - `"memory_virus_raw"` - `"memory_webfilter_raw"` - `"memory_waf_raw"` - `"memory_ips_raw"` - `"memory_anomaly_raw"` - `"memory_app-ctrl_raw"` - `"memory_cifs_raw"` - `"memory_emailfilter_raw"` - `"memory_dlp_raw"` - `"memory_voip_raw"` - `"memory_gtp_raw"` - `"memory_dns_raw"` - `"memory_ssh_raw"` - `"memory_ssl_raw"` - `"memory_file-filter_raw"` - `"fortianalyzer_virus_raw"` - `"fortianalyzer_webfilter_raw"` - `"fortianalyzer_waf_raw"` - `"fortianalyzer_ips_raw"` - `"fortianalyzer_anomaly_raw"` - `"fortianalyzer_app-ctrl_raw"` - `"fortianalyzer_cifs_raw"` - `"fortianalyzer_emailfilter_raw"` - `"fortianalyzer_dlp_raw"` - `"fortianalyzer_voip_raw"` - `"fortianalyzer_gtp_raw"` - `"fortianalyzer_dns_raw"` - `"fortianalyzer_ssh_raw"` - `"fortianalyzer_ssl_raw"` - `"fortianalyzer_file-filter_raw"` - `"forticloud_virus_raw"` - `"forticloud_webfilter_raw"` - `"forticloud_waf_raw"` - `"forticloud_ips_raw"` - `"forticloud_anomaly_raw"` - `"forticloud_app-ctrl_raw"` - `"forticloud_cifs_raw"` - `"forticloud_emailfilter_raw"` - `"forticloud_dlp_raw"` - `"forticloud_voip_raw"` - `"forticloud_gtp_raw"` - `"forticloud_dns_raw"` - `"forticloud_ssh_raw"` - `"forticloud_ssl_raw"` - `"forticloud_file-filter_raw"` - `"disk_event_vpn"` - `"disk_event_user"` - `"disk_event_router"` - `"disk_event_wireless"` - `"disk_event_wad"` - `"disk_event_endpoint"` - `"disk_event_ha"` - `"disk_event_compliance-check"` - `"disk_event_system"` - `"disk_event_connector"` - `"disk_event_security-rating"` - `"disk_event_fortiextender"` - `"disk_traffic_forward"` - `"disk_traffic_local"` - `"disk_traffic_multicast"` - `"disk_traffic_sniffer"` - `"disk_traffic_fortiview"` - `"disk_traffic_threat"` - `"memory_event_vpn"` - `"memory_event_user"` - `"memory_event_router"` - `"memory_event_wireless"` - `"memory_event_wad"` - `"memory_event_endpoint"` - `"memory_event_ha"` - `"memory_event_compliance-check"` - `"memory_event_system"` - `"memory_event_connector"` - `"memory_event_security-rating"` - `"memory_event_fortiextender"` - `"memory_traffic_forward"` - `"memory_traffic_local"` - `"memory_traffic_multicast"` - `"memory_traffic_sniffer"` - `"memory_traffic_fortiview"` - `"memory_traffic_threat"` - `"fortianalyzer_event_vpn"` - `"fortianalyzer_event_user"` - `"fortianalyzer_event_router"` - `"fortianalyzer_event_wireless"` - `"fortianalyzer_event_wad"` - `"fortianalyzer_event_endpoint"` - `"fortianalyzer_event_ha"` - `"fortianalyzer_event_compliance-check"` - `"fortianalyzer_event_system"` - `"fortianalyzer_event_connector"` - `"fortianalyzer_event_security-rating"` - `"fortianalyzer_event_fortiextender"` - `"fortianalyzer_traffic_forward"` - `"fortianalyzer_traffic_local"` - `"fortianalyzer_traffic_multicast"` - `"fortianalyzer_traffic_sniffer"` - `"fortianalyzer_traffic_fortiview"` - `"fortianalyzer_traffic_threat"` - `"forticloud_event_vpn"` - `"forticloud_event_user"` - `"forticloud_event_router"` - `"forticloud_event_wireless"` - `"forticloud_event_wad"` - `"forticloud_event_endpoint"` - `"forticloud_event_ha"` - `"forticloud_event_compliance-check"` - `"forticloud_event_system"` - `"forticloud_event_connector"` - `"forticloud_event_security-rating"` - `"forticloud_event_fortiextender"` - `"forticloud_traffic_forward"` - `"forticloud_traffic_local"` - `"forticloud_traffic_multicast"` - `"forticloud_traffic_sniffer"` - `"forticloud_traffic_fortiview"` - `"forticloud_traffic_threat"` |
| **selectors**  list / elements=dictionary | A list of selectors for retrieving the log type. |
| **filters**  list / elements=string | A list of expressions to filter the returned results.  The items of the list are combined as LOGICAL AND with operator ampersand.  One item itself could be concatenated with a comma as LOGICAL OR. |
| **formatters**  list / elements=string | A list of fields to display for returned results. |
| **params**  dictionary | the parameter for each selector, see definition in above list. |
| **selector**  string / required | selector of the retrieved log type  **Choices:**   - `"disk_virus_archive"` - `"memory_virus_archive"` - `"fortianalyzer_virus_archive"` - `"forticloud_virus_archive"` - `"disk_ips_archive"` - `"disk_app-ctrl_archive"` - `"memory_ips_archive"` - `"memory_app-ctrl_archive"` - `"fortianalyzer_ips_archive"` - `"fortianalyzer_app-ctrl_archive"` - `"forticloud_ips_archive"` - `"forticloud_app-ctrl_archive"` - `"disk_ips_archive-download"` - `"disk_app-ctrl_archive-download"` - `"memory_ips_archive-download"` - `"memory_app-ctrl_archive-download"` - `"fortianalyzer_ips_archive-download"` - `"fortianalyzer_app-ctrl_archive-download"` - `"forticloud_ips_archive-download"` - `"forticloud_app-ctrl_archive-download"` - `"disk_virus_raw"` - `"disk_webfilter_raw"` - `"disk_waf_raw"` - `"disk_ips_raw"` - `"disk_anomaly_raw"` - `"disk_app-ctrl_raw"` - `"disk_cifs_raw"` - `"disk_emailfilter_raw"` - `"disk_dlp_raw"` - `"disk_voip_raw"` - `"disk_gtp_raw"` - `"disk_dns_raw"` - `"disk_ssh_raw"` - `"disk_ssl_raw"` - `"disk_file-filter_raw"` - `"memory_virus_raw"` - `"memory_webfilter_raw"` - `"memory_waf_raw"` - `"memory_ips_raw"` - `"memory_anomaly_raw"` - `"memory_app-ctrl_raw"` - `"memory_cifs_raw"` - `"memory_emailfilter_raw"` - `"memory_dlp_raw"` - `"memory_voip_raw"` - `"memory_gtp_raw"` - `"memory_dns_raw"` - `"memory_ssh_raw"` - `"memory_ssl_raw"` - `"memory_file-filter_raw"` - `"fortianalyzer_virus_raw"` - `"fortianalyzer_webfilter_raw"` - `"fortianalyzer_waf_raw"` - `"fortianalyzer_ips_raw"` - `"fortianalyzer_anomaly_raw"` - `"fortianalyzer_app-ctrl_raw"` - `"fortianalyzer_cifs_raw"` - `"fortianalyzer_emailfilter_raw"` - `"fortianalyzer_dlp_raw"` - `"fortianalyzer_voip_raw"` - `"fortianalyzer_gtp_raw"` - `"fortianalyzer_dns_raw"` - `"fortianalyzer_ssh_raw"` - `"fortianalyzer_ssl_raw"` - `"fortianalyzer_file-filter_raw"` - `"forticloud_virus_raw"` - `"forticloud_webfilter_raw"` - `"forticloud_waf_raw"` - `"forticloud_ips_raw"` - `"forticloud_anomaly_raw"` - `"forticloud_app-ctrl_raw"` - `"forticloud_cifs_raw"` - `"forticloud_emailfilter_raw"` - `"forticloud_dlp_raw"` - `"forticloud_voip_raw"` - `"forticloud_gtp_raw"` - `"forticloud_dns_raw"` - `"forticloud_ssh_raw"` - `"forticloud_ssl_raw"` - `"forticloud_file-filter_raw"` - `"disk_event_vpn"` - `"disk_event_user"` - `"disk_event_router"` - `"disk_event_wireless"` - `"disk_event_wad"` - `"disk_event_endpoint"` - `"disk_event_ha"` - `"disk_event_compliance-check"` - `"disk_event_system"` - `"disk_event_connector"` - `"disk_event_security-rating"` - `"disk_event_fortiextender"` - `"disk_traffic_forward"` - `"disk_traffic_local"` - `"disk_traffic_multicast"` - `"disk_traffic_sniffer"` - `"disk_traffic_fortiview"` - `"disk_traffic_threat"` - `"memory_event_vpn"` - `"memory_event_user"` - `"memory_event_router"` - `"memory_event_wireless"` - `"memory_event_wad"` - `"memory_event_endpoint"` - `"memory_event_ha"` - `"memory_event_compliance-check"` - `"memory_event_system"` - `"memory_event_connector"` - `"memory_event_security-rating"` - `"memory_event_fortiextender"` - `"memory_traffic_forward"` - `"memory_traffic_local"` - `"memory_traffic_multicast"` - `"memory_traffic_sniffer"` - `"memory_traffic_fortiview"` - `"memory_traffic_threat"` - `"fortianalyzer_event_vpn"` - `"fortianalyzer_event_user"` - `"fortianalyzer_event_router"` - `"fortianalyzer_event_wireless"` - `"fortianalyzer_event_wad"` - `"fortianalyzer_event_endpoint"` - `"fortianalyzer_event_ha"` - `"fortianalyzer_event_compliance-check"` - `"fortianalyzer_event_system"` - `"fortianalyzer_event_connector"` - `"fortianalyzer_event_security-rating"` - `"fortianalyzer_event_fortiextender"` - `"fortianalyzer_traffic_forward"` - `"fortianalyzer_traffic_local"` - `"fortianalyzer_traffic_multicast"` - `"fortianalyzer_traffic_sniffer"` - `"fortianalyzer_traffic_fortiview"` - `"fortianalyzer_traffic_threat"` - `"forticloud_event_vpn"` - `"forticloud_event_user"` - `"forticloud_event_router"` - `"forticloud_event_wireless"` - `"forticloud_event_wad"` - `"forticloud_event_endpoint"` - `"forticloud_event_ha"` - `"forticloud_event_compliance-check"` - `"forticloud_event_system"` - `"forticloud_event_connector"` - `"forticloud_event_security-rating"` - `"forticloud_event_fortiextender"` - `"forticloud_traffic_forward"` - `"forticloud_traffic_local"` - `"forticloud_traffic_multicast"` - `"forticloud_traffic_sniffer"` - `"forticloud_traffic_fortiview"` - `"forticloud_traffic_threat"` |
| **sorters**  list / elements=string | A list of expressions to sort the returned results.  The items of the list are in ascending order with operator ampersand.  One item itself could be in decending order with a comma inside. |
| **sorters**  list / elements=string | A list of expressions to sort the returned results.  The items of the list are in ascending order with operator ampersand.  One item itself could be in decending order with a comma inside. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_log_fact_module.md#id4)

> **Note:**
>
> - Different selector may have different parameters, users are expected to look up them for a specific selector.
> - For some selectors, the objects are global, no params are allowed to appear
> - Not all parameters are required for a slector.
> - This module is exclusivly for FortiOS Log API.

## [Examples](fortios_log_fact_module.md#id5)

```yaml+jinja
- hosts: fortigate03
  connection: httpapi
  collections:
  - fortinet.fortios
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: get disk event user and memory event user at once.
    fortios_log_fact:
       enable_log: True
       access_token: ""
       selectors:
         - selector: disk_event_user
           filters:
             - log_id==41000
         - selector: memory_event_user

  - name: Get system event log with logid==0100032038
    fortios_log_fact:
       filters:
         - logid==0100032038
       selector: "disk_event_system"
       params:
         rows: 100

  - name: Get a description of the quarantined virus file
    fortios_log_fact:
       selector: "forticloud_virus_archive"
```

## [Return Values](fortios_log_fact_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **rows**  integer | Number of rows to return  **Returned:** always  **Sample:** `400` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **session_id**  integer | session id for the request  **Returned:** always  **Sample:** `7` |
| **start**  integer | Row number for the first row to return  **Returned:** always  **Sample:** `0` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **subcategory**  string | Type of log that can be retrieved  **Returned:** always  **Sample:** `"system"` |
| **total_lines**  integer | Total lines returned from the result  **Returned:** always  **Sample:** `510` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@fshen01)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
