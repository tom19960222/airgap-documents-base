---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_gtp_message_filter_v2 module – Message filter for GTPv2 messages in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_gtp_message_filter_v2_module.html
fetched_at: 2026-07-28T02:25:31+00:00
---
# fortinet.fortios.fortios_gtp_message_filter_v2 module – Message filter for GTPv2 messages in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_gtp_message_filter_v2_module.md#ansible-collections-fortinet-fortios-fortios-gtp-message-filter-v2-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_gtp_message_filter_v2`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_gtp_message_filter_v2_module.md#synopsis)
- [Requirements](fortios_gtp_message_filter_v2_module.md#requirements)
- [Parameters](fortios_gtp_message_filter_v2_module.md#parameters)
- [Notes](fortios_gtp_message_filter_v2_module.md#notes)
- [Examples](fortios_gtp_message_filter_v2_module.md#examples)
- [Return Values](fortios_gtp_message_filter_v2_module.md#return-values)

## [Synopsis](fortios_gtp_message_filter_v2_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify gtp feature and message_filter_v2 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_gtp_message_filter_v2_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_gtp_message_filter_v2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **gtp_message_filter_v2**  dictionary | Message filter for GTPv2 messages. |
| **alert_mme_notif_ack**  string | Alert MME notification/acknowledge (notif 153, ack 154).  **Choices:**   - `"allow"` - `"deny"` |
| **bearer_resource_cmd_fail**  string | Bearer resource (command 68, failure indication 69).  **Choices:**   - `"allow"` - `"deny"` |
| **change_notification**  string | Change notification (req 38, resp 39).  **Choices:**   - `"allow"` - `"deny"` |
| **configuration_transfer_tunnel**  string | Configuration transfer tunnel (141).  **Choices:**   - `"allow"` - `"deny"` |
| **context_req_res_ack**  string | Context request/response/acknowledge (req 130, resp 131, ack 132).  **Choices:**   - `"allow"` - `"deny"` |
| **create_bearer**  string | Create bearer (req 95, resp 96).  **Choices:**   - `"allow"` - `"deny"` |
| **create_forwarding_tunnel_req_resp**  string | Create forwarding tunnel request/response (req 160, resp 161).  **Choices:**   - `"allow"` - `"deny"` |
| **create_indirect_forwarding_tunnel_req_resp**  string | Create indirect data forwarding tunnel request/response (req 166, resp 167).  **Choices:**   - `"allow"` - `"deny"` |
| **create_session**  string | Create session (req 32, resp 33).  **Choices:**   - `"allow"` - `"deny"` |
| **cs_paging**  string | CS paging indication (151)  **Choices:**   - `"allow"` - `"deny"` |
| **delete_bearer_cmd_fail**  string | Delete bearer (command 66, failure indication 67).  **Choices:**   - `"allow"` - `"deny"` |
| **delete_bearer_req_resp**  string | Delete bearer (req 99, resp 100).  **Choices:**   - `"allow"` - `"deny"` |
| **delete_indirect_forwarding_tunnel_req_resp**  string | Delete indirect data forwarding tunnel request/response (req 168, resp 169).  **Choices:**   - `"allow"` - `"deny"` |
| **delete_pdn_connection_set**  string | Delete PDN connection set (req 101, resp 102).  **Choices:**   - `"allow"` - `"deny"` |
| **delete_session**  string | Delete session (req 36, resp 37).  **Choices:**   - `"allow"` - `"deny"` |
| **detach_notif_ack**  string | Detach notification/acknowledge (notif 149, ack 150).  **Choices:**   - `"allow"` - `"deny"` |
| **dlink_data_notif_ack**  string | Downlink data notification/acknowledge (notif 176, ack 177).  **Choices:**   - `"allow"` - `"deny"` |
| **dlink_notif_failure**  string | Downlink data notification failure indication (70).  **Choices:**   - `"allow"` - `"deny"` |
| **echo**  string | Echo (req 1, resp 2).  **Choices:**   - `"allow"` - `"deny"` |
| **forward_access_notif_ack**  string | Forward access context notification/acknowledge (notif 137, ack 138).  **Choices:**   - `"allow"` - `"deny"` |
| **forward_relocation_cmp_notif_ack**  string | Forward relocation complete notification/acknowledge (notif 135, ack 136).  **Choices:**   - `"allow"` - `"deny"` |
| **forward_relocation_req_res**  string | Forward relocation request/response (req 133, resp 134).  **Choices:**   - `"allow"` - `"deny"` |
| **identification_req_resp**  string | Identification request/response (req 128, resp 129).  **Choices:**   - `"allow"` - `"deny"` |
| **isr_status**  string | ISR status indication (157).  **Choices:**   - `"allow"` - `"deny"` |
| **mbms_session_start_req_resp**  string | MBMS session start request/response (req 231, resp 232).  **Choices:**   - `"allow"` - `"deny"` |
| **mbms_session_stop_req_resp**  string | MBMS session stop request/response (req 235, resp 236).  **Choices:**   - `"allow"` - `"deny"` |
| **mbms_session_update_req_resp**  string | MBMS session update request/response (req 233, resp 234).  **Choices:**   - `"allow"` - `"deny"` |
| **modify_access_req_resp**  string | Modify access bearers request/response (req 211, resp 212).  **Choices:**   - `"allow"` - `"deny"` |
| **modify_bearer_cmd_fail**  string | Modify bearer (command 64 , failure indication 65).  **Choices:**   - `"allow"` - `"deny"` |
| **modify_bearer_req_resp**  string | Modify bearer (req 34, resp 35).  **Choices:**   - `"allow"` - `"deny"` |
| **name**  string / required | Message filter name. |
| **pgw_dlink_notif_ack**  string | PGW downlink triggering notification/acknowledge (notif 103, ack 104).  **Choices:**   - `"allow"` - `"deny"` |
| **pgw_restart_notif_ack**  string | PGW restart notification/acknowledge (notif 179, ack 180).  **Choices:**   - `"allow"` - `"deny"` |
| **ran_info_relay**  string | RAN information relay (152).  **Choices:**   - `"allow"` - `"deny"` |
| **release_access_bearer_req_resp**  string | Release access bearers request/response (req 170, resp 171).  **Choices:**   - `"allow"` - `"deny"` |
| **relocation_cancel_req_resp**  string | Relocation cancel request/response (req 139, resp 140).  **Choices:**   - `"allow"` - `"deny"` |
| **remote_ue_report_notif_ack**  string | Remote UE report notification/acknowledge (notif 40, ack 41).  **Choices:**   - `"allow"` - `"deny"` |
| **reserved_for_earlier_version**  string | Reserved for earlier version of the GTP specification (178).  **Choices:**   - `"allow"` - `"deny"` |
| **resume**  string | Resume (notify 164 , ack 165).  **Choices:**   - `"allow"` - `"deny"` |
| **stop_paging_indication**  string | Stop Paging Indication (73).  **Choices:**   - `"allow"` - `"deny"` |
| **suspend**  string | Suspend (notify 162, ack 163).  **Choices:**   - `"allow"` - `"deny"` |
| **trace_session**  string | Trace session (activation 71, deactivation 72).  **Choices:**   - `"allow"` - `"deny"` |
| **ue_activity_notif_ack**  string | UE activity notification/acknowledge (notif 155, ack 156).  **Choices:**   - `"allow"` - `"deny"` |
| **ue_registration_query_req_resp**  string | UE registration query request/response (req 158, resp 159).  **Choices:**   - `"allow"` - `"deny"` |
| **unknown_message**  string | Allow or Deny unknown messages.  **Choices:**   - `"allow"` - `"deny"` |
| **unknown_message_white_list**  list / elements=dictionary | White list (to allow) of unknown messages. |
| **id**  integer / required | Message IDs. see <a href=’#notes’>Notes</a>. |
| **update_bearer**  string | Update bearer (req 97, resp 98).  **Choices:**   - `"allow"` - `"deny"` |
| **update_pdn_connection_set**  string | Update PDN connection set (req 200, resp 201).  **Choices:**   - `"allow"` - `"deny"` |
| **version_not_support**  string | Version not supported (3).  **Choices:**   - `"allow"` - `"deny"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_gtp_message_filter_v2_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_gtp_message_filter_v2_module.md#id5)

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
  - name: Message filter for GTPv2 messages.
    fortios_gtp_message_filter_v2:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      gtp_message_filter_v2:
        alert_mme_notif_ack: "allow"
        bearer_resource_cmd_fail: "allow"
        change_notification: "allow"
        configuration_transfer_tunnel: "allow"
        context_req_res_ack: "allow"
        create_bearer: "allow"
        create_forwarding_tunnel_req_resp: "allow"
        create_indirect_forwarding_tunnel_req_resp: "allow"
        create_session: "allow"
        cs_paging: "allow"
        delete_bearer_cmd_fail: "allow"
        delete_bearer_req_resp: "allow"
        delete_indirect_forwarding_tunnel_req_resp: "allow"
        delete_pdn_connection_set: "allow"
        delete_session: "allow"
        detach_notif_ack: "allow"
        dlink_data_notif_ack: "allow"
        dlink_notif_failure: "allow"
        echo: "allow"
        forward_access_notif_ack: "allow"
        forward_relocation_cmp_notif_ack: "allow"
        forward_relocation_req_res: "allow"
        identification_req_resp: "allow"
        isr_status: "allow"
        mbms_session_start_req_resp: "allow"
        mbms_session_stop_req_resp: "allow"
        mbms_session_update_req_resp: "allow"
        modify_access_req_resp: "allow"
        modify_bearer_cmd_fail: "allow"
        modify_bearer_req_resp: "allow"
        name: "default_name_33"
        pgw_dlink_notif_ack: "allow"
        pgw_restart_notif_ack: "allow"
        ran_info_relay: "allow"
        release_access_bearer_req_resp: "allow"
        relocation_cancel_req_resp: "allow"
        remote_ue_report_notif_ack: "allow"
        reserved_for_earlier_version: "allow"
        resume: "allow"
        stop_paging_indication: "allow"
        suspend: "allow"
        trace_session: "allow"
        ue_activity_notif_ack: "allow"
        ue_registration_query_req_resp: "allow"
        unknown_message: "allow"
        unknown_message_white_list:
         -
            id:  "49"
        update_bearer: "allow"
        update_pdn_connection_set: "allow"
        version_not_support: "allow"
```

## [Return Values](fortios_gtp_message_filter_v2_module.md#id6)

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
