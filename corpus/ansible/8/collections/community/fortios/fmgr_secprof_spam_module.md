---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_spam module – spam filter profile for FMG"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_spam_module.html
fetched_at: 2026-07-28T01:44:22+00:00
---
# community.fortios.fmgr_secprof_spam module – spam filter profile for FMG

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_spam`.

- [Synopsis](fmgr_secprof_spam_module.md#synopsis)
- [Parameters](fmgr_secprof_spam_module.md#parameters)
- [Notes](fmgr_secprof_spam_module.md#notes)
- [Examples](fmgr_secprof_spam_module.md#examples)
- [Return Values](fmgr_secprof_spam_module.md#return-values)

## [Synopsis](fmgr_secprof_spam_module.md#id1)

- Manage spam filter security profiles within FortiManager via API

## [Parameters](fmgr_secprof_spam_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **comment**  string | Comment. |
| **external**  string | Enable/disable external Email inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **flow_based**  string | Enable/disable flow-based spam filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **gmail**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **gmail_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **imap**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **imap_action**  string | Action for spam email.  **Choices:**   - `"pass"` - `"tag"` |
| **imap_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **imap_tag_msg**  string | Subject text or header added to spam email. |
| **imap_tag_type**  string | Tag subject or header for spam email.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"subject"` - `"header"` - `"spaminfo"` |
| **mapi**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **mapi_action**  string | Action for spam email.  **Choices:**   - `"pass"` - `"discard"` |
| **mapi_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **msn_hotmail**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **msn_hotmail_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string | Profile name. |
| **options**  string | None  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"bannedword"` - `"spamfsip"` - `"spamfssubmit"` - `"spamfschksum"` - `"spamfsurl"` - `"spamhelodns"` - `"spamraddrdns"` - `"spamrbl"` - `"spamhdrcheck"` - `"spamfsphish"` - `"spambwl"` |
| **pop3**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **pop3_action**  string | Action for spam email.  **Choices:**   - `"pass"` - `"tag"` |
| **pop3_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **pop3_tag_msg**  string | Subject text or header added to spam email. |
| **pop3_tag_type**  string | Tag subject or header for spam email.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"subject"` - `"header"` - `"spaminfo"` |
| **replacemsg_group**  string | Replacement message group. |
| **smtp**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **smtp_action**  string | Action for spam email.  **Choices:**   - `"pass"` - `"tag"` - `"discard"` |
| **smtp_hdrip**  string | Enable/disable SMTP email header IP checks for spamfsip, spamrbl and spambwl filters.  **Choices:**   - `"disable"` - `"enable"` |
| **smtp_local_override**  string | Enable/disable local filter to override SMTP remote check result.  **Choices:**   - `"disable"` - `"enable"` |
| **smtp_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **smtp_tag_msg**  string | Subject text or header added to spam email. |
| **smtp_tag_type**  string | Tag subject or header for spam email.  FLAG Based Options. Specify multiple in list form.  **Choices:**   - `"subject"` - `"header"` - `"spaminfo"` |
| **spam_bwl_table**  string | Anti-spam black/white list table ID. |
| **spam_bword_table**  string | Anti-spam banned word table ID. |
| **spam_bword_threshold**  string | Spam banned word threshold. |
| **spam_filtering**  string | Enable/disable spam filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **spam_iptrust_table**  string | Anti-spam IP trust table ID. |
| **spam_log**  string | Enable/disable spam logging for email filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **spam_log_fortiguard_response**  string | Enable/disable logging FortiGuard spam response.  **Choices:**   - `"disable"` - `"enable"` |
| **spam_mheader_table**  string | Anti-spam MIME header table ID. |
| **spam_rbl_table**  string | Anti-spam DNSBL table ID. |
| **yahoo_mail**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **yahoo_mail_log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |

## [Notes](fmgr_secprof_spam_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_spam_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_spam:
    name: "Ansible_Spam_Filter_Profile"
    mode: "delete"

- name: Create FMGR_SPAMFILTER_PROFILE
  community.fortios.fmgr_secprof_spam:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    mode: "set"
    adom: "root"
    spam_log_fortiguard_response: "enable"
    spam_iptrust_table:
    spam_filtering: "enable"
    spam_bword_threshold: 10
    options: ["bannedword", "spamfsip", "spamfsurl", "spamrbl", "spamfsphish", "spambwl"]
    name: "Ansible_Spam_Filter_Profile"
    flow_based: "enable"
    external: "enable"
    comment: "Created by Ansible"
    gmail_log: "enable"
    spam_log: "enable"
```

## [Return Values](fmgr_secprof_spam_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
