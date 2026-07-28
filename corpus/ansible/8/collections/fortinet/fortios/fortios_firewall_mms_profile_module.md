---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_mms_profile module – Configure MMS profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_mms_profile_module.html
fetched_at: 2026-07-28T02:24:48+00:00
---
# fortinet.fortios.fortios_firewall_mms_profile module – Configure MMS profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_mms_profile_module.md#ansible-collections-fortinet-fortios-fortios-firewall-mms-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_mms_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_mms_profile_module.md#synopsis)
- [Requirements](fortios_firewall_mms_profile_module.md#requirements)
- [Parameters](fortios_firewall_mms_profile_module.md#parameters)
- [Notes](fortios_firewall_mms_profile_module.md#notes)
- [Examples](fortios_firewall_mms_profile_module.md#examples)
- [Return Values](fortios_firewall_mms_profile_module.md#return-values)

## [Synopsis](fortios_firewall_mms_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and mms_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_mms_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_mms_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_mms_profile**  dictionary | Configure MMS profiles. |
| **avnotificationtable**  integer | AntiVirus notification table ID. Source antivirus.notification.id. |
| **bwordtable**  integer | MMS banned word table ID. Source webfilter.content.id. |
| **carrier_endpoint_prefix**  string | Enable/disable prefixing of end point values.  **Choices:**   - `"enable"` - `"disable"` |
| **carrier_endpoint_prefix_range_max**  integer | Maximum length of end point value that can be prefixed (1 - 48). |
| **carrier_endpoint_prefix_range_min**  integer | Minimum end point length to be prefixed (1 - 48). |
| **carrier_endpoint_prefix_string**  string | String with which to prefix End point values. |
| **carrierendpointbwltable**  integer | Carrier end point filter table ID. Source firewall.carrier-endpoint-bwl.id. |
| **comment**  string | Comment. |
| **dupe**  list / elements=dictionary | Duplicate configuration. |
| **action1**  list / elements=string | Action to take when threshold reached.  **Choices:**   - `"block"` - `"archive"` - `"log"` - `"archive-first"` - `"alert-notif"` |
| **action2**  list / elements=string | Action to take when threshold reached.  **Choices:**   - `"block"` - `"archive"` - `"log"` - `"archive-first"` - `"alert-notif"` |
| **action3**  list / elements=string | Action to take when threshold reached.  **Choices:**   - `"block"` - `"archive"` - `"log"` - `"archive-first"` - `"alert-notif"` |
| **block_time1**  integer | Duration for which action takes effect (0 - 35791 min). |
| **block_time2**  integer | Duration for which action takes effect (0 - 35791 min). |
| **block_time3**  integer | Duration action takes effect (0 - 35791 min). |
| **limit1**  integer | Maximum number of messages allowed. |
| **limit2**  integer | Maximum number of messages allowed. |
| **limit3**  integer | Maximum number of messages allowed. |
| **protocol**  string / required | Protocol. |
| **status1**  string | Enable/disable status1 detection.  **Choices:**   - `"enable"` - `"disable"` |
| **status2**  string | Enable/disable status2 detection.  **Choices:**   - `"enable"` - `"disable"` |
| **status3**  string | Enable/disable status3 detection.  **Choices:**   - `"enable"` - `"disable"` |
| **window1**  integer | Window to count messages over (1 - 2880 min). |
| **window2**  integer | Window to count messages over (1 - 2880 min). |
| **window3**  integer | Window to count messages over (1 - 2880 min). |
| **extended_utm_log**  string | Enable/disable detailed UTM log messages. |
| **flood**  list / elements=dictionary | Flood configuration. |
| **action1**  list / elements=string | Action to take when threshold reached.  **Choices:**   - `"block"` - `"archive"` - `"log"` - `"archive-first"` - `"alert-notif"` |
| **action2**  list / elements=string | Action to take when threshold reached.  **Choices:**   - `"block"` - `"archive"` - `"log"` - `"archive-first"` - `"alert-notif"` |
| **action3**  list / elements=string | Action to take when threshold reached.  **Choices:**   - `"block"` - `"archive"` - `"log"` - `"archive-first"` - `"alert-notif"` |
| **block_time1**  integer | Duration for which action takes effect (0 - 35791 min). |
| **block_time2**  integer | Duration for which action takes effect (0 - 35791 min). |
| **block_time3**  integer | Duration action takes effect (0 - 35791 min). |
| **limit1**  integer | Maximum number of messages allowed. |
| **limit2**  integer | Maximum number of messages allowed. |
| **limit3**  integer | Maximum number of messages allowed. |
| **protocol**  string / required | Protocol. |
| **status1**  string | Enable/disable status1 detection.  **Choices:**   - `"enable"` - `"disable"` |
| **status2**  string | Enable/disable status2 detection.  **Choices:**   - `"enable"` - `"disable"` |
| **status3**  string | Enable/disable status3 detection.  **Choices:**   - `"enable"` - `"disable"` |
| **window1**  integer | Window to count messages over (1 - 2880 min). |
| **window2**  integer | Window to count messages over (1 - 2880 min). |
| **window3**  integer | Window to count messages over (1 - 2880 min). |
| **mm1**  list / elements=string | MM1 options.  **Choices:**   - `"avmonitor"` - `"oversize"` - `"quarantine"` - `"scan"` - `"bannedword"` - `"chunkedbypass"` - `"clientcomfort"` - `"servercomfort"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"mms-checksum"` |
| **mm1_addr_hdr**  string | HTTP header field (for MM1) containing user address. |
| **mm1_addr_source**  string | Source for MM1 user address.  **Choices:**   - `"http-header"` - `"cookie"` |
| **mm1_convert_hex**  string | Enable/disable converting user address from HEX string for MM1.  **Choices:**   - `"enable"` - `"disable"` |
| **mm1_outbreak_prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm1_retr_dupe**  string | Enable/disable duplicate scanning of MM1 retr.  **Choices:**   - `"enable"` - `"disable"` |
| **mm1_retrieve_scan**  string | Enable/disable scanning on MM1 retrieve configuration messages.  **Choices:**   - `"enable"` - `"disable"` |
| **mm1comfortamount**  integer | MM1 comfort amount (0 - 4294967295). |
| **mm1comfortinterval**  integer | MM1 comfort interval (0 - 4294967295). |
| **mm1oversizelimit**  integer | Maximum file size to scan (1 - 819200 kB). |
| **mm3**  list / elements=string | MM3 options.  **Choices:**   - `"avmonitor"` - `"oversize"` - `"quarantine"` - `"scan"` - `"bannedword"` - `"fragmail"` - `"splice"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"mms-checksum"` |
| **mm3_outbreak_prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm3oversizelimit**  integer | Maximum file size to scan (1 - 819200 kB). |
| **mm4**  list / elements=string | MM4 options.  **Choices:**   - `"avmonitor"` - `"oversize"` - `"quarantine"` - `"scan"` - `"bannedword"` - `"fragmail"` - `"splice"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"mms-checksum"` |
| **mm4_outbreak_prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm4oversizelimit**  integer | Maximum file size to scan (1 - 819200 kB). |
| **mm7**  list / elements=string | MM7 options.  **Choices:**   - `"avmonitor"` - `"oversize"` - `"quarantine"` - `"scan"` - `"bannedword"` - `"chunkedbypass"` - `"clientcomfort"` - `"servercomfort"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"mms-checksum"` |
| **mm7_addr_hdr**  string | HTTP header field (for MM7) containing user address. |
| **mm7_addr_source**  string | Source for MM7 user address.  **Choices:**   - `"http-header"` - `"cookie"` |
| **mm7_convert_hex**  string | Enable/disable conversion of user address from HEX string for MM7.  **Choices:**   - `"enable"` - `"disable"` |
| **mm7_outbreak_prevention**  string | Enable Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm7comfortamount**  integer | MM7 comfort amount (0 - 4294967295). |
| **mm7comfortinterval**  integer | MM7 comfort interval (0 - 4294967295). |
| **mm7oversizelimit**  integer | Maximum file size to scan (1 - 819200 kB). |
| **mms_antispam_mass_log**  string | Enable/disable logging for MMS antispam mass.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_av_block_log**  string | Enable/disable logging for MMS antivirus file blocking.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_av_oversize_log**  string | Enable/disable logging for MMS antivirus oversize file blocking.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_av_virus_log**  string | Enable/disable logging for MMS antivirus scanning.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_carrier_endpoint_filter_log**  string | Enable/disable logging for MMS end point filter blocking.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_checksum_log**  string | Enable/disable MMS content checksum logging.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_checksum_table**  integer | MMS content checksum table ID. Source antivirus.mms-checksum.id. |
| **mms_notification_log**  string | Enable/disable logging for MMS notification messages.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_web_content_log**  string | Enable/disable logging for MMS web content blocking.  **Choices:**   - `"enable"` - `"disable"` |
| **mmsbwordthreshold**  integer | MMS banned word threshold. |
| **name**  string / required | Profile name. |
| **notif_msisdn**  list / elements=dictionary | Notification for MSISDNs. |
| **msisdn**  string / required | Recipient MSISDN. |
| **threshold**  list / elements=string | Thresholds on which this MSISDN will receive an alert.  **Choices:**   - `"flood-thresh-1"` - `"flood-thresh-2"` - `"flood-thresh-3"` - `"dupe-thresh-1"` - `"dupe-thresh-2"` - `"dupe-thresh-3"` |
| **notification**  list / elements=dictionary | Notification configuration. |
| **alert_int**  integer | Alert notification send interval. |
| **alert_int_mode**  string | Alert notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **alert_src_msisdn**  string | Specify from address for alert messages. |
| **alert_status**  string | Alert notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **bword_int**  integer | Banned word notification send interval. |
| **bword_int_mode**  string | Banned word notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **bword_status**  string | Banned word notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **carrier_endpoint_bwl_int**  integer | Carrier end point black/white list notification send interval. |
| **carrier_endpoint_bwl_int_mode**  string | Carrier end point black/white list notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **carrier_endpoint_bwl_status**  string | Carrier end point black/white list notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **days_allowed**  list / elements=string | Weekdays on which notification messages may be sent.  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **detect_server**  string | Enable/disable automatic server address determination.  **Choices:**   - `"enable"` - `"disable"` |
| **dupe_int**  integer | Duplicate notification send interval. |
| **dupe_int_mode**  string | Duplicate notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **dupe_status**  string | Duplicate notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **file_block_int**  integer | File block notification send interval. |
| **file_block_int_mode**  string | File block notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **file_block_status**  string | File block notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **flood_int**  integer | Flood notification send interval. |
| **flood_int_mode**  string | Flood notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **flood_status**  string | Flood notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **from_in_header**  string | Enable/disable insertion of from address in HTTP header.  **Choices:**   - `"enable"` - `"disable"` |
| **mms_checksum_int**  integer | MMS checksum notification send interval. |
| **mms_checksum_int_mode**  string | MMS checksum notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **mms_checksum_status**  string | MMS checksum notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **mmsc_hostname**  string | Host name or IP address of the MMSC. |
| **mmsc_password**  string | Password required for authentication with the MMSC. |
| **mmsc_port**  integer | Port used on the MMSC for sending MMS messages (1 - 65535). |
| **mmsc_url**  string | URL used on the MMSC for sending MMS messages. |
| **mmsc_username**  string | User name required for authentication with the MMSC. |
| **msg_protocol**  string | Protocol to use for sending notification messages.  **Choices:**   - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **msg_type**  string | MM7 message type.  **Choices:**   - `"submit-req"` - `"deliver-req"` |
| **protocol**  string / required | Protocol. |
| **rate_limit**  integer | Rate limit for sending notification messages (0 - 250). |
| **tod_window_duration**  string | Time of day window duration. |
| **tod_window_end**  string | Obsolete. |
| **tod_window_start**  string | Time of day window start. |
| **user_domain**  string | Domain name to which the user addresses belong. |
| **vas_id**  string | VAS identifier. |
| **vasp_id**  string | VASP identifier. |
| **virus_int**  integer | Virus notification send interval. |
| **virus_int_mode**  string | Virus notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **virus_status**  string | Virus notification status.  **Choices:**   - `"enable"` - `"disable"` |
| **outbreak_prevention**  dictionary | Configure Virus Outbreak Prevention settings. |
| **external_blocklist**  string | Enable/disable external malware blocklist.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_service**  string | Enable/disable FortiGuard Virus outbreak prevention service.  **Choices:**   - `"disable"` - `"enable"` |
| **remove_blocked_const_length**  string | Enable/disable MMS replacement of blocked file constant length.  **Choices:**   - `"enable"` - `"disable"` |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_mms_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_mms_profile_module.md#id5)

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
  - name: Configure MMS profiles.
    fortios_firewall_mms_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_mms_profile:
        avnotificationtable: "2147483647"
        bwordtable: "2147483647"
        carrier_endpoint_prefix: "enable"
        carrier_endpoint_prefix_range_max: "24"
        carrier_endpoint_prefix_range_min: "24"
        carrier_endpoint_prefix_string: "<your_own_value>"
        carrierendpointbwltable: "2147483647"
        comment: "Comment."
        dupe:
         -
            action1: "block"
            action2: "block"
            action3: "block"
            block_time1: "17895"
            block_time2: "17895"
            block_time3: "17895"
            limit1: "1073741823"
            limit2: "1073741823"
            limit3: "1073741823"
            protocol: "<your_own_value>"
            status1: "enable"
            status2: "enable"
            status3: "enable"
            window1: "1440"
            window2: "1440"
            window3: "1440"
        extended_utm_log: "<your_own_value>"
        flood:
         -
            action1: "block"
            action2: "block"
            action3: "block"
            block_time1: "17895"
            block_time2: "17895"
            block_time3: "17895"
            limit1: "1073741823"
            limit2: "1073741823"
            limit3: "1073741823"
            protocol: "<your_own_value>"
            status1: "enable"
            status2: "enable"
            status3: "enable"
            window1: "1440"
            window2: "1440"
            window3: "1440"
        mm1: "avmonitor"
        mm1_addr_hdr: "<your_own_value>"
        mm1_addr_source: "http-header"
        mm1_convert_hex: "enable"
        mm1_outbreak_prevention: "disabled"
        mm1_retr_dupe: "enable"
        mm1_retrieve_scan: "enable"
        mm1comfortamount: "2147483647"
        mm1comfortinterval: "2147483647"
        mm1oversizelimit: "409600"
        mm3: "avmonitor"
        mm3_outbreak_prevention: "disabled"
        mm3oversizelimit: "409600"
        mm4: "avmonitor"
        mm4_outbreak_prevention: "disabled"
        mm4oversizelimit: "409600"
        mm7: "avmonitor"
        mm7_addr_hdr: "<your_own_value>"
        mm7_addr_source: "http-header"
        mm7_convert_hex: "enable"
        mm7_outbreak_prevention: "disabled"
        mm7comfortamount: "2147483647"
        mm7comfortinterval: "2147483647"
        mm7oversizelimit: "409600"
        mms_antispam_mass_log: "enable"
        mms_av_block_log: "enable"
        mms_av_oversize_log: "enable"
        mms_av_virus_log: "enable"
        mms_carrier_endpoint_filter_log: "enable"
        mms_checksum_log: "enable"
        mms_checksum_table: "2147483647"
        mms_notification_log: "enable"
        mms_web_content_log: "enable"
        mmsbwordthreshold: "1073741823"
        name: "default_name_80"
        notif_msisdn:
         -
            msisdn: "<your_own_value>"
            threshold: "flood-thresh-1"
        notification:
         -
            alert_int: "720"
            alert_int_mode: "hours"
            alert_src_msisdn: "<your_own_value>"
            alert_status: "enable"
            bword_int: "720"
            bword_int_mode: "hours"
            bword_status: "enable"
            carrier_endpoint_bwl_int: "720"
            carrier_endpoint_bwl_int_mode: "hours"
            carrier_endpoint_bwl_status: "enable"
            days_allowed: "sunday"
            detect_server: "enable"
            dupe_int: "720"
            dupe_int_mode: "hours"
            dupe_status: "enable"
            file_block_int: "720"
            file_block_int_mode: "hours"
            file_block_status: "enable"
            flood_int: "720"
            flood_int_mode: "hours"
            flood_status: "enable"
            from_in_header: "enable"
            mms_checksum_int: "720"
            mms_checksum_int_mode: "hours"
            mms_checksum_status: "enable"
            mmsc_hostname: "myhostname"
            mmsc_password: "<your_own_value>"
            mmsc_port: "32767"
            mmsc_url: "<your_own_value>"
            mmsc_username: "<your_own_value>"
            msg_protocol: "mm1"
            msg_type: "submit-req"
            protocol: "<your_own_value>"
            rate_limit: "125"
            tod_window_duration: "<your_own_value>"
            tod_window_end: "<your_own_value>"
            tod_window_start: "<your_own_value>"
            user_domain: "<your_own_value>"
            vas_id: "<your_own_value>"
            vasp_id: "<your_own_value>"
            virus_int: "720"
            virus_int_mode: "hours"
            virus_status: "enable"
        outbreak_prevention:
            external_blocklist: "disable"
            ftgd_service: "disable"
        remove_blocked_const_length: "enable"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
```

## [Return Values](fortios_firewall_mms_profile_module.md#id6)

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
