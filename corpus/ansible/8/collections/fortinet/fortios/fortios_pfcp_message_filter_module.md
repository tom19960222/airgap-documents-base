---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_pfcp_message_filter module – Message filter for PFCP messages in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_pfcp_message_filter_module.html
fetched_at: 2026-07-28T02:26:33+00:00
---
# fortinet.fortios.fortios_pfcp_message_filter module – Message filter for PFCP messages in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_pfcp_message_filter_module.md#ansible-collections-fortinet-fortios-fortios-pfcp-message-filter-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_pfcp_message_filter`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_pfcp_message_filter_module.md#synopsis)
- [Requirements](fortios_pfcp_message_filter_module.md#requirements)
- [Parameters](fortios_pfcp_message_filter_module.md#parameters)
- [Notes](fortios_pfcp_message_filter_module.md#notes)
- [Examples](fortios_pfcp_message_filter_module.md#examples)
- [Return Values](fortios_pfcp_message_filter_module.md#return-values)

## [Synopsis](fortios_pfcp_message_filter_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify pfcp feature and message_filter category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_pfcp_message_filter_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_pfcp_message_filter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **pfcp_message_filter**  dictionary | Message filter for PFCP messages. |
| **association_release**  string | Allow or deny PFCP association release request (9) and PFCP association release response (10).  **Choices:**   - `"allow"` - `"deny"` |
| **association_setup**  string | Allow or deny PFCP association setup request (5) and PFCP association setup response (6).  **Choices:**   - `"allow"` - `"deny"` |
| **association_update**  string | Allow or deny PFCP association update request (7) and PFCP association update response (8).  **Choices:**   - `"allow"` - `"deny"` |
| **heartbeat**  string | Allow or deny PFCP heartbeat request (1) and PFCP heartbeat response (2).  **Choices:**   - `"allow"` - `"deny"` |
| **name**  string / required | Message filter name. |
| **node_report**  string | Allow or deny PFCP node report request (12) and PFCP node report response (13).  **Choices:**   - `"allow"` - `"deny"` |
| **pfd_management**  string | Allow or deny PFCP PFD management request (3) and PFCP PFD management response (4).  **Choices:**   - `"allow"` - `"deny"` |
| **session_deletion**  string | Allow or deny PFCP session deletion request (54) and PFCP session deletion response (55).  **Choices:**   - `"allow"` - `"deny"` |
| **session_establish**  string | Allow or deny PFCP session establishment request (50) and PFCP session establishment response (51).  **Choices:**   - `"allow"` - `"deny"` |
| **session_modification**  string | Allow or deny PFCP session modification request (52) and PFCP session modification response (53).  **Choices:**   - `"allow"` - `"deny"` |
| **session_report**  string | Allow or deny PFCP session report request (56) and PFCP session report response (57).  **Choices:**   - `"allow"` - `"deny"` |
| **session_set_deletion**  string | Allow or deny PFCP session set deletion request (14) and PFCP session set deletion response (15).  **Choices:**   - `"allow"` - `"deny"` |
| **unknown_message**  string | Allow or deny unknown messages.  **Choices:**   - `"allow"` - `"deny"` |
| **unknown_message_allow_list**  list / elements=dictionary | Allow list of unknown messages. |
| **id**  integer / required | Message IDs (range from 1 to 255). see <a href=’#notes’>Notes</a>. |
| **version_not_support**  string | Allow or deny PFCP version not supported response (11).  **Choices:**   - `"allow"` - `"deny"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_pfcp_message_filter_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_pfcp_message_filter_module.md#id5)

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
  - name: Message filter for PFCP messages.
    fortios_pfcp_message_filter:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      pfcp_message_filter:
        association_release: "allow"
        association_setup: "allow"
        association_update: "allow"
        heartbeat: "allow"
        name: "default_name_7"
        node_report: "allow"
        pfd_management: "allow"
        session_deletion: "allow"
        session_establish: "allow"
        session_modification: "allow"
        session_report: "allow"
        session_set_deletion: "allow"
        unknown_message: "allow"
        unknown_message_allow_list:
         -
            id:  "17"
        version_not_support: "allow"
```

## [Return Values](fortios_pfcp_message_filter_module.md#id6)

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
