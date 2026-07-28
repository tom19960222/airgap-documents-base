---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_spamfilter_profile module – Configure AntiSpam profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_spamfilter_profile_module.html
fetched_at: 2026-07-27T17:43:20+00:00
---
# fortinet.fortios.fortios_spamfilter_profile module – Configure AntiSpam profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_spamfilter_profile_module.md#ansible-collections-fortinet-fortios-fortios-spamfilter-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_spamfilter_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_spamfilter_profile_module.md#synopsis)
- [Requirements](fortios_spamfilter_profile_module.md#requirements)
- [Parameters](fortios_spamfilter_profile_module.md#parameters)
- [Notes](fortios_spamfilter_profile_module.md#notes)
- [Examples](fortios_spamfilter_profile_module.md#examples)
- [Return Values](fortios_spamfilter_profile_module.md#return-values)

## [Synopsis](fortios_spamfilter_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify spamfilter feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_spamfilter_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_spamfilter_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **spamfilter_profile**  dictionary | Configure AntiSpam profiles. |
| **comment**  string | Comment. |
| **external**  string | Enable/disable external Email inspection.  Choices:   - `"enable"` - `"disable"` |
| **flow_based**  string | Enable/disable flow-based spam filtering.  Choices:   - `"enable"` - `"disable"` |
| **gmail**  dictionary | Gmail. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **imap**  dictionary | IMAP. |
| **action**  string | Action for spam email.  Choices:   - `"pass"` - `"tag"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **tag_msg**  string | Subject text or header added to spam email. |
| **tag_type**  list / elements=string | Tag subject or header for spam email.  Choices:   - `"subject"` - `"header"` - `"spaminfo"` |
| **mapi**  dictionary | MAPI. |
| **action**  string | Action for spam email.  Choices:   - `"pass"` - `"discard"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **msn_hotmail**  dictionary | MSN Hotmail. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Profile name. |
| **options**  list / elements=string | Options.  Choices:   - `"bannedword"` - `"spambwl"` - `"spamfsip"` - `"spamfssubmit"` - `"spamfschksum"` - `"spamfsurl"` - `"spamhelodns"` - `"spamraddrdns"` - `"spamrbl"` - `"spamhdrcheck"` - `"spamfsphish"` |
| **pop3**  dictionary | POP3. |
| **action**  string | Action for spam email.  Choices:   - `"pass"` - `"tag"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **tag_msg**  string | Subject text or header added to spam email. |
| **tag_type**  list / elements=string | Tag subject or header for spam email.  Choices:   - `"subject"` - `"header"` - `"spaminfo"` |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **smtp**  dictionary | SMTP. |
| **action**  string | Action for spam email.  Choices:   - `"pass"` - `"tag"` - `"discard"` |
| **hdrip**  string | Enable/disable SMTP email header IP checks for spamfsip, spamrbl and spambwl filters.  Choices:   - `"disable"` - `"enable"` |
| **local_override**  string | Enable/disable local filter to override SMTP remote check result.  Choices:   - `"disable"` - `"enable"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **tag_msg**  string | Subject text or header added to spam email. |
| **tag_type**  list / elements=string | Tag subject or header for spam email.  Choices:   - `"subject"` - `"header"` - `"spaminfo"` |
| **spam_bwl_table**  integer | Anti-spam black/white list table ID. Source spamfilter.bwl.id. |
| **spam_bword_table**  integer | Anti-spam banned word table ID. Source spamfilter.bword.id. |
| **spam_bword_threshold**  integer | Spam banned word threshold. |
| **spam_filtering**  string | Enable/disable spam filtering.  Choices:   - `"enable"` - `"disable"` |
| **spam_iptrust_table**  integer | Anti-spam IP trust table ID. Source spamfilter.iptrust.id. |
| **spam_log**  string | Enable/disable spam logging for email filtering.  Choices:   - `"disable"` - `"enable"` |
| **spam_log_fortiguard_response**  string | Enable/disable logging FortiGuard spam response.  Choices:   - `"disable"` - `"enable"` |
| **spam_mheader_table**  integer | Anti-spam MIME header table ID. Source spamfilter.mheader.id. |
| **spam_rbl_table**  integer | Anti-spam DNSBL table ID. Source spamfilter.dnsbl.id. |
| **yahoo_mail**  dictionary | Yahoo! Mail. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_spamfilter_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_spamfilter_profile_module.md#id5)

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
  - name: Configure AntiSpam profiles.
    fortios_spamfilter_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      spamfilter_profile:
        comment: "Comment."
        external: "enable"
        flow_based: "enable"
        gmail:
            log: "enable"
        imap:
            action: "pass"
            log: "enable"
            tag_msg: "<your_own_value>"
            tag_type: "subject"
        mapi:
            action: "pass"
            log: "enable"
        msn_hotmail:
            log: "enable"
        name: "default_name_18"
        options: "bannedword"
        pop3:
            action: "pass"
            log: "enable"
            tag_msg: "<your_own_value>"
            tag_type: "subject"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        smtp:
            action: "pass"
            hdrip: "disable"
            local_override: "disable"
            log: "enable"
            tag_msg: "<your_own_value>"
            tag_type: "subject"
        spam_bwl_table: "2147483647"
        spam_bword_table: "2147483647"
        spam_bword_threshold: "1073741823"
        spam_filtering: "enable"
        spam_iptrust_table: "2147483647"
        spam_log: "disable"
        spam_log_fortiguard_response: "disable"
        spam_mheader_table: "2147483647"
        spam_rbl_table: "2147483647"
        yahoo_mail:
            log: "enable"
```

## [Return Values](fortios_spamfilter_profile_module.md#id6)

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
