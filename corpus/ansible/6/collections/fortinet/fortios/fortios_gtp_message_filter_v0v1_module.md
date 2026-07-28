---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_gtp_message_filter_v0v1 module – Message filter for GTPv0/v1 messages in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_gtp_message_filter_v0v1_module.html
fetched_at: 2026-07-27T17:41:53+00:00
---
# fortinet.fortios.fortios_gtp_message_filter_v0v1 module – Message filter for GTPv0/v1 messages in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_gtp_message_filter_v0v1_module.md#ansible-collections-fortinet-fortios-fortios-gtp-message-filter-v0v1-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_gtp_message_filter_v0v1`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_gtp_message_filter_v0v1_module.md#synopsis)
- [Requirements](fortios_gtp_message_filter_v0v1_module.md#requirements)
- [Parameters](fortios_gtp_message_filter_v0v1_module.md#parameters)
- [Notes](fortios_gtp_message_filter_v0v1_module.md#notes)
- [Examples](fortios_gtp_message_filter_v0v1_module.md#examples)
- [Return Values](fortios_gtp_message_filter_v0v1_module.md#return-values)

## [Synopsis](fortios_gtp_message_filter_v0v1_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify gtp feature and message_filter_v0v1 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_gtp_message_filter_v0v1_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_gtp_message_filter_v0v1_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **gtp_message_filter_v0v1**  dictionary | Message filter for GTPv0/v1 messages. |
| **create_mbms**  string | GTPv1 create MBMS context (req 100, resp 101).  Choices:   - `"allow"` - `"deny"` |
| **create_pdp**  string | Create PDP context (req 16, resp 17).  Choices:   - `"allow"` - `"deny"` |
| **data_record**  string | Data record transfer (req 240, resp 241).  Choices:   - `"allow"` - `"deny"` |
| **delete_aa_pdp**  string | GTPv0 delete AA PDP context (req 24, resp 25).  Choices:   - `"allow"` - `"deny"` |
| **delete_mbms**  string | GTPv1 delete MBMS context (req 104, resp 105).  Choices:   - `"allow"` - `"deny"` |
| **delete_pdp**  string | Delete PDP context (req 20, resp 21).  Choices:   - `"allow"` - `"deny"` |
| **echo**  string | Echo (req 1, resp 2).  Choices:   - `"allow"` - `"deny"` |
| **end_marker**  string | GTPv1 End marker (254).  Choices:   - `"allow"` - `"deny"` |
| **error_indication**  string | Error indication (26).  Choices:   - `"allow"` - `"deny"` |
| **failure_report**  string | Failure report (req 34, resp 35).  Choices:   - `"allow"` - `"deny"` |
| **fwd_relocation**  string | GTPv1 forward relocation (req 53, resp 54, complete 55, complete ack 59).  Choices:   - `"allow"` - `"deny"` |
| **fwd_srns_context**  string | GTPv1 forward SRNS (context 58, context ack 60).  Choices:   - `"allow"` - `"deny"` |
| **gtp_pdu**  string | PDU (255).  Choices:   - `"allow"` - `"deny"` |
| **identification**  string | Identification (req 48, resp 49).  Choices:   - `"allow"` - `"deny"` |
| **mbms_de_registration**  string | GTPv1 MBMS de-registration (req 114, resp 115).  Choices:   - `"allow"` - `"deny"` |
| **mbms_notification**  string | GTPv1 MBMS notification (req 96, resp 97, reject req 98. reject resp 99).  Choices:   - `"allow"` - `"deny"` |
| **mbms_registration**  string | GTPv1 MBMS registration (req 112, resp 113).  Choices:   - `"allow"` - `"deny"` |
| **mbms_session_start**  string | GTPv1 MBMS session start (req 116, resp 117).  Choices:   - `"allow"` - `"deny"` |
| **mbms_session_stop**  string | GTPv1 MBMS session stop (req 118, resp 119).  Choices:   - `"allow"` - `"deny"` |
| **mbms_session_update**  string | GTPv1 MBMS session update (req 120, resp 121).  Choices:   - `"allow"` - `"deny"` |
| **ms_info_change_notif**  string | GTPv1 MS info change notification (req 128, resp 129).  Choices:   - `"allow"` - `"deny"` |
| **name**  string / required | Message filter name. |
| **node_alive**  string | Node alive (req 4, resp 5).  Choices:   - `"allow"` - `"deny"` |
| **note_ms_present**  string | Note MS GPRS present (req 36, resp 37).  Choices:   - `"allow"` - `"deny"` |
| **pdu_notification**  string | PDU notification (req 27, resp 28, reject req 29, reject resp 30).  Choices:   - `"allow"` - `"deny"` |
| **ran_info**  string | GTPv1 RAN information relay (70).  Choices:   - `"allow"` - `"deny"` |
| **redirection**  string | Redirection (req 6, resp 7).  Choices:   - `"allow"` - `"deny"` |
| **relocation_cancel**  string | GTPv1 relocation cancel (req 56, resp 57).  Choices:   - `"allow"` - `"deny"` |
| **send_route**  string | Send routing information for GPRS (req 32, resp 33).  Choices:   - `"allow"` - `"deny"` |
| **sgsn_context**  string | SGSN context (req 50, resp 51, ack 52).  Choices:   - `"allow"` - `"deny"` |
| **support_extension**  string | GTPv1 supported extension headers notify (31).  Choices:   - `"allow"` - `"deny"` |
| **unknown_message**  string | Allow or Deny unknown messages.  Choices:   - `"allow"` - `"deny"` |
| **unknown_message_white_list**  list / elements=dictionary | White list (to allow) of unknown messages. |
| **id**  integer | Message IDs. |
| **update_mbms**  string | GTPv1 update MBMS context (req 102, resp 103).  Choices:   - `"allow"` - `"deny"` |
| **update_pdp**  string | Update PDP context (req 18, resp 19).  Choices:   - `"allow"` - `"deny"` |
| **v0_create_aa_pdp__v1_init_pdp_ctx**  string | GTPv0 create AA PDP context (req 22, resp 23); Or GTPv1 initiate PDP context (req 22, resp 23).  Choices:   - `"allow"` - `"deny"` |
| **version_not_support**  string | Version not supported (3).  Choices:   - `"allow"` - `"deny"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_gtp_message_filter_v0v1_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_gtp_message_filter_v0v1_module.md#id5)

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
  - name: Message filter for GTPv0/v1 messages.
    fortios_gtp_message_filter_v0v1:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      gtp_message_filter_v0v1:
        create_mbms: "allow"
        create_pdp: "allow"
        data_record: "allow"
        delete_aa_pdp: "allow"
        delete_mbms: "allow"
        delete_pdp: "allow"
        echo: "allow"
        end_marker: "allow"
        error_indication: "allow"
        failure_report: "allow"
        fwd_relocation: "allow"
        fwd_srns_context: "allow"
        gtp_pdu: "allow"
        identification: "allow"
        mbms_de_registration: "allow"
        mbms_notification: "allow"
        mbms_registration: "allow"
        mbms_session_start: "allow"
        mbms_session_stop: "allow"
        mbms_session_update: "allow"
        ms_info_change_notif: "allow"
        name: "default_name_24"
        node_alive: "allow"
        note_ms_present: "allow"
        pdu_notification: "allow"
        ran_info: "allow"
        redirection: "allow"
        relocation_cancel: "allow"
        send_route: "allow"
        sgsn_context: "allow"
        support_extension: "allow"
        unknown_message: "allow"
        unknown_message_white_list:
         -
            id:  "36"
        update_mbms: "allow"
        update_pdp: "allow"
        v0_create_aa_pdp__v1_init_pdp_ctx: "allow"
        version_not_support: "allow"
```

## [Return Values](fortios_gtp_message_filter_v0v1_module.md#id6)

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
