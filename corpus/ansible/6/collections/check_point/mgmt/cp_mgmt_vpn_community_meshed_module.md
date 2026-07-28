---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_vpn_community_meshed module – Manages vpn-community-meshed objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_vpn_community_meshed_module.html
fetched_at: 2026-07-27T16:48:55+00:00
---
# check_point.mgmt.cp_mgmt_vpn_community_meshed module – Manages vpn-community-meshed objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_vpn_community_meshed`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_vpn_community_meshed_module.md#synopsis)
- [Parameters](cp_mgmt_vpn_community_meshed_module.md#parameters)
- [Examples](cp_mgmt_vpn_community_meshed_module.md#examples)
- [Return Values](cp_mgmt_vpn_community_meshed_module.md#return-values)

## [Synopsis](cp_mgmt_vpn_community_meshed_module.md#id1)

- Manages vpn-community-meshed objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_vpn_community_meshed_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  Choices:   - `false` - `true` |
| **color**  string | Color of the object. Should be one of existing colors.  Choices:   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **encryption_method**  string | The encryption method to be used.  Choices:   - `"prefer ikev2 but support ikev1"` - `"ikev2 only"` - `"ikev1 for ipv4 and ikev2 for ipv6 only"` |
| **encryption_suite**  string | The encryption suite to be used.  Choices:   - `"suite-b-gcm-256"` - `"custom"` - `"vpn b"` - `"vpn a"` - `"suite-b-gcm-128"` |
| **gateways**  list / elements=string | Collection of Gateway objects identified by the name or UID. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  Choices:   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  Choices:   - `false` - `true` |
| **ike_phase_1**  dictionary | Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom]. |
| **data_integrity**  string | The hash algorithm to be used.  Choices:   - `"aes-xcbc"` - `"sha1"` - `"sha256"` - `"sha384"` - `"md5"` |
| **diffie_hellman_group**  string | The Diffie-Hellman group to be used.  Choices:   - `"group-1"` - `"group-2"` - `"group-5"` - `"group-14"` - `"group-19"` - `"group-20"` |
| **encryption_algorithm**  string | The encryption algorithm to be used.  Choices:   - `"cast"` - `"aes-256"` - `"des"` - `"aes-128"` - `"3des"` |
| **ike_phase_2**  dictionary | Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom]. |
| **data_integrity**  string | The hash algorithm to be used.  Choices:   - `"aes-xcbc"` - `"sha1"` - `"sha256"` - `"sha384"` - `"md5"` |
| **encryption_algorithm**  string | The encryption algorithm to be used.  Choices:   - `"cast"` - `"aes-gcm-256"` - `"cast-40"` - `"aes-256"` - `"des"` - `"aes-128"` - `"3des"` - `"des-40cp"` - `"aes-gcm-128"` - `"none"` |
| **name**  string / required | Object name. |
| **shared_secrets**  list / elements=string | Shared secrets for external gateways. |
| **external_gateway**  string | External gateway identified by the name or UID. |
| **shared_secret**  string | Shared secret. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **use_shared_secret**  boolean | Indicates whether the shared secret should be used for all external gateways.  Choices:   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_vpn_community_meshed_module.md#id3)

```yaml+jinja
- name: add-vpn-community-meshed
  cp_mgmt_vpn_community_meshed:
    encryption_method: prefer ikev2 but support ikev1
    encryption_suite: custom
    ike_phase_1:
      data_integrity: sha1
      diffie_hellman_group: group 19
      encryption_algorithm: aes-128
    ike_phase_2:
      data_integrity: aes-xcbc
      encryption_algorithm: aes-gcm-128
    name: New_VPN_Community_Meshed_1
    state: present

- name: set-vpn-community-meshed
  cp_mgmt_vpn_community_meshed:
    encryption_method: ikev2 only
    encryption_suite: custom
    ike_phase_1:
      data_integrity: sha1
      diffie_hellman_group: group 19
      encryption_algorithm: aes-128
    ike_phase_2:
      data_integrity: aes-xcbc
      encryption_algorithm: aes-gcm-128
    name: New_VPN_Community_Meshed_1
    state: present

- name: delete-vpn-community-meshed
  cp_mgmt_vpn_community_meshed:
    name: New_VPN_Community_Meshed_1
    state: absent
```

## [Return Values](cp_mgmt_vpn_community_meshed_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_vpn_community_meshed**  dictionary | The checkpoint object created or updated.  Returned: always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
