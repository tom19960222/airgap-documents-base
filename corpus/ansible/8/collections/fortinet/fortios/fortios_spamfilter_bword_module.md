---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_spamfilter_bword module – Configure AntiSpam banned word list in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_spamfilter_bword_module.html
fetched_at: 2026-07-28T02:27:00+00:00
---
# fortinet.fortios.fortios_spamfilter_bword module – Configure AntiSpam banned word list in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_spamfilter_bword_module.md#ansible-collections-fortinet-fortios-fortios-spamfilter-bword-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_spamfilter_bword`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_spamfilter_bword_module.md#synopsis)
- [Requirements](fortios_spamfilter_bword_module.md#requirements)
- [Parameters](fortios_spamfilter_bword_module.md#parameters)
- [Notes](fortios_spamfilter_bword_module.md#notes)
- [Examples](fortios_spamfilter_bword_module.md#examples)
- [Return Values](fortios_spamfilter_bword_module.md#return-values)

## [Synopsis](fortios_spamfilter_bword_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify spamfilter feature and bword category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_spamfilter_bword_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_spamfilter_bword_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **spamfilter_bword**  dictionary | Configure AntiSpam banned word list. |
| **comment**  string | Optional comments. |
| **entries**  list / elements=dictionary | Spam filter banned word. |
| **action**  string | Mark spam or good.  **Choices:**   - `"spam"` - `"clear"` |
| **id**  integer / required | Banned word entry ID. see <a href=’#notes’>Notes</a>. |
| **language**  string | Language for the banned word.  **Choices:**   - `"western"` - `"simch"` - `"trach"` - `"japanese"` - `"korean"` - `"french"` - `"thai"` - `"spanish"` |
| **pattern**  string | Pattern for the banned word. |
| **pattern_type**  string | Wildcard pattern or regular expression.  **Choices:**   - `"wildcard"` - `"regexp"` |
| **score**  integer | Score value. |
| **status**  string | Enable/disable status.  **Choices:**   - `"enable"` - `"disable"` |
| **where**  string | Component of the email to be scanned.  **Choices:**   - `"subject"` - `"body"` - `"all"` |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **name**  string | Name of table. |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_spamfilter_bword_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_spamfilter_bword_module.md#id5)

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
  - name: Configure AntiSpam banned word list.
    fortios_spamfilter_bword:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      spamfilter_bword:
        comment: "Optional comments."
        entries:
         -
            action: "spam"
            id:  "6"
            language: "western"
            pattern: "<your_own_value>"
            pattern_type: "wildcard"
            score: "49999"
            status: "enable"
            where: "subject"
        id:  "13"
        name: "default_name_14"
```

## [Return Values](fortios_spamfilter_bword_module.md#id6)

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
