---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_dlp_sensor module – Configure sensors used by DLP blocking in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_dlp_sensor_module.html
fetched_at: 2026-07-27T17:40:10+00:00
---
# fortinet.fortios.fortios_dlp_sensor module – Configure sensors used by DLP blocking in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_dlp_sensor_module.md#ansible-collections-fortinet-fortios-fortios-dlp-sensor-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_dlp_sensor`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_dlp_sensor_module.md#synopsis)
- [Requirements](fortios_dlp_sensor_module.md#requirements)
- [Parameters](fortios_dlp_sensor_module.md#parameters)
- [Notes](fortios_dlp_sensor_module.md#notes)
- [Examples](fortios_dlp_sensor_module.md#examples)
- [Return Values](fortios_dlp_sensor_module.md#return-values)

## [Synopsis](fortios_dlp_sensor_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify dlp feature and sensor category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_dlp_sensor_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_dlp_sensor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **dlp_sensor**  dictionary | Configure sensors used by DLP blocking. |
| **comment**  string | Optional comments. |
| **dlp_log**  string | Enable/disable DLP logging.  Choices:   - `"enable"` - `"disable"` |
| **entries**  list / elements=dictionary | DLP sensor entries. |
| **count**  integer | Count of dictionary matches to trigger sensor entry match (Dictionary might not be able to trigger more than once based on its “repeat” option, 1 - 255). |
| **dictionary**  string | Select a DLP dictionary. Source dlp.dictionary.name. |
| **id**  integer | ID. |
| **status**  string | Enable/disable this entry.  Choices:   - `"enable"` - `"disable"` |
| **eval**  string | Expression to evaluate. |
| **extended_log**  string | Enable/disable extended logging for data leak prevention.  Choices:   - `"enable"` - `"disable"` |
| **feature_set**  string | Flow/proxy feature set.  Choices:   - `"flow"` - `"proxy"` |
| **filter**  list / elements=dictionary | Set up DLP filters for this sensor. |
| **action**  string | Action to take with content that this DLP sensor matches.  Choices:   - `"allow"` - `"log-only"` - `"block"` - `"quarantine-ip"` |
| **archive**  string | Enable/disable DLP archiving.  Choices:   - `"disable"` - `"enable"` |
| **company_identifier**  string | Enter a company identifier watermark to match. Only watermarks that your company has placed on the files are matched. |
| **expiry**  string | Quarantine duration in days, hours, minutes (format = dddhhmm). |
| **file_size**  integer | Match files this size or larger (0 - 4294967295 kbytes). |
| **file_type**  integer | Select the number of a DLP file pattern table to match. Source dlp.filepattern.id. |
| **filter_by**  string | Select the type of content to match.  Choices:   - `"credit-card"` - `"ssn"` - `"regexp"` - `"file-type"` - `"file-size"` - `"fingerprint"` - `"watermark"` - `"encrypted"` |
| **fp_sensitivity**  list / elements=dictionary | Select a DLP file pattern sensitivity to match. |
| **name**  string | Select a DLP sensitivity. Source dlp.fp-sensitivity.name. |
| **id**  integer | ID. |
| **match_percentage**  integer | Percentage of fingerprints in the fingerprint databases designated with the selected sensitivity to match. |
| **name**  string | Filter name. |
| **proto**  list / elements=string | Check messages or files over one or more of these protocols.  Choices:   - `"smtp"` - `"pop3"` - `"imap"` - `"http-get"` - `"http-post"` - `"ftp"` - `"nntp"` - `"mapi"` - `"ssh"` - `"cifs"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **regexp**  string | Enter a regular expression to match (max. 255 characters). |
| **sensitivity**  list / elements=dictionary | Select a DLP file pattern sensitivity to match. |
| **name**  string | Select a DLP sensitivity. Source dlp.sensitivity.name. |
| **severity**  string | Select the severity or threat level that matches this filter.  Choices:   - `"info"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **type**  string | Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).  Choices:   - `"file"` - `"fos_message"` |
| **flow_based**  string | Enable/disable flow-based DLP.  Choices:   - `"enable"` - `"disable"` |
| **full_archive_proto**  list / elements=string | Protocols to always content archive.  Choices:   - `"smtp"` - `"pop3"` - `"imap"` - `"http-get"` - `"http-post"` - `"ftp"` - `"nntp"` - `"mapi"` - `"ssh"` - `"cifs"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **match_type**  string | Logical relation between entries .  Choices:   - `"match-all"` - `"match-any"` - `"match-eval"` |
| **nac_quar_log**  string | Enable/disable NAC quarantine logging.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Name of table containing the sensor. |
| **options**  string | Configure DLP options. |
| **replacemsg_group**  string | Replacement message group used by this DLP sensor. Source system.replacemsg-group.name. |
| **summary_proto**  list / elements=string | Protocols to always log summary.  Choices:   - `"smtp"` - `"pop3"` - `"imap"` - `"http-get"` - `"http-post"` - `"ftp"` - `"nntp"` - `"mapi"` - `"ssh"` - `"cifs"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_dlp_sensor_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_dlp_sensor_module.md#id5)

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
  - name: Configure sensors used by DLP blocking.
    fortios_dlp_sensor:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      dlp_sensor:
        comment: "Optional comments."
        dlp_log: "enable"
        entries:
         -
            count: "1"
            dictionary: "<your_own_value> (source dlp.dictionary.name)"
            id:  "8"
            status: "enable"
        eval: "<your_own_value>"
        extended_log: "enable"
        feature_set: "flow"
        filter:
         -
            action: "allow"
            archive: "disable"
            company_identifier:  "myId_16"
            expiry: "<your_own_value>"
            file_size: "10"
            file_type: "0"
            filter_by: "credit-card"
            fp_sensitivity:
             -
                name: "default_name_22 (source dlp.fp-sensitivity.name)"
            id:  "23"
            match_percentage: "10"
            name: "default_name_25"
            proto: "smtp"
            regexp: "<your_own_value>"
            sensitivity:
             -
                name: "default_name_29 (source dlp.sensitivity.name)"
            severity: "info"
            type: "file"
        flow_based: "enable"
        full_archive_proto: "smtp"
        match_type: "match-all"
        nac_quar_log: "enable"
        name: "default_name_36"
        options: "<your_own_value>"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        summary_proto: "smtp"
```

## [Return Values](fortios_dlp_sensor_module.md#id6)

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
