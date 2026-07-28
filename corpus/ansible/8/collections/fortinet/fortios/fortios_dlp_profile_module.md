---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_dlp_profile module – Configure DLP profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_dlp_profile_module.html
fetched_at: 2026-07-28T02:23:39+00:00
---
# fortinet.fortios.fortios_dlp_profile module – Configure DLP profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_dlp_profile_module.md#ansible-collections-fortinet-fortios-fortios-dlp-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_dlp_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_dlp_profile_module.md#synopsis)
- [Requirements](fortios_dlp_profile_module.md#requirements)
- [Parameters](fortios_dlp_profile_module.md#parameters)
- [Notes](fortios_dlp_profile_module.md#notes)
- [Examples](fortios_dlp_profile_module.md#examples)
- [Return Values](fortios_dlp_profile_module.md#return-values)

## [Synopsis](fortios_dlp_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify dlp feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_dlp_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_dlp_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **dlp_profile**  dictionary | Configure DLP profiles. |
| **comment**  string | Comment. |
| **dlp_log**  string | Enable/disable DLP logging.  **Choices:**   - `"enable"` - `"disable"` |
| **extended_log**  string | Enable/disable extended logging for data leak prevention.  **Choices:**   - `"enable"` - `"disable"` |
| **feature_set**  string | Flow/proxy feature set.  **Choices:**   - `"flow"` - `"proxy"` |
| **full_archive_proto**  list / elements=string | Protocols to always content archive.  **Choices:**   - `"smtp"` - `"pop3"` - `"imap"` - `"http-get"` - `"http-post"` - `"ftp"` - `"nntp"` - `"mapi"` - `"ssh"` - `"cifs"` |
| **nac_quar_log**  string | Enable/disable NAC quarantine logging.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Name of the DLP profile. |
| **replacemsg_group**  string | Replacement message group used by this DLP profile. Source system.replacemsg-group.name. |
| **rule**  list / elements=dictionary | Set up DLP rules for this profile. |
| **action**  string | Action to take with content that this DLP profile matches.  **Choices:**   - `"allow"` - `"log-only"` - `"block"` - `"quarantine-ip"` |
| **archive**  string | Enable/disable DLP archiving.  **Choices:**   - `"disable"` - `"enable"` |
| **expiry**  string | Quarantine duration in days, hours, minutes (format = dddhhmm). |
| **file_size**  integer | Match files greater than or equal to this size (KB). |
| **file_type**  integer | Select the number of a DLP file pattern table to match. Source dlp.filepattern.id. |
| **filter_by**  string | Select the type of content to match.  **Choices:**   - `"sensor"` - `"mip"` - `"fingerprint"` - `"encrypted"` - `"none"` |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **label**  string | MIP label dictionary. Source dlp.dictionary.name. |
| **match_percentage**  integer | Percentage of fingerprints in the fingerprint databases designated with the selected sensitivity to match. |
| **name**  string | Filter name. |
| **proto**  list / elements=string | Check messages or files over one or more of these protocols.  **Choices:**   - `"smtp"` - `"pop3"` - `"imap"` - `"http-get"` - `"http-post"` - `"ftp"` - `"nntp"` - `"mapi"` - `"ssh"` - `"cifs"` |
| **sensitivity**  list / elements=dictionary | Select a DLP file pattern sensitivity to match. |
| **name**  string / required | Select a DLP sensitivity. Source dlp.sensitivity.name. |
| **sensor**  list / elements=dictionary | Select DLP sensors. |
| **name**  string / required | Address name. Source dlp.sensor.name. |
| **severity**  string | Select the severity or threat level that matches this filter.  **Choices:**   - `"info"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **type**  string | Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).  **Choices:**   - `"file"` - `"fos_message"` |
| **summary_proto**  list / elements=string | Protocols to always log summary.  **Choices:**   - `"smtp"` - `"pop3"` - `"imap"` - `"http-get"` - `"http-post"` - `"ftp"` - `"nntp"` - `"mapi"` - `"ssh"` - `"cifs"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_dlp_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_dlp_profile_module.md#id5)

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
  - name: Configure DLP profiles.
    fortios_dlp_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      dlp_profile:
        comment: "Comment."
        dlp_log: "enable"
        extended_log: "enable"
        feature_set: "flow"
        full_archive_proto: "smtp"
        nac_quar_log: "enable"
        name: "default_name_9"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        rule:
         -
            action: "allow"
            archive: "disable"
            expiry: "<your_own_value>"
            file_size: "0"
            file_type: "0"
            filter_by: "sensor"
            id:  "18"
            label: "<your_own_value> (source dlp.dictionary.name)"
            match_percentage: "10"
            name: "default_name_21"
            proto: "smtp"
            sensitivity:
             -
                name: "default_name_24 (source dlp.sensitivity.name)"
            sensor:
             -
                name: "default_name_26 (source dlp.sensor.name)"
            severity: "info"
            type: "file"
        summary_proto: "smtp"
```

## [Return Values](fortios_dlp_profile_module.md#id6)

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
