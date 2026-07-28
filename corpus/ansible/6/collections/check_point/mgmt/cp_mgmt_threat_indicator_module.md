---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_threat_indicator module – Manages threat-indicator objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_threat_indicator_module.html
fetched_at: 2026-07-27T16:48:43+00:00
---
# check_point.mgmt.cp_mgmt_threat_indicator module – Manages threat-indicator objects on Check Point over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_threat_indicator`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_threat_indicator_module.md#synopsis)
- [Parameters](cp_mgmt_threat_indicator_module.md#parameters)
- [Examples](cp_mgmt_threat_indicator_module.md#examples)
- [Return Values](cp_mgmt_threat_indicator_module.md#return-values)

## [Synopsis](cp_mgmt_threat_indicator_module.md#id1)

- Manages threat-indicator objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_threat_indicator_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | The indicator’s action.  Choices:   - `"Inactive"` - `"Ask"` - `"Prevent"` - `"Detect"` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **name**  string / required | Object name. |
| **observables**  list / elements=string | The indicator’s observables. |
| **comments**  string | Comments string. |
| **confidence**  string | The confidence level the indicator has that a real threat has been uncovered.  Choices:   - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **domain**  string | The name of a domain. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **ip_address**  string | A valid IP-Address. |
| **ip_address_first**  string | A valid IP-Address, the beginning of the range. If you configure this parameter with a value, you must also configure the value of the ‘ip-address-last’ parameter. |
| **ip_address_last**  string | A valid IP-Address, the end of the range. If you configure this parameter with a value, you must also configure the value of the ‘ip-address-first’ parameter. |
| **mail_cc**  string | A valid E-Mail address, cc field. |
| **mail_from**  string | A valid E-Mail address, sender field. |
| **mail_reply_to**  string | A valid E-Mail address, reply-to field. |
| **mail_subject**  string | Subject of E-Mail. |
| **mail_to**  string | A valid E-Mail address, recipient filed. |
| **md5**  string | A valid MD5 sequence. |
| **name**  string | Object name. Should be unique in the domain. |
| **product**  string | The software blade that processes the observable, AV - AntiVirus, AB - AntiBot.  Choices:   - `"AV"` - `"AB"` |
| **severity**  string | The severity level of the threat.  Choices:   - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **url**  string | A valid URL. |
| **observables_raw_data**  string | The contents of a file containing the indicator’s observables. |
| **profile_overrides**  list / elements=string | Profiles in which to override the indicator’s default action. |
| **action**  string | The indicator’s action in this profile.  Choices:   - `"Inactive"` - `"Ask"` - `"Prevent"` - `"Detect"` |
| **profile**  string | The profile in which to override the indicator’s action. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_threat_indicator_module.md#id3)

```yaml+jinja
- name: add-threat-indicator
  cp_mgmt_threat_indicator:
    action: ask
    ignore_warnings: true
    name: My_Indicator
    observables:
    - confidence: medium
      mail_to: someone@somewhere.com
      name: My_Observable
      product: AV
      severity: low
    profile_overrides:
    - action: detect
      profile: My_Profile
    state: present

- name: set-threat-indicator
  cp_mgmt_threat_indicator:
    action: prevent
    ignore_warnings: true
    name: My_Indicator
    state: present

- name: delete-threat-indicator
  cp_mgmt_threat_indicator:
    name: My_Indicator
    state: absent
```

## [Return Values](cp_mgmt_threat_indicator_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_threat_indicator**  dictionary | The checkpoint object created or updated.  Returned: always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
