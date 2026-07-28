---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_threat_profile module – Manages threat-profile objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_threat_profile_module.html
fetched_at: 2026-07-28T01:18:13+00:00
---
# check_point.mgmt.cp_mgmt_threat_profile module – Manages threat-profile objects on Check Point over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_threat_profile`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_threat_profile_module.md#synopsis)
- [Parameters](cp_mgmt_threat_profile_module.md#parameters)
- [Examples](cp_mgmt_threat_profile_module.md#examples)
- [Return Values](cp_mgmt_threat_profile_module.md#return-values)

## [Synopsis](cp_mgmt_threat_profile_module.md#id1)

- Manages threat-profile objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_threat_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **activate_protections_by_extended_attributes**  list / elements=dictionary | Activate protections by these extended attributes. |
| **category**  string | IPS tag category name. |
| **name**  string | IPS tag name. |
| **active_protections_performance_impact**  string | Protections with this performance impact only will be activated in the profile.  **Choices:**   - `"high"` - `"medium"` - `"low"` - `"very_low"` |
| **active_protections_severity**  string | Protections with this severity only will be activated in the profile.  **Choices:**   - `"Critical"` - `"High"` - `"Medium or above"` - `"Low or above"` |
| **anti_bot**  boolean | Is Anti-Bot blade activated.  **Choices:**   - `false` - `true` |
| **anti_virus**  boolean | Is Anti-Virus blade activated.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **confidence_level_high**  string | Action for protections with high confidence level.  **Choices:**   - `"Inactive"` - `"Ask"` - `"Prevent"` - `"Detect"` |
| **confidence_level_low**  string | Action for protections with low confidence level.  **Choices:**   - `"Inactive"` - `"Ask"` - `"Prevent"` - `"Detect"` |
| **confidence_level_medium**  string | Action for protections with medium confidence level.  **Choices:**   - `"Inactive"` - `"Ask"` - `"Prevent"` - `"Detect"` |
| **deactivate_protections_by_extended_attributes**  list / elements=dictionary | Deactivate protections by these extended attributes. |
| **category**  string | IPS tag category name. |
| **name**  string | IPS tag name. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **indicator_overrides**  list / elements=dictionary | Indicators whose action will be overridden in this profile. |
| **action**  string | The indicator’s action in this profile.  **Choices:**   - `"Inactive"` - `"Ask"` - `"Prevent"` - `"Detect"` |
| **indicator**  string | The indicator whose action is to be overridden. |
| **ips**  boolean | Is IPS blade activated.  **Choices:**   - `false` - `true` |
| **ips_settings**  dictionary | IPS blade settings. |
| **exclude_protection_with_performance_impact**  boolean | Whether to exclude protections depending on their level of performance impact.  **Choices:**   - `false` - `true` |
| **exclude_protection_with_performance_impact_mode**  string | Exclude protections with this level of performance impact.  **Choices:**   - `"very low"` - `"low or lower"` - `"medium or lower"` - `"high or lower"` |
| **exclude_protection_with_severity**  boolean | Whether to exclude protections depending on their level of severity.  **Choices:**   - `false` - `true` |
| **exclude_protection_with_severity_mode**  string | Exclude protections with this level of severity.  **Choices:**   - `"low or above"` - `"medium or above"` - `"high or above"` - `"critical"` |
| **newly_updated_protections**  string | Activation of newly updated protections.  **Choices:**   - `"active"` - `"inactive"` - `"staging"` |
| **malicious_mail_policy_settings**  dictionary | Malicious Mail Policy for MTA Gateways. |
| **add_customized_text_to_email_body**  boolean | Add customized text to the malicious email body.  **Choices:**   - `false` - `true` |
| **add_email_subject_prefix**  boolean | Add a prefix to the malicious email subject.  **Choices:**   - `false` - `true` |
| **add_x_header_to_email**  boolean | Add an X-Header to the malicious email.  **Choices:**   - `false` - `true` |
| **email_action**  string | Block - block the entire malicious email<br>Allow - pass the malicious email and apply email changes (like, remove attachments and links, add x-header, etc…).  **Choices:**   - `"allow"` - `"block"` |
| **email_body_customized_text**  string | Customized text for the malicious email body.<br> Available predefined fields,<br> $verdicts$ - the malicious/error attachments/links verdict. |
| **email_subject_prefix_text**  string | Prefix for the malicious email subject. |
| **failed_to_scan_attachments_text**  string | Replace attachments that failed to be scanned with this text.<br> Available predefined fields,<br> $filename$ - the malicious file name.<br> $md5$ - MD5 of the malicious file. |
| **malicious_attachments_text**  string | Replace malicious attachments with this text.<br> Available predefined fields,<br> $filename$ - the malicious file name.<br> $md5$ - MD5 of the malicious file. |
| **malicious_links_text**  string | Replace malicious links with this text.<br> Available predefined fields,<br> $neutralized_url$ - neutralized malicious link. |
| **remove_attachments_and_links**  boolean | Remove attachments and links from the malicious email.  **Choices:**   - `false` - `true` |
| **send_copy**  boolean | Send a copy of the malicious email to the recipient list.  **Choices:**   - `false` - `true` |
| **send_copy_list**  list / elements=string | Recipient list to send a copy of the malicious email. |
| **name**  string / required | Object name. |
| **overrides**  list / elements=dictionary | Overrides per profile for this protection. |
| **action**  string | Protection action.  **Choices:**   - `"Threat Cloud: Inactive"` - `"Detect"` - `"Prevent <br> Core: Drop"` - `"Inactive"` - `"Accept"` |
| **capture_packets**  boolean | Capture packets.  **Choices:**   - `false` - `true` |
| **protection**  string | IPS protection identified by name or UID. |
| **track**  string | Tracking method for protection.  **Choices:**   - `"none"` - `"log"` - `"alert"` - `"mail"` - `"snmp trap"` - `"user alert"` - `"user alert 1"` - `"user alert 2"` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **threat_emulation**  boolean | Is Threat Emulation blade activated.  **Choices:**   - `false` - `true` |
| **use_extended_attributes**  boolean | Whether to activate/deactivate IPS protections according to the extended attributes.  **Choices:**   - `false` - `true` |
| **use_indicators**  boolean | Indicates whether the profile should make use of indicators.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_threat_profile_module.md#id3)

```yaml+jinja
- name: add-threat-profile
  cp_mgmt_threat_profile:
    active_protections_performance_impact: low
    active_protections_severity: low or above
    anti_bot: true
    anti_virus: true
    confidence_level_high: prevent
    confidence_level_medium: prevent
    ips: true
    ips_settings:
      exclude_protection_with_performance_impact: true
      exclude_protection_with_performance_impact_mode: high or lower
      newly_updated_protections: staging
    name: New Profile 1
    state: present
    threat_emulation: true

- name: set-threat-profile
  cp_mgmt_threat_profile:
    active_protections_performance_impact: low
    active_protections_severity: low or above
    anti_bot: true
    anti_virus: false
    comments: update recommended profile
    confidence_level_high: prevent
    confidence_level_low: prevent
    confidence_level_medium: prevent
    ips: false
    ips_settings:
      exclude_protection_with_performance_impact: true
      exclude_protection_with_performance_impact_mode: high or lower
      newly_updated_protections: active
    name: New Profile 1
    state: present
    threat_emulation: true

- name: delete-threat-profile
  cp_mgmt_threat_profile:
    name: New Profile 1
    state: absent
```

## [Return Values](cp_mgmt_threat_profile_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_threat_profile**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
