---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_vpn_community_star module – Manages vpn-community-star objects on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_vpn_community_star_module.html
fetched_at: 2026-07-28T01:18:31+00:00
---
# check_point.mgmt.cp_mgmt_vpn_community_star module – Manages vpn-community-star objects on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_vpn_community_star`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_vpn_community_star_module.md#synopsis)
- [Parameters](cp_mgmt_vpn_community_star_module.md#parameters)
- [Examples](cp_mgmt_vpn_community_star_module.md#examples)
- [Return Values](cp_mgmt_vpn_community_star_module.md#return-values)

## [Synopsis](cp_mgmt_vpn_community_star_module.md#id1)

- Manages vpn-community-star objects on Check Point devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_vpn_community_star_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **center_gateways**  list / elements=string | Collection of center VPN Gateway and VPN Device objects identified by the name or UID. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **encryption_method**  string | The encryption method to be used.  **Choices:**   - `"prefer ikev2 but support ikev1"` - `"ikev2 only"` - `"ikev1 for ipv4 and ikev2 for ipv6 only"` |
| **encryption_suite**  string | The encryption suite to be used.  **Choices:**   - `"suite-b-gcm-256"` - `"custom"` - `"vpn b"` - `"vpn a"` - `"suite-b-gcm-128"` |
| **granular_encryptions**  list / elements=dictionary  *added in check_point.mgmt 5.1.0* | VPN granular encryption settings. |
| **encryption_method**  string | The encryption method to be used.  **Choices:**   - `"prefer ikev2 but support ikev1"` - `"ikev2 only"` - `"ikev1 for ipv4 and ikev2 for ipv6 only"` |
| **encryption_suite**  string | The encryption suite to be used.  **Choices:**   - `"suite-b-gcm-256"` - `"custom"` - `"vpn b"` - `"vpn a"` - `"suite-b-gcm-128"` |
| **external_gateway**  string | Externally managed or 3rd party gateway identified by name or UID. |
| **ike_phase_1**  dictionary | Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom]. |
| **data_integrity**  string | The hash algorithm to be used.  **Choices:**   - `"aes-xcbc"` - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` - `"md5"` |
| **diffie_hellman_group**  string | The Diffie-Hellman group to be used.  **Choices:**   - `"group-1"` - `"group-2"` - `"group-5"` - `"group-14"` - `"group-15"` - `"group-16"` - `"group-17"` - `"group-18"` - `"group-19"` - `"group-20"` - `"group-24"` |
| **encryption_algorithm**  string | The encryption algorithm to be used.  **Choices:**   - `"cast"` - `"aes-256"` - `"des"` - `"aes-128"` - `"3des"` |
| **ike_p1_rekey_time**  integer | Indicates the time interval for IKE phase 1 renegotiation. |
| **ike_p1_rekey_time_unit**  string | Indicates the time unit for [ike-p1-rekey-time-unit] parameter, rounded up to minutes scale.  **Choices:**   - `"days"` - `"hours"` - `"minutes"` - `"seconds"` |
| **ike_phase_2**  dictionary | Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom]. |
| **data_integrity**  string | The hash algorithm to be used.  **Choices:**   - `"aes-xcbc"` - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` - `"md5"` |
| **encryption_algorithm**  string | The encryption algorithm to be used.  **Choices:**   - `"cast"` - `"aes-gcm-256"` - `"cast-40"` - `"aes-256"` - `"des"` - `"aes-128"` - `"3des"` - `"des-40cp"` - `"aes-gcm-128"` - `"none"` |
| **ike_p2_pfs_dh_grp**  string | The Diffie-Hellman group to be used.  **Choices:**   - `"group-1"` - `"group-2"` - `"group-5"` - `"group-14"` - `"group-15"` - `"group-16"` - `"group-17"` - `"group-18"` - `"group-19"` - `"group-20"` - `"group-24"` |
| **ike_p2_rekey_time**  integer | Indicates the time interval for IKE phase 2 renegotiation. |
| **ike_p2_rekey_time_unit**  string | Indicates the time unit for [ike-p2-rekey-time-unit] parameter.  **Choices:**   - `"days"` - `"hours"` - `"minutes"` - `"seconds"` |
| **ike_p2_use_pfs**  boolean | Indicates whether Perfect Forward Secrecy (PFS) is being used for IKE phase 2.  **Choices:**   - `false` - `true` |
| **internal_gateway**  string | Internally managed Check Point gateway identified by name or UID, or ‘Any’ for all internal-gateways participants in this community. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **ike_phase_1**  dictionary | Ike Phase 1 settings. Only applicable when the encryption-suite is set to [custom]. |
| **data_integrity**  string | The hash algorithm to be used.  **Choices:**   - `"aes-xcbc"` - `"sha1"` - `"sha256"` - `"sha384"` - `"md5"` |
| **diffie_hellman_group**  string | The Diffie-Hellman group to be used.  **Choices:**   - `"group-1"` - `"group-2"` - `"group-5"` - `"group-14"` - `"group-19"` - `"group-20"` |
| **encryption_algorithm**  string | The encryption algorithm to be used.  **Choices:**   - `"cast"` - `"aes-256"` - `"des"` - `"aes-128"` - `"3des"` |
| **ike_p1_rekey_time**  integer  *added in check_point.mgmt 5.1.0* | Indicates the time interval for IKE phase 1 renegotiation. |
| **ike_p1_rekey_time_unit**  string  *added in check_point.mgmt 5.1.0* | Indicates the time unit for [ike-p1-rekey-time-unit] parameter, rounded up to minutes scale.  **Choices:**   - `"days"` - `"hours"` - `"minutes"` - `"seconds"` |
| **ike_phase_2**  dictionary | Ike Phase 2 settings. Only applicable when the encryption-suite is set to [custom]. |
| **data_integrity**  string | The hash algorithm to be used.  **Choices:**   - `"aes-xcbc"` - `"sha1"` - `"sha256"` - `"sha384"` - `"md5"` |
| **encryption_algorithm**  string | The encryption algorithm to be used.  **Choices:**   - `"cast"` - `"aes-gcm-256"` - `"cast-40"` - `"aes-256"` - `"des"` - `"aes-128"` - `"3des"` - `"des-40cp"` - `"aes-gcm-128"` - `"none"` |
| **ike_p2_pfs_dh_grp**  string  *added in check_point.mgmt 5.1.0* | The Diffie-Hellman group to be used.  **Choices:**   - `"group-1"` - `"group-2"` - `"group-5"` - `"group-14"` - `"group-15"` - `"group-16"` - `"group-17"` - `"group-18"` - `"group-19"` - `"group-20"` - `"group-24"` |
| **ike_p2_rekey_time**  integer  *added in check_point.mgmt 5.1.0* | Indicates the time interval for IKE phase 2 renegotiation. |
| **ike_p2_rekey_time_unit**  string  *added in check_point.mgmt 5.1.0* | Indicates the time unit for [ike-p2-rekey-time-unit] parameter.  **Choices:**   - `"days"` - `"hours"` - `"minutes"` - `"seconds"` |
| **ike_p2_use_pfs**  boolean  *added in check_point.mgmt 5.1.0* | Indicates whether Perfect Forward Secrecy (PFS) is being used for IKE phase 2.  **Choices:**   - `false` - `true` |
| **mesh_center_gateways**  boolean | Indicates whether the meshed community is in center.  **Choices:**   - `false` - `true` |
| **name**  string / required | Object name. |
| **override_vpn_domains**  list / elements=dictionary  *added in check_point.mgmt 5.1.0* | The Overrides VPN Domains of the participants GWs. |
| **gateway**  string | Participant gateway in override VPN domain identified by the name or UID. |
| **vpn_domain**  string | VPN domain network identified by the name or UID. |
| **satellite_gateways**  list / elements=string | Collection of Gateway objects representing satellite gateways identified by the name or UID. |
| **shared_secrets**  list / elements=dictionary | Shared secrets for external gateways. |
| **external_gateway**  string | External gateway identified by the name or UID. |
| **shared_secret**  string | Shared secret. |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **tunnel_granularity**  string  *added in check_point.mgmt 5.1.0* | VPN tunnel sharing option to be used.  **Choices:**   - `"per_host"` - `"per_subnet"` - `"universal"` |
| **use_shared_secret**  boolean | Indicates whether the shared secret should be used for all external gateways.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_vpn_community_star_module.md#id3)

```yaml+jinja
- name: add-vpn-community-star
  cp_mgmt_vpn_community_star:
    center_gateways: Second_Security_Gateway
    encryption_method: prefer ikev2 but support ikev1
    encryption_suite: custom
    ike_phase_1:
      data_integrity: sha1
      diffie_hellman_group: group 19
      encryption_algorithm: aes-128
    ike_phase_2:
      data_integrity: aes-xcbc
      encryption_algorithm: aes-gcm-128
    name: New_VPN_Community_Star_1
    state: present

- name: set-vpn-community-star
  cp_mgmt_vpn_community_star:
    encryption_method: ikev2 only
    encryption_suite: custom
    ike_phase_1:
      data_integrity: sha1
      diffie_hellman_group: group 19
      encryption_algorithm: aes-128
    ike_phase_2:
      data_integrity: aes-xcbc
      encryption_algorithm: aes-gcm-128
    name: New_VPN_Community_Star_1
    state: present

- name: delete-vpn-community-star
  cp_mgmt_vpn_community_star:
    name: New_VPN_Community_Star_1
    state: absent
```

## [Return Values](cp_mgmt_vpn_community_star_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_vpn_community_star**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
