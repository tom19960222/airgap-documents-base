---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_access_rule module – Manages access-rule objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_access_rule_module.html
fetched_at: 2026-07-28T01:15:38+00:00
---
# check_point.mgmt.cp_mgmt_access_rule module – Manages access-rule objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_access_rule`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_access_rule_module.md#synopsis)
- [Parameters](cp_mgmt_access_rule_module.md#parameters)
- [Examples](cp_mgmt_access_rule_module.md#examples)
- [Return Values](cp_mgmt_access_rule_module.md#return-values)

## [Synopsis](cp_mgmt_access_rule_module.md#id1)

- Manages access-rule objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_access_rule_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | a “Accept”, “Drop”, “Ask”, “Inform”, “Reject”, “User Auth”, “Client Auth”, “Apply Layer”. |
| **action_settings**  dictionary | Action settings. |
| **enable_identity_captive_portal**  boolean | N/A  **Choices:**   - `false` - `true` |
| **limit**  string | N/A |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **comments**  string | Comments string. |
| **content**  list / elements=dictionary | List of processed file types that this rule applies on. |
| **content_direction**  string | On which direction the file types processing is applied.  **Choices:**   - `"any"` - `"up"` - `"down"` |
| **content_negate**  boolean | True if negate is set for data.  **Choices:**   - `false` - `true` |
| **custom_fields**  dictionary | Custom fields. |
| **field_1**  string | First custom field. |
| **field_2**  string | Second custom field. |
| **field_3**  string | Third custom field. |
| **destination**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **destination_negate**  boolean | True if negate is set for destination.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **enabled**  boolean | Enable/Disable the rule.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **inline_layer**  string | Inline Layer identified by the name or UID. Relevant only if “Action” was set to “Apply Layer”. |
| **install_on**  list / elements=string | Which Gateways identified by the name or UID to install the policy on. |
| **layer**  string | Layer that the rule belongs to identified by the name or UID. |
| **name**  string / required | Object name. |
| **position**  string | Position in the rulebase. The use of values “top” and “bottom” may not be idempotent. |
| **relative_position**  dictionary | Position in the rulebase.  Use of this field may not be idempotent. |
| **above**  string | Add rule above specific rule/section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **below**  string | Add rule below specific rule/section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **bottom**  string | Add rule to the bottom of a specific section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **top**  string | Add rule to the top of a specific section identified by name (limited to 50 rules if search_entire_rulebase is False). |
| **search_entire_rulebase**  boolean | Whether to search the entire rulebase for a rule that’s been edited in its relative_position field to make sure there indeed has been a change in its position or the section it might be in.  **Choices:**   - `false` ← (default) - `true` |
| **service**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **service_negate**  boolean | True if negate is set for service.  **Choices:**   - `false` - `true` |
| **source**  list / elements=string | Collection of Network objects identified by the name or UID. |
| **source_negate**  boolean | True if negate is set for source.  **Choices:**   - `false` - `true` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time**  list / elements=string | List of time objects. For example, “Weekend”, “Off-Work”, “Every-Day”. |
| **track**  dictionary | Track Settings. |
| **accounting**  boolean | Turns accounting for track on and off.  **Choices:**   - `false` - `true` |
| **alert**  string | Type of alert for the track.  **Choices:**   - `"none"` - `"alert"` - `"snmp"` - `"mail"` - `"user alert 1"` - `"user alert 2"` - `"user alert 3"` |
| **enable_firewall_session**  boolean | Determine whether to generate session log to firewall only connections.  **Choices:**   - `false` - `true` |
| **per_connection**  boolean | Determines whether to perform the log per connection.  **Choices:**   - `false` - `true` |
| **per_session**  boolean | Determines whether to perform the log per session.  **Choices:**   - `false` - `true` |
| **type**  string | a “Log”, “Extended Log”, “Detailed Log”, “None”. |
| **user_check**  dictionary | User check settings. |
| **confirm**  string | N/A  **Choices:**   - `"per rule"` - `"per category"` - `"per application/site"` - `"per data type"` |
| **custom_frequency**  dictionary | N/A |
| **every**  integer | N/A |
| **unit**  string | N/A  **Choices:**   - `"hours"` - `"days"` - `"weeks"` - `"months"` |
| **frequency**  string | N/A  **Choices:**   - `"once a day"` - `"once a week"` - `"once a month"` - `"custom frequency..."` |
| **interaction**  string | N/A |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **vpn**  string | Any or All_GwToGw.  **Choices:**   - `"Any"` - `"All_GwToGw"` |
| **vpn_list**  list / elements=dictionary | Communities or Directional. |
| **community**  list / elements=string | List of community name or UID. |
| **directional**  list / elements=dictionary | Communities directional match condition. |
| **from**  string | From community name or UID. |
| **to**  string | To community name or UID. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_access_rule_module.md#id3)

```yaml+jinja
- name: add-access-rule
  cp_mgmt_access_rule:
    layer: Network
    name: Rule 1
    position: 1
    service:
    - SMTP
    - AOL
    vpn: All_GwToGw
    state: present

- name: set-access-rule
  cp_mgmt_access_rule:
    action: Ask
    action_settings:
      enable_identity_captive_portal: true
      limit: Upload_1Gbps
    layer: Network
    name: Rule 1
    state: present

- name: delete-access-rule
  cp_mgmt_access_rule:
    layer: Network
    name: Rule 2
    state: absent
```

## [Return Values](cp_mgmt_access_rule_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_access_rule**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
